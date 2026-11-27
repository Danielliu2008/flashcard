package com.anatomy.flashcard.ui.screens

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.spring
import androidx.compose.animation.core.tween
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.gestures.awaitEachGesture
import androidx.compose.foundation.gestures.awaitFirstDown
import androidx.compose.foundation.layout.Arrangement
import kotlin.math.abs
import kotlin.math.sqrt
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
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.automirrored.filled.ArrowForward
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.MoreVert
import androidx.compose.material.icons.filled.Refresh
import androidx.compose.material.icons.filled.Shuffle
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateMapOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.anatomy.flashcard.model.CardAcquisition
import com.anatomy.flashcard.model.Flashcard
import com.anatomy.flashcard.model.FlashcardDeck
import com.anatomy.flashcard.model.StudyProgress
import com.anatomy.flashcard.ui.components.CardStackContainer
import com.anatomy.flashcard.ui.components.StudyControlBar
import com.anatomy.flashcard.ui.theme.AppBackground
import com.anatomy.flashcard.ui.theme.AppCardBg
import com.anatomy.flashcard.ui.theme.AppSurface
import com.anatomy.flashcard.ui.theme.GoogleBlue
import com.anatomy.flashcard.ui.theme.GotItGreen
import com.anatomy.flashcard.ui.theme.GotItGreenBg
import com.anatomy.flashcard.ui.theme.MissedItRed
import com.anatomy.flashcard.ui.theme.MissedItRedBg
import com.anatomy.flashcard.ui.theme.TextPrimary
import com.anatomy.flashcard.ui.theme.TextSecondary
import com.anatomy.flashcard.ui.theme.TextTertiary
import kotlinx.coroutines.launch

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun StudyScreen(
    deck: FlashcardDeck,
    initialProgress: StudyProgress,
    onSaveProgress: (StudyProgress) -> Unit,
    onBack: () -> Unit,
    modifier: Modifier = Modifier
) {
    // Current acquisitions mapping
    val acquisitions = remember {
        mutableStateMapOf<Int, CardAcquisition>().apply {
            putAll(initialProgress.acquisitions)
        }
    }

    var isShuffled by remember { mutableStateOf(initialProgress.isShuffled) }
    var filterMissedOnly by remember { mutableStateOf(initialProgress.filterMissedOnly) }

    // Cards list according to shuffle / filter
    val activeCards = remember(deck, isShuffled, filterMissedOnly) {
        var list = deck.cards
        if (filterMissedOnly) {
            list = list.filter { card -> acquisitions[card.id] == CardAcquisition.NOT_ACQUIRED }
            if (list.isEmpty()) {
                list = deck.cards // fallback if none missed
            }
        }
        if (isShuffled) {
            list = list.shuffled()
        }
        list
    }

    var currentIndex by remember(activeCards) {
        val safeIndex = initialProgress.currentIndex.coerceIn(0, (activeCards.size - 1).coerceAtLeast(0))
        mutableIntStateOf(safeIndex)
    }

    var isFlipped by remember { mutableStateOf(false) }
    var showMenu by remember { mutableStateOf(false) }
    var isFinished by remember { mutableStateOf(false) }

    val currentCard = activeCards.getOrNull(currentIndex)

    fun persist() {
        onSaveProgress(
            StudyProgress(
                deckId = deck.id,
                currentIndex = currentIndex,
                acquisitions = acquisitions.toMap(),
                isShuffled = isShuffled,
                filterMissedOnly = filterMissedOnly
            )
        )
    }

    fun goToNextCard() {
        if (currentIndex < activeCards.size - 1) {
            currentIndex++
            isFlipped = false
            persist()
        } else {
            isFinished = true
        }
    }

    fun goToPreviousCard() {
        if (currentIndex > 0) {
            currentIndex--
            isFlipped = false
            persist()
        }
    }

    if (isFinished || currentCard == null) {
        FinalSummaryScreen(
            deck = deck,
            progress = StudyProgress(deck.id, currentIndex, acquisitions.toMap()),
            onRestartSet = {
                currentIndex = 0
                isFlipped = false
                isFinished = false
                acquisitions.clear()
                filterMissedOnly = false
                persist()
            },
            onStudyMissedOnly = {
                filterMissedOnly = true
                currentIndex = 0
                isFlipped = false
                isFinished = false
                persist()
            },
            onBackToDecks = onBack
        )
        return
    }

    val progressRatio by animateFloatAsState(
        targetValue = if (activeCards.isNotEmpty()) (currentIndex + 1).toFloat() / activeCards.size.toFloat() else 0f,
        animationSpec = tween(durationMillis = 300),
        label = "ProgressBarAnimation"
    )

    // Match topic category name
    val topicName = remember(currentCard, deck) {
        val topicIdx = ((currentCard.categoryIndex - 1) * deck.topics.covered.size / deck.cards.size).coerceIn(0, (deck.topics.covered.size - 1).coerceAtLeast(0))
        deck.topics.covered.getOrNull(topicIdx)
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Column {
                        Text(
                            text = deck.title,
                            fontSize = 17.sp,
                            fontWeight = FontWeight.Bold,
                            color = TextPrimary
                        )
                        Text(
                            text = "${currentIndex + 1} / ${activeCards.size}${if (filterMissedOnly) " (错题模式)" else ""}${if (isShuffled) " (随机)" else ""}",
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
                actions = {
                    IconButton(onClick = { showMenu = true }) {
                        Icon(
                            imageVector = Icons.Default.MoreVert,
                            contentDescription = "更多选项",
                            tint = TextPrimary
                        )
                    }

                    DropdownMenu(
                        expanded = showMenu,
                        onDismissRequest = { showMenu = false }
                    ) {
                        DropdownMenuItem(
                            text = { Text("重新开始本组 (Restart set)") },
                            leadingIcon = { Icon(Icons.Default.Refresh, contentDescription = null) },
                            onClick = {
                                showMenu = false
                                currentIndex = 0
                                isFlipped = false
                                acquisitions.clear()
                                persist()
                            }
                        )

                        DropdownMenuItem(
                            text = { Text(if (isShuffled) "恢复顺序排列" else "随机乱序 (Shuffle set)") },
                            leadingIcon = { Icon(Icons.Default.Shuffle, contentDescription = null) },
                            onClick = {
                                showMenu = false
                                isShuffled = !isShuffled
                                currentIndex = 0
                                isFlipped = false
                                persist()
                            }
                        )

                        DropdownMenuItem(
                            text = { Text(if (filterMissedOnly) "显示全部卡片" else "只复习未掌握卡片 (Study missed)") },
                            onClick = {
                                showMenu = false
                                filterMissedOnly = !filterMissedOnly
                                currentIndex = 0
                                isFlipped = false
                                persist()
                            }
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
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.SpaceBetween
        ) {
            // Linear Progress Bar
            LinearProgressIndicator(
                progress = { progressRatio },
                color = GoogleBlue,
                trackColor = Color(0xFFE0E3E7),
                modifier = Modifier
                    .fillMaxWidth()
                    .height(4.dp)
            )

            Spacer(modifier = Modifier.height(16.dp))

            // 3D Flip Card Container with 2D Drag & Directional Swipe Overlay Gestures
            val coroutineScope = rememberCoroutineScope()
            var gestureMode by remember { mutableStateOf(SwipeGestureMode.NONE) }
            var dragOffsetX by remember { mutableFloatStateOf(0f) }
            var dragOffsetY by remember { mutableFloatStateOf(0f) }
            val animX = remember { Animatable(0f) }
            val animY = remember { Animatable(0f) }

            LaunchedEffect(currentIndex) {
                dragOffsetX = 0f
                dragOffsetY = 0f
                animX.snapTo(0f)
                animY.snapTo(0f)
                gestureMode = SwipeGestureMode.NONE
            }

            Box(
                modifier = Modifier
                    .weight(1f)
                    .fillMaxWidth()
                    .padding(bottom = 24.dp)
                    .pointerInput(currentIndex) {
                        awaitEachGesture {
                            val down = awaitFirstDown(requireUnconsumed = false)
                            val downPos = down.position
                            var currentMode = SwipeGestureMode.NONE
                            gestureMode = SwipeGestureMode.NONE
                            var currentDx = 0f
                            var currentDy = 0f

                            while (true) {
                                val event = awaitPointerEvent()
                                val change = event.changes.firstOrNull { it.id == down.id }
                                if (change == null || !change.pressed) {
                                    break
                                }

                                val totalDx = change.position.x - downPos.x
                                val totalDy = change.position.y - downPos.y

                                if (currentMode == SwipeGestureMode.NONE) {
                                    val absDx = abs(totalDx)
                                    val absDy = abs(totalDy)
                                    // 只要手指移动超过 8px (极高灵敏度，毫无滞后感)
                                    if (absDx > 8f || absDy > 8f) {
                                        // 核心手势分流规则：
                                        // 只有当明确向下开始时（totalDy > 8f 并且向下分量明显大于水平分量 totalDy > absDx * 1.1f），
                                        // 才进入向下评判模式！
                                        if (totalDy > 8f && totalDy > absDx * 1.1f) {
                                            currentMode = SwipeGestureMode.DOWN_JUDGEMENT
                                        } else {
                                            // 左右开始（或任意非明确向下手势）锁定为左右翻卡模式
                                            currentMode = SwipeGestureMode.HORIZONTAL_NAV
                                        }
                                        gestureMode = currentMode
                                    }
                                }

                                if (currentMode != SwipeGestureMode.NONE) {
                                    change.consume()
                                    if (currentMode == SwipeGestureMode.DOWN_JUDGEMENT) {
                                        currentDy = totalDy.coerceAtLeast(0f)
                                        currentDx = totalDx * 0.85f
                                    } else {
                                        currentDx = totalDx
                                        currentDy = 0f // 水平模式锁定 Y 轴为 0
                                    }
                                    dragOffsetX = currentDx
                                    dragOffsetY = currentDy
                                }
                            }

                            // 手指抬起处理
                            when (currentMode) {
                                SwipeGestureMode.NONE -> {
                                    // 未发生明显拖动，触发翻转卡片
                                    isFlipped = !isFlipped
                                }
                                SwipeGestureMode.DOWN_JUDGEMENT -> {
                                    // 向下拖动阈值 (110px)
                                    if (currentDy > 110f) {
                                        if (currentDx < -20f) {
                                            // 向左下飞出：未掌握
                                            coroutineScope.launch {
                                                animX.snapTo(currentDx)
                                                animY.snapTo(currentDy)
                                                launch {
                                                    animX.animateTo(currentDx - 500f, tween(160)) {
                                                        dragOffsetX = value
                                                    }
                                                }
                                                animY.animateTo(currentDy + 500f, tween(160)) {
                                                    dragOffsetY = value
                                                }
                                                acquisitions[currentCard.id] = CardAcquisition.NOT_ACQUIRED
                                                persist()
                                                dragOffsetX = 0f
                                                dragOffsetY = 0f
                                                gestureMode = SwipeGestureMode.NONE
                                                goToNextCard()
                                            }
                                        } else if (currentDx > 20f) {
                                            // 向右下飞出：已掌握
                                            coroutineScope.launch {
                                                animX.snapTo(currentDx)
                                                animY.snapTo(currentDy)
                                                launch {
                                                    animX.animateTo(currentDx + 500f, tween(160)) {
                                                        dragOffsetX = value
                                                    }
                                                }
                                                animY.animateTo(currentDy + 500f, tween(160)) {
                                                    dragOffsetY = value
                                                }
                                                acquisitions[currentCard.id] = CardAcquisition.ACQUIRED
                                                persist()
                                                dragOffsetX = 0f
                                                dragOffsetY = 0f
                                                gestureMode = SwipeGestureMode.NONE
                                                goToNextCard()
                                            }
                                        } else {
                                            // 正向下没有偏向左右，轻微判定
                                            coroutineScope.launch {
                                                val toRight = currentDx >= 0f
                                                animX.snapTo(currentDx)
                                                animY.snapTo(currentDy)
                                                launch {
                                                    animX.animateTo(if (toRight) currentDx + 400f else currentDx - 400f, tween(160)) {
                                                        dragOffsetX = value
                                                    }
                                                }
                                                animY.animateTo(currentDy + 500f, tween(160)) {
                                                    dragOffsetY = value
                                                }
                                                acquisitions[currentCard.id] = if (toRight) CardAcquisition.ACQUIRED else CardAcquisition.NOT_ACQUIRED
                                                persist()
                                                dragOffsetX = 0f
                                                dragOffsetY = 0f
                                                gestureMode = SwipeGestureMode.NONE
                                                goToNextCard()
                                            }
                                        }
                                    } else {
                                        // 未达到阈值，弹簧平滑回弹
                                        coroutineScope.launch {
                                            animX.snapTo(currentDx)
                                            animY.snapTo(currentDy)
                                            launch {
                                                animX.animateTo(0f, spring(dampingRatio = Spring.DampingRatioMediumBouncy, stiffness = Spring.StiffnessLow)) {
                                                    dragOffsetX = value
                                                }
                                            }
                                            animY.animateTo(0f, spring(dampingRatio = Spring.DampingRatioMediumBouncy, stiffness = Spring.StiffnessLow)) {
                                                dragOffsetY = value
                                            }
                                            gestureMode = SwipeGestureMode.NONE
                                        }
                                    }
                                }
                                SwipeGestureMode.HORIZONTAL_NAV -> {
                                    // 水平滑动阈值 (100px)
                                    if (currentDx < -100f) {
                                        // 向左滑：下一张
                                        coroutineScope.launch {
                                            animX.snapTo(currentDx)
                                            animX.animateTo(currentDx - 500f, tween(160)) {
                                                dragOffsetX = value
                                            }
                                            dragOffsetX = 0f
                                            dragOffsetY = 0f
                                            gestureMode = SwipeGestureMode.NONE
                                            goToNextCard()
                                        }
                                    } else if (currentDx > 100f && currentIndex > 0) {
                                        // 向右滑：上一张
                                        coroutineScope.launch {
                                            animX.snapTo(currentDx)
                                            animX.animateTo(currentDx + 500f, tween(160)) {
                                                dragOffsetX = value
                                            }
                                            dragOffsetX = 0f
                                            dragOffsetY = 0f
                                            gestureMode = SwipeGestureMode.NONE
                                            goToPreviousCard()
                                        }
                                    } else {
                                        // 未达到阈值，弹簧平滑回弹
                                        coroutineScope.launch {
                                            animX.snapTo(currentDx)
                                            animX.animateTo(0f, spring(dampingRatio = Spring.DampingRatioMediumBouncy, stiffness = Spring.StiffnessLow)) {
                                                dragOffsetX = value
                                            }
                                            gestureMode = SwipeGestureMode.NONE
                                        }
                                    }
                                }
                            }
                        }
                    },
                contentAlignment = Alignment.Center
            ) {
                // Front interactive card with dynamic translation and tilt
                Box(
                    modifier = Modifier
                        .fillMaxSize()
                        .graphicsLayer {
                            translationX = dragOffsetX
                            translationY = dragOffsetY
                            rotationZ = (dragOffsetX / 32f).coerceIn(-14f, 14f)
                        }
                ) {
                    CardStackContainer(
                        card = currentCard,
                        isFlipped = isFlipped,
                        onFlip = { isFlipped = !isFlipped },
                        cardIndex = currentIndex + 1,
                        totalCards = activeCards.size,
                        categoryName = topicName,
                        modifier = Modifier.fillMaxSize()
                    )

                    // Overlay 动画效果
                    SwipeCardOverlay(
                        mode = gestureMode,
                        dragX = dragOffsetX,
                        dragY = dragOffsetY,
                        hasPrevious = currentIndex > 0,
                        modifier = Modifier.fillMaxSize()
                    )
                }
            }

            // Bottom Evaluation & Navigation Bar
            StudyControlBar(
                hasPrevious = currentIndex > 0,
                hasNext = true,
                currentStatus = acquisitions[currentCard.id],
                onPrevious = { goToPreviousCard() },
                onNext = { goToNextCard() },
                onMissedIt = {
                    acquisitions[currentCard.id] = CardAcquisition.NOT_ACQUIRED
                    persist()
                    goToNextCard()
                },
                onGotIt = {
                    acquisitions[currentCard.id] = CardAcquisition.ACQUIRED
                    persist()
                    goToNextCard()
                }
            )
        }
    }
}

enum class SwipeGestureMode {
    NONE,
    DOWN_JUDGEMENT, // 明确向下开始：评判模式
    HORIZONTAL_NAV  // 左右水平开始：翻卡模式
}

private data class SwipeOverlayConfig(
    val scrimColor: Color,
    val badgeBg: Color,
    val badgeBorder: Color,
    val badgeText: Color,
    val badgeIcon: ImageVector,
    val rotationAngle: Float,
    val label: String
)

@Composable
fun SwipeCardOverlay(
    mode: SwipeGestureMode,
    dragX: Float,
    dragY: Float,
    hasPrevious: Boolean,
    modifier: Modifier = Modifier
) {
    if (mode == SwipeGestureMode.NONE) return

    val config = when (mode) {
        SwipeGestureMode.DOWN_JUDGEMENT -> {
            val progress = (dragY / 120f).coerceIn(0f, 1f)
            when {
                dragX < -15f -> SwipeOverlayConfig(
                    scrimColor = MissedItRed.copy(alpha = progress * 0.18f),
                    badgeBg = MissedItRedBg,
                    badgeBorder = MissedItRed,
                    badgeText = MissedItRed,
                    badgeIcon = Icons.Default.Close,
                    rotationAngle = -12f,
                    label = "未掌握"
                )
                dragX > 15f -> SwipeOverlayConfig(
                    scrimColor = GotItGreen.copy(alpha = progress * 0.18f),
                    badgeBg = GotItGreenBg,
                    badgeBorder = GotItGreen,
                    badgeText = GotItGreen,
                    badgeIcon = Icons.Default.Check,
                    rotationAngle = 12f,
                    label = "已掌握"
                )
                else -> SwipeOverlayConfig(
                    scrimColor = Color.Black.copy(alpha = progress * 0.08f),
                    badgeBg = AppCardBg,
                    badgeBorder = TextTertiary,
                    badgeText = TextSecondary,
                    badgeIcon = Icons.Default.Refresh,
                    rotationAngle = 0f,
                    label = ""
                )
            }
        }
        SwipeGestureMode.HORIZONTAL_NAV -> {
            val progress = (abs(dragX) / 120f).coerceIn(0f, 1f)
            when {
                dragX < -20f -> SwipeOverlayConfig(
                    scrimColor = GoogleBlue.copy(alpha = progress * 0.12f),
                    badgeBg = AppCardBg,
                    badgeBorder = GoogleBlue,
                    badgeText = GoogleBlue,
                    badgeIcon = Icons.AutoMirrored.Filled.ArrowForward,
                    rotationAngle = 0f,
                    label = "下一张"
                )
                dragX > 20f && hasPrevious -> SwipeOverlayConfig(
                    scrimColor = GoogleBlue.copy(alpha = progress * 0.12f),
                    badgeBg = AppCardBg,
                    badgeBorder = GoogleBlue,
                    badgeText = GoogleBlue,
                    badgeIcon = Icons.AutoMirrored.Filled.ArrowBack,
                    rotationAngle = 0f,
                    label = "上一张"
                )
                dragX > 20f -> SwipeOverlayConfig(
                    scrimColor = Color.Transparent,
                    badgeBg = AppCardBg,
                    badgeBorder = TextTertiary,
                    badgeText = TextTertiary,
                    badgeIcon = Icons.AutoMirrored.Filled.ArrowBack,
                    rotationAngle = 0f,
                    label = "已经是第一张"
                )
                else -> return
            }
        }
        else -> return
    }

    val progress = when (mode) {
        SwipeGestureMode.DOWN_JUDGEMENT -> (dragY / 120f).coerceIn(0f, 1f)
        SwipeGestureMode.HORIZONTAL_NAV -> (abs(dragX) / 120f).coerceIn(0f, 1f)
        else -> 0f
    }
    if (progress < 0.1f) return

    Box(
        modifier = modifier
            .clip(RoundedCornerShape(34.dp))
            .background(config.scrimColor),
        contentAlignment = Alignment.Center
    ) {
        Surface(
            shape = RoundedCornerShape(22.dp),
            color = config.badgeBg.copy(alpha = 0.94f),
            border = BorderStroke(2.dp, config.badgeBorder.copy(alpha = progress)),
            shadowElevation = (6 * progress).dp,
            modifier = Modifier
                .graphicsLayer {
                    rotationZ = config.rotationAngle
                    scaleX = 0.75f + progress * 0.35f
                    scaleY = 0.75f + progress * 0.35f
                    alpha = (progress * 1.3f).coerceIn(0f, 1f)
                }
        ) {
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.Center,
                modifier = Modifier.padding(horizontal = 20.dp, vertical = 12.dp)
            ) {
                if (config.label == "下一张") {
                    Text(
                        text = config.label,
                        color = config.badgeText,
                        fontWeight = FontWeight.ExtraBold,
                        fontSize = 19.sp
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Icon(
                        imageVector = config.badgeIcon,
                        contentDescription = null,
                        tint = config.badgeText,
                        modifier = Modifier.size(24.dp)
                    )
                } else {
                    Icon(
                        imageVector = config.badgeIcon,
                        contentDescription = null,
                        tint = config.badgeText,
                        modifier = Modifier.size(24.dp)
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text(
                        text = config.label,
                        color = config.badgeText,
                        fontWeight = FontWeight.ExtraBold,
                        fontSize = 19.sp
                    )
                }
            }
        }
    }
}
