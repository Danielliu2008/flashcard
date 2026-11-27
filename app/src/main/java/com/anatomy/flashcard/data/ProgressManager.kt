package com.anatomy.flashcard.data

import android.content.Context
import android.content.SharedPreferences
import com.anatomy.flashcard.model.CardAcquisition
import com.anatomy.flashcard.model.StudyProgress
import org.json.JSONObject

class ProgressManager(context: Context) {
    private val prefs: SharedPreferences = context.getSharedPreferences("notebook_flashcard_prefs", Context.MODE_PRIVATE)

    fun getProgress(deckId: String): StudyProgress {
        val currentIndex = prefs.getInt("index_$deckId", 0)
        val isShuffled = prefs.getBoolean("shuffled_$deckId", false)
        val filterMissedOnly = prefs.getBoolean("filter_missed_$deckId", false)

        val mappingJson = prefs.getString("acquisitions_$deckId", "{}") ?: "{}"
        val acquisitions = mutableMapOf<Int, CardAcquisition>()
        try {
            val json = JSONObject(mappingJson)
            val keys = json.keys()
            while (keys.hasNext()) {
                val key = keys.next()
                val cardId = key.toIntOrNull() ?: continue
                val status = json.getString(key)
                acquisitions[cardId] = when (status) {
                    "acquired" -> CardAcquisition.ACQUIRED
                    "not_acquired" -> CardAcquisition.NOT_ACQUIRED
                    else -> CardAcquisition.UNSTUDIED
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }

        return StudyProgress(
            deckId = deckId,
            currentIndex = currentIndex,
            acquisitions = acquisitions,
            isShuffled = isShuffled,
            filterMissedOnly = filterMissedOnly
        )
    }

    fun saveProgress(progress: StudyProgress) {
        val json = JSONObject()
        progress.acquisitions.forEach { (cardId, status) ->
            val value = when (status) {
                CardAcquisition.ACQUIRED -> "acquired"
                CardAcquisition.NOT_ACQUIRED -> "not_acquired"
                CardAcquisition.UNSTUDIED -> "unstudied"
            }
            json.put(cardId.toString(), value)
        }

        prefs.edit()
            .putInt("index_${progress.deckId}", progress.currentIndex)
            .putBoolean("shuffled_${progress.deckId}", progress.isShuffled)
            .putBoolean("filter_missed_${progress.deckId}", progress.filterMissedOnly)
            .putString("acquisitions_${progress.deckId}", json.toString())
            .apply()
    }

    fun resetDeckProgress(deckId: String) {
        prefs.edit()
            .remove("index_$deckId")
            .remove("shuffled_$deckId")
            .remove("filter_missed_$deckId")
            .remove("acquisitions_$deckId")
            .apply()
    }
}
