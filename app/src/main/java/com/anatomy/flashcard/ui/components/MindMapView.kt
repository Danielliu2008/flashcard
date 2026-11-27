package com.anatomy.flashcard.ui.components

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
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
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AccountTree
import androidx.compose.material.icons.filled.ChevronRight
import androidx.compose.material.icons.filled.ExpandLess
import androidx.compose.material.icons.filled.ExpandMore
import androidx.compose.material.icons.filled.Info
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateMapOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.rotate
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.foundation.isSystemInDarkTheme
import com.anatomy.flashcard.model.MindMapData
import com.anatomy.flashcard.model.MindMapNode
import com.anatomy.flashcard.ui.theme.AppBackground
import com.anatomy.flashcard.ui.theme.AppCardBg
import com.anatomy.flashcard.ui.theme.CardBorder
import com.anatomy.flashcard.ui.theme.ChipBg
import com.anatomy.flashcard.ui.theme.GoogleBlue
import com.anatomy.flashcard.ui.theme.GoogleBlueDarkTheme
import com.anatomy.flashcard.ui.theme.GoogleBlueLight
import com.anatomy.flashcard.ui.theme.TextPrimary
import com.anatomy.flashcard.ui.theme.TextSecondary
import com.anatomy.flashcard.ui.theme.TextTertiary

@Composable
fun InteractiveMindMapView(
    mindMap: MindMapData,
    modifier: Modifier = Modifier
) {
    // Track expanded state for node IDs
    val expandedMap = remember {
        mutableStateMapOf<String, Boolean>().apply {
            // Expand root and level 1 by default
            put(mindMap.root.id, true)
            mindMap.root.children.forEach { child ->
                put(child.id, true)
            }
        }
    }

    var allExpanded by remember { mutableStateOf(false) }

    fun toggleAll(expand: Boolean) {
        allExpanded = expand
        fun setRecursive(node: MindMapNode) {
            expandedMap[node.id] = expand
            node.children.forEach { setRecursive(it) }
        }
        setRecursive(mindMap.root)
    }

    val isDark = isSystemInDarkTheme()

    Column(
        modifier = modifier
            .fillMaxSize()
            .background(AppBackground)
    ) {
        // Controls Header
        Surface(
            color = AppCardBg,
            border = BorderStroke(1.dp, CardBorder),
            modifier = Modifier.fillMaxWidth()
        ) {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 16.dp, vertical = 10.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Icon(
                        imageVector = Icons.Default.AccountTree,
                        contentDescription = null,
                        tint = GoogleBlue,
                        modifier = Modifier.size(20.dp)
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text(
                        text = mindMap.title,
                        fontWeight = FontWeight.Bold,
                        fontSize = 15.sp,
                        color = TextPrimary
                    )
                }

                OutlinedButton(
                    onClick = { toggleAll(!allExpanded) },
                    shape = RoundedCornerShape(20.dp),
                    border = BorderStroke(1.dp, CardBorder)
                ) {
                    Text(
                        text = if (allExpanded) "收起分支" else "全部展开",
                        fontSize = 12.sp,
                        color = if (isDark) GoogleBlueLight else GoogleBlue
                    )
                }
            }
        }

        // Tree List View
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            item {
                MindMapNodeItem(
                    node = mindMap.root,
                    depth = 0,
                    isExpanded = expandedMap[mindMap.root.id] ?: true,
                    onToggle = {
                        val current = expandedMap[mindMap.root.id] ?: true
                        expandedMap[mindMap.root.id] = !current
                    },
                    expandedMap = expandedMap
                )
            }
        }
    }
}

@Composable
fun MindMapNodeItem(
    node: MindMapNode,
    depth: Int,
    isExpanded: Boolean,
    onToggle: () -> Unit,
    expandedMap: MutableMap<String, Boolean>
) {
    val hasChildren = node.children.isNotEmpty()
    val rotation by animateFloatAsState(
        targetValue = if (isExpanded) 90f else 0f,
        label = "ChevronRotation"
    )

    val isDark = isSystemInDarkTheme()
    val nodeBg = when (depth) {
        0 -> if (isDark) GoogleBlueDarkTheme else GoogleBlue
        1 -> AppCardBg
        2 -> ChipBg
        else -> if (isDark) Color(0xFF333538) else Color(0xFFE8EAED)
    }

    val textColor = when (depth) {
        0 -> if (isDark) Color(0xFF041E49) else Color.White
        else -> TextPrimary
    }

    val borderColor = when (depth) {
        0 -> Color.Transparent
        1 -> if (isDark) GoogleBlueDarkTheme.copy(alpha = 0.3f) else GoogleBlue.copy(alpha = 0.3f)
        else -> CardBorder
    }

    Column(modifier = Modifier.fillMaxWidth()) {
        Card(
            shape = RoundedCornerShape(if (depth == 0) 18.dp else 14.dp),
            colors = CardDefaults.cardColors(containerColor = nodeBg),
            border = BorderStroke(1.dp, borderColor),
            elevation = CardDefaults.cardElevation(defaultElevation = if (depth <= 1) 2.dp else 0.dp),
            modifier = Modifier
                .fillMaxWidth()
                .padding(start = (depth * 16).dp)
                .clickable(enabled = hasChildren, onClick = onToggle)
        ) {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 14.dp, vertical = 12.dp),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    modifier = Modifier.weight(1f)
                ) {
                    if (hasChildren) {
                        Icon(
                            imageVector = Icons.Default.ChevronRight,
                            contentDescription = if (isExpanded) "Collapse" else "Expand",
                            tint = if (depth == 0) (if (isDark) Color(0xFF041E49) else Color.White) else (if (isDark) GoogleBlueDarkTheme else GoogleBlue),
                            modifier = Modifier
                                .size(20.dp)
                                .rotate(rotation)
                        )
                        Spacer(modifier = Modifier.width(6.dp))
                    } else {
                        Box(
                            modifier = Modifier
                                .size(8.dp)
                                .background(if (isDark) GoogleBlueDarkTheme.copy(alpha = 0.6f) else GoogleBlue.copy(alpha = 0.5f), CircleShape)
                        )
                        Spacer(modifier = Modifier.width(10.dp))
                    }

                    Column {
                        Text(
                            text = node.title,
                            fontSize = if (depth == 0) 17.sp else if (depth == 1) 15.sp else 13.sp,
                            fontWeight = if (depth <= 1) FontWeight.Bold else FontWeight.Medium,
                            color = textColor
                        )
                        if (node.note.isNotEmpty()) {
                            Text(
                                text = node.note,
                                fontSize = 11.sp,
                                color = if (depth == 0) (if (isDark) Color(0xFF041E49).copy(alpha = 0.85f) else Color.White.copy(alpha = 0.8f)) else TextSecondary,
                                modifier = Modifier.padding(top = 2.dp)
                            )
                        }
                    }
                }

                if (hasChildren) {
                    Surface(
                        shape = RoundedCornerShape(10.dp),
                        color = if (depth == 0) {
                            if (isDark) Color(0xFF041E49).copy(alpha = 0.15f) else Color.White.copy(alpha = 0.2f)
                        } else {
                            if (isDark) GoogleBlueDarkTheme.copy(alpha = 0.2f) else GoogleBlueLight.copy(alpha = 0.6f)
                        }
                    ) {
                        Text(
                            text = "${node.children.size}",
                            fontSize = 11.sp,
                            fontWeight = FontWeight.SemiBold,
                            color = if (depth == 0) {
                                if (isDark) Color(0xFF041E49) else Color.White
                            } else {
                                if (isDark) GoogleBlueDarkTheme else GoogleBlue
                            },
                            modifier = Modifier.padding(horizontal = 7.dp, vertical = 3.dp)
                        )
                    }
                }
            }
        }

        // Sub-branches
        AnimatedVisibility(visible = isExpanded && hasChildren) {
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(top = 6.dp),
                verticalArrangement = Arrangement.spacedBy(6.dp)
            ) {
                node.children.forEach { child ->
                    val childExpanded = expandedMap[child.id] ?: false
                    MindMapNodeItem(
                        node = child,
                        depth = depth + 1,
                        isExpanded = childExpanded,
                        onToggle = {
                            expandedMap[child.id] = !childExpanded
                        },
                        expandedMap = expandedMap
                    )
                }
            }
        }
    }
}
