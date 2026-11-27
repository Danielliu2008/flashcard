package com.anatomy.flashcard.data

import android.content.Context
import android.content.SharedPreferences
import com.anatomy.flashcard.model.Subject
import com.anatomy.flashcard.model.SubjectViewMode
import org.json.JSONArray
import org.json.JSONObject

class SubjectManager(private val context: Context) {

    private val prefs: SharedPreferences =
        context.getSharedPreferences("memory_aid_subjects", Context.MODE_PRIVATE)

    companion object {
        private const val KEY_SUBJECTS = "saved_subjects"
        private const val KEY_VIEW_MODE = "subject_view_mode"
        private const val KEY_LAST_SUBJECT_ID = "last_selected_subject_id"

        val DEFAULT_ANATOMY = Subject(
            id = "anatomy",
            name = "系统解剖学",
            emoji = "🫀",
            description = "骨骼、肌肉、神经系统知识导图、闪卡与考题",
            isBuiltIn = true,
            colorHex = 0xFF1A73E8
        )

        val DEFAULT_MICROBIOLOGY = Subject(
            id = "microbiology",
            name = "医学微生物学",
            emoji = "🦠",
            description = "细菌学、病毒学、真菌学8大章节知识导图、闪卡与考题",
            isBuiltIn = true,
            colorHex = 0xFF188038
        )

        val DEFAULT_IMMUNOLOGY = Subject(
            id = "immunology",
            name = "医学免疫学",
            emoji = "🧬",
            description = "免疫系统、固有免疫、抗原MHC、淋巴细胞应答与应用知识导图、闪卡与考题",
            isBuiltIn = true,
            colorHex = 0xFF9334E6
        )
    }

    /**
     * 获取所有学科列表（保证系统解剖学、医学微生物学、医学免疫学为内置学科）
     */
    fun getSubjects(): List<Subject> {
        val jsonStr = prefs.getString(KEY_SUBJECTS, null)
        if (jsonStr.isNullOrEmpty()) {
            val defaults = listOf(
                DEFAULT_ANATOMY,
                DEFAULT_MICROBIOLOGY,
                DEFAULT_IMMUNOLOGY,
                Subject(
                    id = "physiology",
                    name = "生理学",
                    emoji = "⚡",
                    description = "细胞、神经、循环与各系统生理机制调节",
                    isBuiltIn = false,
                    colorHex = 0xFF188038
                ),
                Subject(
                    id = "pathology",
                    name = "病理学",
                    emoji = "🔬",
                    description = "疾病病理变化、发病机理与形态学特征",
                    isBuiltIn = false,
                    colorHex = 0xFFD93025
                ),
                Subject(
                    id = "pharmacology",
                    name = "药理学",
                    emoji = "💊",
                    description = "药物作用机制、药代动力学与不良反应",
                    isBuiltIn = false,
                    colorHex = 0xFFF29900
                )
            )
            saveSubjects(defaults)
            return defaults
        }

        try {
            val array = JSONArray(jsonStr)
            val list = mutableListOf<Subject>()
            for (i in 0 until array.length()) {
                val obj = array.getJSONObject(i)
                list.add(
                    Subject(
                        id = obj.getString("id"),
                        name = obj.getString("name"),
                        emoji = obj.optString("emoji", "📚"),
                        description = obj.optString("description", ""),
                        isBuiltIn = obj.optBoolean("isBuiltIn", false),
                        colorHex = obj.optLong("colorHex", 0xFF1A73E8)
                    )
                )
            }
            val defaultMap = mapOf(
                DEFAULT_ANATOMY.id to DEFAULT_ANATOMY,
                DEFAULT_MICROBIOLOGY.id to DEFAULT_MICROBIOLOGY,
                DEFAULT_IMMUNOLOGY.id to DEFAULT_IMMUNOLOGY
            )
            // 确保内置学科始终采用最新的属性与内置状态
            for (i in list.indices) {
                val sub = list[i]
                if (defaultMap.containsKey(sub.id)) {
                    list[i] = defaultMap[sub.id]!!
                }
            }
            if (list.none { it.id == DEFAULT_ANATOMY.id }) {
                list.add(0, DEFAULT_ANATOMY)
            }
            if (list.none { it.id == DEFAULT_MICROBIOLOGY.id }) {
                val index = list.indexOfFirst { it.id == DEFAULT_ANATOMY.id } + 1
                list.add(index, DEFAULT_MICROBIOLOGY)
            }
            if (list.none { it.id == DEFAULT_IMMUNOLOGY.id }) {
                val index = list.indexOfFirst { it.id == DEFAULT_MICROBIOLOGY.id } + 1
                list.add(index, DEFAULT_IMMUNOLOGY)
            }
            saveSubjects(list)
            return list
        } catch (e: Exception) {
            e.printStackTrace()
            return listOf(DEFAULT_ANATOMY, DEFAULT_MICROBIOLOGY, DEFAULT_IMMUNOLOGY)
        }
    }

    fun saveSubjects(list: List<Subject>) {
        val array = JSONArray()
        list.forEach { sub ->
            val obj = JSONObject().apply {
                put("id", sub.id)
                put("name", sub.name)
                put("emoji", sub.emoji)
                put("description", sub.description)
                put("isBuiltIn", sub.isBuiltIn)
                put("colorHex", sub.colorHex)
            }
            array.put(obj)
        }
        prefs.edit().putString(KEY_SUBJECTS, array.toString()).apply()
    }

    fun addSubject(name: String, emoji: String, description: String): Subject {
        val id = "sub_" + System.currentTimeMillis()
        val colors = listOf(0xFF1A73E8, 0xFF188038, 0xFFD93025, 0xFFF29900, 0xFF9334E6, 0xFF129EAF)
        val randomColor = colors.random()
        val newSub = Subject(
            id = id,
            name = name,
            emoji = if (emoji.isBlank()) "📚" else emoji,
            description = description,
            isBuiltIn = false,
            colorHex = randomColor
        )
        val current = getSubjects().toMutableList()
        current.add(newSub)
        saveSubjects(current)
        return newSub
    }

    fun updateSubjectEmoji(id: String, newEmoji: String) {
        val current = getSubjects().toMutableList()
        val index = current.indexOfFirst { it.id == id }
        if (index != -1) {
            val old = current[index]
            current[index] = old.copy(emoji = newEmoji)
            saveSubjects(current)
        }
    }

    fun updateSubject(id: String, newName: String, newEmoji: String, newDescription: String) {
        val current = getSubjects().toMutableList()
        val index = current.indexOfFirst { it.id == id }
        if (index != -1) {
            val old = current[index]
            current[index] = old.copy(
                name = newName,
                emoji = if (newEmoji.isBlank()) old.emoji else newEmoji,
                description = newDescription
            )
            saveSubjects(current)
        }
    }

    fun deleteSubject(id: String): Boolean {
        if (id == DEFAULT_ANATOMY.id || id == DEFAULT_MICROBIOLOGY.id || id == DEFAULT_IMMUNOLOGY.id) return false // 内置学科不允许删除
        val current = getSubjects().toMutableList()
        val removed = current.removeAll { it.id == id }
        if (removed) {
            saveSubjects(current)
        }
        return removed
    }

    fun getViewMode(): SubjectViewMode {
        val modeStr = prefs.getString(KEY_VIEW_MODE, SubjectViewMode.GRID.name)
        return try {
            SubjectViewMode.valueOf(modeStr ?: SubjectViewMode.GRID.name)
        } catch (_: Exception) {
            SubjectViewMode.GRID
        }
    }

    fun setViewMode(mode: SubjectViewMode) {
        prefs.edit().putString(KEY_VIEW_MODE, mode.name).apply()
    }

    fun getLastSelectedSubjectId(): String? {
        return prefs.getString(KEY_LAST_SUBJECT_ID, null)
    }

    fun setLastSelectedSubjectId(id: String) {
        prefs.edit().putString(KEY_LAST_SUBJECT_ID, id).apply()
    }
}
