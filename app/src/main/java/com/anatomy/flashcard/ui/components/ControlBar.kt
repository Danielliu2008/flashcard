package com.anatomy.flashcard.ui.components

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.automirrored.filled.ArrowForward
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Close
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.FilledTonalIconButton
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButtonDefaults
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.anatomy.flashcard.ui.motion.motionPressEffect
import com.anatomy.flashcard.model.CardAcquisition
import com.anatomy.flashcard.ui.theme.ChipBg
import com.anatomy.flashcard.ui.theme.GotItGreen
import com.anatomy.flashcard.ui.theme.GotItGreenBg
import com.anatomy.flashcard.ui.theme.GotItGreenBorder
import com.anatomy.flashcard.ui.theme.MissedItRed
import com.anatomy.flashcard.ui.theme.MissedItRedBg
import com.anatomy.flashcard.ui.theme.MissedItRedBorder
import com.anatomy.flashcard.ui.theme.TextPrimary

@Composable
fun StudyControlBar(
    hasPrevious: Boolean,
    hasNext: Boolean,
    currentStatus: CardAcquisition?,
    onPrevious: () -> Unit,
    onNext: () -> Unit,
    onMissedIt: () -> Unit,
    onGotIt: () -> Unit,
    modifier: Modifier = Modifier
) {
    Row(
        modifier = modifier
            .fillMaxWidth()
            .padding(horizontal = 12.dp, vertical = 10.dp),
        horizontalArrangement = Arrangement.spacedBy(10.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        // Previous Card Button (固定高度 50dp，同级高度统一)
        FilledTonalIconButton(
            onClick = onPrevious,
            enabled = hasPrevious,
            shape = RoundedCornerShape(16.dp),
            modifier = Modifier
                .size(50.dp)
                .motionPressEffect(pressedScale = 0.92f),
            colors = IconButtonDefaults.filledTonalIconButtonColors(
                containerColor = ChipBg,
                contentColor = TextPrimary
            )
        ) {
            Icon(
                imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                contentDescription = "上一张"
            )
        }

        // "未掌握" (Missed It) 按钮 (高度 50dp，权重 1f)
        val isMissed = currentStatus == CardAcquisition.NOT_ACQUIRED
        OutlinedButton(
            onClick = onMissedIt,
            shape = RoundedCornerShape(16.dp),
            contentPadding = PaddingValues(horizontal = 6.dp, vertical = 0.dp),
            border = BorderStroke(
                1.5.dp,
                if (isMissed) MissedItRed else MissedItRedBorder
            ),
            colors = ButtonDefaults.outlinedButtonColors(
                containerColor = if (isMissed) MissedItRedBg else Color.Transparent,
                contentColor = MissedItRed
            ),
            modifier = Modifier
                .weight(1f)
                .height(50.dp)
                .motionPressEffect(pressedScale = 0.94f)
        ) {
            Icon(
                imageVector = Icons.Default.Close,
                contentDescription = null,
                modifier = Modifier.size(18.dp)
            )
            Spacer(modifier = Modifier.width(4.dp))
            Text(
                text = "未掌握",
                fontSize = 13.5.sp,
                fontWeight = FontWeight.Bold,
                maxLines = 1
            )
        }

        // "已掌握" (Got It) 按钮 (高度 50dp，权重 1f)
        val isGot = currentStatus == CardAcquisition.ACQUIRED
        OutlinedButton(
            onClick = onGotIt,
            shape = RoundedCornerShape(16.dp),
            contentPadding = PaddingValues(horizontal = 6.dp, vertical = 0.dp),
            border = BorderStroke(
                1.5.dp,
                if (isGot) GotItGreen else GotItGreenBorder
            ),
            colors = ButtonDefaults.outlinedButtonColors(
                containerColor = if (isGot) GotItGreenBg else Color.Transparent,
                contentColor = GotItGreen
            ),
            modifier = Modifier
                .weight(1f)
                .height(50.dp)
                .motionPressEffect(pressedScale = 0.94f)
        ) {
            Icon(
                imageVector = Icons.Default.Check,
                contentDescription = null,
                modifier = Modifier.size(18.dp)
            )
            Spacer(modifier = Modifier.width(4.dp))
            Text(
                text = "已掌握",
                fontSize = 13.5.sp,
                fontWeight = FontWeight.Bold,
                maxLines = 1
            )
        }

        // Next Card Button (固定高度 50dp，同级高度统一)
        FilledTonalIconButton(
            onClick = onNext,
            shape = RoundedCornerShape(16.dp),
            modifier = Modifier
                .size(50.dp)
                .motionPressEffect(pressedScale = 0.92f),
            colors = IconButtonDefaults.filledTonalIconButtonColors(
                containerColor = ChipBg,
                contentColor = TextPrimary
            )
        ) {
            Icon(
                imageVector = Icons.AutoMirrored.Filled.ArrowForward,
                contentDescription = "下一张"
            )
        }
    }
}
