package com.anatomy.flashcard.data

import android.content.Context
import com.anatomy.flashcard.model.AnatomySystemType
import com.anatomy.flashcard.model.FlashcardDeck
import com.anatomy.flashcard.model.MindMapData
import com.anatomy.flashcard.model.MindMapNode
import com.anatomy.flashcard.model.QuizOption
import com.anatomy.flashcard.model.QuizQuestion
import com.anatomy.flashcard.model.QuizSet
import com.anatomy.flashcard.model.StudyUnit
import org.json.JSONArray
import org.json.JSONObject
import java.io.File
import java.io.InputStreamReader

class DataManager(private val context: Context) {

    private val deckRepository = DeckRepository(context)
    val importManager = ImportManager(context)

    fun getUnitsForSubject(subjectId: String): List<StudyUnit> {
        val builtIns = when (subjectId) {
            "anatomy" -> StudyUnit.ANATOMY_UNITS
            "microbiology" -> StudyUnit.MICROBIOLOGY_UNITS
            "immunology" -> StudyUnit.IMMUNOLOGY_UNITS
            else -> emptyList()
        }

        val result = builtIns.toMutableList()

        // 尝试从 custom_data/{subjectId}/units.json 和 assets/subjects/{subjectId}/units.json 读取动态注册章节
        var jsonUnitsStr: String? = null
        val customUnitsFile = File(context.filesDir, "custom_data/$subjectId/units.json")
        if (customUnitsFile.exists() && customUnitsFile.length() > 0) {
            try {
                jsonUnitsStr = customUnitsFile.readText(Charsets.UTF_8)
            } catch (_: Exception) {}
        }
        if (jsonUnitsStr.isNullOrEmpty()) {
            try {
                context.assets.open("subjects/$subjectId/units.json").use { stream ->
                    jsonUnitsStr = InputStreamReader(stream, Charsets.UTF_8).readText()
                }
            } catch (_: Exception) {}
        }

        if (!jsonUnitsStr.isNullOrEmpty()) {
            try {
                val array = JSONArray(jsonUnitsStr)
                for (i in 0 until array.length()) {
                    val obj = array.getJSONObject(i)
                    val uid = obj.getString("id")
                    if (result.none { it.id == uid }) {
                        result.add(
                            StudyUnit(
                                id = uid,
                                subjectId = subjectId,
                                title = obj.optString("title", uid),
                                subtitle = obj.optString("subtitle", "章节"),
                                description = obj.optString("description", ""),
                                filename = obj.optString("filename", uid)
                            )
                        )
                    }
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }

        return result
    }

    fun loadDeck(systemType: AnatomySystemType): FlashcardDeck? {
        return deckRepository.loadDeck(systemType)
    }

    fun loadAllDecks(): List<FlashcardDeck> {
        return deckRepository.loadAllDecks()
    }

    fun loadMindMap(systemType: AnatomySystemType): MindMapData? {
        val fileName = if (systemType.filename.endsWith(".json")) systemType.filename else "${systemType.filename}.json"

        // 1. 优先检查 custom_data
        var jsonString: String? = null
        val customFiles = listOf(
            File(File(context.filesDir, "custom_data/${systemType.subjectId}/mindmaps"), fileName),
            File(importManager.mindmapsDir, fileName)
        )
        for (f in customFiles) {
            if (f.exists() && f.length() > 0) {
                try {
                    jsonString = f.readText(Charsets.UTF_8)
                    break
                } catch (_: Exception) {}
            }
        }

        // 2. 回退到 assets
        if (jsonString.isNullOrEmpty()) {
            val assetPaths = listOf(
                "subjects/${systemType.subjectId}/mindmaps/$fileName",
                "mindmaps/$fileName"
            )
            for (path in assetPaths) {
                try {
                    context.assets.open(path).use { inputStream ->
                        jsonString = InputStreamReader(inputStream, Charsets.UTF_8).readText()
                    }
                    if (!jsonString.isNullOrEmpty()) break
                } catch (_: Exception) {}
            }

            if (jsonString.isNullOrEmpty()) {
                try {
                    val list = context.assets.list("subjects/${systemType.subjectId}/mindmaps")
                    if (list != null) {
                        for (item in list) {
                            if (item.endsWith(".json")) {
                                val pure = item.removeSuffix(".json")
                                if (pure.contains(systemType.id) || pure.contains(systemType.title) || systemType.title.contains(pure)) {
                                    context.assets.open("subjects/${systemType.subjectId}/mindmaps/$item").use { s ->
                                        jsonString = InputStreamReader(s, Charsets.UTF_8).readText()
                                    }
                                    if (!jsonString.isNullOrEmpty()) break
                                }
                            }
                        }
                    }
                } catch (_: Exception) {}
            }
        }

        if (jsonString.isNullOrEmpty()) return null

        return try {
            val rootJson = JSONObject(jsonString)
            var counter = 0
            fun parseNode(obj: JSONObject): MindMapNode {
                val name = obj.optString("name", "未命名节点")
                val childrenList = mutableListOf<MindMapNode>()
                val childrenArray = obj.optJSONArray("children")
                if (childrenArray != null) {
                    for (i in 0 until childrenArray.length()) {
                        val childObj = childrenArray.optJSONObject(i)
                        if (childObj != null) {
                            childrenList.add(parseNode(childObj))
                        }
                    }
                }
                counter++
                return MindMapNode(
                    id = "node_$counter",
                    title = name,
                    children = childrenList
                )
            }

            val rootNode = parseNode(rootJson)
            MindMapData(
                id = "${systemType.id}_mindmap",
                systemType = systemType,
                title = "${systemType.title} 知识图谱",
                root = rootNode
            )
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }

    fun loadQuizSet(systemType: AnatomySystemType): QuizSet? {
        val fileName = if (systemType.filename.endsWith(".json")) systemType.filename else "${systemType.filename}.json"

        // 1. 优先检查 custom_data
        var jsonString: String? = null
        val customFiles = listOf(
            File(File(context.filesDir, "custom_data/${systemType.subjectId}/quizzes"), fileName),
            File(importManager.quizzesDir, fileName)
        )
        for (f in customFiles) {
            if (f.exists() && f.length() > 0) {
                try {
                    jsonString = f.readText(Charsets.UTF_8)
                    break
                } catch (_: Exception) {}
            }
        }

        // 2. 回退到 assets
        if (jsonString.isNullOrEmpty()) {
            val assetPaths = listOf(
                "subjects/${systemType.subjectId}/quizzes/$fileName",
                "quizzes/$fileName"
            )
            for (path in assetPaths) {
                try {
                    context.assets.open(path).use { inputStream ->
                        jsonString = InputStreamReader(inputStream, Charsets.UTF_8).readText()
                    }
                    if (!jsonString.isNullOrEmpty()) break
                } catch (_: Exception) {}
            }

            if (jsonString.isNullOrEmpty()) {
                try {
                    val list = context.assets.list("subjects/${systemType.subjectId}/quizzes")
                    if (list != null) {
                        for (item in list) {
                            if (item.endsWith(".json")) {
                                val pure = item.removeSuffix(".json")
                                if (pure.contains(systemType.id) || pure.contains(systemType.title) || systemType.title.contains(pure)) {
                                    context.assets.open("subjects/${systemType.subjectId}/quizzes/$item").use { s ->
                                        jsonString = InputStreamReader(s, Charsets.UTF_8).readText()
                                    }
                                    if (!jsonString.isNullOrEmpty()) break
                                }
                            }
                        }
                    }
                } catch (_: Exception) {}
            }
        }

        if (jsonString.isNullOrEmpty()) return null

        return try {
            val rootJson = JSONObject(jsonString)
            val quizArray = rootJson.optJSONArray("quiz") ?: rootJson.optJSONArray("questions") ?: JSONArray()
            val questions = mutableListOf<QuizQuestion>()

            for (i in 0 until quizArray.length()) {
                val qObj = quizArray.getJSONObject(i)
                val type = qObj.optString("type", "multiple_choice")
                val questionText = qObj.optString("question").ifEmpty { qObj.optString("prompt", "") }
                val hint = qObj.optString("hint", "")
                val rationale = qObj.optString("rationale", "")

                val optArray = qObj.optJSONArray("answerOptions") ?: qObj.optJSONArray("options") ?: JSONArray()
                val options = mutableListOf<QuizOption>()
                for (j in 0 until optArray.length()) {
                    val optObj = optArray.getJSONObject(j)
                    options.add(
                        QuizOption(
                            text = optObj.optString("text", ""),
                            isCorrect = optObj.optBoolean("isCorrect", false),
                            rationale = optObj.optString("rationale", "")
                        )
                    )
                }

                // 选项顺序已在题库生成时经过打乱，加载时保持稳定固定，确保用户作答进度索引的准确恢复
                val finalOptions = options

                val blankArray = qObj.optJSONArray("blankAnswers") ?: qObj.optJSONArray("blanks")
                val blankAnswers = mutableListOf<String>()
                if (blankArray != null) {
                    for (k in 0 until blankArray.length()) {
                        blankAnswers.add(blankArray.getString(k))
                    }
                }

                questions.add(
                    QuizQuestion(
                        id = i + 1,
                        type = type,
                        question = questionText,
                        options = finalOptions,
                        hint = hint,
                        blankAnswers = blankAnswers,
                        rationale = rationale
                    )
                )
            }

            val topicsObj = rootJson.optJSONObject("topics")
            val coveredTopics = mutableListOf<String>()
            val coveredArray = topicsObj?.optJSONArray("covered")
            if (coveredArray != null) {
                for (k in 0 until coveredArray.length()) {
                    coveredTopics.add(coveredArray.getString(k))
                }
            }

            QuizSet(
                id = "${systemType.id}_quiz",
                systemType = systemType,
                title = "${systemType.title} 专项小测",
                description = if (coveredTopics.isNotEmpty()) "涵盖${coveredTopics.take(3).joinToString("、")}等核心考点" else "精选题库专项练习",
                coveredTopics = coveredTopics,
                questions = questions
            )
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }
}
