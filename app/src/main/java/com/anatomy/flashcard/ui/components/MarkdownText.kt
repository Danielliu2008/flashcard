package com.anatomy.flashcard.ui.components

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.LocalTextStyle
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.BaselineShift
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.TextUnit
import androidx.compose.ui.unit.sp
import com.anatomy.flashcard.ui.theme.GoogleBlue
import com.anatomy.flashcard.ui.theme.GoogleBlueDarkTheme
import java.util.regex.Pattern

/**
 * 全局统一的 Markdown 与 LaTeX 数学公式 ($...$ 和 $$...$$) 渲染组件。
 * 纯原生 Compose AnnotatedString 实现，零外部重型依赖，离线极速运行。
 */
object MarkdownEngine {

    private val GREEK_MAP = mapOf(
        "\\alpha" to "α", "\\beta" to "β", "\\gamma" to "γ", "\\delta" to "δ",
        "\\epsilon" to "ε", "\\varepsilon" to "ε", "\\zeta" to "ζ", "\\eta" to "η",
        "\\theta" to "θ", "\\iota" to "ι", "\\kappa" to "κ", "\\lambda" to "λ",
        "\\mu" to "μ", "\\nu" to "ν", "\\xi" to "ξ", "\\pi" to "π",
        "\\rho" to "ρ", "\\sigma" to "σ", "\\tau" to "τ", "\\upsilon" to "υ",
        "\\phi" to "φ", "\\varphi" to "φ", "\\chi" to "χ", "\\psi" to "ψ", "\\omega" to "ω",
        "\\Gamma" to "Γ", "\\Delta" to "Δ", "\\Theta" to "Θ", "\\Lambda" to "Λ",
        "\\Xi" to "Ξ", "\\Pi" to "Π", "\\Sigma" to "Σ", "\\Phi" to "Φ",
        "\\Psi" to "Ψ", "\\Omega" to "Ω"
    )

    private val SYMBOL_MAP = mapOf(
        "\\AA" to "Å",
        "\\circ" to "°",
        "\\ge" to "≥", "\\geq" to "≥",
        "\\le" to "≤", "\\leq" to "≤",
        "\\approx" to "≈", "\\sim" to "~",
        "\\pm" to "±", "\\mp" to "∓",
        "\\times" to "×", "\\div" to "÷",
        "\\cdot" to "·", "\\neq" to "≠",
        "\\equiv" to "≡", "\\infty" to "∞",
        "\\rightarrow" to "→", "\\to" to "→",
        "\\leftarrow" to "←",
        "\\Rightarrow" to "⇒", "\\Leftarrow" to "⇐",
        "\\leftrightarrow" to "↔",
        "\\%" to "%", "\\$" to "$", "\\_" to "_", "\\&" to "&"
    )

    private val SUP_MAP = mapOf(
        '0' to '⁰', '1' to '¹', '2' to '²', '3' to '³', '4' to '⁴', '5' to '⁵',
        '6' to '⁶', '7' to '⁷', '8' to '⁸', '9' to '⁹', '+' to '⁺', '-' to '⁻',
        '=' to '⁼', '(' to '⁽', ')' to '⁾', 'n' to 'ⁿ', 'i' to 'ⁱ'
    )

    private val SUB_MAP = mapOf(
        '0' to '₀', '1' to '₁', '2' to '₂', '3' to '₃', '4' to '₄', '5' to '₅',
        '6' to '₆', '7' to '₇', '8' to '₈', '9' to '₉', '+' to '₊', '-' to '₋',
        '=' to '₌', '(' to '₍', ')' to '₎', 'a' to 'ₐ', 'e' to 'ₑ', 'o' to 'ₒ',
        'x' to 'ₓ', 'h' to 'ₕ', 'k' to 'ₖ', 'l' to 'ₗ', 'm' to 'ₘ', 'n' to 'ₙ',
        'p' to 'ₚ', 's' to 'ₛ', 't' to 'ₜ', 'i' to 'ᵢ', 'j' to 'ⱼ',
        'L' to 'ₗ', 'H' to 'ₕ'
    )

    private fun toSuperscript(s: String): String {
        val sb = StringBuilder()
        for (ch in s) {
            sb.append(SUP_MAP[ch] ?: ch)
        }
        return sb.toString()
    }

    private fun toSubscript(s: String): String {
        val sb = StringBuilder()
        for (ch in s) {
            sb.append(SUB_MAP[ch] ?: ch)
        }
        return sb.toString()
    }

    /**
     * 将包含 LaTeX 的单条公式文本转写为高可读 Unicode 数学符号
     */
    fun parseMathFormula(latex: String): String {
        var s = latex.trim()

        // 1. 替换已知符号与希腊字母
        for ((k, v) in SYMBOL_MAP) {
            s = s.replace(k, v)
        }
        for ((k, v) in GREEK_MAP) {
            s = s.replace(Regex(Pattern.quote(k) + "(?![a-zA-Z])"), v)
        }

        // 2. 分数 \frac{a}{b} -> a/b
        s = s.replace(Regex("""\\frac\{([^{}]+)\}\{([^{}]+)\}""")) {
            "${it.groupValues[1]}/${it.groupValues[2]}"
        }

        // 3. 字体样式包装 \text{...}, \mathrm{...}, \textbf{...}, \mathit{...}
        s = s.replace(Regex("""\\(?:text|mathrm|textbf|mathit)\{([^{}]+)\}""")) {
            it.groupValues[1]
        }

        // 4. 上标转写 ^{...} 与 ^c
        s = s.replace(Regex("""\^\{([^{}]+)\}""")) {
            toSuperscript(it.groupValues[1])
        }
        s = s.replace(Regex("""\^([0-9\+\-°])""")) {
            toSuperscript(it.groupValues[1])
        }

        // 5. 下标转写 _{...} 与 _c
        s = s.replace(Regex("""_\{([^{}]+)\}""")) {
            toSubscript(it.groupValues[1])
        }
        s = s.replace(Regex("""_([0-9a-zA-Z\+\-])""")) {
            toSubscript(it.groupValues[1])
        }

        // 6. 清理间距命令与残留斜杠
        s = s.replace(Regex("""\\(?:quad|qquad|;|,|\s)"""), " ")
        s = s.replace("\\", "")

        return s.trim()
    }

    /**
     * 核心构建：将 Markdown + Math 文本编译为带样式的 AnnotatedString
     */
    fun buildAnnotatedString(
        source: String,
        isDark: Boolean,
        inlineMathHighlight: Boolean = true
    ): AnnotatedString {
        if (source.isEmpty()) return AnnotatedString("")

        // 1. 隔离数学公式（避免公式内部的 _ 下标和 * 乘号被 Markdown 错认为斜体/加粗）
        val mathBlocks = mutableListOf<String>()
        val mathInlines = mutableListOf<String>()

        var processed = source
        // 1.1 块级公式 $$...$$
        processed = processed.replace(Regex("""\$\$([\s\S]+?)\$\$""")) {
            mathBlocks.add(parseMathFormula(it.groupValues[1]))
            "%%%MATH_BLOCK_${mathBlocks.size - 1}%%%"
        }

        // 1.2 行内公式 $...$（排除转义的 \$）
        processed = processed.replace(Regex("""(?<!\\)\$([^\$\n]+?)(?<!\\)\$""")) {
            mathInlines.add(parseMathFormula(it.groupValues[1]))
            "%%%MATH_INLINE_${mathInlines.size - 1}%%%"
        }

        // 2. 颜色方案
        val mathColor = if (inlineMathHighlight) {
            if (isDark) GoogleBlueDarkTheme else GoogleBlue
        } else Color.Unspecified

        val codeBgColor = if (isDark) Color(0xFF2D2E30) else Color(0xFFF1F3F4)
        val codeTextColor = if (isDark) Color(0xFFFFC107) else Color(0xFFB06000)
        val quoteBarColor = if (isDark) GoogleBlueDarkTheme else GoogleBlue

        // 3. 构建 AnnotatedString
        return buildAnnotatedString {
            val lines = processed.split("\n")

            for (lineIndex in lines.indices) {
                var line = lines[lineIndex]

                if (lineIndex > 0) {
                    append("\n")
                }

                // 处理引用块 > ...
                if (line.startsWith("> ") || line == ">") {
                    line = line.removePrefix(">").trimStart()
                    pushStyle(SpanStyle(color = quoteBarColor, fontWeight = FontWeight.Bold))
                    append("▎ ")
                    pop()
                    pushStyle(SpanStyle(fontStyle = FontStyle.Italic))
                    renderInlineStyles(line, mathBlocks, mathInlines, mathColor, codeBgColor, codeTextColor)
                    pop()
                    continue
                }

                // 处理标题
                when {
                    line.startsWith("### ") -> {
                        pushStyle(SpanStyle(fontSize = 17.sp, fontWeight = FontWeight.Bold))
                        renderInlineStyles(line.removePrefix("### ").trim(), mathBlocks, mathInlines, mathColor, codeBgColor, codeTextColor)
                        pop()
                        continue
                    }
                    line.startsWith("## ") -> {
                        pushStyle(SpanStyle(fontSize = 19.sp, fontWeight = FontWeight.Bold))
                        renderInlineStyles(line.removePrefix("## ").trim(), mathBlocks, mathInlines, mathColor, codeBgColor, codeTextColor)
                        pop()
                        continue
                    }
                    line.startsWith("# ") -> {
                        pushStyle(SpanStyle(fontSize = 22.sp, fontWeight = FontWeight.ExtraBold))
                        renderInlineStyles(line.removePrefix("# ").trim(), mathBlocks, mathInlines, mathColor, codeBgColor, codeTextColor)
                        pop()
                        continue
                    }
                }

                // 处理无序列表 (- 或 *)
                if (line.matches(Regex("""^\s*[\*\-]\s+.*"""))) {
                    val content = line.replaceFirst(Regex("""^\s*[\*\-]\s+"""), "")
                    pushStyle(SpanStyle(color = quoteBarColor, fontWeight = FontWeight.Bold))
                    append(" •  ")
                    pop()
                    renderInlineStyles(content, mathBlocks, mathInlines, mathColor, codeBgColor, codeTextColor)
                    continue
                }

                // 处理普通行与行内元素
                renderInlineStyles(line, mathBlocks, mathInlines, mathColor, codeBgColor, codeTextColor)
            }
        }
    }

    /**
     * 解析单行内的样式标记：加粗、斜体、行内代码、数学公式占位符
     */
    private fun AnnotatedString.Builder.renderInlineStyles(
        text: String,
        mathBlocks: List<String>,
        mathInlines: List<String>,
        mathColor: Color,
        codeBgColor: Color,
        codeTextColor: Color
    ) {
        // 使用正则扫描复合标记
        // 捕获：代码 `...`、粗斜体 ***...***、粗体 **...**、斜体 *...*、删除线 ~~...~~、公式占位符 %%%MATH_...%%%
        val tokenRegex = Regex(
            """(%%%MATH_BLOCK_\d+%%%|%%%MATH_INLINE_\d+%%%|`[^`]+`|\*\*\*[^\*]+\*\*\*|\*\*[^\*]+\*\*|\*[^\*]+\*|~~[^~]+~~|\[[^\]]+\]\([^\)]+\))"""
        )

        var lastIdx = 0
        val matches = tokenRegex.findAll(text)

        for (match in matches) {
            val start = match.range.first
            val end = match.range.last + 1

            if (start > lastIdx) {
                append(text.substring(lastIdx, start))
            }

            val token = match.value

            when {
                // 块级公式占位符
                token.startsWith("%%%MATH_BLOCK_") -> {
                    val idx = token.removePrefix("%%%MATH_BLOCK_").removeSuffix("%%%").toIntOrNull() ?: 0
                    val formula = mathBlocks.getOrElse(idx) { "" }
                    pushStyle(SpanStyle(fontWeight = FontWeight.Bold, color = mathColor, fontStyle = FontStyle.Italic))
                    append("\n  $formula  \n")
                    pop()
                }

                // 行内公式占位符
                token.startsWith("%%%MATH_INLINE_") -> {
                    val idx = token.removePrefix("%%%MATH_INLINE_").removeSuffix("%%%").toIntOrNull() ?: 0
                    val formula = mathInlines.getOrElse(idx) { "" }
                    pushStyle(SpanStyle(fontWeight = FontWeight.SemiBold, color = mathColor, fontStyle = FontStyle.Normal))
                    append(" $formula ")
                    pop()
                }

                // 行内代码 `...`
                token.startsWith("`") && token.endsWith("`") -> {
                    val code = token.substring(1, token.length - 1)
                    pushStyle(SpanStyle(fontFamily = FontFamily.Monospace, background = codeBgColor, color = codeTextColor, fontSize = 13.sp))
                    append(" $code ")
                    pop()
                }

                // 粗斜体 ***...***
                token.startsWith("***") && token.endsWith("***") -> {
                    val content = token.substring(3, token.length - 3)
                    pushStyle(SpanStyle(fontWeight = FontWeight.Bold, fontStyle = FontStyle.Italic))
                    append(content)
                    pop()
                }

                // 加粗 **...**
                token.startsWith("**") && token.endsWith("**") -> {
                    val content = token.substring(2, token.length - 2)
                    pushStyle(SpanStyle(fontWeight = FontWeight.Bold))
                    append(content)
                    pop()
                }

                // 斜体 *...*
                token.startsWith("*") && token.endsWith("*") -> {
                    val content = token.substring(1, token.length - 1)
                    pushStyle(SpanStyle(fontStyle = FontStyle.Italic))
                    append(content)
                    pop()
                }

                // 删除线 ~~...~~
                token.startsWith("~~") && token.endsWith("~~") -> {
                    val content = token.substring(2, token.length - 2)
                    pushStyle(SpanStyle(textDecoration = TextDecoration.LineThrough))
                    append(content)
                    pop()
                }

                // 链接 [text](url) -> 提取 text 并加下划线蓝色
                token.startsWith("[") && token.contains("](") && token.endsWith(")") -> {
                    val title = token.substringAfter("[").substringBefore("]")
                    pushStyle(SpanStyle(color = mathColor, textDecoration = TextDecoration.Underline))
                    append(title)
                    pop()
                }

                else -> append(token)
            }

            lastIdx = end
        }

        if (lastIdx < text.length) {
            append(text.substring(lastIdx))
        }
    }
}

/**
 * 全局 Markdown 与 LaTeX 数学公式渲染 Composable。
 * 可直接替换 Material3 Text，自动支持 `*加粗*`、`$T_3$`、`\text{Ca}^{2+}` 等富文本与公式显示。
 */
@Composable
fun MarkdownText(
    text: String,
    modifier: Modifier = Modifier,
    color: Color = Color.Unspecified,
    fontSize: TextUnit = TextUnit.Unspecified,
    fontStyle: FontStyle? = null,
    fontWeight: FontWeight? = null,
    fontFamily: FontFamily? = null,
    letterSpacing: TextUnit = TextUnit.Unspecified,
    textDecoration: TextDecoration? = null,
    textAlign: TextAlign? = null,
    lineHeight: TextUnit = TextUnit.Unspecified,
    overflow: TextOverflow = TextOverflow.Clip,
    softWrap: Boolean = true,
    maxLines: Int = Int.MAX_VALUE,
    minLines: Int = 1,
    inlineMathHighlight: Boolean = false,
    style: TextStyle = LocalTextStyle.current
) {
    val isDark = isSystemInDarkTheme()
    val annotatedString = remember(text, isDark, inlineMathHighlight) {
        MarkdownEngine.buildAnnotatedString(text, isDark, inlineMathHighlight)
    }

    Text(
        text = annotatedString,
        modifier = modifier,
        color = color,
        fontSize = fontSize,
        fontStyle = fontStyle,
        fontWeight = fontWeight,
        fontFamily = fontFamily,
        letterSpacing = letterSpacing,
        textDecoration = textDecoration,
        textAlign = textAlign,
        lineHeight = lineHeight,
        overflow = overflow,
        softWrap = softWrap,
        maxLines = maxLines,
        minLines = minLines,
        style = style
    )
}
