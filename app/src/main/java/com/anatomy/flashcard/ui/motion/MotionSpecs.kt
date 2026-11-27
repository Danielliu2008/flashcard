package com.anatomy.flashcard.ui.motion

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.CubicBezierEasing
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.spring
import androidx.compose.animation.core.tween
import androidx.compose.foundation.clickable
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.offset
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.composed
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlin.math.roundToInt

/**
 * motion-prompt 动效系统设计规范 (基于 showheyohtaki/motion-prompt)
 *
 * 核心动效术语与实现映射：
 * - #001 弹性入场 (Pop-in): 元素以轻微过冲的弹簧出现 (Overshoot 约 10%)
 * - #002 交错动画 (Stagger): 列表项按序号错开延迟依次滑入淡显
 * - #009 缓动 (Easing): FastOutSlowIn 与 CubicBezier(0.2, 0.0, 0.0, 1.0)
 * - #010 过冲回弹 (Overshoot): Spring 阻尼振荡
 * - #011 挤压与拉伸 (Squash & Stretch): 点击按压时轻微压缩 (0.95x)，松手回弹 (1.02x -> 1.0x)
 */
object MotionSpecs {
    // 弹性入场与按钮回弹 (#001 Pop-in, #010 Overshoot)
    val SpringBouncy = spring<Float>(
        dampingRatio = 0.72f,
        stiffness = 380f
    )

    // 平滑页面滑动与位置过渡 (#009 Easing)
    val SpringSmooth = spring<Float>(
        dampingRatio = 0.88f,
        stiffness = 450f
    )

    // 经典强调曲线
    val EmphasizedEasing = CubicBezierEasing(0.2f, 0.0f, 0.0f, 1.0f)
    val EmphasizedDecelerate = CubicBezierEasing(0.05f, 0.7f, 0.1f, 1.0f)

    // 交错动画默认单步延迟
    const val StaggerStepDelayMs = 45
}

/**
 * #011 挤压与拉伸 (Squash & Stretch) 按压微交互修饰符
 * 按下时平滑缩放至 0.95f，松手或滑开时以弹簧弹性恢复 1.0f
 */
fun Modifier.motionPressEffect(
    pressedScale: Float = 0.96f,
    onClick: (() -> Unit)? = null
): Modifier = composed {
    var isPressed by remember { mutableStateOf(false) }
    val scale = remember { Animatable(1f) }

    LaunchedEffect(isPressed) {
        if (isPressed) {
            scale.animateTo(
                targetValue = pressedScale,
                animationSpec = tween(durationMillis = 100, easing = MotionSpecs.EmphasizedDecelerate)
            )
        } else {
            scale.animateTo(
                targetValue = 1f,
                animationSpec = MotionSpecs.SpringBouncy
            )
        }
    }

    this
        .graphicsLayer {
            scaleX = scale.value
            scaleY = scale.value
        }
        .pointerInput(onClick) {
            detectTapGestures(
                onPress = {
                    isPressed = true
                    val released = try {
                        tryAwaitRelease()
                    } catch (e: Exception) {
                        false
                    }
                    isPressed = false
                    if (released && onClick != null) {
                        onClick()
                    }
                }
            )
        }
}

/**
 * #002 交错动画 (Stagger Animation)
 * 列表/网格项根据 index 错峰自下方滑入并渐变淡出
 */
fun Modifier.staggeredEntrance(
    index: Int,
    baseDelayMs: Int = MotionSpecs.StaggerStepDelayMs,
    initialOffsetY: Float = 50f
): Modifier = composed {
    val alphaAnim = remember { Animatable(0f) }
    val offsetAnim = remember { Animatable(initialOffsetY) }

    LaunchedEffect(Unit) {
        val delayTime = (index.coerceAtMost(12) * baseDelayMs).toLong()
        delay(delayTime)
        // 并发执行透明度与位移动画
        launch {
            alphaAnim.animateTo(
                targetValue = 1f,
                animationSpec = tween(durationMillis = 280, easing = FastOutSlowInEasing)
            )
        }
        launch {
            offsetAnim.animateTo(
                targetValue = 0f,
                animationSpec = spring(
                    dampingRatio = 0.78f,
                    stiffness = 360f
                )
            )
        }
    }

    this
        .offset { IntOffset(0, offsetAnim.value.roundToInt()) }
        .alpha(alphaAnim.value)
}

/**
 * #001 弹性弹出修饰符 (Pop-in)
 */
fun Modifier.popInEntrance(
    delayMs: Long = 0L
): Modifier = composed {
    val scaleAnim = remember { Animatable(0.7f) }
    val alphaAnim = remember { Animatable(0f) }

    LaunchedEffect(Unit) {
        if (delayMs > 0) delay(delayMs)
        launch {
            scaleAnim.animateTo(1f, animationSpec = MotionSpecs.SpringBouncy)
        }
        launch {
            alphaAnim.animateTo(1f, animationSpec = tween(200))
        }
    }

    this
        .graphicsLayer {
            scaleX = scaleAnim.value
            scaleY = scaleAnim.value
        }
        .alpha(alphaAnim.value)
}
