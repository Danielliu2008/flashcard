package com.anatomy.flashcard.data

import android.content.Context
import com.anatomy.flashcard.model.DeckTopics
import com.anatomy.flashcard.model.Flashcard
import com.anatomy.flashcard.model.FlashcardDeck
import com.anatomy.flashcard.model.StudyUnit
import org.json.JSONObject
import java.io.File

class DeckRepository(private val context: Context) {

    private val deckMeta = listOf(
        Triple("nervous_system.json", "神经系统 闪卡", "系统解剖学·脑、脊髓、脑神经、脊神经与自主神经系统核心考点"),
        Triple("skeletal_system.json", "人体骨骼 闪卡", "系统解剖学·骨学总论、中轴骨、附肢骨、关节学及骨连结构造"),
        Triple("muscular_system.json", "肌肉闪卡", "系统解剖学·骨骼肌分布、肌纤维微细结构、肌节及肌力学效应"),
        Triple("endocrine_system.json", "内分泌系统 闪卡", "系统解剖学·甲状腺、垂体、肾上腺及内分泌细胞群调控机制"),
        Triple("sensory_system.json", "感觉器官 闪卡", "系统解剖学·视器、前庭蜗器及眼耳受器与传导构造")
    )

    fun loadAllDecks(): List<FlashcardDeck> {
        return StudyUnit.ANATOMY_UNITS.mapNotNull { unit ->
            loadDeck(unit)
        }
    }

    fun loadDeck(unit: StudyUnit): FlashcardDeck? {
        val filename = if (unit.filename.endsWith(".json")) unit.filename else "${unit.filename}.json"
        val fallbackTitle = "${unit.title} 闪卡"
        val description = unit.description.ifEmpty { "卡组考点复习" }

        // 1. 优先检查 custom_data 目录
        val customFiles = listOf(
            File(File(context.filesDir, "custom_data/${unit.subjectId}/decks"), filename),
            File(File(context.filesDir, "custom_data/decks"), filename)
        )
        for (f in customFiles) {
            if (f.exists() && f.length() > 0) {
                try {
                    val jsonString = f.readText(Charsets.UTF_8)
                    val deck = parseDeckJson(jsonString, filename, fallbackTitle, description, unit.id)
                    if (deck != null) return deck
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
        }

        // 2. 回退到 assets 查找 (先精确，后目录模糊匹配)
        val assetPaths = listOf(
            "subjects/${unit.subjectId}/decks/$filename",
            "decks/$filename"
        )
        for (path in assetPaths) {
            try {
                val jsonString = context.assets.open(path).bufferedReader().use { it.readText() }
                val deck = parseDeckJson(jsonString, filename, fallbackTitle, description, unit.id)
                if (deck != null) return deck
            } catch (_: Exception) {
            }
        }

        // 3. 智能目录匹配
        try {
            val list = context.assets.list("subjects/${unit.subjectId}/decks")
            if (list != null) {
                for (item in list) {
                    if (item.endsWith(".json")) {
                        val pureName = item.removeSuffix(".json")
                        if (pureName.contains(unit.id) || pureName.contains(unit.title) || unit.title.contains(pureName)) {
                            val jsonString = context.assets.open("subjects/${unit.subjectId}/decks/$item").bufferedReader().use { it.readText() }
                            val deck = parseDeckJson(jsonString, item, fallbackTitle, description, unit.id)
                            if (deck != null) return deck
                        }
                    }
                }
            }
        } catch (_: Exception) {}

        return null
    }

    fun loadDeck(filename: String): FlashcardDeck? {
        val actualFilename = if (filename.endsWith(".json")) filename else "$filename.json"
        val meta = deckMeta.find { it.first == actualFilename }
        val fallbackTitle = meta?.second ?: actualFilename.removeSuffix(".json")
        val description = meta?.third ?: "自定义导入卡组"

        // 优先检查 custom_data/decks 目录
        val customFile = File(File(context.filesDir, "custom_data/decks"), actualFilename)
        if (customFile.exists() && customFile.length() > 0) {
            try {
                val jsonString = customFile.readText(Charsets.UTF_8)
                val deck = parseDeckJson(jsonString, actualFilename, fallbackTitle, description, actualFilename.removeSuffix(".json"))
                if (deck != null) return deck
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }

        // 回退到 assets
        return loadDeckFromAsset(actualFilename, fallbackTitle, description)
    }

    private fun loadDeckFromAsset(filename: String, fallbackTitle: String, description: String): FlashcardDeck? {
        return try {
            val jsonString = context.assets.open("decks/$filename").bufferedReader().use { it.readText() }
            parseDeckJson(jsonString, filename, fallbackTitle, description, filename.removeSuffix(".json"))
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }

    private fun parseDeckJson(
        jsonString: String,
        filename: String,
        fallbackTitle: String,
        description: String,
        deckIdOverride: String? = null
    ): FlashcardDeck? {
        return try {
            val root = JSONObject(jsonString)
            val id = deckIdOverride ?: root.optString("id", filename.removeSuffix(".json"))
            val title = root.optString("title", fallbackTitle)

            val cardsList = mutableListOf<Flashcard>()
            val cardsArray = root.optJSONArray("flashcards")
            if (cardsArray != null) {
                for (i in 0 until cardsArray.length()) {
                    val cardObj = cardsArray.getJSONObject(i)
                    val cardId = cardObj.optInt("c", i + 1)

                    var frontText = ""
                    val fObj = cardObj.optJSONObject("f")
                    val fBlocks = fObj?.optJSONArray("flashcardContentBlock")
                    if (fBlocks != null && fBlocks.length() > 0) {
                        frontText = fBlocks.getJSONObject(0).optString("content", "")
                    }

                    var backText = ""
                    var isImage = false
                    var imageAlt: String? = null
                    val bObj = cardObj.optJSONObject("b")
                    val bBlocks = bObj?.optJSONArray("flashcardContentBlock")
                    if (bBlocks != null && bBlocks.length() > 0) {
                        val firstB = bBlocks.getJSONObject(0)
                        backText = firstB.optString("content", "")
                        if (firstB.optString("type") == "image") {
                            isImage = true
                            imageAlt = firstB.optString("alt")
                        }
                    }

                    val pointType = cardObj.optString("pointType", "")
                    val starRating = cardObj.optString("starRating", "★★★")
                    val importance = cardObj.optInt("importance", 3)

                    cardsList.add(
                        Flashcard(
                            id = cardId,
                            frontText = frontText,
                            backText = backText,
                            categoryIndex = cardId,
                            isImage = isImage,
                            imageAlt = imageAlt,
                            pointType = pointType,
                            starRating = starRating,
                            importance = importance
                        )
                    )
                }
            }

            val topicsObj = root.optJSONObject("topics")
            val coveredList = mutableListOf<String>()
            val followUpList = mutableListOf<String>()

            val coveredArray = topicsObj?.optJSONArray("covered")
            if (coveredArray != null) {
                for (i in 0 until coveredArray.length()) {
                    coveredList.add(coveredArray.getString(i))
                }
            }

            val followUpArray = topicsObj?.optJSONArray("followUp")
            if (followUpArray != null) {
                for (i in 0 until followUpArray.length()) {
                    followUpList.add(followUpArray.getString(i))
                }
            }

            FlashcardDeck(
                id = id,
                filename = filename,
                title = title,
                description = description,
                iconName = when {
                    filename.contains("nervous") -> "Psychology"
                    filename.contains("skeletal") -> "Accessibility"
                    filename.contains("bacterial") || filename.contains("micro") -> "Biotech"
                    filename.contains("immu") -> "Shield"
                    else -> "FitnessCenter"
                },
                cards = cardsList,
                topics = DeckTopics(covered = coveredList, followUp = followUpList)
            )
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }
}
