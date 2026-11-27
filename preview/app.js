/**
 * 记忆辅助 App - Windows 桌面极速预览框架 核心逻辑
 * 核心特色：全屏拖入任意 JSON/ZIP -> 自动智能嗅探类型 -> 零操作秒级直接打开！
 */

// 轻量且强大的 Markdown + LaTeX 数学公式解析引擎
const MATH_SYMBOLS = {
  "\\AA": "Å", "\\circ": "°", "\\ge": "≥", "\\geq": "≥", "\\le": "≤", "\\leq": "≤",
  "\\approx": "≈", "\\sim": "~", "\\pm": "±", "\\mp": "∓", "\\times": "×", "\\div": "÷",
  "\\cdot": "·", "\\neq": "≠", "\\equiv": "≡", "\\infty": "∞", "\\rightarrow": "→", "\\to": "→",
  "\\leftarrow": "←", "\\Rightarrow": "⇒", "\\Leftarrow": "⇐", "\\leftrightarrow": "↔",
  "\\alpha": "α", "\\beta": "β", "\\gamma": "γ", "\\delta": "δ", "\\epsilon": "ε",
  "\\varepsilon": "ε", "\\zeta": "ζ", "\\eta": "η", "\\theta": "θ", "\\iota": "ι",
  "\\kappa": "κ", "\\lambda": "λ", "\\mu": "μ", "\\nu": "ν", "\\xi": "ξ", "\\pi": "π",
  "\\rho": "ρ", "\\sigma": "σ", "\\tau": "τ", "\\upsilon": "υ", "\\phi": "φ", "\\varphi": "φ",
  "\\chi": "χ", "\\psi": "ψ", "\\omega": "ω", "\\Gamma": "Γ", "\\Delta": "Δ", "\\Theta": "Θ",
  "\\Lambda": "Λ", "\\Xi": "Ξ", "\\Pi": "Π", "\\Sigma": "Σ", "\\Phi": "Φ", "\\Psi": "Ψ", "\\Omega": "Ω"
};

const SUP_MAP = { '0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹','+':'⁺','-':'⁻','=':'⁼','(':'⁽',')':'⁾','n':'ⁿ','i':'ⁱ' };
const SUB_MAP = { '0':'₀','1':'₁','2':'₂','3':'₃','4':'₄','5':'₅','6':'₆','7':'₇','8':'₈','9':'₉','+':'₊','-':'₋','=':'₌','(':'₍',')':'₎','a':'ₐ','e':'ₑ','o':'ₒ','x':'ₓ','h':'ₕ','k':'ₖ','l':'ₗ','m':'ₘ','n':'ₙ','p':'ₚ','s':'ₛ','t':'ₜ','i':'ᵢ','j':'ⱼ','L':'ₗ','H':'ₕ' };

function parseMathFormulaFallback(latex) {
  let s = String(latex || "").trim();
  for (const [k, v] of Object.entries(MATH_SYMBOLS)) {
    s = s.replace(new RegExp(k.replace(/\\/g, "\\\\") + "(?![a-zA-Z])", "g"), v);
  }
  s = s.replace(/\\frac\{([^{}]+)\}\{([^{}]+)\}/g, "$1/$2");
  s = s.replace(/\\(?:text|mathrm|textbf|mathit)\{([^{}]+)\}/g, "$1");
  s = s.replace(/\^\{([^{}]+)\}/g, (_, m) => m.split('').map(c => SUP_MAP[c] || c).join(''));
  s = s.replace(/\^([0-9\+\-°])/g, (_, m) => SUP_MAP[m] || m);
  s = s.replace(/_\{([^{}]+)\}/g, (_, m) => m.split('').map(c => SUB_MAP[c] || c).join(''));
  s = s.replace(/_([0-9a-zA-Z\+\-])/g, (_, m) => SUB_MAP[m] || m);
  s = s.replace(/\\(?:quad|qquad|;|,|\s)/g, " ");
  s = s.replace(/\\/g, "");
  return s.trim();
}

function renderMarkdown(md) {
  if (!md) return "";
  let text = String(md).trim();

  // 1. 抽取并隔离数学公式（避免公式中的 _ 下标和 * 乘号被 Markdown 误识别）
  const mathBlocks = [];
  const mathInlines = [];

  // 1.1 块级数学公式 $$...$$
  text = text.replace(/\$\$([\s\S]+?)\$\$/g, (match, formula) => {
    mathBlocks.push(formula.trim());
    return `%%%MATH_BLOCK_${mathBlocks.length - 1}%%%`;
  });

  // 1.2 行内数学公式 $...$
  text = text.replace(/\$([^\$\n]+?)\$/g, (match, formula) => {
    mathInlines.push(formula.trim());
    return `%%%MATH_INLINE_${mathInlines.length - 1}%%%`;
  });

  // 2. 转义 HTML 基础特殊字符
  text = text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  // 3. 多行代码块 ```lang\ncode\n```
  text = text.replace(/```([a-zA-Z0-9_-]*)\n?([\s\S]*?)```/g, (match, lang, code) => {
    return `<pre class="md-pre"><code class="md-code-block">${code.trim()}</code></pre>`;
  });

  // 4. 行内代码 `code`
  text = text.replace(/`([^`]+)`/g, '<code class="md-inline-code">$1</code>');

  // 5. 标题 # H1, ## H2, ### H3
  text = text.replace(/^### (.*$)/gim, '<div class="md-h3">$1</div>');
  text = text.replace(/^## (.*$)/gim, '<div class="md-h2">$1</div>');
  text = text.replace(/^# (.*$)/gim, '<div class="md-h1">$1</div>');

  // 6. 引用块 > quote
  text = text.replace(/^\> (.*$)/gim, '<blockquote class="md-quote">$1</blockquote>');

  // 7. 加粗与斜体与删除线
  text = text.replace(/\*\*(.*?)\*\*/g, '<strong class="md-strong">$1</strong>');
  text = text.replace(/__(.*?)__/g, '<strong class="md-strong">$1</strong>');
  text = text.replace(/\*(.*?)\*/g, '<em class="md-em">$1</em>');
  text = text.replace(/~~(.*?)~~/g, '<del class="md-del">$1</del>');

  // 8. 链接 [text](url)
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a class="md-link" href="$2" target="_blank">$1</a>');

  // 9. 列表解析 (无序列表与有序列表)
  text = text.replace(/^[\*\-] (.*$)/gim, '<li class="md-li">$1</li>');
  text = text.replace(/(<li class="md-li">[\s\S]*?<\/li>)/gim, '<ul class="md-ul">$1</ul>');
  text = text.replace(/<\/ul>\s*<ul class="md-ul">/gim, '');

  text = text.replace(/^\d+\. (.*$)/gim, '<li class="md-oli">$1</li>');
  text = text.replace(/(<li class="md-oli">[\s\S]*?<\/li>)/gim, '<ol class="md-ol">$1</ol>');
  text = text.replace(/<\/ol>\s*<ol class="md-ol">/gim, '');

  // 10. 段落与普通换行
  text = text.replace(/\n\n+/g, '<div class="md-p-gap"></div>');
  text = text.replace(/\n/g, '<br>');

  // 11. 将占位符渲染替换为 KaTeX 数学公式
  // 11.1 块级公式
  text = text.replace(/%%%MATH_BLOCK_(\d+)%%%/g, (match, idx) => {
    const raw = mathBlocks[parseInt(idx, 10)];
    if (!raw) return "";
    if (typeof window.katex !== "undefined") {
      try {
        return `<div class="katex-display-container">${window.katex.renderToString(raw, { displayMode: true, throwOnError: false })}</div>`;
      } catch (_) {}
    }
    return `<div class="katex-fallback-block">${parseMathFormulaFallback(raw)}</div>`;
  });

  // 11.2 行内公式
  text = text.replace(/%%%MATH_INLINE_(\d+)%%%/g, (match, idx) => {
    const raw = mathInlines[parseInt(idx, 10)];
    if (!raw) return "";
    if (typeof window.katex !== "undefined") {
      try {
        return window.katex.renderToString(raw, { displayMode: false, throwOnError: false });
      } catch (_) {}
    }
    return `<span class="katex-fallback-inline">${parseMathFormulaFallback(raw)}</span>`;
  });

  return text;
}

// 全局应用状态
const state = {
  theme: localStorage.getItem("flashcard_theme") || "dark",
  isFrameless: localStorage.getItem("flashcard_frameless") === "true",
  subjectViewMode: localStorage.getItem("flashcard_subject_view") || "grid",
  
  subjects: [],
  customSubjects: JSON.parse(localStorage.getItem("flashcard_custom_subjects") || "[]"),
  currentSubject: null,
  units: [],
  currentUnit: null,

  // 闪卡复习状态
  deckData: null,
  cardIndex: 0,
  isFlipped: false,
  masteredCount: 0,
  reviewCount: 0,

  // 单元小测状态
  quizData: null,
  quizIndex: 0,
  quizScore: 0,
  quizTimerId: null,
  quizSeconds: 0,
  quizAnswered: false,

  // 思维导图缩放平移状态
  mindmapData: null,
  mindmapScale: 1.0,
  mindmapPanX: 40,
  mindmapPanY: 40,
  isDraggingMindmap: false,
  dragStartX: 0,
  dragStartY: 0
};

// 页面 DOM 缓存
const dom = {
  themeHtml: document.documentElement,
  btnToggleTheme: document.getElementById("btn-toggle-theme"),
  themeIcon: document.getElementById("theme-icon"),
  themeText: document.getElementById("theme-text"),
  btnToggleFrame: document.getElementById("btn-toggle-frame"),
  phoneFrame: document.getElementById("phone-frame"),
  btnReloadData: document.getElementById("btn-reload-data"),
  btnTopImport: document.getElementById("btn-top-import"),
  currentPageBadge: document.getElementById("current-page-badge"),
  statusClock: document.getElementById("status-clock"),

  // 拖拽与上传元素
  globalDragOverlay: document.getElementById("global-drag-overlay"),
  dropZoneCard: document.getElementById("drop-zone-card"),
  miniDropZone: document.getElementById("mini-drop-zone"),
  btnBrowseFile: document.getElementById("btn-browse-file"),
  filePicker: document.getElementById("file-picker"),
  appToast: document.getElementById("app-toast"),

  // 弹窗
  addSubjectModal: document.getElementById("add-subject-modal"),
  inputSubjectName: document.getElementById("input-subject-name"),
  inputSubjectEmoji: document.getElementById("input-subject-emoji"),
  inputSubjectDesc: document.getElementById("input-subject-desc"),
  btnCancelAddSubject: document.getElementById("btn-cancel-add-subject"),
  btnConfirmAddSubject: document.getElementById("btn-confirm-add-subject"),

  importTargetModal: document.getElementById("import-target-modal"),
  importTargetFileInfo: document.getElementById("import-target-file-info"),
  importTargetSubjectsList: document.getElementById("import-target-subjects-list"),
  btnImportPreviewOnly: document.getElementById("btn-import-preview-only"),
  btnCancelImportTarget: document.getElementById("btn-cancel-import-target"),

  // 页面容器
  screens: {
    subjectSelect: document.getElementById("screen-subject-select"),
    home: document.getElementById("screen-home"),
    study: document.getElementById("screen-study"),
    quiz: document.getElementById("screen-quiz"),
    mindmap: document.getElementById("screen-mindmap")
  },

  // 学科大厅
  subjectsContainer: document.getElementById("subjects-container"),
  btnSwitchSubjectView: document.getElementById("btn-switch-subject-view"),
  btnAddSubject: document.getElementById("btn-add-subject"),

  // 学科主页
  btnBackToSubjects: document.getElementById("btn-back-to-subjects"),
  homeSubjectTitle: document.getElementById("home-subject-title"),
  homeSubjectDesc: document.getElementById("home-subject-desc"),
  homeSubjectEmoji: document.getElementById("home-subject-emoji"),
  unitsContainer: document.getElementById("units-container"),

  // 闪卡
  btnBackFromStudy: document.getElementById("btn-back-from-study"),
  studyUnitTitle: document.getElementById("study-unit-title"),
  studyProgressText: document.getElementById("study-progress-text"),
  badgeMastered: document.getElementById("badge-mastered"),
  badgeReview: document.getElementById("badge-review"),
  flashcard3d: document.getElementById("flashcard-3d"),
  cardFrontContent: document.getElementById("card-front-content"),
  cardBackContent: document.getElementById("card-back-content"),
  overlayMastered: document.getElementById("overlay-mastered"),
  overlayReview: document.getElementById("overlay-review"),
  btnCardMissed: document.getElementById("btn-card-missed"),
  btnCardFlip: document.getElementById("btn-card-flip"),
  btnCardGotit: document.getElementById("btn-card-gotit"),

  // 小测
  btnBackFromQuiz: document.getElementById("btn-back-from-quiz"),
  quizUnitTitle: document.getElementById("quiz-unit-title"),
  quizProgressText: document.getElementById("quiz-progress-text"),
  quizTimer: document.getElementById("quiz-timer"),
  quizTypeBadge: document.getElementById("quiz-type-badge"),
  quizScoreBadge: document.getElementById("quiz-score-badge"),
  quizQuestionText: document.getElementById("quiz-question-text"),
  quizOptionsContainer: document.getElementById("quiz-options-container"),
  quizRationaleBox: document.getElementById("quiz-rationale-box"),
  quizRationaleText: document.getElementById("quiz-rationale-text"),
  btnQuizNext: document.getElementById("btn-quiz-next"),

  // 导图
  btnBackFromMindmap: document.getElementById("btn-back-from-mindmap"),
  mindmapUnitTitle: document.getElementById("mindmap-unit-title"),
  mindmapViewport: document.getElementById("mindmap-viewport"),
  mindmapCanvas: document.getElementById("mindmap-canvas"),
  mindmapTreeRoot: document.getElementById("mindmap-tree-root"),
  btnMindmapZoomIn: document.getElementById("btn-mindmap-zoom-in"),
  btnMindmapZoomOut: document.getElementById("btn-mindmap-zoom-out"),
  btnMindmapReset: document.getElementById("btn-mindmap-reset")
};

// ==========================================
// 1. 初始化与顶栏控制
// ==========================================
function initApp() {
  updateStatusClock();
  setInterval(updateStatusClock, 1000);

  applyTheme(state.theme);
  applyFrameless(state.isFrameless);

  dom.btnToggleTheme.addEventListener("click", () => {
    applyTheme(state.theme === "dark" ? "light" : "dark");
  });

  dom.btnToggleFrame.addEventListener("click", () => {
    applyFrameless(!state.isFrameless);
  });

  dom.btnReloadData.addEventListener("click", () => {
    loadSubjects();
    showToast("🔄 已重新同步本地 Assets 数据源");
  });

  dom.btnSwitchSubjectView.addEventListener("click", () => {
    state.subjectViewMode = state.subjectViewMode === "grid" ? "list" : "grid";
    localStorage.setItem("flashcard_subject_view", state.subjectViewMode);
    renderSubjects();
  });

  dom.btnBackToSubjects.addEventListener("click", () => {
    state.currentSubject = null;
    showScreen("subjectSelect");
  });
  dom.btnBackFromStudy.addEventListener("click", () => showScreen(state.currentSubject ? "home" : "subjectSelect"));
  dom.btnBackFromQuiz.addEventListener("click", () => {
    clearInterval(state.quizTimerId);
    showScreen(state.currentSubject ? "home" : "subjectSelect");
  });
  dom.btnBackFromMindmap.addEventListener("click", () => showScreen(state.currentSubject ? "home" : "subjectSelect"));

  // 闪卡交互绑定
  initFlashcardGestures();

  // 导图交互绑定
  initMindmapPanZoom();

  // 键盘快捷键监听
  window.addEventListener("keydown", handleGlobalKeydown);

  // 拖入导入功能初始化 (全屏支持拖入)
  initDragAndDrop();

  // 新建学科弹窗功能初始化
  initAddSubjectModal();

  // 初始加载学科列表
  loadSubjects();
}

function updateStatusClock() {
  const d = new Date();
  const h = String(d.getHours()).padStart(2, "0");
  const m = String(d.getMinutes()).padStart(2, "0");
  dom.statusClock.textContent = `${h}:${m}`;
}

function applyTheme(theme) {
  state.theme = theme;
  localStorage.setItem("flashcard_theme", theme);
  dom.themeHtml.setAttribute("data-theme", theme);
  dom.themeIcon.textContent = theme === "dark" ? "🌙" : "☀️";
  dom.themeText.textContent = theme === "dark" ? "深色" : "浅色";
}

function applyFrameless(isFrameless) {
  state.isFrameless = isFrameless;
  localStorage.setItem("flashcard_frameless", isFrameless);
  if (isFrameless) {
    dom.phoneFrame.classList.add("frameless");
    dom.btnToggleFrame.classList.add("active");
  } else {
    dom.phoneFrame.classList.remove("frameless");
    dom.btnToggleFrame.classList.remove("active");
  }
}

function showScreen(name) {
  Object.keys(dom.screens).forEach(key => {
    if (dom.screens[key]) {
      dom.screens[key].classList.toggle("active", key === name);
    }
  });

  const titles = {
    subjectSelect: "学科大厅",
    home: state.currentSubject ? state.currentSubject.name : "学科主页",
    study: "闪卡复习",
    quiz: "单元小测",
    mindmap: "思维导图"
  };
  dom.currentPageBadge.textContent = titles[name] || "预览模式";
}

function showToast(msg) {
  dom.appToast.textContent = msg;
  dom.appToast.classList.add("show");
  clearTimeout(dom.appToast._timer);
  dom.appToast._timer = setTimeout(() => {
    dom.appToast.classList.remove("show");
  }, 3200);
}

// ==========================================
// 2. 核心：拖入 JSON / ZIP 自动解析类型并直接打开！
// ==========================================
function initDragAndDrop() {
  // 点击按钮触发本地文件选择
  const triggerPicker = () => dom.filePicker.click();
  dom.btnTopImport.addEventListener("click", triggerPicker);
  dom.btnBrowseFile?.addEventListener("click", triggerPicker);
  dom.dropZoneCard?.addEventListener("click", (e) => {
    if (e.target !== dom.btnBrowseFile) triggerPicker();
  });
  dom.miniDropZone?.addEventListener("click", triggerPicker);

  // 文件选择器监听
  dom.filePicker.addEventListener("change", (e) => {
    const file = e.target.files?.[0];
    if (file) handleIncomingFile(file);
    dom.filePicker.value = "";
  });

  // 全屏拖入悬浮监听
  let dragCounter = 0;

  window.addEventListener("dragenter", (e) => {
    e.preventDefault();
    dragCounter++;
    dom.globalDragOverlay.classList.add("active");
  });

  window.addEventListener("dragover", (e) => {
    e.preventDefault();
  });

  window.addEventListener("dragleave", (e) => {
    e.preventDefault();
    dragCounter--;
    if (dragCounter <= 0) {
      dragCounter = 0;
      dom.globalDragOverlay.classList.remove("active");
    }
  });

  window.addEventListener("drop", (e) => {
    e.preventDefault();
    dragCounter = 0;
    dom.globalDragOverlay.classList.remove("active");

    const file = e.dataTransfer?.files?.[0];
    if (file) {
      handleIncomingFile(file);
    }
  });
}

// 统一文件处理分发器
function handleIncomingFile(file) {
  const fileName = file.name;
  const isZip = fileName.endsWith(".zip");

  if (isZip) {
    showToast(`📦 收到 ZIP 打包文件: ${fileName}，正在扫描解包...`);
    // 读取 ZIP 包
    handleIncomingZip(file);
    return;
  }

  // 处理 JSON
  const reader = new FileReader();
  reader.onload = (e) => {
    try {
      const rawText = e.target.result;
      const data = JSON.parse(rawText);
      inspectAndOpenJson(data, fileName);
    } catch (err) {
      showToast(`❌ JSON 解析失败: ${err.message}`);
    }
  };
  reader.readAsText(file, "utf-8");
}

// 从文件名与内容中提取干净的章节名称与唯一 ID
function extractUnitInfo(fileName, category, data) {
  let title = (fileName || "").replace(/\.json$/i, "").trim();
  // 去除尾部和头部的分类标志词（闪卡、考题、导图、quiz 等）
  title = title.replace(/(闪卡|考题|小测|测验|导图|思维导图|脑图|decks?|quiz(zes)?|mindmaps?)/gi, "").trim();
  title = title.replace(/[-_]+$/, "").trim();
  if (!title && data?.name) title = data.name;
  if (!title) title = "自定义章节";

  // 生成安全 ID (保留中文与英文数字下划线)
  const clean = title.replace(/[\s\/\\]+/g, "_").replace(/[^a-zA-Z0-9_\u4e00-\u9fa5]/g, "");
  const unitId = clean || ("u_" + Date.now());
  return { unitTitle: title, unitId };
}

// 将导入的单元数据持久化发送到后端保存到磁盘与 assets
async function persistUnitToServer(subject, category, unitTitle, unitId, data) {
  try {
    const res = await fetch("/api/save-unit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        subjectId: subject.id,
        category,
        unitTitle,
        unitId,
        data
      })
    });
    const result = await res.json();
    if (result.success) {
      if (state.currentSubject && state.currentSubject.id === subject.id) {
        await loadUnits(subject.id);
      }
      return true;
    }
  } catch (err) {
    console.error("保存单元至磁盘失败:", err);
  }
  return false;
}

// 弹窗询问：拖入的数据存入哪门学科（在大厅未进入学科时触发）
function promptSelectSubjectForUnit(info) {
  const { unitTitle, unitId, category, typeLabel, fileName, data, previewAction } = info;
  dom.importTargetFileInfo.textContent = `📄 文件: ${fileName} → ${typeLabel}`;
  dom.importTargetSubjectsList.innerHTML = "";

  state.subjects.forEach(sub => {
    const btn = document.createElement("button");
    btn.className = "import-sub-btn";
    btn.innerHTML = `
      <span style="font-size: 20px;">${sub.emoji}</span>
      <div style="flex:1;">
        <div style="font-size: 14px; font-weight: 700;">${sub.name}</div>
        <div style="font-size: 11px; color: var(--text-tertiary);">${sub.isBuiltIn ? "内置核心学科" : "自定义学科"}</div>
      </div>
      <span style="font-size: 12px; color: var(--primary);">存入并打开 →</span>
    `;
    btn.addEventListener("click", async () => {
      dom.importTargetModal.style.display = "none";
      await persistUnitToServer(sub, category, unitTitle, unitId, data);
      showToast(`💾 已长期持久化保存【${unitTitle}】到【${sub.name}】！`);
      // 切换到该学科并进入预览
      selectSubject(sub);
      previewAction(unitTitle);
    });
    dom.importTargetSubjectsList.appendChild(btn);
  });

  // 临时预览按钮
  dom.btnImportPreviewOnly.onclick = () => {
    dom.importTargetModal.style.display = "none";
    previewAction(unitTitle);
    showToast(`👁️ 临时预览【${unitTitle}】`);
  };

  // 取消按钮
  dom.btnCancelImportTarget.onclick = () => {
    dom.importTargetModal.style.display = "none";
  };

  dom.importTargetModal.style.display = "flex";
}

// 智能嗅探 JSON 类型并直接秒开 + 长期保存
async function inspectAndOpenJson(data, fileName = "导入组件") {
  let category = null;
  let typeLabel = "";
  let previewAction = null;

  // 1. 判断是否为闪卡 (Flashcards)
  if (data.flashcards && Array.isArray(data.flashcards)) {
    category = "decks";
    typeLabel = `闪卡复习 (${data.flashcards.length} 张卡片)`;
    previewAction = (title) => {
      state.deckData = data.flashcards;
      state.cardIndex = 0;
      state.masteredCount = 0;
      state.reviewCount = 0;
      dom.studyUnitTitle.textContent = title;
      showScreen("study");
      renderFlashcard();
    };
  }
  // 2. 判断是否为单元小测 (Quiz)
  else if (data.quiz && Array.isArray(data.quiz)) {
    category = "quizzes";
    typeLabel = `单元小测 (${data.quiz.length} 道考题)`;
    previewAction = (title) => {
      state.quizData = data.quiz;
      state.quizIndex = 0;
      state.quizScore = 0;
      state.quizSeconds = 0;
      dom.quizUnitTitle.textContent = title;
      showScreen("quiz");
      renderQuizQuestion();

      clearInterval(state.quizTimerId);
      state.quizTimerId = setInterval(() => {
        state.quizSeconds++;
        const m = String(Math.floor(state.quizSeconds / 60)).padStart(2, "0");
        const s = String(state.quizSeconds % 60).padStart(2, "0");
        dom.quizTimer.textContent = `${m}:${s}`;
      }, 1000);
    };
  }
  // 3. 判断是否为知识思维导图 (Mindmap)
  else if (data.name && (data.children || Array.isArray(data.children))) {
    category = "mindmaps";
    typeLabel = `知识思维导图 (${data.name})`;
    previewAction = (title) => {
      state.mindmapData = data;
      dom.mindmapUnitTitle.textContent = data.name || title;
      showScreen("mindmap");
      renderMindmapTree();
      resetMindmapView();
    };
  }
  // 4. 容错处理：若是顶层数组
  else if (Array.isArray(data)) {
    if (data[0]?.f && data[0]?.b) {
      category = "decks";
      typeLabel = `闪卡列表 (${data.length} 张)`;
      previewAction = (title) => {
        state.deckData = data;
        state.cardIndex = 0;
        dom.studyUnitTitle.textContent = title;
        showScreen("study");
        renderFlashcard();
      };
    } else if (data[0]?.answerOptions || data[0]?.question) {
      category = "quizzes";
      typeLabel = `小测考题 (${data.length} 题)`;
      previewAction = (title) => {
        state.quizData = data;
        state.quizIndex = 0;
        dom.quizUnitTitle.textContent = title;
        showScreen("quiz");
        renderQuizQuestion();
      };
    }
  }

  if (!category || !previewAction) {
    showToast("⚠️ 未知数据格式：未检测到 flashcards / quiz / mindmap 结构");
    return;
  }

  const { unitTitle, unitId } = extractUnitInfo(fileName, category, data);

  // 场景 A：当前已在某个学科主页中，直接自动落盘保存到该学科！
  if (state.currentSubject) {
    await persistUnitToServer(state.currentSubject, category, unitTitle, unitId, data);
    previewAction(unitTitle);
    showToast(`💾 已自动持久化保存【${unitTitle}】到【${state.currentSubject.name}】！`);
    return;
  }

  // 场景 B：在大厅拖入，弹窗供用户选择保存到哪个学科（或临时预览）
  promptSelectSubjectForUnit({
    unitTitle,
    unitId,
    category,
    typeLabel,
    fileName,
    data,
    previewAction
  });
}

// 简易 ZIP 解压解析支持
async function handleIncomingZip(file) {
  showToast(`📦 已收到压缩包【${file.name}】，若需要查看包含的多个章节，也可直接解压后将具体 JSON 拖入！`);
}

// ==========================================
// 3. 学科大厅与新建学科功能
// ==========================================
async function loadSubjects() {
  try {
    const res = await fetch("/api/subjects");
    state.subjects = await res.json();
    renderSubjects();
  } catch (err) {
    console.error("加载学科失败:", err);
  }
}

function renderSubjects() {
  dom.subjectsContainer.className = `subject-grid ${state.subjectViewMode === "list" ? "list-mode" : ""}`;
  dom.subjectsContainer.innerHTML = "";

  state.subjects.forEach(sub => {
    const card = document.createElement("div");
    card.className = "subject-card";
    card.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <span class="subject-card-icon">${sub.emoji}</span>
        <div style="display:flex; align-items:center; gap:6px;">
          ${sub.isBuiltIn ? '<span class="subject-badge">内置核心</span>' : '<span class="subject-badge" style="color:#fbbc04;background:rgba(251,188,4,0.15)">自定义</span>'}
          ${!sub.isBuiltIn ? `<button class="btn-delete-unit" data-sub-id="${sub.id}" title="删除学科" style="padding:0 4px;">🗑️</button>` : ''}
        </div>
      </div>
      <div>
        <div class="subject-card-title">${sub.name}</div>
        <div class="subject-card-desc">${renderMarkdown(sub.description || "包含系统考点精析与测试")}</div>
      </div>
    `;
    card.addEventListener("click", (e) => {
      if (e.target.closest(".btn-delete-unit")) return;
      selectSubject(sub);
    });

    const delSubBtn = card.querySelector(".btn-delete-unit");
    if (delSubBtn) {
      delSubBtn.addEventListener("click", async (e) => {
        e.stopPropagation();
        if (confirm(`确定删除自定义学科【${sub.name}】吗？`)) {
          try {
            await fetch("/api/delete-subject", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ subjectId: sub.id })
            });
            showToast(`🗑️ 已删除学科【${sub.name}】`);
            await loadSubjects();
          } catch (err) {
            alert("删除失败: " + err.message);
          }
        }
      });
    }

    dom.subjectsContainer.appendChild(card);
  });
}

function initAddSubjectModal() {
  dom.btnAddSubject.addEventListener("click", () => {
    dom.inputSubjectName.value = "";
    dom.inputSubjectEmoji.value = "📚";
    dom.inputSubjectDesc.value = "";
    dom.addSubjectModal.style.display = "flex";
    dom.inputSubjectName.focus();
  });

  dom.btnCancelAddSubject.addEventListener("click", () => {
    dom.addSubjectModal.style.display = "none";
  });

  dom.btnConfirmAddSubject.addEventListener("click", async () => {
    const name = dom.inputSubjectName.value.trim();
    const emoji = dom.inputSubjectEmoji.value.trim() || "📚";
    const desc = dom.inputSubjectDesc.value.trim() || "包含章节闪卡、小测与知识导图";

    if (!name) {
      alert("请输入学科名称！");
      return;
    }

    const newSub = {
      id: "sub_" + Date.now(),
      name,
      emoji,
      description: desc,
      isBuiltIn: false,
      colorHex: "#4285F4"
    };

    try {
      const res = await fetch("/api/subjects", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newSub)
      });
      const data = await res.json();
      if (data.success) {
        dom.addSubjectModal.style.display = "none";
        await loadSubjects();
        showToast(`🎉 学科【${name}】已成功持久化保存！已为您自动打开。`);
        const found = state.subjects.find(s => s.id === newSub.id) || newSub;
        selectSubject(found);
      } else {
        alert("创建失败: " + (data.error || "未知原因"));
      }
    } catch (err) {
      console.error("创建学科异常:", err);
      alert("创建失败: " + err.message);
    }
  });
}

async function selectSubject(sub) {
  state.currentSubject = sub;
  dom.homeSubjectTitle.textContent = sub.name;
  dom.homeSubjectDesc.textContent = sub.description;
  dom.homeSubjectEmoji.textContent = sub.emoji;

  showScreen("home");
  loadUnits(sub.id);
}

// ==========================================
// 4. 学科主页章节列表逻辑
// ==========================================
async function loadUnits(subjectId) {
  dom.unitsContainer.innerHTML = `<div style="text-align:center; padding: 40px; color:var(--text-secondary);">加载章节中...</div>`;
  try {
    const res = await fetch(`/api/units?subjectId=${subjectId}`);
    state.units = await res.json();
    renderUnits();
  } catch (err) {
    console.error("加载章节失败:", err);
  }
}

function renderUnits() {
  dom.unitsContainer.innerHTML = "";
  if (!state.units || state.units.length === 0) {
    dom.unitsContainer.innerHTML = `
      <div style="text-align:center; padding: 40px 20px; color:var(--text-secondary);">
        <div style="font-size: 36px; margin-bottom: 10px;">📥</div>
        <div style="font-weight: 700; font-size: 15px; color:var(--text-primary);">本学科暂无预置章节</div>
        <div style="font-size: 12px; margin-top: 8px; color:var(--text-tertiary); line-height: 1.6;">
          直接将该学科的 <strong>闪卡 / 小测 / 导图 JSON</strong> 拖入此窗口<br>
          系统将自动长期保存并生成章节卡片！
        </div>
      </div>
    `;
    return;
  }

  state.units.forEach((unit, idx) => {
    const card = document.createElement("div");
    card.className = "unit-card";

    const progressKey = `progress_${state.currentSubject.id}_${unit.id}`;
    const savedProgress = JSON.parse(localStorage.getItem(progressKey) || "{}");
    const masteredRatio = savedProgress.ratio || 0;

    const isCustom = unit.isCustom || !state.currentSubject.isBuiltIn;

    card.innerHTML = `
      <div class="unit-header">
        <div class="unit-title-group" style="flex:1;">
          <div class="unit-title" style="display:flex; align-items:center; justify-content:space-between;">
            <span>${unit.title}</span>
            ${isCustom ? `<button class="btn-delete-unit" data-id="${unit.id}" title="删除该章节">🗑️</button>` : ''}
          </div>
          <div class="unit-subtitle">${unit.subtitle || ""}</div>
        </div>
        <span style="font-size: 11px; font-weight:700; color:var(--primary); margin-left:8px;">CH.${String(idx+1).padStart(2, '0')}</span>
      </div>
      <div class="unit-desc">${renderMarkdown(unit.description || "")}</div>

      <div class="progress-container">
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" style="width: ${masteredRatio}%;"></div>
        </div>
        <span class="progress-text">${masteredRatio}% 已掌握</span>
      </div>

      <div class="unit-actions-row">
        <button class="unit-action-btn mindmap-btn" data-unit="${unit.id}">
          <span>🧠</span> 导图
        </button>
        <button class="unit-action-btn flashcard-btn" data-unit="${unit.id}">
          <span>🃏</span> 闪卡
        </button>
        <button class="unit-action-btn quiz-btn" data-unit="${unit.id}">
          <span>📝</span> 小测
        </button>
      </div>
    `;

    const delBtn = card.querySelector(".btn-delete-unit");
    if (delBtn) {
      delBtn.addEventListener("click", async (e) => {
        e.stopPropagation();
        if (confirm(`确定删除章节【${unit.title}】吗？`)) {
          try {
            await fetch("/api/delete-unit", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                subjectId: state.currentSubject.id,
                unitId: unit.id
              })
            });
            showToast(`🗑️ 已删除章节【${unit.title}】`);
            await loadUnits(state.currentSubject.id);
          } catch (err) {
            alert("删除失败: " + err.message);
          }
        }
      });
    }

    card.querySelector(".mindmap-btn").addEventListener("click", (e) => {
      e.stopPropagation();
      openMindmap(unit);
    });
    card.querySelector(".flashcard-btn").addEventListener("click", (e) => {
      e.stopPropagation();
      openStudy(unit);
    });
    card.querySelector(".quiz-btn").addEventListener("click", (e) => {
      e.stopPropagation();
      openQuiz(unit);
    });

    dom.unitsContainer.appendChild(card);
  });
}

// ==========================================
// 5. 闪卡复习与 3D 翻转/手势评判逻辑
// ==========================================
async function openStudy(unit) {
  state.currentUnit = unit;
  dom.studyUnitTitle.textContent = `${unit.title} · 闪卡`;
  dom.cardFrontContent.textContent = "正在获取闪卡数据...";
  dom.cardBackContent.textContent = "";

  showScreen("study");

  try {
    const res = await fetch(`/api/data?subjectId=${state.currentSubject.id}&unitId=${unit.id}&category=decks`);
    const data = await res.json();
    state.deckData = data.flashcards || [];
    state.cardIndex = 0;
    state.isFlipped = false;
    state.masteredCount = 0;
    state.reviewCount = 0;

    renderFlashcard();
  } catch (err) {
    dom.cardFrontContent.textContent = "未能读取到闪卡 JSON 数据";
  }
}

function renderFlashcard() {
  state.isFlipped = false;
  dom.flashcard3d.classList.remove("flipped");
  dom.flashcard3d.style.transform = "";
  dom.overlayMastered.style.opacity = "0";
  dom.overlayReview.style.opacity = "0";

  const total = state.deckData ? state.deckData.length : 0;
  dom.studyProgressText.textContent = `卡片 ${state.cardIndex + 1} / ${total}`;
  dom.badgeMastered.textContent = `✅ ${state.masteredCount}`;
  dom.badgeReview.textContent = `❌ ${state.reviewCount}`;

  if (!state.deckData || state.deckData.length === 0) {
    dom.cardFrontContent.textContent = "当前章节暂无卡片数据";
    dom.cardBackContent.textContent = "";
    return;
  }

  const card = state.deckData[state.cardIndex];
  const frontBlock = card?.f?.flashcardContentBlock?.[0]?.content || "无内容";
  const backBlock = card?.b?.flashcardContentBlock?.[0]?.content || "无解析";

  const frontTagEl = dom.flashcard3d.querySelector(".flashcard-front .card-tag span");
  if (frontTagEl) {
    if (card?.pointType) {
      frontTagEl.textContent = `🏷️ ${card.pointType} · ${card.starRating || '★★★'}`;
    } else {
      frontTagEl.textContent = "ℹ️ 考点问题";
    }
  }
  const backTagEl = dom.flashcard3d.querySelector(".flashcard-back .card-tag span");
  if (backTagEl) {
    if (card?.pointType) {
      backTagEl.textContent = `💡 ${card.pointType} · ${card.starRating || '★★★'}`;
    } else {
      backTagEl.textContent = "💡 核心解析";
    }
  }

  const cleanFront = frontBlock.replace(/^【[^】]+】\s*/, "");
  dom.cardFrontContent.innerHTML = renderMarkdown(cleanFront);
  dom.cardBackContent.innerHTML = renderMarkdown(backBlock);
}

function flipCard() {
  state.isFlipped = !state.isFlipped;
  dom.flashcard3d.classList.toggle("flipped", state.isFlipped);
}

function judgeCard(isMastered) {
  if (isMastered) {
    state.masteredCount++;
  } else {
    state.reviewCount++;
  }

  const total = state.deckData.length;
  const ratio = Math.round((state.masteredCount / total) * 100);
  if (state.currentSubject && state.currentUnit) {
    const progressKey = `progress_${state.currentSubject.id}_${state.currentUnit.id}`;
    localStorage.setItem(progressKey, JSON.stringify({ ratio, mastered: state.masteredCount }));
  }

  if (state.cardIndex < total - 1) {
    state.cardIndex++;
    renderFlashcard();
  } else {
    alert(`🎉 恭喜！本章节复习完成！\n已掌握: ${state.masteredCount} 张\n待复习: ${state.reviewCount} 张`);
    showScreen(state.currentSubject ? "home" : "subjectSelect");
    if (state.currentSubject) renderUnits();
  }
}

function initFlashcardGestures() {
  dom.btnCardFlip.addEventListener("click", flipCard);
  dom.flashcard3d.addEventListener("click", () => {
    if (!isDraggingCard) flipCard();
  });

  dom.btnCardGotit.addEventListener("click", () => judgeCard(true));
  dom.btnCardMissed.addEventListener("click", () => judgeCard(false));

  let startX = 0, startY = 0;
  let currentX = 0, currentY = 0;
  let isDraggingCard = false;

  const cardEl = dom.flashcard3d;

  cardEl.addEventListener("mousedown", (e) => {
    startX = e.clientX;
    startY = e.clientY;
    isDraggingCard = true;
    cardEl.style.transition = "none";
  });

  window.addEventListener("mousemove", (e) => {
    if (!isDraggingCard) return;
    currentX = e.clientX - startX;
    currentY = e.clientY - startY;

    if (currentY > 15 && currentY > Math.abs(currentX) * 0.9) {
      const rot = (currentX / 20).toFixed(2);
      cardEl.style.transform = `translate(${currentX}px, ${currentY}px) rotate(${rot}deg) ${state.isFlipped ? 'rotateY(180deg)' : ''}`;

      if (currentX > 20) {
        dom.overlayMastered.style.opacity = Math.min(currentX / 120, 0.95);
        dom.overlayReview.style.opacity = "0";
      } else if (currentX < -20) {
        dom.overlayReview.style.opacity = Math.min(-currentX / 120, 0.95);
        dom.overlayMastered.style.opacity = "0";
      }
    } else {
      cardEl.style.transform = `translate(${currentX}px, 0px) ${state.isFlipped ? 'rotateY(180deg)' : ''}`;
    }
  });

  window.addEventListener("mouseup", () => {
    if (!isDraggingCard) return;
    isDraggingCard = false;
    cardEl.style.transition = "transform 0.45s cubic-bezier(0.175, 0.885, 0.32, 1.275)";

    const moveDist = Math.hypot(currentX, currentY);
    if (moveDist < 10) {
      // 点击卡片，直接翻转
      flipCard();
    } else if (currentY > 80) {
      if (currentX > 60) {
        judgeCard(true);
      } else if (currentX < -60) {
        judgeCard(false);
      } else {
        cardEl.style.transform = state.isFlipped ? "rotateY(180deg)" : "";
      }
    } else if (Math.abs(currentX) > 100) {
      if (currentX < 0 && state.cardIndex < state.deckData.length - 1) {
        state.cardIndex++;
        renderFlashcard();
      } else if (currentX > 0 && state.cardIndex > 0) {
        state.cardIndex--;
        renderFlashcard();
      } else {
        cardEl.style.transform = state.isFlipped ? "rotateY(180deg)" : "";
      }
    } else {
      cardEl.style.transform = state.isFlipped ? "rotateY(180deg)" : "";
    }

    dom.overlayMastered.style.opacity = "0";
    dom.overlayReview.style.opacity = "0";
    currentX = 0;
    currentY = 0;
  });
}

// ==========================================
// 6. 单元小测逻辑
// ==========================================
async function openQuiz(unit) {
  state.currentUnit = unit;
  dom.quizUnitTitle.textContent = `${unit.title} · 测验`;
  showScreen("quiz");

  state.quizIndex = 0;
  state.quizScore = 0;
  state.quizSeconds = 0;
  state.quizAnswered = false;

  clearInterval(state.quizTimerId);
  state.quizTimerId = setInterval(() => {
    state.quizSeconds++;
    const m = String(Math.floor(state.quizSeconds / 60)).padStart(2, "0");
    const s = String(state.quizSeconds % 60).padStart(2, "0");
    dom.quizTimer.textContent = `${m}:${s}`;
  }, 1000);

  try {
    const res = await fetch(`/api/data?subjectId=${state.currentSubject.id}&unitId=${unit.id}&category=quizzes`);
    const data = await res.json();
    state.quizData = data.quiz || [];
    renderQuizQuestion();
  } catch (err) {
    dom.quizQuestionText.textContent = "未能获取小测题目数据";
  }
}

function renderQuizQuestion() {
  state.quizAnswered = false;
  dom.quizRationaleBox.classList.remove("visible");
  dom.btnQuizNext.style.display = "none";

  const total = state.quizData ? state.quizData.length : 0;
  dom.quizProgressText.textContent = `第 ${state.quizIndex + 1} / ${total} 题`;

  if (!state.quizData || state.quizData.length === 0) {
    dom.quizQuestionText.textContent = "当前单元无考题";
    dom.quizOptionsContainer.innerHTML = "";
    return;
  }

  const q = state.quizData[state.quizIndex];
  dom.quizQuestionText.innerHTML = renderMarkdown(q.question);
  dom.quizOptionsContainer.innerHTML = "";

  if (q.type === "fill_in_blank" || q.type === "fill_blank") {
    dom.quizTypeBadge.textContent = "填空自测";
    const blanks = q.blankAnswers || [];
    const container = document.createElement("div");
    container.className = "quiz-blanks-box";
    container.style.display = "flex";
    container.style.flexDirection = "column";
    container.style.gap = "10px";
    container.style.marginTop = "8px";

    blanks.forEach((ans, bIdx) => {
      const row = document.createElement("div");
      row.style.display = "flex";
      row.style.flexDirection = "column";
      row.style.gap = "4px";

      row.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:space-between;">
          <span style="font-weight:700; color:var(--primary); font-size:12.5px;">第 (${bIdx + 1}) 空：</span>
          <span class="blank-status-badge-${bIdx}" style="font-size:12px; font-weight:bold;"></span>
        </div>
        <input type="text" class="quiz-blank-input" data-bidx="${bIdx}" placeholder="在此输入作答（可简写或留空）" style="width:100%; box-sizing:border-box; padding:9px 12px; border-radius:8px; border:1px solid var(--border); background:var(--surface); color:var(--text); font-size:14px; outline:none;" />
        <div class="blank-standard-ans-${bIdx}" style="display:none; font-size:12.5px; color:#34A853; font-weight:600; padding:2px 4px;"></div>
      `;
      container.appendChild(row);
    });

    const btnRow = document.createElement("div");
    btnRow.style.display = "flex";
    btnRow.style.gap = "10px";
    btnRow.style.marginTop = "12px";

    const btnPeek = document.createElement("button");
    btnPeek.className = "btn";
    btnPeek.style.flex = "1";
    btnPeek.style.background = "var(--surface)";
    btnPeek.style.border = "1px solid var(--border)";
    btnPeek.style.color = "var(--text-sec)";
    btnPeek.style.borderRadius = "10px";
    btnPeek.style.padding = "10px";
    btnPeek.style.fontWeight = "600";
    btnPeek.style.cursor = "pointer";
    btnPeek.textContent = "直接看答案";

    const btnSubmit = document.createElement("button");
    btnSubmit.className = "btn";
    btnSubmit.style.flex = "1";
    btnSubmit.style.background = "var(--primary)";
    btnSubmit.style.color = "#fff";
    btnSubmit.style.border = "none";
    btnSubmit.style.borderRadius = "10px";
    btnSubmit.style.padding = "10px";
    btnSubmit.style.fontWeight = "bold";
    btnSubmit.style.cursor = "pointer";
    btnSubmit.textContent = "提交核对";

    btnRow.appendChild(btnPeek);
    btnRow.appendChild(btnSubmit);
    container.appendChild(btnRow);
    dom.quizOptionsContainer.appendChild(container);

    function checkBlankMatch(user, standard) {
      if (!user || !user.trim()) return false;
      const u = user.trim().toLowerCase();
      const s = standard.trim().toLowerCase();
      if (u === s) return true;
      const parts = s.split(/[（）()、\/或，,]/).map(x => x.trim()).filter(Boolean);
      return parts.some(p => p === u || u.includes(p) || p.includes(u));
    }

    function finalizeBlanks(isPeek) {
      if (state.quizAnswered) return;
      state.quizAnswered = true;
      btnRow.style.display = "none";

      const inputs = container.querySelectorAll(".quiz-blank-input");
      let allCorrect = true;

      inputs.forEach(input => {
        input.disabled = true;
        const bIdx = parseInt(input.getAttribute("data-bidx"), 10);
        const standard = blanks[bIdx];
        const userVal = input.value;
        const matched = !isPeek && checkBlankMatch(userVal, standard);
        if (!matched) allCorrect = false;

        const badge = container.querySelector(`.blank-status-badge-${bIdx}`);
        const ansBox = container.querySelector(`.blank-standard-ans-${bIdx}`);

        if (matched) {
          input.style.borderColor = "#34A853";
          input.style.background = "rgba(52, 168, 83, 0.08)";
          badge.textContent = "✓ 作答正确";
          badge.style.color = "#34A853";
        } else {
          input.style.borderColor = "#EA4335";
          input.style.background = "rgba(234, 67, 53, 0.08)";
          badge.textContent = isPeek ? "参考对照" : "✗ 待强化";
          badge.style.color = isPeek ? "var(--text-sec)" : "#EA4335";
          ansBox.style.display = "block";
          ansBox.innerHTML = `标准参考：<b>${standard}</b>`;
        }
      });

      if (!isPeek && allCorrect) {
        state.quizScore++;
      }

      const explanation = q.rationale || q.hint || "填空自测考点核对完成。";
      dom.quizRationaleText.innerHTML = renderMarkdown(explanation);
      dom.quizRationaleBox.classList.add("visible");
      dom.btnQuizNext.style.display = "inline-flex";
    }

    btnSubmit.addEventListener("click", () => finalizeBlanks(false));
    btnPeek.addEventListener("click", () => finalizeBlanks(true));
    return;
  }

  dom.quizTypeBadge.textContent = q.type === "multiple_select" ? "多项选择" : "单项选择";
  const letters = ["A", "B", "C", "D", "E", "F"];
  const opts = q.answerOptions || [];
  const selectedMulti = new Set();

  opts.forEach((opt, idx) => {
    const btn = document.createElement("button");
    btn.className = "quiz-opt-btn";
    btn.innerHTML = `
      <span style="font-weight:700; color:var(--primary); min-width: 18px;">${letters[idx]}.</span>
      <span style="flex:1;">${renderMarkdown(opt.text)}</span>
    `;

    btn.addEventListener("click", () => {
      if (state.quizAnswered) return;
      if (q.type === "multiple_select") {
        if (selectedMulti.has(idx)) {
          selectedMulti.delete(idx);
          btn.style.borderColor = "var(--border)";
          btn.style.background = "var(--surface)";
        } else {
          selectedMulti.add(idx);
          btn.style.borderColor = "var(--primary)";
          btn.style.background = "rgba(66, 133, 244, 0.08)";
        }
      } else {
        handleQuizOptionClick(btn, opt, q);
      }
    });

    dom.quizOptionsContainer.appendChild(btn);
  });

  if (q.type === "multiple_select") {
    const submitBtn = document.createElement("button");
    submitBtn.className = "btn";
    submitBtn.style.width = "100%";
    submitBtn.style.marginTop = "12px";
    submitBtn.style.background = "var(--primary)";
    submitBtn.style.color = "#fff";
    submitBtn.style.border = "none";
    submitBtn.style.borderRadius = "10px";
    submitBtn.style.padding = "10px";
    submitBtn.style.fontWeight = "bold";
    submitBtn.style.cursor = "pointer";
    submitBtn.textContent = "确认提交本题";

    submitBtn.addEventListener("click", () => {
      if (state.quizAnswered || selectedMulti.size === 0) return;
      state.quizAnswered = true;
      submitBtn.style.display = "none";

      const allBtns = dom.quizOptionsContainer.querySelectorAll(".quiz-opt-btn");
      const correctIndices = new Set(opts.map((o, i) => o.isCorrect ? i : -1).filter(i => i >= 0));
      const isAllCorrect = setsEqual(selectedMulti, correctIndices);

      if (isAllCorrect) state.quizScore++;

      opts.forEach((opt, idx) => {
        if (allBtns[idx]) {
          if (opt.isCorrect) allBtns[idx].classList.add("correct");
          else if (selectedMulti.has(idx)) allBtns[idx].classList.add("wrong");
        }
      });

      const explanation = (isAllCorrect ? "回答完全正确！" : `回答错误，正确答案是：${Array.from(correctIndices).map(i => letters[i]).join(", ")}`) +
        (q.hint ? `\n\n提示：${q.hint}` : "");
      dom.quizRationaleText.innerHTML = renderMarkdown(explanation);
      dom.quizRationaleBox.classList.add("visible");
      dom.btnQuizNext.style.display = "inline-flex";
    });

    dom.quizOptionsContainer.appendChild(submitBtn);
  }
}

function setsEqual(a, b) {
  if (a.size !== b.size) return false;
  for (const item of a) if (!b.has(item)) return false;
  return true;
}

function handleQuizOptionClick(clickedBtn, selectedOpt, question) {
  state.quizAnswered = true;
  const isCorrect = selectedOpt.isCorrect;

  if (isCorrect) {
    state.quizScore++;
    clickedBtn.classList.add("correct");
  } else {
    clickedBtn.classList.add("wrong");
    const allBtns = dom.quizOptionsContainer.querySelectorAll(".quiz-opt-btn");
    question.answerOptions.forEach((opt, idx) => {
      if (opt.isCorrect && allBtns[idx]) {
        allBtns[idx].classList.add("correct");
      }
    });
  }

  const explanation = selectedOpt.rationale || question.hint || "该选项符合题意考点。";
  dom.quizRationaleText.innerHTML = renderMarkdown(explanation);
  dom.quizRationaleBox.classList.add("visible");
  dom.btnQuizNext.style.display = "inline-flex";
}

dom.btnQuizNext.addEventListener("click", () => {
  if (state.quizIndex < state.quizData.length - 1) {
    state.quizIndex++;
    renderQuizQuestion();
  } else {
    clearInterval(state.quizTimerId);
    const total = state.quizData.length;
    const rate = Math.round((state.quizScore / total) * 100);
    alert(`🏆 测验结束！\n答对: ${state.quizScore} / ${total} 题\n得分率: ${rate}%\n用时: ${dom.quizTimer.textContent}`);
    showScreen(state.currentSubject ? "home" : "subjectSelect");
  }
});

// ==========================================
// 7. 知识思维导图渲染与缩放平移
// ==========================================
async function openMindmap(unit) {
  state.currentUnit = unit;
  dom.mindmapUnitTitle.textContent = `${unit.title} · 知识导图`;
  showScreen("mindmap");

  try {
    const res = await fetch(`/api/data?subjectId=${state.currentSubject.id}&unitId=${unit.id}&category=mindmaps`);
    state.mindmapData = await res.json();
    renderMindmapTree();
    resetMindmapView();
  } catch (err) {
    dom.mindmapTreeRoot.innerHTML = `<div style="color:#fff; padding:40px;">暂无导图数据</div>`;
  }
}

function renderMindmapTree() {
  dom.mindmapTreeRoot.innerHTML = "";
  if (!state.mindmapData || !state.mindmapData.name) {
    dom.mindmapTreeRoot.innerHTML = "<div style='color:#fff;'>无法解析思维导图节点</div>";
    return;
  }

  function createNodeEl(node, level = 0) {
    const row = document.createElement("div");
    row.className = "mindmap-node-row";

    const hasChildren = node.children && node.children.length > 0;
    const card = document.createElement("div");
    card.className = `mindmap-node-card level-${Math.min(level, 2)}`;
    card.innerHTML = `
      <span>${node.name}</span>
      ${hasChildren ? '<span class="mindmap-toggle-icon">▼</span>' : ''}
    `;

    row.appendChild(card);

    if (hasChildren) {
      const childrenContainer = document.createElement("div");
      childrenContainer.style.marginLeft = "24px";
      childrenContainer.style.borderLeft = "2px dashed rgba(255,255,255,0.15)";
      childrenContainer.style.paddingLeft = "12px";

      node.children.forEach(child => {
        childrenContainer.appendChild(createNodeEl(child, level + 1));
      });

      row.appendChild(childrenContainer);

      card.addEventListener("click", () => {
        const isHidden = childrenContainer.style.display === "none";
        childrenContainer.style.display = isHidden ? "block" : "none";
        const icon = card.querySelector(".mindmap-toggle-icon");
        if (icon) icon.textContent = isHidden ? "▼" : "▶";
      });
    }

    return row;
  }

  dom.mindmapTreeRoot.appendChild(createNodeEl(state.mindmapData, 0));
}

function initMindmapPanZoom() {
  const vp = dom.mindmapViewport;

  vp.addEventListener("mousedown", (e) => {
    state.isDraggingMindmap = true;
    state.dragStartX = e.clientX - state.mindmapPanX;
    state.dragStartY = e.clientY - state.mindmapPanY;
  });

  window.addEventListener("mousemove", (e) => {
    if (!state.isDraggingMindmap) return;
    state.mindmapPanX = e.clientX - state.dragStartX;
    state.mindmapPanY = e.clientY - state.dragStartY;
    updateMindmapTransform();
  });

  window.addEventListener("mouseup", () => {
    state.isDraggingMindmap = false;
  });

  vp.addEventListener("wheel", (e) => {
    e.preventDefault();
    const delta = e.deltaY < 0 ? 0.12 : -0.12;
    state.mindmapScale = Math.min(Math.max(state.mindmapScale + delta, 0.4), 2.5);
    updateMindmapTransform();
  });

  dom.btnMindmapZoomIn.addEventListener("click", () => {
    state.mindmapScale = Math.min(state.mindmapScale + 0.2, 2.5);
    updateMindmapTransform();
  });
  dom.btnMindmapZoomOut.addEventListener("click", () => {
    state.mindmapScale = Math.max(state.mindmapScale - 0.2, 0.4);
    updateMindmapTransform();
  });
  dom.btnMindmapReset.addEventListener("click", resetMindmapView);
}

function resetMindmapView() {
  state.mindmapScale = 1.0;
  state.mindmapPanX = 30;
  state.mindmapPanY = 30;
  updateMindmapTransform();
}

function updateMindmapTransform() {
  dom.mindmapCanvas.style.transform = `translate(${state.mindmapPanX}px, ${state.mindmapPanY}px) scale(${state.mindmapScale})`;
}

// ==========================================
// 8. 全局键盘快捷键
// ==========================================
function handleGlobalKeydown(e) {
  if (e.target && (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA")) {
    return;
  }
  if (dom.screens.study.classList.contains("active")) {
    if (e.code === "Space") {
      e.preventDefault();
      flipCard();
    } else if (e.code === "ArrowRight") {
      if (state.cardIndex < state.deckData.length - 1) {
        state.cardIndex++;
        renderFlashcard();
      }
    } else if (e.code === "ArrowLeft") {
      if (state.cardIndex > 0) {
        state.cardIndex--;
        renderFlashcard();
      }
    } else if (e.key === "1" || e.code === "Digit1") {
      judgeCard(false);
    } else if (e.key === "2" || e.code === "Digit2") {
      judgeCard(true);
    }
  }
}

// 启动执行
window.addEventListener("DOMContentLoaded", initApp);
