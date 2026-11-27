package com.anatomy.flashcard.model

data class MindMapNode(
    val id: String,
    val title: String,
    val note: String = "",
    val children: List<MindMapNode> = emptyList()
)

data class MindMapData(
    val id: String,
    val systemType: AnatomySystemType,
    val title: String,
    val root: MindMapNode,
    val rawHtml: String = ""
)
