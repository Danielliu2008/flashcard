() => {
  // Remove any previously injected instances
  const existingBtn = document.getElementById('nlm-exporter-btn');
  if (existingBtn) existingBtn.remove();
  const existingModal = document.getElementById('nlm-exporter-modal');
  if (existingModal) existingModal.remove();

  // Helper function to create DOM element without innerHTML
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

  // Scan artifacts
  function scanArtifacts() {
    const items = Array.from(document.querySelectorAll('[id^="artifact-labels-"]')).map(el => {
      const id = el.id.replace('artifact-labels-', '');
      const btn = el.closest('button, [role="button"]') || el.parentElement;
      const lines = btn.innerText.split('\n').map(s => s.trim()).filter(Boolean);
      const icon = btn.querySelector('mat-icon')?.innerText?.trim() || '';
      const filtered = lines.filter(l => l !== 'Unread' && l !== icon && !l.includes('sources') && !l.includes('ago'));
      const title = filtered[0] || lines[0] || '未命名资源';
      
      let type = 'other';
      let typeLabel = '其他资源';
      let typeEmoji = '📄';
      if (icon === 'copy' || title.includes('闪卡') || title.includes('Flashcard')) {
        type = 'flashcard';
        typeLabel = '闪卡 (Flashcard)';
        typeEmoji = '🗂️';
      } else if (icon === 'quiz' || title.includes('测验') || title.includes('小测') || title.includes('Quiz')) {
        type = 'quiz';
        typeLabel = '测验 (Quiz)';
        typeEmoji = '📝';
      } else if (icon === 'flowchart' || title.includes('思维导图') || title.includes('脑图') || title.includes('知识图谱') || title.includes('Mind Map')) {
        type = 'mindmap';
        typeLabel = '思维导图 (Mindmap)';
        typeEmoji = '🧠';
      }
      return { id, title, type, typeLabel, typeEmoji };
    });

    // Deduplicate by ID
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

  // Fetch JSON via v9rmvd
  async function fetchArtifactJson(artifactId) {
    const at = window.WIZ_global_data?.SNlM0e;
    const fsid = window.WIZ_global_data?.FdrFJe;
    if (!at || !fsid) throw new Error("无法获取 NotebookLM 会话凭证 (WIZ_global_data)");
    
    const reqPayload = JSON.stringify([[["v9rmvd", JSON.stringify([artifactId, [2,null,null,[1,null,null,null,null,null,null,null,null,null,[1]],[[1,4,8,10,14,2,3,6,7]]]]), null, "generic"]]]);
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
    if (!rawDataStr) throw new Error("该 Artifact 暂无内嵌 JSON 数据");
    return JSON.parse(rawDataStr);
  }

  // Toast notification
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

  // Modal Dialog UI
  function openModal() {
    let modal = document.getElementById('nlm-exporter-modal');
    if (modal) modal.remove();

    const artifacts = scanArtifacts();
    let currentFilter = 'all';

    // List container
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

        // Copy button
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
              await navigator.clipboard.writeText(JSON.stringify(data, null, 2));
              statusSpan.textContent = ' ✅ 已复制！';
              showToast(`已成功复制《${item.title}》JSON 到剪贴板！`);
            } catch (err) {
              statusSpan.textContent = ' ❌ ' + err.message;
              alert("复制失败: " + err.message);
            } finally {
              btn.disabled = false;
            }
          }
        }, '📋 复制');

        // Download button
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
              a.download = `${item.title}.json`;
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

    // Filter tab buttons
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

    // Modal structure
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
          width: '720px',
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
        // Header
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
        // Footer
        h('div', {
          style: {
            padding: '12px 20px',
            borderTop: '1px solid #3c4043',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            fontSize: '12px',
            color: '#9aa0a6'
          }
        },
          h('span', {}, '支持一键将闪卡/测验/导图导出为干净的结构化 JSON'),
          h('button', {
            style: {
              background: '#303134',
              color: '#e8eaed',
              border: '1px solid #5f6368',
              borderRadius: '6px',
              padding: '6px 14px',
              cursor: 'pointer'
            },
            onClick: () => {
              renderList();
              showToast('列表已刷新！');
            }
          }, '🔄 重新扫描')
        )
      )
    );

    document.body.appendChild(modal);
    renderList();
  }

  // Floating trigger button
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
  return {
    success: true,
    buttonAdded: !!document.getElementById('nlm-exporter-btn'),
    artifactsCount: scanArtifacts().length
  };
}