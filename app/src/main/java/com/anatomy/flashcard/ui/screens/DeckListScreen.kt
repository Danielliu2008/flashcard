package com.anatomy.flashcard.ui.screens

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AccessibilityNew
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.FitnessCenter
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material.icons.filled.Psychology
import androidx.compose.material.icons.filled.School
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MediumTopAppBar
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.anatomy.flashcard.model.FlashcardDeck
import com.anatomy.flashcard.model.StudyProgress
import com.anatomy.flashcard.ui.components.MarkdownText
import com.anatomy.flashcard.ui.theme.CardBorder
import com.anatomy.flashcard.ui.theme.GoogleBlue
import com.anatomy.flashcard.ui.theme.GoogleBlueLight
import com.anatomy.flashcard.ui.theme.GotItGreen
import com.anatomy.flashcard.ui.theme.MissedItRed
import com.anatomy.flashcard.ui.theme.SurfaceLight
import com.anatomy.flashcard.ui.theme.TextPrimary
import com.anatomy.flashcard.ui.theme.TextSecondary
import com.anatomy.flashcard.ui.theme.TextTertiary

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DeckListScreen(
    decks: List<FlashcardDeck>,
    progressMap: Map<String, StudyProgress>,
    onSelectDeck: (FlashcardDeck) -> Unit,
    modifier: Modifier = Modifier
) {
    Scaffold(
        topBar = {
            MediumTopAppBar(
                title = {
                    Column {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Icon(
                                imageVector = Icons.Default.School,
                                contentDescription = null,
                                tint = GoogleBlue,
                                modifier = Modifier.size(28.dp)
                            )
                            Spacer(modifier = Modifier.width(10.dp))
                            Text(
                                text = "系统解剖学 闪卡",
                                fontWeight = FontWeight.Bold,
                                color = TextPrimary,
                                fontSize = 24.sp
                            )
                        }
                        Text(
                            text = "Gemini NotebookLM 本地化题库 · 3 大核心系统 194 张精编闪卡",
                            color = TextSecondary,
                            fontSize = 12.sp,
                            modifier = Modifier.padding(top = 4.dp)
                        )
                    }
                },
                colors = TopAppBarDefaults.mediumTopAppBarColors(
                    containerColor = SurfaceLight
                )
            )
        },
        containerColor = Color(0xFFF9FAFB),
        modifier = modifier
    ) { innerPadding ->
        LazyColumn(
            contentPadding = innerPadding,
            verticalArrangement = Arrangement.spacedBy(16.dp),
            modifier = Modifier
                .fillMaxSize()
                .padding(horizontal = 16.dp, vertical = 12.dp)
        ) {
            items(decks) { deck ->
                val progress = progressMap[deck.id] ?: StudyProgress(deck.id)
                DeckCardItem(
                    deck = deck,
                    progress = progress,
                    onClick = { onSelectDeck(deck) }
                )
            }
        }
    }
}

@OptIn(ExperimentalLayoutApi::class)
@Composable
private fun DeckCardItem(
    deck: FlashcardDeck,
    progress: StudyProgress,
    onClick: () -> Unit
) {
    val total = deck.cards.size
    val acquired = progress.acquiredCount
    val missed = progress.missedCount
    val studiedRatio = if (total > 0) (acquired.toFloat() / total.toFloat()).coerceIn(0f, 1f) else 0f

    val icon = when {
        deck.filename.contains("nervous") -> Icons.Default.Psychology
        deck.filename.contains("skeletal") -> Icons.Default.AccessibilityNew
        else -> Icons.Default.FitnessCenter
    }

    val iconTint = when {
        deck.filename.contains("nervous") -> Color(0xFF1A73E8)
        deck.filename.contains("skeletal") -> Color(0xFFE37400)
        else -> Color(0xFF188038)
    }

    val iconBg = when {
        deck.filename.contains("nervous") -> Color(0xFFE8F0FE)
        deck.filename.contains("skeletal") -> Color(0xFFFEF7E0)
        else -> Color(0xFFE6F4EA)
    }

    Card(
        shape = RoundedCornerShape(24.dp),
        colors = CardDefaults.cardColors(containerColor = Color.White),
        border = BorderStroke(1.dp, CardBorder),
        elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
        modifier = Modifier
            .fillMaxWidth()
            .clickable(onClick = onClick)
    ) {
        Column(modifier = Modifier.padding(20.dp)) {
            // Deck Header
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Surface(
                        shape = CircleShape,
                        color = iconBg,
                        modifier = Modifier.size(48.dp)
                    ) {
                        Box(contentAlignment = Alignment.Center) {
                            Icon(
                                imageVector = icon,
                                contentDescription = null,
                                tint = iconTint,
                                modifier = Modifier.size(26.dp)
                            )
                        }
                    }

                    Spacer(modifier = Modifier.width(14.dp))

                    Column {
                        Text(
                            text = deck.title,
                            fontSize = 18.sp,
                            fontWeight = FontWeight.Bold,
                            color = TextPrimary
                        )
                        Text(
                            text = "${total} 张闪卡",
                            fontSize = 13.sp,
                            color = TextSecondary
                        )
                    }
                }

                if (acquired == total && total > 0) {
                    Icon(
                        imageVector = Icons.Default.CheckCircle,
                        contentDescription = "All Acquired",
                        tint = GotItGreen,
                        modifier = Modifier.size(24.dp)
                    )
                }
            }

            Spacer(modifier = Modifier.height(12.dp))

            // Description
            MarkdownText(
                text = deck.description,
                fontSize = 13.sp,
                color = TextSecondary,
                lineHeight = 18.sp
            )

            Spacer(modifier = Modifier.height(14.dp))

            // Progress Bar
            Column(modifier = Modifier.fillMaxWidth()) {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {
                    Text(
                        text = "学习进度",
                        fontSize = 12.sp,
                        color = TextSecondary
                    )
                    Text(
                        text = "已掌握 $acquired / $total (未掌握: $missed)",
                        fontSize = 12.sp,
                        fontWeight = FontWeight.Medium,
                        color = TextPrimary
                    )
                }

                Spacer(modifier = Modifier.height(6.dp))

                LinearProgressIndicator(
                    progress = { studiedRatio },
                    color = GotItGreen,
                    trackColor = Color(0xFFF1F3F4),
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(8.dp)
                )
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Topic Tags Flow
            if (deck.topics.covered.isNotEmpty()) {
                FlowRow(
                    horizontalArrangement = Arrangement.spacedBy(6.dp),
                    verticalArrangement = Arrangement.spacedBy(6.dp),
                    modifier = Modifier.fillMaxWidth()
                ) {
                    deck.topics.covered.take(4).forEach { topic ->
                        Surface(
                            shape = RoundedCornerShape(8.dp),
                            color = Color(0xFFF1F3F4)
                        ) {
                            Text(
                                text = topic,
                                fontSize = 11.sp,
                                color = TextSecondary,
                                modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                            )
                        }
                    }
                    if (deck.topics.covered.size > 4) {
                        Surface(
                            shape = RoundedCornerShape(8.dp),
                            color = Color(0xFFF1F3F4)
                        ) {
                            Text(
                                text = "+${deck.topics.covered.size - 4} 个考点",
                                fontSize = 11.sp,
                                color = TextTertiary,
                                modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                            )
                        }
                    }
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Action Button
            Button(
                onClick = onClick,
                shape = RoundedCornerShape(14.dp),
                colors = ButtonDefaults.buttonColors(containerColor = GoogleBlue),
                modifier = Modifier.fillMaxWidth()
            ) {
                Icon(
                    imageVector = Icons.Default.PlayArrow,
                    contentDescription = null,
                    modifier = Modifier.size(18.dp)
                )
                Spacer(modifier = Modifier.width(6.dp))
                Text(
                    text = if (progress.currentIndex > 0) "继续学习 (从第 ${progress.currentIndex + 1} 题开始)" else "开始复习",
                    fontSize = 14.sp,
                    fontWeight = FontWeight.SemiBold
                )
            }
        }
    }
}
