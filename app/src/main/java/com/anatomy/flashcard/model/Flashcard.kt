package com.anatomy.flashcard.model

data class FlashcardContent(
    val type: String = "text",
    val content: String = "",
    val reference: String? = null,
    val alt: String? = null
)

data class Flashcard(
    val id: Int,
    val frontText: String,
    val backText: String,
    val categoryIndex: Int,
    val isImage: Boolean = false,
    val imageAlt: String? = null,
    val pointType: String = "",
    val starRating: String = "★★★",
    val importance: Int = 3
)

data class DeckTopics(
    val covered: List<String> = emptyList(),
    val followUp: List<String> = emptyList()
)

data class FlashcardDeck(
    val id: String,
    val filename: String,
    val title: String,
    val description: String,
    val iconName: String,
    val cards: List<Flashcard>,
    val topics: DeckTopics
)

enum class CardAcquisition {
    ACQUIRED,      // Got It
    NOT_ACQUIRED,  // Missed It
    UNSTUDIED      // 未学习
}

data class StudyProgress(
    val deckId: String,
    val currentIndex: Int = 0,
    val acquisitions: Map<Int, CardAcquisition> = emptyMap(),
    val isShuffled: Boolean = false,
    val shuffledIndices: List<Int> = emptyList(),
    val filterMissedOnly: Boolean = false
) {
    val acquiredCount: Int get() = acquisitions.values.count { it == CardAcquisition.ACQUIRED }
    val missedCount: Int get() = acquisitions.values.count { it == CardAcquisition.NOT_ACQUIRED }
}
