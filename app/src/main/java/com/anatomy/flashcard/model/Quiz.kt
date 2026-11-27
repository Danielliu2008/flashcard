package com.anatomy.flashcard.model

data class QuizOption(
    val text: String,
    val isCorrect: Boolean,
    val rationale: String = ""
)

data class QuizQuestion(
    val id: Int,
    val type: String, // "multiple_choice", "single_choice", "multiple_select", "judge", or "fill_in_blank"
    val question: String,
    val options: List<QuizOption> = emptyList(),
    val hint: String = "",
    val blankAnswers: List<String> = emptyList(),
    val rationale: String = ""
) {
    val isMultiSelect: Boolean get() = type == "multiple_select"
    val isFillBlank: Boolean get() = type == "fill_in_blank" || type == "fill_blank"
    val isJudge: Boolean get() = type == "judge" || question.startsWith("【判断题】") ||
            (options.size == 2 && options.any { it.text in listOf("正确", "对", "√") } && options.any { it.text in listOf("错误", "错", "×") })
    val correctIndices: List<Int> get() = options.mapIndexedNotNull { index, opt -> if (opt.isCorrect) index else null }
}

data class QuizSet(
    val id: String,
    val systemType: AnatomySystemType,
    val title: String,
    val description: String = "",
    val coveredTopics: List<String> = emptyList(),
    val questions: List<QuizQuestion>
) {
    val totalCount: Int get() = questions.size
}

data class QuizRecord(
    val quizId: String,
    val bestScore: Int = 0,
    val totalQuestions: Int = 0,
    val lastAttemptTime: Long = 0L,
    val wrongQuestionIds: Set<Int> = emptySet()
)
