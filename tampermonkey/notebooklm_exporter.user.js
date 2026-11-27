// ==UserScript==
// @name         NotebookLM Studio 资源导出器 (闪卡/测验/导图) - 支持一键ZIP打包
// @namespace    https://notebook.google.com/
// @version      1.2.0
// @description  一键扫描并导出 Google NotebookLM Studio 面板中的闪卡、测验、思维导图为标准 JSON，支持一键批量打包导出为 ZIP 压缩包（自动分类目录）。纯原生 DOM 与纯 JS ZIP 实现，百分之百兼容 Trusted Types 与严格 CSP 策略！
// @author       Assistant & Daniel
// @match        https://notebook.google.com/*
// @grant        GM_setClipboard
// @grant        unsafeWindow
// @run-at       document-idle
// ==/UserScript==

(function () {
  'use strict';

  // 1. Trusted Types 策略兜底（规避部分环境下的严格策略）
  if (window.trustedTypes && window.trustedTypes.createPolicy) {
    try {
      window.trustedTypes.createPolicy('default', {
        createHTML: (string) => string
      });
    } catch (e) {
      // 忽略已存在的策略
    }
  }

  // 2. 纯 DOM 节点构造器，彻底规避 innerHTML 赋值
  function h(tag, props = {}, ...children) {
    const el = document.createElement(tag);
    for (const [k, v] of Object.entries(props)) {
      if (k === 'style' && typeof v === 'object') {
        Object.assign(el.style, v);
      } else if (k.startsWith('on') && typeof v === 'function') {
        el.addEventListener(k.slice(2).toLowerCase(), v);
      } else if (k === 'className') {
        el.className = v;
      } else {
        el.setAttribute(k, v);
      }
    }
    for (const child of children.flat()) {
      if (child == null) continue;
      if (typeof child === 'string' || typeof child === 'number') {
        el.appendChild(document.createTextNode(String(child)));
      } else if (child instanceof Node) {
        el.appendChild(child);
      }
    }
    return el;
  }

  // 3. 原生纯 JS CRC32 计算实现
  const crcTable = (() => {
    let c;
    const table = new Uint32Array(256);
    for (let n = 0; n < 256; n++) {
      c = n;
      for (let k = 0; k < 8; k++) {
        c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
      }
      table[n] = c;
    }
    return table;
  })();

  function computeCrc32(bytes) {
    let crc = 0 ^ (-1);
    for (let i = 0; i < bytes.length; i++) {
      crc = (crc >>> 8) ^ crcTable[(crc ^ bytes[i]) & 0xFF];
    }
    return (crc ^ (-1)) >>> 0;
  }

  // 4. 原生纯 JS ZIP 生成器（Store 模式，支持 UTF-8 中文文件名与目录结构）
  class SimpleZip {
    constructor() {
      this.files = [];
    }

    addFile(filename, content) {
      const encoder = new TextEncoder();
      const data = typeof content === 'string' ? encoder.encode(content) : new Uint8Array(content);
      const nameBytes = encoder.encode(filename.replace(/\\/g, '/'));
      const crc = computeCrc32(data);
      this.files.push({
        name: filename,
        nameBytes,
        data,
        crc,
        size: data.length
      });
    }

    generateBlob() {
      const parts = [];
      const centralDirHeaders = [];
      let offset = 0;

      const now = new Date();
      const dosTime = ((now.getHours() << 11) | (now.getMinutes() << 5) | (now.getSeconds() >> 1)) & 0xFFFF;
      const dosDate = (((now.getFullYear() - 1980) << 9) | ((now.getMonth() + 1) << 5) | now.getDate()) & 0xFFFF;

      for (const f of this.files) {
        // Local File Header (30 bytes + name length)
        const localHeader = new Uint8Array(30 + f.nameBytes.length);
        const lView = new DataView(localHeader.buffer);

        lView.setUint32(0, 0x04034b50, true);  // Local file header signature
        lView.setUint16(4, 20, true);          // Version needed (2.0)
        lView.setUint16(6, 0x0800, true);      // General purpose bit flag (Bit 11: UTF-8)
        lView.setUint16(8, 0, true);           // Compression method: 0 (Store)
        lView.setUint16(10, dosTime, true);
        lView.setUint16(12, dosDate, true);
        lView.setUint32(14, f.crc, true);
        lView.setUint32(18, f.size, true);     // Compressed size
        lView.setUint32(22, f.size, true);     // Uncompressed size
        lView.setUint16(26, f.nameBytes.length, true);
        lView.setUint16(28, 0, true);          // Extra field length
        localHeader.set(f.nameBytes, 30);

        parts.push(localHeader);
        parts.push(f.data);

        // Central Directory Header (46 bytes + name length)
        const cdHeader = new Uint8Array(46 + f.nameBytes.length);
        const cdView = new DataView(cdHeader.buffer);

        cdView.setUint32(0, 0x02014b50, true); // Central directory signature
        cdView.setUint16(4, 20, true);         // Version made by
        cdView.setUint16(6, 20, true);         // Version needed
        cdView.setUint16(8, 0x0800, true);     // Bit 11: UTF-8
        cdView.setUint16(10, 0, true);         // Compression: 0
        cdView.setUint16(12, dosTime, true);
        cdView.setUint16(14, dosDate, true);
        cdView.setUint32(16, f.crc, true);
        cdView.setUint32(20, f.size, true);
        cdView.setUint32(24, f.size, true);
        cdView.setUint16(28, f.nameBytes.length, true);
        cdView.setUint16(30, 0, true);         // Extra field length
        cdView.setUint16(32, 0, true);         // Comment length
        cdView.setUint16(34, 0, true);         // Disk number start
        cdView.setUint16(36, 0, true);         // Internal file attributes
        cdView.setUint32(38, 0, true);         // External file attributes
        cdView.setUint32(42, offset, true);    // Relative offset of local header
        cdHeader.set(f.nameBytes, 46);

        centralDirHeaders.push(cdHeader);
        offset += localHeader.length + f.size;
      }

      const centralDirOffset = offset;
      let centralDirSize = 0;
      for (const h of centralDirHeaders) {
        parts.push(h);
        centralDirSize += h.length;
      }

      // End of Central Directory Record (22 bytes)
      const eocd = new Uint8Array(22);
      const eView = new DataView(eocd.buffer);
      eView.setUint32(0, 0x06054b50, true);
      eView.setUint16(4, 0, true);
      eView.setUint16(6, 0, true);
      eView.setUint16(8, this.files.length, true);
      eView.setUint16(10, this.files.length, true);
      eView.setUint32(12, centralDirSize, true);
      eView.setUint32(16, centralDirOffset, true);
      eView.setUint16(20, 0, true);

      parts.push(eocd);
      return new Blob(parts, { type: 'application/zip' });
    }
  }

  // 5. 扫描页面中的 Artifacts
  function scanArtifacts() {
    const elements = Array.from(document.querySelectorAll('[id^="artifact-labels-"]'));
    const items = elements.map(el => {
      const id = el.id.replace('artifact-labels-', '');
      const btn = el.closest('button, [role="button"]') || el.parentElement;
      const lines = btn.innerText.split('\n').map(s => s.trim()).filter(Boolean);
      const icon = btn.querySelector('mat-icon')?.innerText?.trim() || '';
      const filtered = lines.filter(l => l !== 'Unread' && l !== icon && !l.includes('sources') && !l.includes('ago'));
      const title = filtered[0] || lines[0] || '未命名资源';

      let type = 'other';
      let typeLabel = '其他资源';
      let typeEmoji = '📄';
      let dirName = 'others';
      if (icon === 'copy' || title.includes('闪卡') || title.includes('Flashcard')) {
        type = 'flashcard';
        typeLabel = '闪卡 (Flashcard)';
        typeEmoji = '🗂️';
        dirName = 'flashcards';
      } else if (icon === 'quiz' || title.includes('测验') || title.includes('小测') || title.includes('Quiz')) {
        type = 'quiz';
        typeLabel = '测验 (Quiz)';
        typeEmoji = '📝';
        dirName = 'quizzes';
      } else if (icon === 'flowchart' || title.includes('思维导图') || title.includes('脑图') || title.includes('知识图谱') || title.includes('Mind Map')) {
        type = 'mindmap';
        typeLabel = '思维导图 (Mindmap)';
        typeEmoji = '🧠';
        dirName = 'mindmaps';
      }
      return { id, title, type, typeLabel, typeEmoji, dirName };
    });

    const unique = [];
    const seen = new Set();
    for (const item of items) {
      if (!seen.has(item.id)) {
        seen.add(item.id);
        unique.push(item);
      }
    }
    return unique;
  }

  // 5.1 智能多重提取 WIZ_global_data 会话凭证（彻底解决 Tampermonkey 沙箱隔离与 CSP 混淆问题）
  function getWizGlobalData() {
    // 1) 优先从 unsafeWindow 提取 (Tampermonkey 沙箱上下文环境)
    try {
      if (typeof unsafeWindow !== 'undefined' && unsafeWindow && unsafeWindow.WIZ_global_data) {
        const d = unsafeWindow.WIZ_global_data;
        if (d.SNlM0e && d.FdrFJe) return d;
      }
    } catch (_) {}

    // 2) 尝试从标准全局 window 提取
    try {
      if (typeof window !== 'undefined' && window && window.WIZ_global_data) {
        const d = window.WIZ_global_data;
        if (d.SNlM0e && d.FdrFJe) return d;
      }
    } catch (_) {}

    // 3) 终极穿透兜底：从页面内所有内联 <script> 标签中直接正则匹配提取
    try {
      const scripts = document.querySelectorAll('script');
      for (const s of scripts) {
        const text = s.textContent || '';
        if (text.includes('SNlM0e') && text.includes('FdrFJe')) {
          const atMatch = text.match(/"SNlM0e"\s*:\s*"([^"]+)"/);
          const fsidMatch = text.match(/"FdrFJe"\s*:\s*"([^"]+)"/);
          if (atMatch && fsidMatch) {
            return {
              SNlM0e: atMatch[1],
              FdrFJe: fsidMatch[1]
            };
          }
        }
      }
    } catch (_) {}

    return null;
  }

  // 6. 调用 Google BoQ batchexecute RPC (v9rmvd) 获取结构化数据
  async function fetchArtifactJson(artifactId) {
    const wiz = getWizGlobalData();
    const at = wiz?.SNlM0e;
    const fsid = wiz?.FdrFJe;
    if (!at || !fsid) {
      throw new Error("无法获取 NotebookLM 会话凭证 (WIZ_global_data)。请确保您处于具体的笔记本页面（非列表首页），且页面已完整加载。");
    }

    const reqPayload = JSON.stringify([[["v9rmvd", JSON.stringify([artifactId, [2, null, null, [1, null, null, null, null, null, null, null, null, null, [1]], [[1, 4, 8, 10, 14, 2, 3, 6, 7]]]]), null, "generic"]]]);
    const res = await fetch(`/_/LabsTailwindUi/data/batchexecute?rpcids=v9rmvd&source-path=${encodeURIComponent(window.location.pathname)}&bl=boq_labs-tailwind-frontend_20261013.13_p0&f.sid=${fsid}&hl=en&rt=c`, {
      method: 'POST',
      headers: { 'content-type': 'application/x-www-form-urlencoded;charset=UTF-8' },
      body: `f.req=${encodeURIComponent(reqPayload)}&at=${encodeURIComponent(at)}&`
    });

    const text = await res.text();
    const clean = text.replace(/^\)\]\}'\s*/, '');
    const line = clean.split('\n').find(l => l.includes('v9rmvd'));
    if (!line) throw new Error("RPC 响应中未找到 v9rmvd 数据");
    const parsed = JSON.parse(line);
    const item = parsed.find(x => x[1] === 'v9rmvd');
    const arr = JSON.parse(item[2])[0];
    const rawDataStr = arr[9]?.[3];
    if (!rawDataStr) throw new Error("该 Artifact 暂无内嵌 JSON 数据（可能属于多媒体或尚未生成完毕）");
    return JSON.parse(rawDataStr);
  }

  // 7. 清理文件名，过滤非法字符
  function sanitizeFileName(name) {
    return name.replace(/[\\/:*?"<>|]/g, '_').trim();
  }

  // 8. 轻量 Toast 提示
  function showToast(msg) {
    const old = document.getElementById('nlm-exporter-toast');
    if (old) old.remove();
    const toast = h('div', {
      id: 'nlm-exporter-toast',
      style: {
        position: 'fixed',
        bottom: '80px',
        right: '24px',
        backgroundColor: '#323232',
        color: '#fff',
        padding: '10px 18px',
        borderRadius: '8px',
        fontSize: '13px',
        boxShadow: '0 4px 12px rgba(0,0,0,0.4)',
        zIndex: '10000000',
        transition: 'opacity 0.2s',
        pointerEvents: 'none'
      }
    }, msg);
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2500);
  }

  // 9. 批量导出并打包为 ZIP
  async function exportAllToZip(targetArtifacts, onProgress) {
    const zip = new SimpleZip();
    const summary = {
      exportedAt: new Date().toISOString(),
      notebookTitle: document.title,
      totalCount: targetArtifacts.length,
      items: []
    };

    let processed = 0;
    let successCount = 0;

    for (const item of targetArtifacts) {
      processed++;
      if (onProgress) onProgress(processed, targetArtifacts.length, item.title);
      try {
        const data = await fetchArtifactJson(item.id);
        const fileName = `${item.dirName}/${sanitizeFileName(item.title)}.json`;
        const jsonContent = JSON.stringify(data, null, 2);
        zip.addFile(fileName, jsonContent);
        summary.items.push({
          id: item.id,
          title: item.title,
          type: item.type,
          file: fileName,
          status: 'success'
        });
        successCount++;
      } catch (e) {
        summary.items.push({
          id: item.id,
          title: item.title,
          type: item.type,
          status: 'skipped',
          error: e.message
        });
      }
    }

    // 加入元数据清单 summary.json
    zip.addFile('summary.json', JSON.stringify(summary, null, 2));

    const blob = zip.generateBlob();
    const dateStr = new Date().toISOString().slice(0, 10).replace(/-/g, '');
    const safeTitle = sanitizeFileName(document.title.replace(' - Gemini Notebook', '')) || 'NotebookLM';
    const zipFileName = `${safeTitle}_Studio_Export_${dateStr}.zip`;

    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = zipFileName;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);

    return { successCount, total: targetArtifacts.length, fileName: zipFileName };
  }

  // 10. 弹窗主界面
  function openModal() {
    let modal = document.getElementById('nlm-exporter-modal');
    if (modal) modal.remove();

    const artifacts = scanArtifacts();
    let currentFilter = 'all';

    const listContainer = h('div', {
      style: {
        flex: '1',
        overflowY: 'auto',
        padding: '16px',
        display: 'flex',
        flexDirection: 'column',
        gap: '10px'
      }
    });

    // 状态与进度提示
    const globalStatusSpan = h('span', {
      style: { fontSize: '12px', color: '#8ab4f8', fontWeight: '500' }
    }, '');

    // 批量导出 ZIP 按钮
    const exportZipBtn = h('button', {
      style: {
        background: 'linear-gradient(135deg, #1a73e8, #185abc)',
        color: '#ffffff',
        border: 'none',
        borderRadius: '8px',
        padding: '8px 18px',
        fontSize: '13px',
        fontWeight: '600',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        gap: '6px',
        boxShadow: '0 2px 8px rgba(26,115,232,0.3)',
        transition: 'opacity 0.2s'
      },
      onClick: async () => {
        const filtered = artifacts.filter(a => {
          if (currentFilter === 'all') return true;
          return a.type === currentFilter;
        });

        if (filtered.length === 0) {
          alert('当前分类下没有可导出的资源！');
          return;
        }

        exportZipBtn.disabled = true;
        exportZipBtn.style.opacity = '0.7';

        try {
          const res = await exportAllToZip(filtered, (cur, total, title) => {
            globalStatusSpan.textContent = `⏳ 正在打包 (${cur}/${total}): ${title.slice(0, 15)}...`;
            exportZipBtn.textContent = `打包中 (${cur}/${total})...`;
          });
          globalStatusSpan.textContent = `✅ 打包完成！成功导出 ${res.successCount} 个资源`;
          showToast(`已成功打包下载《${res.fileName}》！`);
        } catch (err) {
          globalStatusSpan.textContent = `❌ 打包失败: ${err.message}`;
          alert(`打包失败: ${err.message}`);
        } finally {
          exportZipBtn.disabled = false;
          exportZipBtn.style.opacity = '1';
          exportZipBtn.textContent = '📦 一键导出全部并打包为 ZIP';
        }
      }
    }, '📦 一键导出全部并打包为 ZIP');

    function renderList() {
      while (listContainer.firstChild) listContainer.removeChild(listContainer.firstChild);

      const filtered = artifacts.filter(a => {
        if (currentFilter === 'all') return true;
        return a.type === currentFilter;
      });

      if (filtered.length === 0) {
        listContainer.appendChild(h('div', {
          style: { textAlign: 'center', color: '#9aa0a6', padding: '30px 0' }
        }, '未找到对应分类的资源'));
        return;
      }

      for (const item of filtered) {
        const statusSpan = h('span', { style: { fontSize: '11px', color: '#9aa0a6', marginLeft: '6px' } }, '');

        // 复制按钮
        const copyBtn = h('button', {
          style: {
            background: '#303134',
            color: '#e8eaed',
            border: '1px solid #5f6368',
            borderRadius: '6px',
            padding: '6px 12px',
            cursor: 'pointer',
            fontSize: '12px',
            fontWeight: '500'
          },
          onClick: async (e) => {
            const btn = e.currentTarget;
            btn.disabled = true;
            statusSpan.textContent = ' 正在获取...';
            try {
              const data = await fetchArtifactJson(item.id);
              const jsonStr = JSON.stringify(data, null, 2);
              if (typeof GM_setClipboard !== 'undefined') {
                GM_setClipboard(jsonStr);
              } else {
                await navigator.clipboard.writeText(jsonStr);
              }
              statusSpan.textContent = ' ✅ 已复制！';
              showToast(`已复制《${item.title}》JSON 到剪贴板！`);
            } catch (err) {
              statusSpan.textContent = ' ❌ ' + err.message;
              alert("复制失败: " + err.message);
            } finally {
              btn.disabled = false;
            }
          }
        }, '📋 复制');

        // 下载按钮
        const downloadBtn = h('button', {
          style: {
            background: '#1a73e8',
            color: '#ffffff',
            border: 'none',
            borderRadius: '6px',
            padding: '6px 12px',
            cursor: 'pointer',
            fontSize: '12px',
            fontWeight: '500'
          },
          onClick: async (e) => {
            const btn = e.currentTarget;
            btn.disabled = true;
            statusSpan.textContent = ' 正在获取...';
            try {
              const data = await fetchArtifactJson(item.id);
              const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
              const url = URL.createObjectURL(blob);
              const a = document.createElement('a');
              a.href = url;
              a.download = `${sanitizeFileName(item.title)}.json`;
              document.body.appendChild(a);
              a.click();
              a.remove();
              URL.revokeObjectURL(url);
              statusSpan.textContent = ' ✅ 已下载！';
              showToast(`已成功下载《${item.title}.json》！`);
            } catch (err) {
              statusSpan.textContent = ' ❌ ' + err.message;
              alert("下载失败: " + err.message);
            } finally {
              btn.disabled = false;
            }
          }
        }, '📥 下载 JSON');

        const row = h('div', {
          style: {
            background: '#282a2d',
            border: '1px solid #3c4043',
            borderRadius: '10px',
            padding: '12px 14px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: '12px'
          }
        },
          h('div', { style: { display: 'flex', alignItems: 'center', gap: '10px', flex: '1', minWidth: '0' } },
            h('span', { style: { fontSize: '20px' } }, item.typeEmoji),
            h('div', { style: { overflow: 'hidden' } },
              h('div', { style: { fontWeight: '500', color: '#e8eaed', fontSize: '13px', whiteSpace: 'nowrap', textOverflow: 'ellipsis', overflow: 'hidden' } }, item.title),
              h('div', { style: { fontSize: '11px', color: '#9aa0a6', marginTop: '2px' } },
                `类型: ${item.typeLabel} | ID: ${item.id}`,
                statusSpan
              )
            )
          ),
          h('div', { style: { display: 'flex', gap: '8px', flexShrink: '0' } },
            copyBtn,
            downloadBtn
          )
        );

        listContainer.appendChild(row);
      }
    }

    function createTab(label, filterVal) {
      const tab = h('button', {
        style: {
          background: currentFilter === filterVal ? '#1a73e8' : '#303134',
          color: currentFilter === filterVal ? '#fff' : '#e8eaed',
          border: 'none',
          borderRadius: '16px',
          padding: '4px 12px',
          fontSize: '12px',
          cursor: 'pointer',
          fontWeight: '500'
        },
        onClick: () => {
          currentFilter = filterVal;
          tabBar.querySelectorAll('button').forEach(b => {
            b.style.background = '#303134';
            b.style.color = '#e8eaed';
          });
          tab.style.background = '#1a73e8';
          tab.style.color = '#fff';
          renderList();
        }
      }, label);
      return tab;
    }

    const tabBar = h('div', {
      style: {
        display: 'flex',
        gap: '8px',
        padding: '0 16px 12px',
        borderBottom: '1px solid #3c4043'
      }
    },
      createTab(`全部 (${artifacts.length})`, 'all'),
      createTab(`🗂️ 闪卡 (${artifacts.filter(a => a.type === 'flashcard').length})`, 'flashcard'),
      createTab(`📝 测验 (${artifacts.filter(a => a.type === 'quiz').length})`, 'quiz'),
      createTab(`🧠 导图 (${artifacts.filter(a => a.type === 'mindmap').length})`, 'mindmap')
    );

    modal = h('div', {
      id: 'nlm-exporter-modal',
      style: {
        position: 'fixed',
        inset: '0',
        backgroundColor: 'rgba(0,0,0,0.65)',
        zIndex: '1000000',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        backdropFilter: 'blur(3px)',
        fontFamily: "'Google Sans', Roboto, sans-serif"
      },
      onClick: (e) => {
        if (e.target === modal) modal.remove();
      }
    },
      h('div', {
        style: {
          width: '740px',
          maxWidth: '92vw',
          maxHeight: '85vh',
          backgroundColor: '#202124',
          borderRadius: '16px',
          border: '1px solid #3c4043',
          boxShadow: '0 12px 36px rgba(0,0,0,0.6)',
          display: 'flex',
          flexDirection: 'column',
          overflow: 'hidden'
        }
      },
        h('div', {
          style: {
            padding: '16px 20px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            borderBottom: '1px solid #3c4043'
          }
        },
          h('div', { style: { display: 'flex', alignItems: 'center', gap: '8px' } },
            h('span', { style: { fontSize: '20px' } }, '📦'),
            h('span', { style: { fontWeight: '600', fontSize: '16px', color: '#e8eaed' } }, 'Studio 资源导出工具'),
            h('span', { style: { fontSize: '12px', color: '#9aa0a6', marginLeft: '6px' } }, `(共扫描到 ${artifacts.length} 个资源)`)
          ),
          h('button', {
            style: {
              background: 'none',
              border: 'none',
              color: '#9aa0a6',
              fontSize: '22px',
              cursor: 'pointer',
              lineHeight: '1'
            },
            onClick: () => modal.remove()
          }, '×')
        ),
        tabBar,
        listContainer,
        h('div', {
          style: {
            padding: '12px 20px',
            borderTop: '1px solid #3c4043',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            gap: '12px',
            backgroundColor: '#1b1c1d'
          }
        },
          h('div', { style: { display: 'flex', flexDirection: 'column', gap: '2px', flex: '1', minWidth: '0' } },
            globalStatusSpan,
            h('span', { style: { fontSize: '11px', color: '#9aa0a6' } }, '纯 DOM + 零依赖纯 JS ZIP 打包，全自动按目录归类')
          ),
          h('div', { style: { display: 'flex', gap: '10px', alignItems: 'center' } },
            h('button', {
              style: {
                background: '#303134',
                color: '#e8eaed',
                border: '1px solid #5f6368',
                borderRadius: '6px',
                padding: '8px 14px',
                cursor: 'pointer',
                fontSize: '12px'
              },
              onClick: () => {
                renderList();
                showToast('列表已刷新！');
              }
            }, '🔄 刷新'),
            exportZipBtn
          )
        )
      )
    );

    document.body.appendChild(modal);
    renderList();
  }

  // 11. 注入右下角浮动按钮
  function initFloatingButton() {
    if (document.getElementById('nlm-exporter-btn')) return;

    const floatBtn = h('button', {
      id: 'nlm-exporter-btn',
      style: {
        position: 'fixed',
        bottom: '24px',
        right: '24px',
        backgroundColor: '#1a73e8',
        color: '#ffffff',
        border: 'none',
        borderRadius: '24px',
        padding: '12px 20px',
        fontSize: '14px',
        fontWeight: '500',
        boxShadow: '0 4px 16px rgba(0,0,0,0.3)',
        cursor: 'pointer',
        zIndex: '999999',
        display: 'flex',
        alignItems: 'center',
        gap: '8px',
        fontFamily: "'Google Sans', Roboto, sans-serif",
        transition: 'transform 0.15s, box-shadow 0.15s'
      },
      onMouseOver: (e) => {
        e.currentTarget.style.transform = 'translateY(-2px)';
        e.currentTarget.style.boxShadow = '0 6px 20px rgba(0,0,0,0.4)';
      },
      onMouseOut: (e) => {
        e.currentTarget.style.transform = 'translateY(0)';
        e.currentTarget.style.boxShadow = '0 4px 16px rgba(0,0,0,0.3)';
      },
      onClick: openModal
    },
      h('span', { style: { fontSize: '16px' } }, '📥'),
      h('span', {}, '导出 Studio 资源')
    );

    document.body.appendChild(floatBtn);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initFloatingButton);
  } else {
    initFloatingButton();
  }
  setInterval(initFloatingButton, 3000);
})();
