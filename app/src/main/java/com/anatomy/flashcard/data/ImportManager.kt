package com.anatomy.flashcard.data

import android.content.Context
import com.anatomy.flashcard.model.AnatomySystemType
import org.json.JSONArray
import org.json.JSONObject
import java.io.File

enum class ImportedDataType(val label: String) {
    FLASHCARD("闪卡卡组"),
    QUIZ("单元小测"),
    MINDMAP("知识导图"),
    UNKNOWN("未知格式")
}

data class ImportInspectionResult(
    val type: ImportedDataType,
    val suggestedSystem: AnatomySystemType,
    val title: String,
    val itemCount: Int,
    val rawJson: String,
    val isValid: Boolean,
    val message: String
)

data class ImportZipResult(
    val totalProcessed: Int,
    val successDecks: Int,
    val successQuizzes: Int,
    val successMindmaps: Int,
    val isSuccess: Boolean,
    val message: String
)

class ImportManager(private val context: Context) {

    val customDataDir: File get() = File(context.filesDir, "custom_data")
    val decksDir: File get() = File(customDataDir, "decks")
    val quizzesDir: File get() = File(customDataDir, "quizzes")
    val mindmapsDir: File get() = File(customDataDir, "mindmaps")

    init {
        decksDir.mkdirs()
        quizzesDir.mkdirs()
        mindmapsDir.mkdirs()
    }

    /**
     * 智能检测 JSON 结构
     */
    fun inspectJson(jsonString: String): ImportInspectionResult {
        try {
            var text = jsonString.trim()
            // 如果是双重转义的 JSON 字符串（例如从 RPC 响应中直接复制）
            if (text.startsWith("\"") && text.endsWith("\"") && text.contains("\\\"")) {
                try {
                    val unescaped = JSONObject("{ \"v\": $text }").getString("v")
                    text = unescaped.trim()
                } catch (_: Exception) {}
            }

            val root = JSONObject(text)

            // 1. 检查是否为闪卡
            if (root.has("flashcards")) {
                val cards = root.optJSONArray("flashcards") ?: JSONArray()
                val system = detectSystem(text)
                val title = root.optString("title", "${system.title} 闪卡")
                return ImportInspectionResult(
                    type = ImportedDataType.FLASHCARD,
                    suggestedSystem = system,
                    title = title,
                    itemCount = cards.length(),
                    rawJson = text,
                    isValid = cards.length() > 0,
                    message = "识别为闪卡卡组，包含 ${cards.length()} 张卡片"
                )
            }

            // 2. 检查是否为小测 (Quiz)
            if (root.has("quiz")) {
                val quiz = root.optJSONArray("quiz") ?: JSONArray()
                val system = detectSystem(text)
                val title = root.optString("title", "${system.title} 测验")
                return ImportInspectionResult(
                    type = ImportedDataType.QUIZ,
                    suggestedSystem = system,
                    title = title,
                    itemCount = quiz.length(),
                    rawJson = text,
                    isValid = quiz.length() > 0,
                    message = "识别为小测题目，包含 ${quiz.length()} 道考题"
                )
            }

            // 3. 检查是否为思维导图 (Mindmap)
            if (root.has("name") && root.has("children")) {
                val name = root.optString("name", "知识脑图")
                val system = detectSystem(text)
                var count = 0
                fun countNodes(obj: JSONObject) {
                    count++
                    val arr = obj.optJSONArray("children")
                    if (arr != null) {
                        for (i in 0 until arr.length()) {
                            val child = arr.optJSONObject(i)
                            if (child != null) countNodes(child)
                        }
                    }
                }
                countNodes(root)
                return ImportInspectionResult(
                    type = ImportedDataType.MINDMAP,
                    suggestedSystem = system,
                    title = name,
                    itemCount = count,
                    rawJson = text,
                    isValid = count > 0,
                    message = "识别为思维导图，包含 $count 个知识节点"
                )
            }

            return ImportInspectionResult(
                type = ImportedDataType.UNKNOWN,
                suggestedSystem = AnatomySystemType.NERVOUS,
                title = "未知格式",
                itemCount = 0,
                rawJson = text,
                isValid = false,
                message = "未识别到有效的闪卡 (flashcards)、测验 (quiz) 或导图 (name+children) 根节点"
            )
        } catch (e: Exception) {
            return ImportInspectionResult(
                type = ImportedDataType.UNKNOWN,
                suggestedSystem = AnatomySystemType.NERVOUS,
                title = "解析失败",
                itemCount = 0,
                rawJson = jsonString,
                isValid = false,
                message = "JSON 格式语法错误: ${e.localizedMessage}"
            )
        }
    }

    /**
     * 执行保存导入
     */
    fun saveImport(
        type: ImportedDataType,
        systemType: AnatomySystemType,
        jsonContent: String
    ): Boolean {
        return try {
            val fileName = when (systemType) {
                AnatomySystemType.NERVOUS -> "nervous_system.json"
                AnatomySystemType.SKELETAL -> "skeletal_system.json"
                AnatomySystemType.MUSCULAR -> "muscular_system.json"
                else -> if (systemType.filename.endsWith(".json")) systemType.filename else "${systemType.filename}.json"
            }

            val baseTargetDir = when (type) {
                ImportedDataType.FLASHCARD -> decksDir
                ImportedDataType.QUIZ -> quizzesDir
                ImportedDataType.MINDMAP -> mindmapsDir
                ImportedDataType.UNKNOWN -> return false
            }

            val targetDir = if (systemType.subjectId != "anatomy") {
                File(context.filesDir, "custom_data/${systemType.subjectId}/${baseTargetDir.name}").apply { mkdirs() }
            } else {
                baseTargetDir
            }

            val targetFile = File(targetDir, fileName)
            targetFile.writeText(jsonContent, Charsets.UTF_8)
            true
        } catch (e: Exception) {
            e.printStackTrace()
            false
        }
    }

    /**
     * 批量导入 ZIP 压缩包（自动扫描并归类所有 flashcards, quizzes, mindmaps）
     */
    fun importZip(inputStream: java.io.InputStream): ImportZipResult {
        var countDecks = 0
        var countQuizzes = 0
        var countMindmaps = 0
        var totalProcessed = 0

        try {
            java.util.zip.ZipInputStream(inputStream).use { zis ->
                var entry = zis.nextEntry
                while (entry != null) {
                    val name = entry.name
                    if (!entry.isDirectory && name.endsWith(".json", ignoreCase = true)
                        && !name.contains("__MACOSX")
                        && !name.endsWith("summary.json", ignoreCase = true)
                        && !name.endsWith("manifest.json", ignoreCase = true)
                    ) {
                        val bytes = zis.readBytes()
                        val text = String(bytes, Charsets.UTF_8)
                        val inspection = inspectJson(text)
                        if (inspection.isValid) {
                            totalProcessed++
                            val saved = saveImport(inspection.type, inspection.suggestedSystem, inspection.rawJson)
                            if (saved) {
                                when (inspection.type) {
                                    ImportedDataType.FLASHCARD -> countDecks++
                                    ImportedDataType.QUIZ -> countQuizzes++
                                    ImportedDataType.MINDMAP -> countMindmaps++
                                    ImportedDataType.UNKNOWN -> {}
                                }
                            }
                        }
                    }
                    zis.closeEntry()
                    entry = zis.nextEntry
                }
            }

            val totalSuccess = countDecks + countQuizzes + countMindmaps
            val isSuccess = totalSuccess > 0
            val message = if (isSuccess) {
                "成功批量导入 ZIP：闪卡 ${countDecks} 套，测验 ${countQuizzes} 套，导图 ${countMindmaps} 套"
            } else {
                "ZIP 压缩包中未检测到有效的解剖学闪卡/测验/导图 JSON 数据"
            }

            return ImportZipResult(
                totalProcessed = totalProcessed,
                successDecks = countDecks,
                successQuizzes = countQuizzes,
                successMindmaps = countMindmaps,
                isSuccess = isSuccess,
                message = message
            )
        } catch (e: Exception) {
            return ImportZipResult(
                totalProcessed = totalProcessed,
                successDecks = countDecks,
                successQuizzes = countQuizzes,
                successMindmaps = countMindmaps,
                isSuccess = false,
                message = "ZIP 解析异常: ${e.localizedMessage}"
            )
        }
    }

    /**
     * 清空所有自定义导入，恢复默认内置 assets
     */
    fun clearAllCustomData(): Boolean {
        return try {
            customDataDir.deleteRecursively()
            decksDir.mkdirs()
            quizzesDir.mkdirs()
            mindmapsDir.mkdirs()
            true
        } catch (e: Exception) {
            e.printStackTrace()
            false
        }
    }

    fun hasCustomData(): Boolean {
        return (decksDir.listFiles()?.isNotEmpty() == true) ||
                (quizzesDir.listFiles()?.isNotEmpty() == true) ||
                (mindmapsDir.listFiles()?.isNotEmpty() == true)
    }

    private fun detectSystem(content: String): AnatomySystemType {
        var nervousScore = 0
        var skeletalScore = 0
        var muscularScore = 0

        val nervousKeywords = listOf("神经", "中枢", "脑", "脊髓", "突触", "交感", "迷走", "神经元", "胶质细胞", "脑脊液")
        val skeletalKeywords = listOf("骨骼", "骨", "关节", "椎骨", "颅骨", "股骨", "胸骨", "骨髓", "足弓", "肋骨", "骨膜")
        val muscularKeywords = listOf("肌肉", "肌", "肌节", "肌丝", "横纹肌", "骨骼肌", "强直收缩", "肌纤维", "肌腹", "竖脊肌")

        nervousKeywords.forEach { if (content.contains(it)) nervousScore++ }
        skeletalKeywords.forEach { if (content.contains(it)) skeletalScore++ }
        muscularKeywords.forEach { if (content.contains(it)) muscularScore++ }

        return when {
            nervousScore >= skeletalScore && nervousScore >= muscularScore -> AnatomySystemType.NERVOUS
            skeletalScore >= muscularScore -> AnatomySystemType.SKELETAL
            else -> AnatomySystemType.MUSCULAR
        }
    }
}
