package com.anatomy.flashcard.ui.components

import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.tween
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.HelpOutline
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.Sync
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.anatomy.flashcard.model.Flashcard
import com.anatomy.flashcard.ui.theme.CardBackground
import com.anatomy.flashcard.ui.theme.CardBorder
import com.anatomy.flashcard.ui.theme.CardStackBg1
import com.anatomy.flashcard.ui.theme.CardStackBg2
import com.anatomy.flashcard.ui.theme.ChipBg
import com.anatomy.flashcard.ui.theme.GoogleBlue
import com.anatomy.flashcard.ui.theme.GoogleBlueLight
import com.anatomy.flashcard.ui.theme.GotItGreen
import com.anatomy.flashcard.ui.theme.GotItGreenBg
import com.anatomy.flashcard.ui.theme.TextPrimary
import com.anatomy.flashcard.ui.theme.TextSecondary
import com.anatomy.flashcard.ui.theme.TextTertiary

import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.spring
import com.anatomy.flashcard.ui.motion.motionPressEffect
import kotlin.math.abs
import kotlin.math.sin

@Composable
fun CardStackContainer(
    card: Flashcard,
    isFlipped: Boolean,
    onFlip: () -> Unit,
    cardIndex: Int,
    totalCards: Int,
    categoryName: String?,
    modifier: Modifier = Modifier
) {
    Box(
        modifier = modifier,
        contentAlignment = Alignment.Center
    ) {
        // Stack Background Layer 2 (Bottom-most card simulation)
        Box(
            modifier = Modifier
                .fillMaxWidth(0.78f)
                .fillMaxSize()
                .offset(y = 24.dp)
                .shadow(elevation = 2.dp, shape = RoundedCornerShape(24.dp))
                .background(CardStackBg2, shape = RoundedCornerShape(24.dp))
        )

        // Stack Background Layer 1 (Middle card simulation)
        Box(
            modifier = Modifier
                .fillMaxWidth(0.88f)
                .fillMaxSize()
                .offset(y = 12.dp)
                .shadow(elevation = 4.dp, shape = RoundedCornerShape(30.dp))
                .background(CardStackBg1, shape = RoundedCornerShape(30.dp))
        )

        // Front Interactive 3D Flip Card
        FlipCard(
            card = card,
            isFlipped = isFlipped,
            onFlip = onFlip,
            cardIndex = cardIndex,
            totalCards = totalCards,
            categoryName = categoryName,
            modifier = Modifier.fillMaxSize()
        )
    }
}

@Composable
fun FlipCard(
    card: Flashcard,
    isFlipped: Boolean,
    onFlip: () -> Unit,
    cardIndex: Int,
    totalCards: Int,
    categoryName: String?,
    modifier: Modifier = Modifier
) {
    // 采用 motion-prompt 物理弹性阻尼翻转动效 (#010 Overshoot Spring)
    val rotation by animateFloatAsState(
        targetValue = if (isFlipped) 180f else 0f,
        animationSpec = spring(
            dampingRatio = 0.82f,
            stiffness = 380f
        ),
        label = "CardFlipAnimation"
    )

    val density = LocalDensity.current.density
    val cardRotation = if (rotation <= 90f) rotation else rotation - 180f

    // 翻转到半空中时卡片动态腾空浮起与轻微缩放，赋予物理实体感
    val flipProgress = abs(sin(Math.toRadians(rotation.toDouble()))).toFloat()
    val dynamicElevation = (8.dp + 16.dp * flipProgress)
    val dynamicScale = 1f + 0.03f * flipProgress

    Card(
        modifier = modifier
            .graphicsLayer {
                rotationY = cardRotation
                cameraDistance = 18f * density
                scaleX = dynamicScale
                scaleY = dynamicScale
            },
        shape = RoundedCornerShape(34.dp),
        colors = CardDefaults.cardColors(containerColor = CardBackground),
        border = BorderStroke(1.dp, CardBorder),
        elevation = CardDefaults.cardElevation(defaultElevation = dynamicElevation)
    ) {
        if (rotation <= 90f) {
            // Card Front (Question)
            CardFrontContent(
                card = card,
                cardIndex = cardIndex,
                totalCards = totalCards,
                categoryName = categoryName,
                onFlip = onFlip
            )
        } else {
            // Card Back (Answer)
            CardBackContent(
                card = card,
                cardIndex = cardIndex,
                totalCards = totalCards,
                categoryName = categoryName,
                onFlip = onFlip
            )
        }
    }
}

@Composable
private fun CardFrontContent(
    card: Flashcard,
    cardIndex: Int,
    totalCards: Int,
    categoryName: String?,
    onFlip: () -> Unit
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 20.dp, vertical = 18.dp),
        verticalArrangement = Arrangement.SpaceBetween
    ) {
        // Header
        val isDark = isSystemInDarkTheme()
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween,
            verticalAlignment = Alignment.CenterVertically
        ) {
            val badgeText = when {
                card.pointType.isNotEmpty() -> "${card.pointType} · ${card.starRating}"
                categoryName != null -> categoryName
                else -> "系统解剖学"
            }
            Surface(
                color = if (isDark) GoogleBlue.copy(alpha = 0.25f) else GoogleBlueLight.copy(alpha = 0.5f),
                shape = RoundedCornerShape(12.dp)
            ) {
                Text(
                    text = badgeText,
                    color = if (isDark) GoogleBlueLight else GoogleBlue,
                    fontSize = 12.sp,
                    fontWeight = FontWeight.SemiBold,
                    modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp)
                )
            }

            Text(
                text = "$cardIndex / $totalCards",
                color = TextSecondary,
                fontSize = 13.sp,
                fontWeight = FontWeight.Medium
            )
        }

        // Center Question
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .weight(1f)
                .verticalScroll(rememberScrollState()),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Surface(
                shape = CircleShape,
                color = if (isDark) GoogleBlue.copy(alpha = 0.2f) else GoogleBlueLight.copy(alpha = 0.45f),
                modifier = Modifier
                    .padding(bottom = 14.dp)
                    .size(38.dp)
            ) {
                Box(contentAlignment = Alignment.Center) {
                    Icon(
                        imageVector = Icons.Default.Info,
                        contentDescription = "考点信息",
                        tint = if (isDark) GoogleBlueLight else GoogleBlue,
                        modifier = Modifier.size(22.dp)
                    )
                }
            }

            val displayQuestion = card.frontText.replace(Regex("^【[^】]+】\\s*"), "")
            MarkdownText(
                text = displayQuestion,
                color = TextPrimary,
                fontSize = 20.sp,
                fontWeight = FontWeight.SemiBold,
                lineHeight = 30.sp,
                modifier = Modifier.padding(horizontal = 8.dp)
            )
        }

        // Bottom Hint
        Surface(
            shape = RoundedCornerShape(50),
            color = ChipBg,
            border = BorderStroke(1.dp, CardBorder),
            modifier = Modifier.fillMaxWidth()
        ) {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 10.dp),
                horizontalArrangement = Arrangement.Center,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Icon(
                    imageVector = Icons.Default.Sync,
                    contentDescription = null,
                    tint = TextSecondary,
                    modifier = Modifier.size(16.dp)
                )
                Spacer(modifier = Modifier.size(8.dp))
                Text(
                    text = "点击卡片翻转查看答案",
                    color = TextSecondary,
                    fontSize = 13.sp,
                    fontWeight = FontWeight.Medium
                )
            }
        }
    }
}

@Composable
private fun CardBackContent(
    card: Flashcard,
    cardIndex: Int,
    totalCards: Int,
    categoryName: String?,
    onFlip: () -> Unit
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 20.dp, vertical = 18.dp),
        verticalArrangement = Arrangement.SpaceBetween
    ) {
        val isDark = isSystemInDarkTheme()
        // Header
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween,
            verticalAlignment = Alignment.CenterVertically
        ) {
            val backBadgeText = when {
                card.pointType.isNotEmpty() -> "${card.pointType} · ${card.starRating}"
                categoryName != null -> categoryName
                else -> null
            }
            Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                if (backBadgeText != null) {
                    Surface(
                        color = if (isDark) GoogleBlue.copy(alpha = 0.25f) else GoogleBlueLight.copy(alpha = 0.5f),
                        shape = RoundedCornerShape(12.dp)
                    ) {
                        Text(
                            text = backBadgeText,
                            color = if (isDark) GoogleBlueLight else GoogleBlue,
                            fontSize = 12.sp,
                            fontWeight = FontWeight.SemiBold,
                            modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp)
                        )
                    }
                }
            }

            Text(
                text = "$cardIndex / $totalCards",
                color = TextSecondary,
                fontSize = 13.sp,
                fontWeight = FontWeight.Medium
            )
        }

        // Center Answer
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .weight(1f)
                .verticalScroll(rememberScrollState()),
            verticalArrangement = Arrangement.Center
        ) {
            MarkdownText(
                text = card.backText,
                color = TextPrimary,
                fontSize = 16.sp,
                fontWeight = FontWeight.Normal,
                lineHeight = 24.sp,
                modifier = Modifier.padding(vertical = 6.dp)
            )

            if (card.imageAlt != null) {
                Spacer(modifier = Modifier.height(12.dp))
                Surface(
                    color = ChipBg,
                    shape = RoundedCornerShape(10.dp),
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Row(
                        modifier = Modifier.padding(10.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Icon(
                            imageVector = Icons.Default.Info,
                            contentDescription = null,
                            tint = GoogleBlue,
                            modifier = Modifier.size(18.dp)
                        )
                        Spacer(modifier = Modifier.size(8.dp))
                        MarkdownText(
                            text = "参考图示：${card.imageAlt}",
                            color = TextSecondary,
                            fontSize = 12.sp
                        )
                    }
                }
            }
        }

        // Bottom Hint
        Surface(
            shape = RoundedCornerShape(50),
            color = ChipBg,
            border = BorderStroke(1.dp, CardBorder),
            modifier = Modifier.fillMaxWidth()
        ) {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 10.dp),
                horizontalArrangement = Arrangement.Center,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Icon(
                    imageVector = Icons.Default.Sync,
                    contentDescription = null,
                    tint = TextSecondary,
                    modifier = Modifier.size(16.dp)
                )
                Spacer(modifier = Modifier.size(8.dp))
                Text(
                    text = "点击卡片翻转查看问题",
                    color = TextSecondary,
                    fontSize = 13.sp,
                    fontWeight = FontWeight.Medium
                )
            }
        }
    }
}
