package com.anatomy.flashcard.ui.components

import android.net.Uri
import android.widget.Toast
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.Info
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExposedDropdownMenuBox
import androidx.compose.material3.ExposedDropdownMenuDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.OutlinedTextFieldDefaults
import androidx.compose.material3.PrimaryTabRow
import androidx.compose.material3.Surface
import androidx.compose.material3.Tab
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.DialogProperties
import com.anatomy.flashcard.data.ImportInspectionResult
import com.anatomy.flashcard.data.ImportManager
import com.anatomy.flashcard.data.ImportedDataType
import com.anatomy.flashcard.model.AnatomySystemType
import com.anatomy.flashcard.ui.theme.AppCardBg
import com.anatomy.flashcard.ui.theme.AppSurface
import com.anatomy.flashcard.ui.theme.CardBorder
import com.anatomy.flashcard.ui.theme.ChipBg
import com.anatomy.flashcard.ui.theme.GoogleBlue
import com.anatomy.flashcard.ui.theme.GotItGreen
import com.anatomy.flashcard.ui.theme.GotItGreenBg
import com.anatomy.flashcard.ui.theme.GotItGreenBorder
import com.anatomy.flashcard.ui.theme.MissedItRed
import com.anatomy.flashcard.ui.theme.MissedItRedBg
import com.anatomy.flashcard.ui.theme.MissedItRedBorder
import com.anatomy.flashcard.ui.theme.TextPrimary
import com.anatomy.flashcard.ui.theme.TextSecondary
import java.io.InputStreamReader

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ImportDialog(
    importManager: ImportManager,
    onDismiss: () -> Unit,
    onImportSuccess: () -> Unit
) {
    val context = LocalContext.current
    var selectedTab by remember { mutableIntStateOf(0) }
    var jsonInputText by remember { mutableStateOf("") }
    var inspectionResult by remember { mutableStateOf<ImportInspectionResult?>(null) }
    var selectedSystem by remember { mutableStateOf(AnatomySystemType.NERVOUS) }
    var systemDropdownExpanded by remember { mutableStateOf(false) }

    fun processContent(content: String) {
        val result = importManager.inspectJson(content)
        inspectionResult = result
        if (result.isValid) {
            selectedSystem = result.suggestedSystem
        }
    }

    val filePickerLauncher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.GetContent()
    ) { uri: Uri? ->
        if (uri != null) {
            try {
                val mimeType = context.contentResolver.getType(uri) ?: ""
                val uriStr = uri.toString().lowercase()

                // 探测是否为 ZIP 压缩包
                val isZipByMime = mimeType.contains("zip") || mimeType.contains("octet-stream")
                val isZipByName = uriStr.endsWith(".zip")
                val isZipHeader = try {
                    context.contentResolver.openInputStream(uri)?.use { s ->
                        val b0 = s.read()
                        val b1 = s.read()
                        b0 == 0x50 && b1 == 0x4B // PK..
                    } ?: false
                } catch (_: Exception) { false }

                if (isZipByMime || isZipByName || isZipHeader) {
                    val zipResult = context.contentResolver.openInputStream(uri)?.use { stream ->
                        importManager.importZip(stream)
                    }
                    if (zipResult?.isSuccess == true) {
                        Toast.makeText(context, zipResult.message, Toast.LENGTH_LONG).show()
                        onImportSuccess()
                        onDismiss()
                    } else {
                        Toast.makeText(context, zipResult?.message ?: "ZIP 导入失败", Toast.LENGTH_LONG).show()
                    }
                    return@rememberLauncherForActivityResult
                }

                // 否则作为普通 JSON 文本读取
                val content = context.contentResolver.openInputStream(uri)?.use { stream ->
                    InputStreamReader(stream, Charsets.UTF_8).readText()
                } ?: ""
                jsonInputText = content
                processContent(content)
            } catch (e: Exception) {
                Toast.makeText(context, "读取文件失败: ${e.localizedMessage}", Toast.LENGTH_SHORT).show()
            }
        }
    }

    AlertDialog(
        onDismissRequest = onDismiss,
        properties = DialogProperties(usePlatformDefaultWidth = false),
        modifier = Modifier
            .fillMaxWidth(0.94f)
            .padding(vertical = 24.dp),
        content = {
            Surface(
                shape = RoundedCornerShape(28.dp),
                color = AppCardBg,
                border = BorderStroke(1.dp, CardBorder)
            ) {
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(20.dp)
                        .verticalScroll(rememberScrollState())
                ) {
                    // Header
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Surface(
                                shape = CircleShape,
                                color = GoogleBlue.copy(alpha = 0.12f),
                                modifier = Modifier.size(38.dp)
                            ) {
                                Box(contentAlignment = Alignment.Center) {
                                    Icon(
                                        imageVector = Icons.Default.Add,
                                        contentDescription = null,
                                        tint = GoogleBlue,
                                        modifier = Modifier.size(20.dp)
                                    )
                                }
                            }
                            Spacer(modifier = Modifier.width(10.dp))
                            Column {
                                Text(
                                    text = "导入数据 (JSON)",
                                    fontSize = 18.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = TextPrimary
                                )
                                Text(
                                    text = "支持单独导入闪卡、导图或测验",
                                    fontSize = 11.sp,
                                    color = TextSecondary
                                )
                            }
                        }

                        IconButton(onClick = onDismiss) {
                            Icon(Icons.Default.Close, contentDescription = "关闭", tint = TextSecondary)
                        }
                    }

                    Spacer(modifier = Modifier.height(14.dp))

                    // Tab: File / Paste
                    PrimaryTabRow(
                        selectedTabIndex = selectedTab,
                        containerColor = ChipBg,
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Tab(
                            selected = selectedTab == 0,
                            onClick = { selectedTab = 0 },
                            text = { Text("📁 选择本地文件", fontSize = 13.sp, color = if (selectedTab == 0) GoogleBlue else TextSecondary) }
                        )
                        Tab(
                            selected = selectedTab == 1,
                            onClick = { selectedTab = 1 },
                            text = { Text("📋 粘贴 JSON 文本", fontSize = 13.sp, color = if (selectedTab == 1) GoogleBlue else TextSecondary) }
                        )
                    }

                    Spacer(modifier = Modifier.height(14.dp))

                    if (selectedTab == 0) {
                        // File picker view
                        Card(
                            shape = RoundedCornerShape(16.dp),
                            colors = CardDefaults.cardColors(containerColor = ChipBg),
                            border = BorderStroke(1.dp, CardBorder),
                            modifier = Modifier
                                .fillMaxWidth()
                                .clickable { filePickerLauncher.launch("*/*") }
                        ) {
                            Column(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .padding(24.dp),
                                horizontalAlignment = Alignment.CenterHorizontally
                            ) {
                                Icon(
                                    imageVector = Icons.Default.Add,
                                    contentDescription = null,
                                    tint = GoogleBlue,
                                    modifier = Modifier.size(40.dp)
                                )
                                Spacer(modifier = Modifier.height(10.dp))
                                Text(
                                    text = "点击从手机选取 .json 或 .zip 文件",
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 14.sp,
                                    color = TextPrimary
                                )
                                Text(
                                    text = "支持油猴脚本一键导出的 ZIP 压缩包全量批量导入，或单个 JSON 文件导入",
                                    fontSize = 11.sp,
                                    color = TextSecondary,
                                    modifier = Modifier.padding(top = 4.dp)
                                )
                            }
                        }
                    } else {
                        // Paste text view
                        OutlinedTextField(
                            value = jsonInputText,
                            onValueChange = {
                                jsonInputText = it
                                processContent(it)
                            },
                            placeholder = { Text("在此粘贴导出的原始 JSON 数据...", fontSize = 12.sp) },
                            maxLines = 6,
                            minLines = 4,
                            shape = RoundedCornerShape(14.dp),
                            colors = OutlinedTextFieldDefaults.colors(
                                focusedBorderColor = GoogleBlue,
                                unfocusedBorderColor = CardBorder
                            ),
                            modifier = Modifier.fillMaxWidth()
                        )
                    }

                    // Inspection Result Card
                    val result = inspectionResult
                    if (result != null) {
                        Spacer(modifier = Modifier.height(14.dp))
                        Card(
                            shape = RoundedCornerShape(16.dp),
                            colors = CardDefaults.cardColors(
                                containerColor = if (result.isValid) GotItGreenBg else MissedItRedBg
                            ),
                            border = BorderStroke(1.dp, if (result.isValid) GotItGreenBorder else MissedItRedBorder),
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Column(modifier = Modifier.padding(14.dp)) {
                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    Icon(
                                        imageVector = if (result.isValid) Icons.Default.Check else Icons.Default.Info,
                                        contentDescription = null,
                                        tint = if (result.isValid) GotItGreen else MissedItRed,
                                        modifier = Modifier.size(20.dp)
                                    )
                                    Spacer(modifier = Modifier.width(8.dp))
                                    Text(
                                        text = result.message,
                                        fontSize = 13.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = if (result.isValid) GotItGreen else MissedItRed
                                    )
                                }

                                if (result.isValid) {
                                    Spacer(modifier = Modifier.height(10.dp))
                                    Text(
                                        text = "导入目标系统：",
                                        fontSize = 12.sp,
                                        fontWeight = FontWeight.SemiBold,
                                        color = TextPrimary
                                    )

                                    Spacer(modifier = Modifier.height(6.dp))

                                    // System selector dropdown
                                    ExposedDropdownMenuBox(
                                        expanded = systemDropdownExpanded,
                                        onExpandedChange = { systemDropdownExpanded = !systemDropdownExpanded }
                                    ) {
                                        OutlinedTextField(
                                            value = "${selectedSystem.title} (${selectedSystem.subtitle})",
                                            onValueChange = {},
                                            readOnly = true,
                                            trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = systemDropdownExpanded) },
                                            shape = RoundedCornerShape(10.dp),
                                            colors = OutlinedTextFieldDefaults.colors(
                                                focusedBorderColor = GoogleBlue,
                                                unfocusedBorderColor = CardBorder
                                            ),
                                            modifier = Modifier
                                                .menuAnchor()
                                                .fillMaxWidth()
                                        )

                                        ExposedDropdownMenu(
                                            expanded = systemDropdownExpanded,
                                            onDismissRequest = { systemDropdownExpanded = false }
                                        ) {
                                            listOf(
                                                AnatomySystemType.SKELETAL,
                                                AnatomySystemType.NERVOUS,
                                                AnatomySystemType.MUSCULAR
                                            ).forEach { sys ->
                                                DropdownMenuItem(
                                                    text = { Text("${sys.title} (${sys.subtitle})") },
                                                    onClick = {
                                                        selectedSystem = sys
                                                        systemDropdownExpanded = false
                                                    }
                                                )
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }

                    Spacer(modifier = Modifier.height(20.dp))

                    // Buttons
                    Column(
                        modifier = Modifier.fillMaxWidth(),
                        verticalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        Button(
                            onClick = {
                                val res = inspectionResult
                                if (res != null && res.isValid) {
                                    val ok = importManager.saveImport(res.type, selectedSystem, res.rawJson)
                                    if (ok) {
                                        Toast.makeText(context, "导入成功！已更新${selectedSystem.title}数据", Toast.LENGTH_SHORT).show()
                                        onImportSuccess()
                                        onDismiss()
                                    } else {
                                        Toast.makeText(context, "保存失败，请检查存储权限", Toast.LENGTH_SHORT).show()
                                    }
                                }
                            },
                            enabled = inspectionResult?.isValid == true,
                            shape = RoundedCornerShape(16.dp),
                            colors = ButtonDefaults.buttonColors(containerColor = GoogleBlue),
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(48.dp)
                        ) {
                            Text("确认导入并生效", fontWeight = FontWeight.Bold)
                        }

                        if (importManager.hasCustomData()) {
                            OutlinedButton(
                                onClick = {
                                    val ok = importManager.clearAllCustomData()
                                    if (ok) {
                                        Toast.makeText(context, "已恢复初始默认内置数据", Toast.LENGTH_SHORT).show()
                                        onImportSuccess()
                                        onDismiss()
                                    }
                                },
                                shape = RoundedCornerShape(16.dp),
                                border = BorderStroke(1.dp, CardBorder),
                                colors = ButtonDefaults.outlinedButtonColors(contentColor = MissedItRed),
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .height(44.dp)
                            ) {
                                Icon(Icons.Default.Delete, contentDescription = null, modifier = Modifier.size(16.dp))
                                Spacer(modifier = Modifier.width(6.dp))
                                Text("清空自定义导入，恢复默认数据", fontSize = 12.sp)
                            }
                        }
                    }
                }
            }
        }
    )
}
