package com.anatomy.flashcard.data

import android.content.Context
import android.content.SharedPreferences
import com.anatomy.flashcard.model.QuizRecord
import org.json.JSONArray
import org.json.JSONObject

data class QuizSessionState(
    val quizId: String,
    val currentIndex: Int,
    val userSelections: Map<Int, Set<Int>>,
    val userBlankInputs: Map<String, String>,
    val fillBlankCorrect: Map<Int, Boolean>,
    val submittedQuestions: Map<Int, Boolean>,
    val lastUpdated: Long = System.currentTimeMillis()
)

class QuizPreferences(context: Context) {
    private val prefs: SharedPreferences = context.getSharedPreferences("anatomy_quiz_prefs", Context.MODE_PRIVATE)

    fun getRecord(quizId: String): QuizRecord {
        val score = prefs.getInt("best_score_$quizId", 0)
        val total = prefs.getInt("total_q_$quizId", 0)
        val time = prefs.getLong("last_time_$quizId", 0L)
        val wrongJson = prefs.getString("wrong_ids_$quizId", "[]") ?: "[]"

        val wrongSet = mutableSetOf<Int>()
        try {
            val arr = JSONArray(wrongJson)
            for (i in 0 until arr.length()) {
                wrongSet.add(arr.getInt(i))
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }

        return QuizRecord(
            quizId = quizId,
            bestScore = score,
            totalQuestions = total,
            lastAttemptTime = time,
            wrongQuestionIds = wrongSet
        )
    }

    fun saveAttempt(quizId: String, score: Int, total: Int, wrongIds: Set<Int>) {
        val currentBest = prefs.getInt("best_score_$quizId", 0)
        val newBest = maxOf(currentBest, score)

        val arr = JSONArray()
        wrongIds.forEach { arr.put(it) }

        prefs.edit()
            .putInt("best_score_$quizId", newBest)
            .putInt("total_q_$quizId", total)
            .putLong("last_time_$quizId", System.currentTimeMillis())
            .putString("wrong_ids_$quizId", arr.toString())
            .remove("active_session_$quizId") // Clear unfinished session upon completion
            .apply()
    }

    fun saveSession(session: QuizSessionState) {
        try {
            val obj = JSONObject().apply {
                put("quizId", session.quizId)
                put("currentIndex", session.currentIndex)
                put("lastUpdated", session.lastUpdated)

                // userSelections: Map<Int, Set<Int>>
                val selObj = JSONObject()
                session.userSelections.forEach { (qIdx, selSet) ->
                    val arr = JSONArray()
                    selSet.forEach { arr.put(it) }
                    selObj.put(qIdx.toString(), arr)
                }
                put("userSelections", selObj)

                // userBlankInputs: Map<String, String>
                val blankObj = JSONObject()
                session.userBlankInputs.forEach { (k, v) -> blankObj.put(k, v) }
                put("userBlankInputs", blankObj)

                // fillBlankCorrect: Map<Int, Boolean>
                val fbcObj = JSONObject()
                session.fillBlankCorrect.forEach { (k, v) -> fbcObj.put(k.toString(), v) }
                put("fillBlankCorrect", fbcObj)

                // submittedQuestions: Map<Int, Boolean>
                val subObj = JSONObject()
                session.submittedQuestions.forEach { (k, v) -> subObj.put(k.toString(), v) }
                put("submittedQuestions", subObj)
            }
            prefs.edit().putString("active_session_${session.quizId}", obj.toString()).apply()
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    fun getSession(quizId: String): QuizSessionState? {
        val raw = prefs.getString("active_session_$quizId", null) ?: return null
        return try {
            val obj = JSONObject(raw)
            val currentIndex = obj.optInt("currentIndex", 0)
            val lastUpdated = obj.optLong("lastUpdated", 0L)

            val userSelections = mutableMapOf<Int, Set<Int>>()
            obj.optJSONObject("userSelections")?.let { selObj ->
                selObj.keys().forEach { k ->
                    val arr = selObj.getJSONArray(k)
                    val set = mutableSetOf<Int>()
                    for (i in 0 until arr.length()) set.add(arr.getInt(i))
                    k.toIntOrNull()?.let { userSelections[it] = set }
                }
            }

            val userBlankInputs = mutableMapOf<String, String>()
            obj.optJSONObject("userBlankInputs")?.let { blankObj ->
                blankObj.keys().forEach { k ->
                    userBlankInputs[k] = blankObj.getString(k)
                }
            }

            val fillBlankCorrect = mutableMapOf<Int, Boolean>()
            obj.optJSONObject("fillBlankCorrect")?.let { fbcObj ->
                fbcObj.keys().forEach { k ->
                    k.toIntOrNull()?.let { fillBlankCorrect[it] = fbcObj.getBoolean(k) }
                }
            }

            val submittedQuestions = mutableMapOf<Int, Boolean>()
            obj.optJSONObject("submittedQuestions")?.let { subObj ->
                subObj.keys().forEach { k ->
                    k.toIntOrNull()?.let { submittedQuestions[it] = subObj.getBoolean(k) }
                }
            }

            QuizSessionState(
                quizId = quizId,
                currentIndex = currentIndex,
                userSelections = userSelections,
                userBlankInputs = userBlankInputs,
                fillBlankCorrect = fillBlankCorrect,
                submittedQuestions = submittedQuestions,
                lastUpdated = lastUpdated
            )
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }

    fun clearSession(quizId: String) {
        prefs.edit().remove("active_session_$quizId").apply()
    }
}
