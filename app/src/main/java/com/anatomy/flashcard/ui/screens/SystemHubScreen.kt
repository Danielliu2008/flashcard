package com.anatomy.flashcard.ui.screens

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
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
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.AccountTree
import androidx.compose.material.icons.filled.Assignment
import androidx.compose.material.icons.filled.EmojiEvents
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material.icons.filled.Psychology
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SecondaryTabRow
import androidx.compose.material3.Surface
import androidx.compose.material3.Tab
import androidx.compose.material3.TabRowDefaults
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.anatomy.flashcard.data.QuizSessionState
import com.anatomy.flashcard.model.AnatomySystemType
import com.anatomy.flashcard.model.FlashcardDeck
import com.anatomy.flashcard.model.MindMapData
import com.anatomy.flashcard.model.QuizRecord
import com.anatomy.flashcard.model.QuizSet
import com.anatomy.flashcard.model.StudyProgress
import com.anatomy.flashcard.ui.components.InteractiveMindMapView
import com.anatomy.flashcard.ui.components.MarkdownText
import com.anatomy.flashcard.ui.theme.AppBackground
import com.anatomy.flashcard.ui.theme.AppCardBg
import com.anatomy.flashcard.ui.theme.AppSurface
import com.anatomy.flashcard.ui.theme.CardBorder
import com.anatomy.flashcard.ui.theme.ChipBg
import com.anatomy.flashcard.ui.theme.GoogleBlue
import com.anatomy.flashcard.ui.theme.GoogleBlueLight
import com.anatomy.flashcard.ui.theme.GotItGreen
import com.anatomy.flashcard.ui.theme.TextPrimary
import com.anatomy.flashcard.ui.theme.TextSecondary
import com.anatomy.flashcard.ui.theme.TextTertiary

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SystemHubScreen(
    systemType: AnatomySystemType,
    deck: FlashcardDeck?,
    deckProgress: StudyProgress?,
    quizSet: QuizSet?,
    quizRecord: QuizRecord?,
    quizSession: QuizSessionState? = null,
    mindMap: MindMapData?,
    initialTab: Int = 0,
    onStartFlashcards: () -> Unit,
    onStartQuiz: () -> Unit,
    onBack: () -> Unit,
    modifier: Modifier = Modifier
) {
    var selectedTab by remember(initialTab) { mutableIntStateOf(initialTab.coerceIn(0, 2)) }
    val tabTitles = listOf("闪卡复习", "单元小测", "知识导图")

    Scaffold(
        topBar = {
            Column {
                TopAppBar(
                    title = {
                        Column {
                            Text(
                                text = systemType.title,
                                fontWeight = FontWeight.Bold,
                                fontSize = 18.sp,
                                color = TextPrimary
                            )
                            Text(
                                text = systemType.subtitle,
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

                // 3 Tabs
                SecondaryTabRow(
                    selectedTabIndex = selectedTab,
                    containerColor = AppSurface,
                    indicator = {
                        TabRowDefaults.SecondaryIndicator(
                            color = GoogleBlue,
                            modifier = Modifier.tabIndicatorOffset(selectedTab)
                        )
                    }
                ) {
                    tabTitles.forEachIndexed { index, title ->
                        Tab(
                            selected = selectedTab == index,
                            onClick = { selectedTab = index },
                            text = {
                                Text(
                                    text = title,
                                    fontWeight = if (selectedTab == index) FontWeight.Bold else FontWeight.Normal,
                                    color = if (selectedTab == index) GoogleBlue else TextSecondary,
                                    fontSize = 14.sp
                                )
                            }
                        )
                    }
                }
            }
        },
        containerColor = AppBackground,
        modifier = modifier
    ) { innerPadding ->
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
        ) {
            when (selectedTab) {
                0 -> {
                    // Flashcards Tab
                    FlashcardsTabContent(
                        deck = deck,
                        progress = deckProgress,
                        onStart = onStartFlashcards
                    )
                }
                1 -> {
                    // Quiz Tab
                    QuizTabContent(
                        quizSet = quizSet,
                        record = quizRecord,
                        session = quizSession,
                        onStart = onStartQuiz
                    )
                }
                2 -> {
                    // Mind Map Tab
                    if (mindMap != null) {
                        InteractiveMindMapView(mindMap = mindMap)
                    } else {
                        Box(
                            modifier = Modifier.fillMaxSize(),
                            contentAlignment = Alignment.Center
                        ) {
                            Text(
                                text = "正在生成该系统的知识脑图...",
                                color = TextSecondary
                            )
                        }
                    }
                }
            }
        }
    }
}

@Composable
private fun FlashcardsTabContent(
    deck: FlashcardDeck?,
    progress: StudyProgress?,
    onStart: () -> Unit
) {
    if (deck == null) {
        Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
            Text("未找到闪卡数据", color = TextSecondary)
        }
        return
    }

    val total = deck.cards.size
    val acquired = progress?.acquiredCount ?: 0
    val missed = progress?.missedCount ?: 0
    val ratio = if (total > 0) (acquired.toFloat() / total.toFloat()).coerceIn(0f, 1f) else 0f

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Column(
            modifier = Modifier
                .weight(1f)
                .verticalScroll(rememberScrollState())
        ) {
            Card(
                shape = RoundedCornerShape(24.dp),
                colors = CardDefaults.cardColors(containerColor = AppCardBg),
                border = BorderStroke(1.dp, CardBorder),
                modifier = Modifier.fillMaxWidth()
            ) {
                Column(modifier = Modifier.padding(20.dp)) {
                    Text(
                        text = deck.title,
                        fontSize = 20.sp,
                        fontWeight = FontWeight.Bold,
                        color = TextPrimary
                    )
                    MarkdownText(
                        text = deck.description,
                        fontSize = 13.sp,
                        color = TextSecondary,
                        modifier = Modifier.padding(top = 6.dp)
                    )

                    Spacer(modifier = Modifier.height(18.dp))

                    // Progress Overview
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween
                    ) {
                        Text(text = "掌握度进度", fontSize = 13.sp, color = TextSecondary)
                        Text(
                            text = "$acquired / $total 张已掌握",
                            fontSize = 13.sp,
                            fontWeight = FontWeight.Bold,
                            color = GotItGreen
                        )
                    }

                    Spacer(modifier = Modifier.height(8.dp))

                    LinearProgressIndicator(
                        progress = { ratio },
                        color = GotItGreen,
                        trackColor = ChipBg,
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(8.dp)
                    )

                    Spacer(modifier = Modifier.height(18.dp))

                    // Topics Overview
                    Text(
                        text = "覆盖考点单元",
                        fontSize = 14.sp,
                        fontWeight = FontWeight.SemiBold,
                        color = TextPrimary
                    )

                    Spacer(modifier = Modifier.height(8.dp))

                    deck.topics.covered.forEachIndexed { i, topic ->
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            modifier = Modifier.padding(vertical = 3.dp)
                        ) {
                            Box(
                                modifier = Modifier
                                    .size(6.dp)
                                    .background(GoogleBlue, CircleShape)
                            )
                            Spacer(modifier = Modifier.width(8.dp))
                            Text(text = topic, fontSize = 13.sp, color = TextSecondary)
                        }
                    }
                }
            }
        }

        Spacer(modifier = Modifier.height(14.dp))

        Button(
            onClick = onStart,
            shape = RoundedCornerShape(16.dp),
            colors = ButtonDefaults.buttonColors(containerColor = GoogleBlue),
            modifier = Modifier
                .fillMaxWidth()
                .height(52.dp)
        ) {
            Icon(Icons.Default.PlayArrow, contentDescription = null)
            Spacer(modifier = Modifier.width(8.dp))
            val btnText = if ((progress?.currentIndex ?: 0) > 0) {
                "继续复习 (第 ${(progress?.currentIndex ?: 0) + 1} 张)"
            } else {
                "开始复习 (${total} 张卡片)"
            }
            Text(
                text = btnText,
                fontSize = 15.sp,
                fontWeight = FontWeight.Bold,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
        }
    }
}

@Composable
private fun QuizTabContent(
    quizSet: QuizSet?,
    record: QuizRecord?,
    session: QuizSessionState?,
    onStart: () -> Unit
) {
    if (quizSet == null) {
        Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
            Text("小测数据加载中...", color = TextSecondary)
        }
        return
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Column(
            modifier = Modifier
                .weight(1f)
                .verticalScroll(rememberScrollState())
        ) {
            Card(
                shape = RoundedCornerShape(24.dp),
                colors = CardDefaults.cardColors(containerColor = AppCardBg),
                border = BorderStroke(1.dp, CardBorder),
                modifier = Modifier.fillMaxWidth()
            ) {
                Column(modifier = Modifier.padding(20.dp)) {
                    Text(
                        text = quizSet.title,
                        fontSize = 20.sp,
                        fontWeight = FontWeight.Bold,
                        color = TextPrimary
                    )
                    Text(
                        text = "难度：中等 · 单选题与核心考点测试",
                        fontSize = 13.sp,
                        color = TextSecondary,
                        modifier = Modifier.padding(top = 4.dp)
                    )

                    Spacer(modifier = Modifier.height(20.dp))

                    // Best Score Card
                    Surface(
                        shape = RoundedCornerShape(16.dp),
                        color = ChipBg,
                        border = BorderStroke(1.dp, CardBorder),
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(16.dp),
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Surface(
                                    shape = CircleShape,
                                    color = Color(0xFFFEF7E0),
                                    modifier = Modifier.size(44.dp)
                                ) {
                                    Box(contentAlignment = Alignment.Center) {
                                        Icon(
                                            imageVector = Icons.Default.EmojiEvents,
                                            contentDescription = null,
                                            tint = Color(0xFFF9AB00),
                                            modifier = Modifier.size(24.dp)
                                        )
                                    }
                                }
                                Spacer(modifier = Modifier.width(12.dp))
                                Column {
                                    Text(
                                        text = "历史最高得分",
                                        fontSize = 13.sp,
                                        color = TextSecondary
                                    )
                                    Text(
                                        text = if ((record?.totalQuestions ?: 0) > 0) "${record?.bestScore} / ${record?.totalQuestions} 分" else "暂无做题记录",
                                        fontSize = 16.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = TextPrimary
                                    )
                                }
                            }

                            Text(
                                text = "共 ${quizSet.questions.size} 题",
                                fontSize = 13.sp,
                                color = TextTertiary
                            )
                        }
                    }
                }
            }
        }

        Spacer(modifier = Modifier.height(14.dp))

        Button(
            onClick = onStart,
            shape = RoundedCornerShape(16.dp),
            colors = ButtonDefaults.buttonColors(containerColor = GoogleBlue),
            modifier = Modifier
                .fillMaxWidth()
                .height(52.dp)
        ) {
            Icon(Icons.Default.Assignment, contentDescription = null)
            Spacer(modifier = Modifier.width(8.dp))
            val btnText = if (session != null && (session.currentIndex > 0 || session.submittedQuestions.isNotEmpty())) {
                "继续测验 (第 ${session.currentIndex + 1} 题)"
            } else if ((record?.bestScore ?: 0) > 0) {
                "重新测验 (${quizSet.questions.size} 题)"
            } else {
                "开始小测 (${quizSet.questions.size} 题)"
            }
            Text(
                text = btnText,
                fontSize = 15.sp,
                fontWeight = FontWeight.Bold,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
        }
    }
}
