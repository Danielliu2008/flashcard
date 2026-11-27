package com.anatomy.flashcard.ui.screens

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
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
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.ChevronRight
import androidx.compose.material.icons.filled.Edit
import androidx.compose.material.icons.filled.GridView
import androidx.compose.material.icons.filled.List
import androidx.compose.material.icons.filled.School
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FloatingActionButton
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MediumTopAppBar
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.anatomy.flashcard.model.Subject
import com.anatomy.flashcard.model.SubjectViewMode
import com.anatomy.flashcard.ui.components.EditSubjectDialog
import com.anatomy.flashcard.ui.components.EmojiPickerDialog
import com.anatomy.flashcard.ui.components.MarkdownText
import com.anatomy.flashcard.ui.theme.AppBackground
import com.anatomy.flashcard.ui.theme.AppCardBg
import com.anatomy.flashcard.ui.theme.AppSurface
import com.anatomy.flashcard.ui.theme.CardBorder
import com.anatomy.flashcard.ui.theme.ChipBg
import com.anatomy.flashcard.ui.theme.GoogleBlue
import com.anatomy.flashcard.ui.theme.TextPrimary
import com.anatomy.flashcard.ui.theme.TextSecondary
import com.anatomy.flashcard.ui.theme.TextTertiary

import androidx.compose.foundation.lazy.grid.itemsIndexed
import androidx.compose.foundation.lazy.itemsIndexed
import com.anatomy.flashcard.ui.motion.motionPressEffect
import com.anatomy.flashcard.ui.motion.staggeredEntrance

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SubjectSelectScreen(
    subjects: List<Subject>,
    viewMode: SubjectViewMode,
    onToggleViewMode: () -> Unit,
    onSelectSubject: (Subject) -> Unit,
    onAddSubject: (name: String, emoji: String, description: String) -> Unit,
    onUpdateSubject: (id: String, name: String, emoji: String, description: String) -> Unit,
    onUpdateSubjectEmoji: (id: String, newEmoji: String) -> Unit,
    onDeleteSubject: (id: String) -> Unit,
    modifier: Modifier = Modifier
) {
    var showAddDialog by remember { mutableStateOf(false) }
    var editingSubject by remember { mutableStateOf<Subject?>(null) }
    var emojiPickSubject by remember { mutableStateOf<Subject?>(null) }

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
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Surface(
                                shape = RoundedCornerShape(10.dp),
                                color = GoogleBlue.copy(alpha = 0.12f),
                                modifier = Modifier.size(36.dp)
                            ) {
                                Box(contentAlignment = Alignment.Center) {
                                    Icon(
                                        imageVector = Icons.Default.School,
                                        contentDescription = null,
                                        tint = GoogleBlue,
                                        modifier = Modifier.size(20.dp)
                                    )
                                }
                            }
                            Spacer(modifier = Modifier.width(10.dp))
                            Text(
                                text = "记忆辅助",
                                fontWeight = FontWeight.Bold,
                                color = TextPrimary,
                                fontSize = 22.sp
                            )
                        }

                        // View mode toggle button
                        Surface(
                            shape = RoundedCornerShape(12.dp),
                            color = ChipBg,
                            modifier = Modifier.clickable { onToggleViewMode() }
                        ) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                modifier = Modifier.padding(horizontal = 12.dp, vertical = 7.dp)
                            ) {
                                Icon(
                                    imageVector = if (viewMode == SubjectViewMode.GRID) Icons.Default.List else Icons.Default.GridView,
                                    contentDescription = "切换视图",
                                    tint = GoogleBlue,
                                    modifier = Modifier.size(16.dp)
                                )
                                Spacer(modifier = Modifier.width(6.dp))
                                Text(
                                    text = if (viewMode == SubjectViewMode.GRID) "列表" else "大图标",
                                    fontSize = 12.sp,
                                    fontWeight = FontWeight.SemiBold,
                                    color = TextPrimary
                                )
                            }
                        }
                    }

                    Spacer(modifier = Modifier.height(6.dp))

                    Text(
                        text = "选择复习学科 · 支持闪卡、脑图与小测",
                        color = TextSecondary,
                        fontSize = 12.sp,
                        modifier = Modifier.padding(start = 2.dp)
                    )
                }
            }
        },
        floatingActionButton = {
            FloatingActionButton(
                onClick = { showAddDialog = true },
                containerColor = GoogleBlue,
                contentColor = Color.White,
                shape = CircleShape
            ) {
                Row(
                    modifier = Modifier.padding(horizontal = 16.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Icon(Icons.Default.Add, contentDescription = "新建学科")
                    Spacer(modifier = Modifier.width(6.dp))
                    Text(text = "新建学科", fontWeight = FontWeight.SemiBold, fontSize = 14.sp)
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
            if (viewMode == SubjectViewMode.GRID) {
                // Large Icon / Grid View
                LazyVerticalGrid(
                    columns = GridCells.Fixed(2),
                    modifier = Modifier.fillMaxSize(),
                    contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = 12.dp, bottom = 90.dp),
                    horizontalArrangement = Arrangement.spacedBy(14.dp),
                    verticalArrangement = Arrangement.spacedBy(14.dp)
                ) {
                    itemsIndexed(subjects, key = { _, it -> it.id }) { index, subject ->
                        SubjectGridCard(
                            subject = subject,
                            index = index,
                            onClick = { onSelectSubject(subject) },
                            onEdit = { editingSubject = subject },
                            onChangeEmoji = { emojiPickSubject = subject }
                        )
                    }
                }
            } else {
                // List View
                LazyColumn(
                    modifier = Modifier.fillMaxSize(),
                    contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = 12.dp, bottom = 90.dp),
                    verticalArrangement = Arrangement.spacedBy(12.dp)
                ) {
                    itemsIndexed(subjects, key = { _, it -> it.id }) { index, subject ->
                        SubjectListCard(
                            subject = subject,
                            index = index,
                            onClick = { onSelectSubject(subject) },
                            onEdit = { editingSubject = subject },
                            onChangeEmoji = { emojiPickSubject = subject }
                        )
                    }
                }
            }
        }
    }

    // Add Subject Dialog
    if (showAddDialog) {
        EditSubjectDialog(
            subject = null,
            onSave = { name, emoji, desc ->
                onAddSubject(name, emoji, desc)
            },
            onDismiss = { showAddDialog = false }
        )
    }

    // Edit Subject Dialog
    if (editingSubject != null) {
        EditSubjectDialog(
            subject = editingSubject,
            onSave = { name, emoji, desc ->
                onUpdateSubject(editingSubject!!.id, name, emoji, desc)
                editingSubject = null
            },
            onDelete = {
                onDeleteSubject(editingSubject!!.id)
                editingSubject = null
            },
            onDismiss = { editingSubject = null }
        )
    }

    // Quick Change Emoji Dialog
    if (emojiPickSubject != null) {
        EmojiPickerDialog(
            currentEmoji = emojiPickSubject!!.emoji,
            onEmojiSelected = { newEmoji ->
                onUpdateSubjectEmoji(emojiPickSubject!!.id, newEmoji)
                emojiPickSubject = null
            },
            onDismiss = { emojiPickSubject = null }
        )
    }
}

/**
 * 大图标视图卡片 (Grid Card)
 */
@Composable
private fun SubjectGridCard(
    subject: Subject,
    index: Int,
    onClick: () -> Unit,
    onEdit: () -> Unit,
    onChangeEmoji: () -> Unit
) {
    Card(
        shape = RoundedCornerShape(20.dp),
        colors = CardDefaults.cardColors(containerColor = AppCardBg),
        border = BorderStroke(1.dp, CardBorder),
        elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
        modifier = Modifier
            .fillMaxWidth()
            .staggeredEntrance(index = index)
            .motionPressEffect(pressedScale = 0.95f) { onClick() }
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
        ) {
            // Top Row: Big Emoji + Edit button
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.Top
            ) {
                Box(
                    modifier = Modifier
                        .size(64.dp)
                        .clip(RoundedCornerShape(18.dp))
                        .background(Color(subject.colorHex).copy(alpha = 0.1f))
                        .clickable { onChangeEmoji() },
                    contentAlignment = Alignment.Center
                ) {
                    Text(
                        text = subject.emoji,
                        fontSize = 36.sp
                    )
                }

                IconButton(
                    onClick = onEdit,
                    modifier = Modifier.size(28.dp)
                ) {
                    Icon(
                        imageVector = Icons.Default.Edit,
                        contentDescription = "编辑学科",
                        tint = TextTertiary,
                        modifier = Modifier.size(16.dp)
                    )
                }
            }

            Spacer(modifier = Modifier.height(14.dp))

            Text(
                text = subject.name,
                fontWeight = FontWeight.Bold,
                fontSize = 16.sp,
                color = TextPrimary,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )

            Spacer(modifier = Modifier.height(4.dp))

            MarkdownText(
                text = subject.description.ifEmpty { "点击开始复习" },
                fontSize = 11.sp,
                color = TextSecondary,
                maxLines = 2,
                overflow = TextOverflow.Ellipsis,
                lineHeight = 15.sp,
                modifier = Modifier.height(30.dp)
            )

            Spacer(modifier = Modifier.height(12.dp))

            // Bottom pill: 进入复习
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                if (subject.isBuiltIn) {
                    Surface(
                        shape = RoundedCornerShape(6.dp),
                        color = Color(0xFFE8F0FE)
                    ) {
                        Text(
                            text = "内置学科",
                            fontSize = 10.sp,
                            fontWeight = FontWeight.SemiBold,
                            color = GoogleBlue,
                            modifier = Modifier.padding(horizontal = 6.dp, vertical = 2.dp)
                        )
                    }
                } else {
                    Spacer(modifier = Modifier.width(1.dp))
                }

                Icon(
                    imageVector = Icons.Default.ChevronRight,
                    contentDescription = null,
                    tint = GoogleBlue,
                    modifier = Modifier.size(20.dp)
                )
            }
        }
    }
}

/**
 * 列表视图卡片 (List Card)
 */
@Composable
private fun SubjectListCard(
    subject: Subject,
    index: Int,
    onClick: () -> Unit,
    onEdit: () -> Unit,
    onChangeEmoji: () -> Unit
) {
    Card(
        shape = RoundedCornerShape(16.dp),
        colors = CardDefaults.cardColors(containerColor = AppCardBg),
        border = BorderStroke(1.dp, CardBorder),
        elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
        modifier = Modifier
            .fillMaxWidth()
            .staggeredEntrance(index = index)
            .motionPressEffect(pressedScale = 0.96f) { onClick() }
    ) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(14.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            // Big Rounded Emoji Box
            Box(
                modifier = Modifier
                    .size(52.dp)
                    .clip(RoundedCornerShape(16.dp))
                    .background(Color(subject.colorHex).copy(alpha = 0.12f))
                    .clickable { onChangeEmoji() },
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = subject.emoji,
                    fontSize = 28.sp
                )
            }

            Spacer(modifier = Modifier.width(14.dp))

            Column(modifier = Modifier.weight(1f)) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Text(
                        text = subject.name,
                        fontWeight = FontWeight.Bold,
                        fontSize = 16.sp,
                        color = TextPrimary
                    )
                    if (subject.isBuiltIn) {
                        Spacer(modifier = Modifier.width(6.dp))
                        Surface(
                            shape = RoundedCornerShape(4.dp),
                            color = Color(0xFFE8F0FE)
                        ) {
                            Text(
                                text = "内置",
                                fontSize = 9.sp,
                                fontWeight = FontWeight.Bold,
                                color = GoogleBlue,
                                modifier = Modifier.padding(horizontal = 4.dp, vertical = 1.dp)
                            )
                        }
                    }
                }

                Spacer(modifier = Modifier.height(4.dp))

                MarkdownText(
                    text = subject.description.ifEmpty { "点击开始复习" },
                    fontSize = 12.sp,
                    color = TextSecondary,
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis
                )
            }

            IconButton(
                onClick = onEdit,
                modifier = Modifier.size(32.dp)
            ) {
                Icon(
                    imageVector = Icons.Default.Edit,
                    contentDescription = "编辑学科",
                    tint = TextTertiary,
                    modifier = Modifier.size(16.dp)
                )
            }

            Icon(
                imageVector = Icons.Default.ChevronRight,
                contentDescription = null,
                tint = GoogleBlue,
                modifier = Modifier.size(20.dp)
            )
        }
    }
}
