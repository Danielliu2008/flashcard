package com.anatomy.flashcard.ui.screens

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.AccessibilityNew
import androidx.compose.material.icons.filled.AccountTree
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Assignment
import androidx.compose.material.icons.filled.ChevronRight
import androidx.compose.material.icons.filled.FitnessCenter
import androidx.compose.material.icons.filled.Psychology
import androidx.compose.material.icons.filled.School
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MediumTopAppBar
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.anatomy.flashcard.model.AnatomySystemType
import com.anatomy.flashcard.model.FlashcardDeck
import com.anatomy.flashcard.model.QuizRecord
import com.anatomy.flashcard.model.QuizSet
import com.anatomy.flashcard.model.StudyProgress
import com.anatomy.flashcard.ui.theme.AppBackground
import com.anatomy.flashcard.ui.theme.AppCardBg
import com.anatomy.flashcard.ui.theme.AppSurface
import com.anatomy.flashcard.ui.theme.CardBorder
import com.anatomy.flashcard.ui.theme.ChipBg
import com.anatomy.flashcard.ui.theme.GoogleBlue
import com.anatomy.flashcard.ui.theme.GotItGreen
import com.anatomy.flashcard.ui.theme.TextPrimary
import com.anatomy.flashcard.ui.theme.TextSecondary
import com.anatomy.flashcard.ui.theme.TextTertiary

import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.IconButton
import com.anatomy.flashcard.model.Subject
import com.anatomy.flashcard.ui.components.MarkdownText

import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.tween
import androidx.compose.foundation.lazy.itemsIndexed
import com.anatomy.flashcard.ui.motion.motionPressEffect
import com.anatomy.flashcard.ui.motion.staggeredEntrance

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HomeScreen(
    currentSubject: Subject,
    systems: List<AnatomySystemType>,
    decks: Map<AnatomySystemType, FlashcardDeck>,
    deckProgressMap: Map<String, StudyProgress>,
    quizSets: Map<AnatomySystemType, QuizSet>,
    quizRecords: Map<String, QuizRecord>,
    onSelectSystem: (AnatomySystemType) -> Unit,
    onSelectSystemTab: (AnatomySystemType, Int) -> Unit,
    onOpenImport: () -> Unit,
    onBackToSubjects: () -> Unit,
    modifier: Modifier = Modifier
) {
    Scaffold(
        topBar = {
            Surface(
                color = AppBackground,
                modifier = Modifier
                    .fillMaxWidth()
                    .statusBarsPadding()
            ) {
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 16.dp, vertical = 10.dp)
                ) {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        IconButton(
                            onClick = onBackToSubjects,
                            modifier = Modifier.size(40.dp)
                        ) {
                            Icon(
                                imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                                contentDescription = "返回学科列表",
                                tint = TextPrimary
                            )
                        }

                        Surface(
                            shape = RoundedCornerShape(12.dp),
                            color = ChipBg,
                            modifier = Modifier.clickable(onClick = onOpenImport)
                        ) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                modifier = Modifier.padding(horizontal = 12.dp, vertical = 7.dp)
                            ) {
                                Icon(
                                    imageVector = Icons.Default.Add,
                                    contentDescription = "导入数据",
                                    tint = GoogleBlue,
                                    modifier = Modifier.size(18.dp)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text(
                                    text = "导入数据",
                                    fontSize = 12.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = GoogleBlue
                                )
                            }
                        }
                    }

                    Spacer(modifier = Modifier.height(10.dp))

                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text(
                            text = currentSubject.emoji,
                            fontSize = 28.sp
                        )
                        Spacer(modifier = Modifier.width(10.dp))
                        Text(
                            text = currentSubject.name,
                            fontWeight = FontWeight.Bold,
                            color = TextPrimary,
                            fontSize = 22.sp
                        )
                    }

                    Spacer(modifier = Modifier.height(4.dp))

                    MarkdownText(
                        text = currentSubject.description.ifEmpty { "导图 · 闪卡 · 小测 三位一体复习系统" },
                        color = TextSecondary,
                        fontSize = 12.sp,
                        maxLines = 1
                    )
                }
            }
        },
        containerColor = AppBackground,
        modifier = modifier
    ) { innerPadding ->
        LazyColumn(
            contentPadding = PaddingValues(
                start = 16.dp,
                end = 16.dp,
                top = innerPadding.calculateTopPadding() + 8.dp,
                bottom = 24.dp
            ),
            verticalArrangement = Arrangement.spacedBy(16.dp),
            modifier = Modifier.fillMaxSize()
        ) {
            if (systems.isEmpty()) {
                item {
                    Box(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(vertical = 48.dp),
                        contentAlignment = Alignment.Center
                    ) {
                        Column(horizontalAlignment = Alignment.CenterHorizontally) {
                            Text(
                                text = "📚 该学科暂无章节数据",
                                fontSize = 16.sp,
                                fontWeight = FontWeight.Medium,
                                color = TextSecondary
                            )
                            Spacer(modifier = Modifier.height(8.dp))
                            Text(
                                text = "可通过右上角导入或使用 ZIP 资源包添加",
                                fontSize = 13.sp,
                                color = TextTertiary
                            )
                        }
                    }
                }
            } else {
                itemsIndexed(systems) { index, system ->
                    val deck = decks[system]
                    val deckProgress = deck?.let { deckProgressMap[it.id] }
                    val quiz = quizSets[system]
                    val quizRecord = quiz?.let { quizRecords[it.id] }

                    SystemHeroCard(
                        system = system,
                        index = index,
                        deck = deck,
                        progress = deckProgress,
                        quiz = quiz,
                        record = quizRecord,
                        onClick = { onSelectSystem(system) },
                        onSelectTab = { tab -> onSelectSystemTab(system, tab) }
                    )
                }
            }
        }
    }
}

@Composable
fun SystemHeroCard(
    system: AnatomySystemType,
    index: Int,
    deck: FlashcardDeck?,
    progress: StudyProgress?,
    quiz: QuizSet?,
    record: QuizRecord?,
    onClick: () -> Unit,
    onSelectTab: (Int) -> Unit
) {
    val icon = when {
        system.id.contains("nervous") -> Icons.Default.Psychology
        system.id.contains("skeletal") -> Icons.Default.AccessibilityNew
        system.id.contains("muscular") -> Icons.Default.FitnessCenter
        system.id.contains("immu") -> Icons.Default.School
        else -> Icons.Default.School
    }

    val iconColor = when {
        system.id.contains("nervous") -> Color(0xFF1A73E8)
        system.id.contains("skeletal") -> Color(0xFFE37400)
        system.id.contains("muscular") -> Color(0xFF188038)
        system.id.contains("micro") -> Color(0xFF188038)
        system.id.contains("immu") -> Color(0xFF9334E6)
        else -> Color(0xFF1A73E8)
    }

    val iconBg = when {
        system.id.contains("nervous") -> Color(0xFFE8F0FE)
        system.id.contains("skeletal") -> Color(0xFFFEF7E0)
        system.id.contains("muscular") -> Color(0xFFE6F4EA)
        system.id.contains("micro") -> Color(0xFFE6F4EA)
        system.id.contains("immu") -> Color(0xFFF3E8FD)
        else -> Color(0xFFE8F0FE)
    }

    val totalCards = deck?.cards?.size ?: 0
    val acquiredCards = progress?.acquiredCount ?: 0
    val targetRatio = if (totalCards > 0) (acquiredCards.toFloat() / totalCards.toFloat()).coerceIn(0f, 1f) else 0f
    val animatedProgressRatio by animateFloatAsState(
        targetValue = targetRatio,
        animationSpec = tween(durationMillis = 650, easing = FastOutSlowInEasing),
        label = "ProgressAnimation"
    )

    Card(
        shape = RoundedCornerShape(26.dp),
        colors = CardDefaults.cardColors(containerColor = AppCardBg),
        border = BorderStroke(1.dp, CardBorder),
        elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
        modifier = Modifier
            .fillMaxWidth()
            .staggeredEntrance(index = index)
            .motionPressEffect(pressedScale = 0.96f) { onClick() }
    ) {
        Column(modifier = Modifier.padding(22.dp)) {
            // Header
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Surface(
                        shape = CircleShape,
                        color = iconBg,
                        modifier = Modifier.size(52.dp)
                    ) {
                        Box(contentAlignment = Alignment.Center) {
                            Icon(
                                imageVector = icon,
                                contentDescription = null,
                                tint = iconColor,
                                modifier = Modifier.size(28.dp)
                            )
                        }
                    }

                    Spacer(modifier = Modifier.width(14.dp))

                    Column {
                        Text(
                            text = system.title,
                            fontSize = 20.sp,
                            fontWeight = FontWeight.Bold,
                            color = TextPrimary
                        )
                        Text(
                            text = system.subtitle,
                            fontSize = 12.sp,
                            color = TextSecondary
                        )
                    }
                }

                Icon(
                    imageVector = Icons.Default.ChevronRight,
                    contentDescription = null,
                    tint = TextTertiary
                )
            }

            Spacer(modifier = Modifier.height(14.dp))

            MarkdownText(
                text = system.description,
                fontSize = 13.sp,
                color = TextSecondary,
                lineHeight = 19.sp
            )

            Spacer(modifier = Modifier.height(18.dp))

            // 3 Badges (Flashcards, Quiz, MindMap) - 同级高度对齐且支持独立点击直达
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                // Flashcards badge
                Surface(
                    shape = RoundedCornerShape(12.dp),
                    color = ChipBg,
                    border = BorderStroke(1.dp, CardBorder),
                    modifier = Modifier
                        .weight(1f)
                        .motionPressEffect { onSelectTab(0) }
                ) {
                    Column(modifier = Modifier.padding(10.dp)) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Icon(
                                imageVector = Icons.Default.Psychology,
                                contentDescription = null,
                                tint = GoogleBlue,
                                modifier = Modifier.size(16.dp)
                            )
                            Spacer(modifier = Modifier.width(4.dp))
                            Text(text = "闪卡", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = TextPrimary, maxLines = 1)
                        }
                        Spacer(modifier = Modifier.height(4.dp))
                        Text(
                            text = "$acquiredCards / $totalCards",
                            fontSize = 11.sp,
                            maxLines = 1,
                            overflow = TextOverflow.Ellipsis,
                            color = if (acquiredCards == totalCards && totalCards > 0) GotItGreen else TextSecondary
                        )
                    }
                }

                // Quiz badge
                Surface(
                    shape = RoundedCornerShape(12.dp),
                    color = ChipBg,
                    border = BorderStroke(1.dp, CardBorder),
                    modifier = Modifier
                        .weight(1f)
                        .motionPressEffect { onSelectTab(1) }
                ) {
                    Column(modifier = Modifier.padding(10.dp)) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Icon(
                                imageVector = Icons.Default.Assignment,
                                contentDescription = null,
                                tint = Color(0xFFF9AB00),
                                modifier = Modifier.size(16.dp)
                            )
                            Spacer(modifier = Modifier.width(4.dp))
                            Text(text = "小测", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = TextPrimary, maxLines = 1)
                        }
                        Spacer(modifier = Modifier.height(4.dp))
                        Text(
                            text = if ((record?.bestScore ?: 0) > 0) "${record?.bestScore}分" else "${quiz?.questions?.size ?: 0}题",
                            fontSize = 11.sp,
                            maxLines = 1,
                            overflow = TextOverflow.Ellipsis,
                            color = TextSecondary
                        )
                    }
                }

                // Mind Map badge
                Surface(
                    shape = RoundedCornerShape(12.dp),
                    color = ChipBg,
                    border = BorderStroke(1.dp, CardBorder),
                    modifier = Modifier
                        .weight(1f)
                        .motionPressEffect { onSelectTab(2) }
                ) {
                    Column(modifier = Modifier.padding(10.dp)) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Icon(
                                imageVector = Icons.Default.AccountTree,
                                contentDescription = null,
                                tint = Color(0xFF188038),
                                modifier = Modifier.size(16.dp)
                            )
                            Spacer(modifier = Modifier.width(4.dp))
                            Text(text = "脑图", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = TextPrimary, maxLines = 1)
                        }
                        Spacer(modifier = Modifier.height(4.dp))
                        Text(text = "结构化树", fontSize = 11.sp, color = TextSecondary, maxLines = 1, overflow = TextOverflow.Ellipsis)
                    }
                }
            }

            Spacer(modifier = Modifier.height(14.dp))

            // Progress bar
            LinearProgressIndicator(
                progress = { animatedProgressRatio },
                color = GotItGreen,
                trackColor = ChipBg,
                modifier = Modifier
                    .fillMaxWidth()
                    .height(6.dp)
            )
        }
    }
}
