// Pytest Forensic Validation Tests Module for Wolfi OpenSSL FIPS Dashboard

let activeTestSuiteVariant = 'distroless';

// Helper Function: Safely Render Code Block or Empty State
function renderCodeOrEmptyState(rawContent, emptyMessage = "No logs or data captured.", customClasses = "") {
  if (!rawContent || typeof rawContent !== 'string' || rawContent.trim().length === 0) {
    return `
      <div class="empty-log-state">
        <svg class="empty-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
        <p>${emptyMessage}</p>
      </div>
    `;
  }
  
  // Safely escape HTML to prevent XSS and rendering issues
  const safeContent = rawContent
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

  const classes = customClasses || "whitespace-pre-wrap leading-relaxed mt-1 text-slate-300 font-mono text-[11px]";
  return `<pre class="code-block ${classes}"><code>${safeContent}</code></pre>`;
}

export function initTestsSuiteViewer(data) {
  const container = document.getElementById('pytest-runs-container');
  const targetButtons = document.querySelectorAll('.test-variant-btn');

  if (!container) return;

  function renderSuite() {
    const report = data.reports?.[activeTestSuiteVariant] || {};
    const tests = report.tests || [];
    const stats = report.summary || { passed: 0, failed: 0, duration: 0, total: 0 };

    // Update statistics scorecard inside tests panel
    updateTestSummaryMetrics(stats, report.environment || {});

    if (tests.length === 0) {
      container.innerHTML = `
        <div class="text-center py-12 text-xs text-[var(--text-secondary)] italic">
          No automated test findings available for openssl-${activeTestSuiteVariant}.
        </div>
      `;
      return;
    }

    container.innerHTML = '';
    tests.forEach((test, idx) => {
      const isPassed = test.outcome === 'passed';
      const cleanTitle = test.nodeid.split('::').pop()
        .replace('test_', '')
        .replace(/_/g, ' ')
        .replace(/\b\w/g, c => c.toUpperCase());

      const card = document.createElement('div');
      card.className = 'test-card';
      
      const duration = test.call?.duration ? test.call.duration.toFixed(3) : '0.000';
      const outcomeBadge = isPassed 
        ? '<span class="badge badge-success text-[10px] font-bold py-0.5 px-2">Passed</span>' 
        : '<span class="badge badge-error text-[10px] font-bold py-0.5 px-2">Failed</span>';

      card.innerHTML = `
        <div class="flex items-start gap-3 min-w-0 flex-1">
          <div class="w-8 h-8 rounded-full flex items-center justify-center font-bold text-sm shrink-0 ${
            isPassed ? 'bg-emerald-500/10 text-emerald-500' : 'bg-red-500/10 text-red-500'
          }">
            ${isPassed ? '✓' : '✗'}
          </div>
          <div class="test-card-info">
            <h4 class="text-xs font-semibold text-[var(--text-primary)] flex items-center gap-2">
              ${escapeHTML(cleanTitle)}
              ${outcomeBadge}
            </h4>
            <span class="test-card-node-id select-all">${escapeHTML(test.nodeid)}</span>
          </div>
        </div>
        
        <div class="test-card-actions">
          <div class="text-left md:text-right font-mono text-[10px] text-[var(--text-secondary)]">
            <span class="block">Duration: <strong>${duration}s</strong></span>
            <span class="block text-[var(--text-muted)] mt-0.5">Setup: ${(test.setup?.duration || 0).toFixed(3)}s</span>
          </div>
          <button class="inspect-btn bg-[var(--bg-secondary)] border border-[var(--border-color)] hover:bg-[var(--bg-tertiary)] hover:text-[var(--text-primary)] text-[var(--text-secondary)] font-semibold transition-all" onclick="openForensicLogsDrawer('${activeTestSuiteVariant}', ${idx})">
            <svg class="w-3.5 h-3.5 text-[var(--text-muted)] shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
            </svg>
            Inspect Logs
          </button>
        </div>
      `;
      container.appendChild(card);
    });
  }

  // Set action triggers
  targetButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      targetButtons.forEach(b => b.classList.remove('bg-indigo-600', 'text-white'));
      targetButtons.forEach(b => b.classList.add('bg-[var(--bg-tertiary)]', 'text-[var(--text-secondary)]'));

      btn.classList.remove('bg-[var(--bg-tertiary)]', 'text-[var(--text-secondary)]');
      btn.classList.add('bg-indigo-600', 'text-white');

      activeTestSuiteVariant = btn.getAttribute('data-suite');
      renderSuite();
    });
  });

  // Load first suite draw
  renderSuite();

  // Create sliding forensic console drawer overlay dynamically to be absolutely self-contained
  initLogDrawerOverlay();
}

function updateTestSummaryMetrics(stats, environment) {
  const container = document.getElementById('pytest-summary-scorecard');
  if (!container) return;

  const total = stats.total || stats.passed + stats.failed || 0;
  const passRate = total > 0 ? Math.round((stats.passed / total) * 100) : 100;
  
  container.innerHTML = `
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
      <div class="p-3 bg-[var(--bg-primary)] border border-[var(--border-color)] rounded-xl">
        <span class="text-[10px] font-bold uppercase tracking-wider text-[var(--text-muted)]">Test Execution Status</span>
        <div class="text-lg font-bold text-[var(--color-success)] mt-1 font-mono">${passRate}% Pass Rate</div>
      </div>
      <div class="p-3 bg-[var(--bg-primary)] border border-[var(--border-color)] rounded-xl">
        <span class="text-[10px] font-bold uppercase tracking-wider text-[var(--text-muted)]">Asserted Cases</span>
        <div class="text-lg font-bold text-[var(--text-primary)] mt-1 font-mono">${stats.passed} / ${total} Passed</div>
      </div>
      <div class="p-3 bg-[var(--bg-primary)] border border-[var(--border-color)] rounded-xl">
        <span class="text-[10px] font-bold uppercase tracking-wider text-[var(--text-muted)]">Cumulated Latency</span>
        <div class="text-lg font-bold text-[var(--text-primary)] mt-1 font-mono">${(stats.duration || 0).toFixed(3)}s</div>
      </div>
      <div class="p-3 bg-[var(--bg-primary)] border border-[var(--border-color)] rounded-xl">
        <span class="text-[10px] font-bold uppercase tracking-wider text-[var(--text-muted)]">Verified Sandbox Base</span>
        <div class="text-lg font-bold text-[var(--text-primary)] mt-1 truncate" title="${escapeHTML(environment.Platform || 'Linux')}">${escapeHTML(environment.Python || 'Python 3.11')}</div>
      </div>
    </div>
  `;
}

function initLogDrawerOverlay() {
  if (document.getElementById('forensicLogDrawerOverlay')) return;

  const overlay = document.createElement('div');
  overlay.id = 'forensicLogDrawerOverlay';
  overlay.className = 'fixed inset-0 bg-slate-950/60 backdrop-blur-sm z-50 flex justify-end opacity-0 pointer-events-none transition-opacity duration-300';
  
  overlay.innerHTML = `
    <div id="forensicDrawerContent" class="w-full max-w-2xl bg-[var(--bg-secondary)] border-l border-[var(--border-color)] h-full flex flex-col translate-x-full transition-transform duration-300">
      <!-- Drawer Header -->
      <div class="p-5 border-b border-[var(--border-color)] flex items-center justify-between">
        <div>
          <span class="badge badge-accent text-[10px] py-0 px-1.5 font-bold mb-1">Pytest Standard Logs</span>
          <h3 class="text-base font-bold text-[var(--text-primary)]" id="drawerTestTitle">FIPS Self Test Executions</h3>
          <p class="text-[10px] text-[var(--text-secondary)] font-mono mt-1 select-all" id="drawerTestNodeId">test_fips.py::test_module</p>
        </div>
        <button class="p-2 rounded-lg bg-[var(--bg-primary)] border border-[var(--border-color)] hover:bg-[var(--bg-tertiary)] text-[var(--text-secondary)] hover:text-[var(--text-primary)] transition-all cursor-pointer" onclick="closeForensicLogsDrawer()">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
      
      <!-- Drawer Tabs -->
      <div class="flex border-b border-[var(--border-color)] px-4 bg-[var(--bg-primary)]">
        <button id="tabBtnCallLogs" class="py-2.5 px-3 border-b-2 border-indigo-500 text-xs font-semibold text-[var(--text-primary)]">Runtime Output Logs</button>
        <button id="tabBtnFailureTrace" class="py-2.5 px-3 border-b-2 border-transparent text-xs font-medium text-[var(--text-secondary)] hover:text-[var(--text-primary)]">Assertion Failures / Traceback</button>
      </div>

      <!-- Drawer Output Logs scrollable -->
      <div class="p-5 flex-1 overflow-y-auto font-mono text-xs text-[var(--text-secondary)] bg-[var(--bg-primary)]" id="drawerConsoleContainer">
        <!-- Terminal Logs injected here -->
      </div>

      <!-- Drawer Footer actions -->
      <div class="p-4 border-t border-[var(--border-color)] flex items-center justify-between bg-[var(--bg-secondary)] gap-4">
        <span class="text-[10px] text-[var(--text-muted)] font-semibold">Wolfi OpenSSL FIPS Core Audit Platform</span>
        <button class="px-3.5 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-lg transition-all cursor-pointer" id="copyConsoleLogsBtn">
          Copy Raw Logs
        </button>
      </div>
    </div>
  `;

  document.body.appendChild(overlay);

  // Close when overlay background is clicked
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) {
      closeForensicLogsDrawer();
    }
  });
}

// Global forensic drawers toggles mapped to window scope
window.openForensicLogsDrawer = function(suiteVariant, testIndex) {
  const overlay = document.getElementById('forensicLogDrawerOverlay');
  const drawer = document.getElementById('forensicDrawerContent');
  if (!overlay || !drawer) return;

  // Fetch test data from window/global context (which holds state in main.js)
  const appData = window.globalDashboardState;
  if (!appData) return;

  const testRecord = appData.reports?.[suiteVariant]?.tests?.[testIndex];
  if (!testRecord) return;

  const isPassed = testRecord.outcome === 'passed';
  const cleanTitle = testRecord.nodeid.split('::').pop()
    .replace('test_', '')
    .replace(/_/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase());

  // Update labels
  document.getElementById('drawerTestTitle').textContent = cleanTitle;
  document.getElementById('drawerTestNodeId').textContent = testRecord.nodeid;
  
  const variantBadge = document.querySelector('#forensicLogDrawerOverlay .badge-accent');
  if (variantBadge) {
    variantBadge.textContent = `Pytest Run: openssl-${suiteVariant}`;
    variantBadge.className = isPassed ? 'badge badge-success text-[10px] py-0 px-1.5 font-bold mb-1' : 'badge badge-error text-[10px] py-0 px-1.5 font-bold mb-1';
  }

  // Handle Tab contents initialization
  const callLogsTab = document.getElementById('tabBtnCallLogs');
  const failureTab = document.getElementById('tabBtnFailureTrace');
  const container = document.getElementById('drawerConsoleContainer');

  let logsHtml = '';
  const emittedLogs = testRecord.call?.log || [];
  const stdoutLogs = testRecord.call?.stdout || '';
  const stderrLogs = testRecord.call?.stderr || '';

  if (emittedLogs.length > 0) {
    logsHtml += emittedLogs.map(l => {
      const levelClass = l.levelname === 'ERROR' || l.levelname === 'WARNING' ? 'text-amber-500 font-bold' : 'text-emerald-500';
      return `<div class="mb-2"><span class="text-[var(--text-muted)] font-bold">[${l.levelname}]</span> <span class="${levelClass}">${escapeHTML(l.msg)}</span></div>`;
    }).join('');
  }

  logsHtml += `<div class="mt-4 pt-4 border-t border-[var(--border-color)]"><span class="text-indigo-400 font-bold">[STDOUT]</span>`;
  logsHtml += renderCodeOrEmptyState(stdoutLogs, "No console stdout or framework loggings were captured.", "whitespace-pre-wrap leading-relaxed mt-1 text-slate-300 font-mono text-[11px]");
  logsHtml += `</div>`;

  logsHtml += `<div class="mt-4 pt-4 border-t border-[var(--border-color)]"><span class="text-rose-400 font-bold">[STDERR]</span>`;
  logsHtml += renderCodeOrEmptyState(stderrLogs, "No console stderr captured.", "whitespace-pre-wrap leading-relaxed mt-1 text-rose-300 font-mono text-[11px]");
  logsHtml += `</div>`;

  container.innerHTML = logsHtml;

  // Active failure log content setup
  const longTrace = testRecord.failure_repr || testRecord.call?.crash?.message || '';
  if (longTrace) {
    failureTab.classList.remove('hidden');
  } else {
    failureTab.classList.add('hidden');
  }

  // Set action click listeners to switch tabs inside Drawer
  callLogsTab.className = 'py-2.5 px-3 border-b-2 border-indigo-500 text-xs font-semibold text-[var(--text-primary)] cursor-pointer';
  failureTab.className = 'py-2.5 px-3 border-b-2 border-transparent text-xs font-medium text-[var(--text-secondary)] hover:text-[var(--text-primary)] cursor-pointer';

  callLogsTab.onclick = () => {
    callLogsTab.className = 'py-2.5 px-3 border-b-2 border-indigo-500 text-xs font-semibold text-[var(--text-primary)] cursor-pointer';
    failureTab.className = 'py-2.5 px-3 border-b-2 border-transparent text-xs font-medium text-[var(--text-secondary)] hover:text-[var(--text-primary)] cursor-pointer';
    container.innerHTML = logsHtml;
  };

  failureTab.onclick = () => {
    failureTab.className = 'py-2.5 px-3 border-b-2 border-indigo-500 text-xs font-semibold text-[var(--text-primary)] cursor-pointer';
    callLogsTab.className = 'py-2.5 px-3 border-b-2 border-transparent text-xs font-medium text-[var(--text-secondary)] hover:text-[var(--text-primary)] cursor-pointer';
    container.innerHTML = renderCodeOrEmptyState(longTrace, "No assertion failures or tracebacks recorded for this test case.", "whitespace-pre-wrap leading-relaxed text-red-400 text-[11px] font-mono select-all bg-slate-950 p-4 rounded-xl border border-red-950");
  };

  // Setup raw copy action
  const copyBtn = document.getElementById('copyConsoleLogsBtn');
  if (copyBtn) {
    copyBtn.onclick = () => {
      const textToCopy = container.innerText;
      navigator.clipboard.writeText(textToCopy).then(() => {
        const origText = copyBtn.textContent;
        copyBtn.textContent = 'Copied!';
        copyBtn.className = 'px-3.5 py-1.5 bg-emerald-600 text-white text-xs font-semibold rounded-lg transition-all';
        setTimeout(() => {
          copyBtn.textContent = origText;
          copyBtn.className = 'px-3.5 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-lg transition-all';
        }, 1200);
      });
    };
  }

  // Slide-in transitions
  overlay.classList.remove('pointer-events-none');
  overlay.classList.add('opacity-100');
  drawer.classList.remove('translate-x-full');
};

window.closeForensicLogsDrawer = function() {
  const overlay = document.getElementById('forensicLogDrawerOverlay');
  const drawer = document.getElementById('forensicDrawerContent');
  if (overlay && drawer) {
    overlay.classList.remove('opacity-100');
    overlay.classList.add('pointer-events-none');
    drawer.classList.add('translate-x-full');
  }
};

function escapeHTML(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
}
