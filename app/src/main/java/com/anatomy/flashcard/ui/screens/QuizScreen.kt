package com.anatomy.flashcard.ui.screens

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.scaleIn
import androidx.compose.animation.scaleOut
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.border
import androidx.compose.foundation.gestures.detectVerticalDragGestures
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.input.ImeAction
import com.anatomy.flashcard.R
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.automirrored.filled.ArrowForward
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.EmojiEvents
import androidx.compose.material.icons.filled.HelpOutline
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.KeyboardArrowUp
import androidx.compose.material.icons.filled.Refresh
import androidx.compose.material.icons.filled.SkipNext
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.BottomSheetDefaults
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.OutlinedTextFieldDefaults
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateMapOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.anatomy.flashcard.data.QuizSessionState
import com.anatomy.flashcard.ui.components.MarkdownText
import com.anatomy.flashcard.ui.motion.motionPressEffect
import com.anatomy.flashcard.ui.motion.popInEntrance
import com.anatomy.flashcard.ui.motion.MotionSpecs
import com.anatomy.flashcard.model.QuizQuestion
import com.anatomy.flashcard.model.QuizSet
import com.anatomy.flashcard.ui.theme.AppBackground
import com.anatomy.flashcard.ui.theme.AppCardBg
import com.anatomy.flashcard.ui.theme.AppSurface
import com.anatomy.flashcard.ui.theme.CardBorder
import com.anatomy.flashcard.ui.theme.ChipBg
import com.anatomy.flashcard.ui.theme.GoogleBlue
import com.anatomy.flashcard.ui.theme.GoogleBlueLight
import com.anatomy.flashcard.ui.theme.GotItGreen
import com.anatomy.flashcard.ui.theme.GotItGreenBg
import com.anatomy.flashcard.ui.theme.GotItGreenBorder
import com.anatomy.flashcard.ui.theme.MissedItRed
import com.anatomy.flashcard.ui.theme.MissedItRedBg
import com.anatomy.flashcard.ui.theme.MissedItRedBorder
import com.anatomy.flashcard.ui.theme.SurfaceLight
import com.anatomy.flashcard.ui.theme.TextPrimary
import com.anatomy.flashcard.ui.theme.TextSecondary

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun QuizScreen(
    quizSet: QuizSet,
    initialSession: QuizSessionState? = null,
    onSaveSession: (QuizSessionState) -> Unit = {},
    onClearSession: () -> Unit = {},
    onFinishQuiz: (score: Int, total: Int, wrongIds: Set<Int>) -> Unit,
    onBack: () -> Unit,
    modifier: Modifier = Modifier
) {
    val initialIdx = (initialSession?.currentIndex ?: 0).coerceIn(0, (quizSet.questions.size - 1).coerceAtLeast(0))
    var currentIndex by remember { mutableIntStateOf(initialIdx) }
    // questionIndex -> set of selected option indices
    val userSelections = remember {
        mutableStateMapOf<Int, Set<Int>>().apply {
            initialSession?.userSelections?.let { putAll(it) }
        }
    }
    // "${questionIndex}_${blankIndex}" -> user input text
    val userBlankInputs = remember {
        mutableStateMapOf<String, String>().apply {
            initialSession?.userBlankInputs?.let { putAll(it) }
        }
    }
    // questionIndex -> is fill blank answered correctly
    val fillBlankCorrect = remember {
        mutableStateMapOf<Int, Boolean>().apply {
            initialSession?.fillBlankCorrect?.let { putAll(it) }
        }
    }
    // questionIndex -> is submitted for this question
    val submittedQuestions = remember {
        mutableStateMapOf<Int, Boolean>().apply {
            initialSession?.submittedQuestions?.let { putAll(it) }
            // Ensure any single-choice/judge questions with existing selection are marked submitted
            initialSession?.userSelections?.forEach { (idx, sel) ->
                if (sel.isNotEmpty()) {
                    val q = quizSet.questions.getOrNull(idx)
                    if (q != null && !q.isMultiSelect && !q.isFillBlank) {
                        put(idx, true)
                    }
                }
            }
        }
    }
    var isQuizCompleted by remember { mutableStateOf(false) }
    var showResumePromptDialog by remember {
        mutableStateOf(
            initialSession != null &&
                    (initialSession.currentIndex > 0 ||
                            initialSession.submittedQuestions.isNotEmpty() ||
                            initialSession.userSelections.isNotEmpty())
        )
    }
    var showQuestionBoard by remember { mutableStateOf(false) }
    var showConfirmSubmitDialog by remember { mutableStateOf(false) }

    fun isQuestionAnswered(idx: Int): Boolean {
        if (idx !in quizSet.questions.indices) return false
        val q = quizSet.questions[idx]
        return if (q.isFillBlank || q.isMultiSelect) {
            submittedQuestions[idx] == true
        } else {
            (userSelections[idx]?.size ?: 0) > 0
        }
    }

    fun isQuestionCorrect(idx: Int): Boolean? {
        if (!isQuestionAnswered(idx)) return null
        val q = quizSet.questions[idx]
        return if (q.isFillBlank) {
            fillBlankCorrect[idx] == true
        } else {
            (userSelections[idx] ?: emptySet()) == q.correctIndices.toSet()
        }
    }

    val answeredCount = quizSet.questions.indices.count { isQuestionAnswered(it) }
    val unansweredCount = quizSet.questions.size - answeredCount
    val hasUnanswered = unansweredCount > 0

    fun submitQuiz() {
        val correct = quizSet.questions.indices.count { i ->
            val q = quizSet.questions[i]
            if (q.isFillBlank) {
                fillBlankCorrect[i] == true
            } else {
                (userSelections[i] ?: emptySet()) == q.correctIndices.toSet()
            }
        }
        val wrongIds = quizSet.questions.indices.filter { i ->
            val q = quizSet.questions[i]
            if (q.isFillBlank) {
                fillBlankCorrect[i] != true
            } else {
                (userSelections[i] ?: emptySet()) != q.correctIndices.toSet()
            }
        }.map { quizSet.questions[it].id }.toSet()
        onFinishQuiz(correct, quizSet.questions.size, wrongIds)
        isQuizCompleted = true
    }

    var saveVersion by remember { mutableIntStateOf(0) }

    fun getCurrentSessionState() = QuizSessionState(
        quizId = quizSet.id,
        currentIndex = currentIndex,
        userSelections = userSelections.toMap(),
        userBlankInputs = userBlankInputs.toMap(),
        fillBlankCorrect = fillBlankCorrect.toMap(),
        submittedQuestions = submittedQuestions.toMap()
    )

    fun persistSessionNow() {
        if (!isQuizCompleted) {
            onSaveSession(getCurrentSessionState())
        }
    }

    fun notifyDataChanged() {
        saveVersion++
        persistSessionNow()
    }

    // Save on disposal (when navigating away or app backgrounded)
    DisposableEffect(quizSet.id) {
        onDispose {
            persistSessionNow()
        }
    }

    // Auto-save on progress or interaction updates
    LaunchedEffect(currentIndex, saveVersion) {
        persistSessionNow()
    }

    val currentQuestion = quizSet.questions.getOrNull(currentIndex)
    val currentSelected = userSelections[currentIndex] ?: emptySet()
    val isCurrentAnswered = submittedQuestions[currentIndex] == true

    if (isQuizCompleted || currentQuestion == null) {
        val correctCount = quizSet.questions.indices.count { i ->
            val q = quizSet.questions[i]
            if (q.isFillBlank) {
                fillBlankCorrect[i] == true
            } else {
                val selected = userSelections[i] ?: emptySet()
                selected == q.correctIndices.toSet()
            }
        }
        val wrongIds = quizSet.questions.indices.filter { i ->
            val q = quizSet.questions[i]
            if (q.isFillBlank) {
                fillBlankCorrect[i] != true
            } else {
                val selected = userSelections[i] ?: emptySet()
                selected != q.correctIndices.toSet()
            }
        }.map { quizSet.questions[it].id }.toSet()

        QuizResultView(
            title = quizSet.title,
            correctCount = correctCount,
            totalCount = quizSet.questions.size,
            onRetryAll = {
                onClearSession()
                userSelections.clear()
                userBlankInputs.clear()
                fillBlankCorrect.clear()
                submittedQuestions.clear()
                currentIndex = 0
                isQuizCompleted = false
                showResumePromptDialog = false
            },
            onBack = onBack
        )
        return
    }

    val progress by animateFloatAsState(
        targetValue = (currentIndex + 1).toFloat() / quizSet.questions.size.toFloat(),
        label = "QuizProgress"
    )

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Column {
                        Text(
                            text = quizSet.title,
                            fontSize = 17.sp,
                            fontWeight = FontWeight.Bold,
                            color = TextPrimary
                        )
                        Text(
                            text = "第 ${currentIndex + 1} 题 / 共 ${quizSet.questions.size} 题",
                            fontSize = 12.sp,
                            color = TextSecondary
                        )
                    }
                },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(
                            imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                            contentDescription = "返回",
                            tint = TextPrimary
                        )
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = AppSurface)
            )
        },
        containerColor = AppBackground,
        modifier = modifier
    ) { innerPadding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
                .padding(horizontal = 20.dp, vertical = 8.dp),
            verticalArrangement = Arrangement.SpaceBetween
        ) {
            // Progress Bar
            LinearProgressIndicator(
                progress = { progress },
                color = GoogleBlue,
                trackColor = Color(0xFFE0E3E7),
                modifier = Modifier
                    .fillMaxWidth()
                    .height(4.dp)
            )

            // 异常退出再次进入时的恢复提示对话框 (不再在顶部常驻显示 Banner)
            if (showResumePromptDialog) {
                AlertDialog(
                    onDismissRequest = { showResumePromptDialog = false },
                    title = {
                        Text(
                            text = "恢复作答进度",
                            fontWeight = FontWeight.Bold,
                            color = TextPrimary
                        )
                    },
                    text = {
                        Text(
                            text = "检测到上次未完成的作答进度（已作答至第 ${(initialSession?.currentIndex ?: 0) + 1} 题）。\n请选择继续上次作答还是从头开始？",
                            color = TextSecondary,
                            lineHeight = 20.sp
                        )
                    },
                    confirmButton = {
                        Button(
                            onClick = { showResumePromptDialog = false },
                            colors = ButtonDefaults.buttonColors(containerColor = GoogleBlue)
                        ) {
                            Text("继续作答")
                        }
                    },
                    dismissButton = {
                        TextButton(
                            onClick = {
                                showResumePromptDialog = false
                                onClearSession()
                                userSelections.clear()
                                userBlankInputs.clear()
                                fillBlankCorrect.clear()
                                submittedQuestions.clear()
                                currentIndex = 0
                                notifyDataChanged()
                            }
                        ) {
                            Text("从头开始", color = MissedItRed, fontWeight = FontWeight.SemiBold)
                        }
                    }
                )
            }

            Spacer(modifier = Modifier.height(14.dp))

            // Scrollable Question & Options with Floating Action Button
            Box(
                modifier = Modifier
                    .weight(1f)
                    .fillMaxWidth()
            ) {
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .verticalScroll(rememberScrollState())
                        .padding(bottom = 76.dp)
                ) {
                // Type badge & Topic tags
                Row(
                    modifier = Modifier.padding(bottom = 10.dp),
                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    val isDarkTheme = isSystemInDarkTheme()
                    val badgeText = when {
                        currentQuestion.isFillBlank -> "填空自测"
                        currentQuestion.isMultiSelect -> "多选题"
                        currentQuestion.isJudge -> "判断题"
                        else -> "单选题"
                    }
                    val badgeBg = if (isDarkTheme) {
                        when {
                            currentQuestion.isFillBlank -> Color(0xFF00796B).copy(alpha = 0.25f)
                            currentQuestion.isMultiSelect -> Color(0xFF673AB7).copy(alpha = 0.25f)
                            currentQuestion.isJudge -> Color(0xFFE65100).copy(alpha = 0.25f)
                            else -> GoogleBlue.copy(alpha = 0.25f)
                        }
                    } else {
                        when {
                            currentQuestion.isFillBlank -> Color(0xFFE0F2F1)
                            currentQuestion.isMultiSelect -> Color(0xFFEDE7F6)
                            currentQuestion.isJudge -> Color(0xFFFFF3E0)
                            else -> Color(0xFFE8F0FE)
                        }
                    }
                    val badgeTextColor = if (isDarkTheme) {
                        when {
                            currentQuestion.isFillBlank -> Color(0xFF80CBC4)
                            currentQuestion.isMultiSelect -> Color(0xFFD1C4E9)
                            currentQuestion.isJudge -> Color(0xFFFFB74D)
                            else -> GoogleBlueLight
                        }
                    } else {
                        when {
                            currentQuestion.isFillBlank -> Color(0xFF00796B)
                            currentQuestion.isMultiSelect -> Color(0xFF673AB7)
                            currentQuestion.isJudge -> Color(0xFFE65100)
                            else -> GoogleBlue
                        }
                    }

                    Surface(
                        shape = RoundedCornerShape(6.dp),
                        color = badgeBg
                    ) {
                        Text(
                            text = badgeText,
                            fontSize = 11.sp,
                            fontWeight = FontWeight.Bold,
                            color = badgeTextColor,
                            modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                        )
                    }
                }

                // Question Title
                MarkdownText(
                    text = "${currentIndex + 1}. ${currentQuestion.question}",
                    fontSize = 17.sp,
                    fontWeight = FontWeight.Bold,
                    color = TextPrimary,
                    lineHeight = 25.sp,
                    modifier = Modifier.padding(bottom = 18.dp)
                )

                val optionPrefixes = listOf("A", "B", "C", "D", "E", "F")
                val isDark = isSystemInDarkTheme()

                if (currentQuestion.isFillBlank) {
                    // Fill-in-the-blank Question Card UI
                    val blankAnswers = currentQuestion.blankAnswers

                    Column(
                        modifier = Modifier.fillMaxWidth(),
                        verticalArrangement = Arrangement.spacedBy(10.dp)
                    ) {
                        blankAnswers.forEachIndexed { bIdx, standardAns ->
                            val blankKey = "${currentIndex}_$bIdx"
                            val userText = userBlankInputs[blankKey] ?: ""
                            val isMatched = isFillBlankMatched(userText, standardAns)

                            Card(
                                shape = RoundedCornerShape(14.dp),
                                colors = CardDefaults.cardColors(
                                    containerColor = when {
                                        !isCurrentAnswered -> AppCardBg
                                        isMatched -> GotItGreenBg
                                        else -> MissedItRedBg
                                    }
                                ),
                                border = BorderStroke(
                                    1.2.dp,
                                    when {
                                        !isCurrentAnswered -> CardBorder
                                        isMatched -> GotItGreen
                                        else -> MissedItRed
                                    }
                                ),
                                modifier = Modifier.fillMaxWidth()
                            ) {
                                Column(modifier = Modifier.padding(12.dp)) {
                                    Row(
                                        verticalAlignment = Alignment.CenterVertically,
                                        horizontalArrangement = Arrangement.SpaceBetween,
                                        modifier = Modifier.fillMaxWidth()
                                    ) {
                                        Surface(
                                            shape = RoundedCornerShape(6.dp),
                                            color = if (isDark) Color(0xFF004D40) else Color(0xFFE0F2F1)
                                        ) {
                                            Text(
                                                text = "空 (${bIdx + 1})",
                                                fontSize = 12.sp,
                                                fontWeight = FontWeight.Bold,
                                                color = if (isDark) Color(0xFF80CBC4) else Color(0xFF00796B),
                                                modifier = Modifier.padding(horizontal = 8.dp, vertical = 3.dp)
                                            )
                                        }

                                        if (isCurrentAnswered) {
                                            Row(verticalAlignment = Alignment.CenterVertically) {
                                                Icon(
                                                    imageVector = if (isMatched) Icons.Default.Check else Icons.Default.Close,
                                                    contentDescription = null,
                                                    tint = if (isMatched) GotItGreen else MissedItRed,
                                                    modifier = Modifier.size(16.dp)
                                                )
                                                Spacer(modifier = Modifier.width(4.dp))
                                                Text(
                                                    text = if (isMatched) "作答正确" else "待强化",
                                                    fontSize = 12.sp,
                                                    fontWeight = FontWeight.Bold,
                                                    color = if (isMatched) GotItGreen else MissedItRed
                                                )
                                            }
                                        }
                                    }

                                    Spacer(modifier = Modifier.height(8.dp))

                                    if (!isCurrentAnswered) {
                                        OutlinedTextField(
                                            value = userText,
                                            onValueChange = { newVal ->
                                                userBlankInputs[blankKey] = newVal
                                                notifyDataChanged()
                                            },
                                            placeholder = { Text("在此输入作答（可简写或留空）", fontSize = 13.5.sp, color = TextSecondary) },
                                            singleLine = true,
                                            shape = RoundedCornerShape(10.dp),
                                            colors = OutlinedTextFieldDefaults.colors(
                                                focusedTextColor = TextPrimary,
                                                unfocusedTextColor = TextPrimary,
                                                focusedBorderColor = GoogleBlue,
                                                unfocusedBorderColor = CardBorder,
                                                focusedContainerColor = AppSurface,
                                                unfocusedContainerColor = AppSurface,
                                                cursorColor = GoogleBlue
                                            ),
                                            keyboardOptions = KeyboardOptions(
                                                imeAction = if (bIdx < blankAnswers.size - 1) ImeAction.Next else ImeAction.Done
                                            ),
                                            modifier = Modifier.fillMaxWidth()
                                        )
                                    } else {
                                        Column(verticalArrangement = Arrangement.spacedBy(4.dp)) {
                                            if (userText.isNotBlank()) {
                                                Row {
                                                    Text("你的作答：", fontSize = 13.sp, color = TextSecondary)
                                                    Text(
                                                        text = userText,
                                                        fontSize = 13.5.sp,
                                                        fontWeight = FontWeight.Medium,
                                                        color = if (isMatched) GotItGreen else MissedItRed
                                                    )
                                                }
                                            }
                                            Row {
                                                Text("标准参考：", fontSize = 13.sp, color = TextSecondary)
                                                Text(
                                                    text = standardAns,
                                                    fontSize = 13.5.sp,
                                                    fontWeight = FontWeight.Bold,
                                                    color = GotItGreen
                                                )
                                            }
                                        }
                                    }
                                }
                            }
                        }

                        if (!isCurrentAnswered) {
                            Spacer(modifier = Modifier.height(10.dp))
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.End
                            ) {
                                Text(
                                    text = "不作答直接看参考答案",
                                    fontSize = 12.sp,
                                    color = TextSecondary,
                                    modifier = Modifier
                                        .clickable {
                                            fillBlankCorrect[currentIndex] = false
                                            submittedQuestions[currentIndex] = true
                                            notifyDataChanged()
                                        }
                                        .padding(horizontal = 6.dp, vertical = 4.dp)
                                )
                            }
                        }
                    }
                } else {
                    // Option Cards for Single / Multiple Choice
                    currentQuestion.options.forEachIndexed { optIndex, option ->
                        val isSelected = currentSelected.contains(optIndex)
                        val isCorrect = option.isCorrect

                        val (containerColor, borderColor, textColor) = when {
                            !isCurrentAnswered -> {
                                if (isSelected) Triple(
                                    if (isDark) GoogleBlue.copy(alpha = 0.25f) else Color(0xFFE8F0FE),
                                    GoogleBlue,
                                    if (isDark) GoogleBlueLight else GoogleBlue
                                )
                                else Triple(AppCardBg, CardBorder, TextPrimary)
                            }
                            isCorrect -> Triple(GotItGreenBg, GotItGreen, GotItGreen)
                            isSelected && !isCorrect -> Triple(MissedItRedBg, MissedItRed, MissedItRed)
                            else -> Triple(ChipBg, CardBorder, TextSecondary)
                        }

                        Card(
                            shape = RoundedCornerShape(16.dp),
                            colors = CardDefaults.cardColors(containerColor = containerColor),
                            border = BorderStroke(1.5.dp, borderColor),
                            elevation = CardDefaults.cardElevation(defaultElevation = if (isSelected) 3.dp else 0.5.dp),
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(vertical = 5.dp)
                                .then(
                                    if (!isCurrentAnswered) {
                                        Modifier.motionPressEffect(pressedScale = 0.97f) {
                                            if (currentQuestion.isMultiSelect) {
                                                val newSet = currentSelected.toMutableSet()
                                                if (isSelected) newSet.remove(optIndex) else newSet.add(optIndex)
                                                userSelections[currentIndex] = newSet
                                                notifyDataChanged()
                                            } else {
                                                userSelections[currentIndex] = setOf(optIndex)
                                                submittedQuestions[currentIndex] = true
                                                notifyDataChanged()
                                            }
                                        }
                                    } else Modifier
                                )
                        ) {
                            Column(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .padding(14.dp)
                            ) {
                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    Surface(
                                        shape = CircleShape,
                                        color = when {
                                            isCurrentAnswered && isCorrect -> GotItGreen
                                            isCurrentAnswered && isSelected -> MissedItRed
                                            isSelected -> GoogleBlue
                                            else -> ChipBg
                                        },
                                        modifier = Modifier.size(30.dp)
                                    ) {
                                        Box(contentAlignment = Alignment.Center) {
                                            val prefixText = if (currentQuestion.isJudge) {
                                                if (option.text.contains("正确") || option.text.contains("对") || option.text.contains("√")) "√" else "×"
                                            } else {
                                                optionPrefixes.getOrElse(optIndex) { "${optIndex + 1}" }
                                            }
                                            Text(
                                                text = prefixText,
                                                fontSize = 13.sp,
                                                fontWeight = FontWeight.Bold,
                                                color = if (isSelected || (isCurrentAnswered && (isCorrect || isSelected))) Color.White else TextPrimary
                                            )
                                        }
                                    }

                                    Spacer(modifier = Modifier.width(12.dp))

                                    MarkdownText(
                                        text = option.text,
                                        fontSize = 14.5.sp,
                                        color = textColor,
                                        lineHeight = 21.sp,
                                        modifier = Modifier.weight(1f)
                                    )
                                }

                                // Rationale (Shown after submission)
                                if (isCurrentAnswered && option.rationale.isNotEmpty()) {
                                    Spacer(modifier = Modifier.height(8.dp))
                                    MarkdownText(
                                        text = "解析：${option.rationale}",
                                        fontSize = 12.sp,
                                        color = if (isCorrect) GotItGreen else TextSecondary,
                                        lineHeight = 18.sp,
                                        modifier = Modifier.padding(start = 42.dp)
                                    )
                                }
                            }
                        }
                    }


                }

                // Hint / Summary Box
                AnimatedVisibility(visible = isCurrentAnswered) {
                    val isUserAllCorrect = if (currentQuestion.isFillBlank) {
                        fillBlankCorrect[currentIndex] == true
                    } else {
                        currentSelected == currentQuestion.correctIndices.toSet()
                    }
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(top = 16.dp)
                    ) {
                        Card(
                            shape = RoundedCornerShape(16.dp),
                            colors = CardDefaults.cardColors(
                                containerColor = if (isUserAllCorrect) GotItGreenBg else MissedItRedBg
                            ),
                            border = BorderStroke(1.dp, if (isUserAllCorrect) GotItGreenBorder else MissedItRedBorder),
                            modifier = Modifier
                                .fillMaxWidth()
                                .popInEntrance()
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    Icon(
                                        imageVector = if (isUserAllCorrect) Icons.Default.CheckCircle else Icons.Default.Info,
                                        contentDescription = null,
                                        tint = if (isUserAllCorrect) GotItGreen else MissedItRed,
                                        modifier = Modifier.size(20.dp)
                                    )
                                    Spacer(modifier = Modifier.width(8.dp))
                                    val statusMsg = when {
                                        currentQuestion.isFillBlank -> if (isUserAllCorrect) "填空全部回答正确！" else "已核对参考答案，请注意专有名词的标准书写"
                                        isUserAllCorrect -> "回答完全正确！"
                                        else -> {
                                            val correctLetters = currentQuestion.correctIndices.map { optionPrefixes.getOrElse(it) { "" } }.joinToString(", ")
                                            "回答错误，正确答案是：$correctLetters"
                                        }
                                    }
                                    Text(
                                        text = statusMsg,
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 14.sp,
                                        color = if (isUserAllCorrect) GotItGreen else MissedItRed
                                    )
                                }

                                val fullRationale = if (currentQuestion.rationale.isNotBlank()) currentQuestion.rationale else ""
                                if (fullRationale.isNotBlank()) {
                                    Spacer(modifier = Modifier.height(8.dp))
                                    MarkdownText(
                                        text = fullRationale,
                                        fontSize = 13.sp,
                                        color = TextPrimary,
                                        lineHeight = 19.sp
                                    )
                                }

                                if (currentQuestion.hint.isNotEmpty()) {
                                    Spacer(modifier = Modifier.height(8.dp))
                                    Row(verticalAlignment = Alignment.Top) {
                                        Icon(
                                            imageVector = Icons.Default.HelpOutline,
                                            contentDescription = null,
                                            tint = TextSecondary,
                                            modifier = Modifier.size(16.dp).padding(top = 2.dp)
                                        )
                                        Spacer(modifier = Modifier.width(6.dp))
                                        MarkdownText(
                                            text = "思考提示：${currentQuestion.hint}",
                                            fontSize = 12.5.sp,
                                            color = TextSecondary,
                                            lineHeight = 18.sp
                                        )
                                    }
                                }
                            }
                        }
                    }
                }
            }

                // 右下角悬浮对号确认提交圆角矩形按钮 (仅多选或填空未提交时展示)
                val showFloatingSubmit = (currentQuestion.isFillBlank || currentQuestion.isMultiSelect) && !isCurrentAnswered
                val isSubmitEnabled = if (currentQuestion.isMultiSelect) currentSelected.isNotEmpty() else true

                if (showFloatingSubmit) {
                    Surface(
                        onClick = {
                            if (isSubmitEnabled) {
                                if (currentQuestion.isMultiSelect) {
                                    submittedQuestions[currentIndex] = true
                                    notifyDataChanged()
                                } else if (currentQuestion.isFillBlank) {
                                    val allMatch = currentQuestion.blankAnswers.indices.all { bIdx ->
                                        val userVal = userBlankInputs["${currentIndex}_$bIdx"] ?: ""
                                        isFillBlankMatched(userVal, currentQuestion.blankAnswers[bIdx])
                                    }
                                    fillBlankCorrect[currentIndex] = allMatch
                                    submittedQuestions[currentIndex] = true
                                    notifyDataChanged()
                                }
                            }
                        },
                        enabled = isSubmitEnabled,
                        shape = RoundedCornerShape(18.dp),
                        color = if (isSubmitEnabled) GoogleBlue else GoogleBlue.copy(alpha = 0.35f),
                        shadowElevation = 6.dp,
                        modifier = Modifier
                            .align(Alignment.BottomEnd)
                            .padding(bottom = 14.dp, end = 6.dp)
                            .size(56.dp)
                            .popInEntrance()
                            .motionPressEffect(pressedScale = 0.92f)
                    ) {
                        Box(contentAlignment = Alignment.Center) {
                            Icon(
                                imageVector = Icons.Default.Check,
                                contentDescription = "确认提交",
                                tint = Color.White,
                                modifier = Modifier.size(28.dp)
                            )
                        }
                    }
                }
            }

            // Bottom Navigation & Question Board Panel (上一题 + 正方形题板按钮 + 下一题/跳过)
            val isLastQuestion = currentIndex >= quizSet.questions.size - 1

            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .pointerInput(Unit) {
                        detectVerticalDragGestures { _, dragAmount ->
                            // 上滑超过 15dp 自动展开题板
                            if (dragAmount < -15f) {
                                showQuestionBoard = true
                            }
                        }
                    }
                    .padding(vertical = 10.dp),
                horizontalArrangement = Arrangement.spacedBy(10.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                // 1. 上一题
                OutlinedButton(
                    onClick = {
                        if (currentIndex > 0) {
                            currentIndex--
                            persistSessionNow()
                        }
                    },
                    enabled = currentIndex > 0,
                    shape = RoundedCornerShape(16.dp),
                    border = BorderStroke(1.dp, CardBorder),
                    modifier = Modifier
                        .weight(1f)
                        .height(50.dp)
                ) {
                    Icon(
                        imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                        contentDescription = null,
                        modifier = Modifier.size(16.dp)
                    )
                    Spacer(modifier = Modifier.width(6.dp))
                    Text("上一题", maxLines = 1, fontWeight = FontWeight.SemiBold)
                }

                // 2. 中间正方形题板按钮 (50dp x 50dp，使用 receipt_long SVG 图标)
                Surface(
                    onClick = { showQuestionBoard = true },
                    shape = RoundedCornerShape(16.dp),
                    color = AppSurface,
                    border = BorderStroke(1.dp, CardBorder),
                    modifier = Modifier
                        .size(50.dp)
                        .motionPressEffect(pressedScale = 0.94f)
                ) {
                    Box(contentAlignment = Alignment.Center) {
                        Icon(
                            painter = painterResource(id = R.drawable.ic_receipt_long),
                            contentDescription = "答题卡题板",
                            tint = if (isSystemInDarkTheme()) GoogleBlueLight else GoogleBlue,
                            modifier = Modifier.size(24.dp)
                        )
                    }
                }

                // 3. 下一题 / 跳过此题 / 交卷
                if (!isCurrentAnswered) {
                    // 未作答状态：支持跳过此题进入下一题！
                    Button(
                        onClick = {
                            if (isLastQuestion) {
                                if (hasUnanswered) {
                                    showConfirmSubmitDialog = true
                                } else {
                                    submitQuiz()
                                }
                            } else {
                                currentIndex++
                                persistSessionNow()
                            }
                        },
                        shape = RoundedCornerShape(16.dp),
                        colors = ButtonDefaults.buttonColors(
                            containerColor = if (isLastQuestion) MissedItRed.copy(alpha = 0.12f) else GoogleBlue.copy(alpha = 0.12f),
                            contentColor = if (isLastQuestion) MissedItRed else GoogleBlue
                        ),
                        border = BorderStroke(1.dp, if (isLastQuestion) MissedItRedBorder else GoogleBlue.copy(alpha = 0.3f)),
                        modifier = Modifier
                            .weight(1f)
                            .height(50.dp)
                    ) {
                        Text(
                            text = if (isLastQuestion) "交卷 (未答 $unansweredCount)" else "跳过此题",
                            maxLines = 1,
                            fontWeight = FontWeight.Bold
                        )
                        Spacer(modifier = Modifier.width(6.dp))
                        Icon(
                            imageVector = if (isLastQuestion) Icons.Default.Check else Icons.Filled.SkipNext,
                            contentDescription = null,
                            modifier = Modifier.size(16.dp)
                        )
                    }
                } else {
                    // 已作答状态：标准下一题或交卷
                    Button(
                        onClick = {
                            if (isLastQuestion) {
                                if (hasUnanswered) {
                                    showConfirmSubmitDialog = true
                                } else {
                                    submitQuiz()
                                }
                            } else {
                                currentIndex++
                                persistSessionNow()
                            }
                        },
                        shape = RoundedCornerShape(16.dp),
                        colors = ButtonDefaults.buttonColors(
                            containerColor = if (isLastQuestion && !hasUnanswered) GotItGreen else GoogleBlue
                        ),
                        modifier = Modifier
                            .weight(1f)
                            .height(50.dp)
                    ) {
                        Text(
                            text = if (isLastQuestion) {
                                if (hasUnanswered) "交卷 (未答 $unansweredCount)" else "完成交卷"
                            } else "下一题",
                            maxLines = 1,
                            fontWeight = FontWeight.Bold
                        )
                        Spacer(modifier = Modifier.width(6.dp))
                        Icon(
                            imageVector = if (isLastQuestion) Icons.Default.Check else Icons.AutoMirrored.Filled.ArrowForward,
                            contentDescription = null,
                            modifier = Modifier.size(16.dp)
                        )
                    }
                }
            }

            // 未答题目交卷确认弹窗
            if (showConfirmSubmitDialog) {
                AlertDialog(
                    onDismissRequest = { showConfirmSubmitDialog = false },
                    title = {
                        Text(
                            text = "提前交卷确认",
                            fontWeight = FontWeight.Bold,
                            color = TextPrimary
                        )
                    },
                    text = {
                        Text(
                            text = "当前尚有 $unansweredCount 道题目未作答（已跳过）。\n确定要现在提交小测吗？未作答题目将被计为未完成。",
                            color = TextSecondary,
                            lineHeight = 20.sp
                        )
                    },
                    confirmButton = {
                        Button(
                            onClick = {
                                showConfirmSubmitDialog = false
                                val firstUnanswered = quizSet.questions.indices.firstOrNull { !isQuestionAnswered(it) }
                                if (firstUnanswered != null) {
                                    currentIndex = firstUnanswered
                                    persistSessionNow()
                                }
                            },
                            colors = ButtonDefaults.buttonColors(containerColor = GoogleBlue)
                        ) {
                            Text("去补做未答题")
                        }
                    },
                    dismissButton = {
                        TextButton(
                            onClick = {
                                showConfirmSubmitDialog = false
                                submitQuiz()
                            }
                        ) {
                            Text("坚持交卷", color = MissedItRed, fontWeight = FontWeight.SemiBold)
                        }
                    }
                )
            }

            // 题板底部抽屉 (ModalBottomSheet)
            if (showQuestionBoard) {
                ModalBottomSheet(
                    onDismissRequest = { showQuestionBoard = false },
                    containerColor = AppBackground,
                    dragHandle = { BottomSheetDefaults.DragHandle() }
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(horizontal = 20.dp, vertical = 4.dp)
                    ) {
                        // 头部标题与统计
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Column {
                                Text(
                                    text = "答题卡题板",
                                    fontSize = 18.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = TextPrimary
                                )
                                Spacer(modifier = Modifier.height(2.dp))
                                Text(
                                    text = "已完成 $answeredCount · 未答/跳过 $unansweredCount · 全套 ${quizSet.questions.size} 题",
                                    fontSize = 12.sp,
                                    color = TextSecondary
                                )
                            }

                            Button(
                                onClick = {
                                    showQuestionBoard = false
                                    if (hasUnanswered) {
                                        showConfirmSubmitDialog = true
                                    } else {
                                        submitQuiz()
                                    }
                                },
                                colors = ButtonDefaults.buttonColors(
                                    containerColor = if (hasUnanswered) MissedItRed else GoogleBlue
                                ),
                                shape = RoundedCornerShape(12.dp),
                                modifier = Modifier.height(36.dp)
                            ) {
                                Text("立即交卷", fontSize = 12.5.sp, fontWeight = FontWeight.Bold)
                            }
                        }

                        Spacer(modifier = Modifier.height(12.dp))

                        // 图例行 (Legend)
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .background(AppSurface, RoundedCornerShape(10.dp))
                                .border(1.dp, CardBorder, RoundedCornerShape(10.dp))
                                .padding(horizontal = 12.dp, vertical = 8.dp),
                            horizontalArrangement = Arrangement.SpaceAround,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Box(
                                    modifier = Modifier
                                        .size(12.dp)
                                        .background(GoogleBlue.copy(alpha = 0.2f), CircleShape)
                                        .border(1.5.dp, GoogleBlue, CircleShape)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text("当前", fontSize = 11.sp, color = TextSecondary)
                            }

                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Box(
                                    modifier = Modifier
                                        .size(12.dp)
                                        .background(GotItGreen, CircleShape)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text("正确", fontSize = 11.sp, color = TextSecondary)
                            }

                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Box(
                                    modifier = Modifier
                                        .size(12.dp)
                                        .background(MissedItRed, CircleShape)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text("错误", fontSize = 11.sp, color = TextSecondary)
                            }

                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Box(
                                    modifier = Modifier
                                        .size(12.dp)
                                        .background(Color.Gray.copy(alpha = 0.25f), CircleShape)
                                        .border(1.dp, CardBorder, CircleShape)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text("未答/跳过", fontSize = 11.sp, color = TextSecondary)
                            }
                        }

                        Spacer(modifier = Modifier.height(14.dp))

                        // 题号网格 (6列)
                        LazyVerticalGrid(
                            columns = GridCells.Fixed(6),
                            modifier = Modifier
                                .fillMaxWidth()
                                .heightIn(max = 360.dp),
                            horizontalArrangement = Arrangement.spacedBy(8.dp),
                            verticalArrangement = Arrangement.spacedBy(8.dp)
                        ) {
                            items(quizSet.questions.size) { idx ->
                                val isCurrent = idx == currentIndex
                                val answered = isQuestionAnswered(idx)
                                val correct = isQuestionCorrect(idx)

                                val itemBg = when {
                                    isCurrent -> GoogleBlue.copy(alpha = 0.18f)
                                    correct == true -> GotItGreenBg
                                    correct == false -> MissedItRedBg
                                    answered -> GoogleBlue.copy(alpha = 0.1f)
                                    else -> AppSurface
                                }

                                val itemTextColor = when {
                                    isCurrent -> GoogleBlue
                                    correct == true -> GotItGreen
                                    correct == false -> MissedItRed
                                    answered -> GoogleBlue
                                    else -> TextSecondary
                                }

                                val itemBorder = when {
                                    isCurrent -> BorderStroke(2.dp, GoogleBlue)
                                    correct == true -> BorderStroke(1.dp, GotItGreenBorder)
                                    correct == false -> BorderStroke(1.dp, MissedItRedBorder)
                                    else -> BorderStroke(1.dp, CardBorder)
                                }

                                Surface(
                                    shape = RoundedCornerShape(12.dp),
                                    color = itemBg,
                                    border = itemBorder,
                                    modifier = Modifier
                                        .size(46.dp)
                                        .clickable {
                                            currentIndex = idx
                                            showQuestionBoard = false
                                            persistSessionNow()
                                        }
                                ) {
                                    Box(contentAlignment = Alignment.Center) {
                                        Text(
                                            text = "${idx + 1}",
                                            fontSize = 14.sp,
                                            fontWeight = if (isCurrent) FontWeight.Bold else FontWeight.Medium,
                                            color = itemTextColor
                                        )
                                    }
                                }
                            }
                        }

                        Spacer(modifier = Modifier.height(24.dp))
                    }
                }
            }
        }
    }
}

@Composable
fun QuizResultView(
    title: String,
    correctCount: Int,
    totalCount: Int,
    onRetryAll: () -> Unit,
    onBack: () -> Unit
) {
    val rate = if (totalCount > 0) (correctCount * 100 / totalCount) else 0

    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(AppBackground)
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.SpaceBetween
    ) {
        Spacer(modifier = Modifier.height(20.dp))

        Card(
            shape = RoundedCornerShape(32.dp),
            colors = CardDefaults.cardColors(containerColor = AppCardBg),
            border = BorderStroke(1.dp, CardBorder),
            elevation = CardDefaults.cardElevation(defaultElevation = 6.dp),
            modifier = Modifier.fillMaxWidth()
        ) {
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(32.dp),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Surface(
                    shape = CircleShape,
                    color = Color(0xFFFEF7E0),
                    modifier = Modifier.size(76.dp)
                ) {
                    Box(contentAlignment = Alignment.Center) {
                        Icon(
                            imageVector = Icons.Default.EmojiEvents,
                            contentDescription = null,
                            tint = Color(0xFFF9AB00),
                            modifier = Modifier.size(40.dp)
                        )
                    }
                }

                Spacer(modifier = Modifier.height(16.dp))

                Text(
                    text = "小测成绩单",
                    fontSize = 22.sp,
                    fontWeight = FontWeight.Bold,
                    color = TextPrimary
                )

                Text(
                    text = title,
                    fontSize = 14.sp,
                    color = TextSecondary,
                    modifier = Modifier.padding(top = 4.dp)
                )

                Spacer(modifier = Modifier.height(24.dp))

                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceEvenly
                ) {
                    Column(horizontalAlignment = Alignment.CenterHorizontally) {
                        Text(
                            text = "$correctCount",
                            fontSize = 24.sp,
                            fontWeight = FontWeight.Bold,
                            color = GotItGreen
                        )
                        Text(text = "答对", fontSize = 12.sp, color = TextSecondary)
                    }
                    Column(horizontalAlignment = Alignment.CenterHorizontally) {
                        Text(
                            text = "${totalCount - correctCount}",
                            fontSize = 24.sp,
                            fontWeight = FontWeight.Bold,
                            color = MissedItRed
                        )
                        Text(text = "答错", fontSize = 12.sp, color = TextSecondary)
                    }
                    Column(horizontalAlignment = Alignment.CenterHorizontally) {
                        Text(
                            text = "$rate%",
                            fontSize = 24.sp,
                            fontWeight = FontWeight.Bold,
                            color = GoogleBlue
                        )
                        Text(text = "正确率", fontSize = 12.sp, color = TextSecondary)
                    }
                }
            }
        }

        Column(
            modifier = Modifier.fillMaxWidth(),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            Button(
                onClick = onRetryAll,
                shape = RoundedCornerShape(16.dp),
                colors = ButtonDefaults.buttonColors(containerColor = GoogleBlue),
                modifier = Modifier
                    .fillMaxWidth()
                    .height(50.dp)
            ) {
                Icon(Icons.Default.Refresh, contentDescription = null)
                Spacer(modifier = Modifier.width(8.dp))
                Text("再做一次")
            }

            OutlinedButton(
                onClick = onBack,
                shape = RoundedCornerShape(16.dp),
                border = BorderStroke(1.dp, CardBorder),
                modifier = Modifier
                    .fillMaxWidth()
                    .height(50.dp)
            ) {
                Text("返回系统主页", color = TextPrimary)
            }
        }
    }
}

private fun isFillBlankMatched(user: String, standard: String): Boolean {
    val cleanUser = user.trim().lowercase()
    if (cleanUser.isEmpty()) return false
    val cleanStandard = standard.trim().lowercase()
    if (cleanUser == cleanStandard) return true
    val parts = cleanStandard.split("（", "）", "(", ")", "、", "/", "或", "，", ",")
        .map { it.trim() }
        .filter { it.isNotEmpty() }
    if (parts.any { it == cleanUser || cleanUser.contains(it) || it.contains(cleanUser) }) {
        return true
    }
    return false
}
