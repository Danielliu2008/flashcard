package com.anatomy.flashcard.model

data class Subject(
    val id: String,
    val name: String,
    val emoji: String,
    val description: String,
    val isBuiltIn: Boolean = false,
    val colorHex: Long = 0xFF1A73E8
)

enum class SubjectViewMode {
    GRID,
    LIST
}
