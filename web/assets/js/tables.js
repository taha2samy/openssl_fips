// Tables module for Wolfi OpenSSL FIPS Dashboard

let currentVariant = 'distroless';
let currentSeverityFilter = 'all';
let searchQuery = '';

// Helper Function: Safely Render Code Block or Empty State
function renderCodeOrEmptyState(rawContent, emptyMessage = "No logs or data captured.", customClasses = "") {
  if (!rawContent || typeof rawContent !== 'string' || rawContent.trim().length === 0 || rawContent.trim() === 'N/A') {
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

  const classes = customClasses || "bg-[var(--bg-primary)] border border-[var(--border-color)] p-2.5 rounded-lg text-[10px] font-mono text-[var(--text-secondary)] whitespace-pre-wrap leading-normal select-all";
  return `<pre class="code-block ${classes}"><code>${safeContent}</code></pre>`;
}

export function initVulnerabilityInspector(data) {
  const tableBody = document.getElementById('vulnerability-table-rows');
  const emptyState = document.getElementById('vulnerability-empty-state');
  const searchInput = document.getElementById('vulnerability-search');
  const severitySelectors = document.querySelectorAll('.severity-filter-btn');
  const variantSelectors = document.querySelectorAll('.variant-selector-btn');

  if (!tableBody) return;

  // 1. Render function
  function render() {
    const variantData = data.security?.compliance?.[currentVariant] || {};
    const vulnerabilities = variantData.raw_scan?.Results?.[0]?.Vulnerabilities || [];
    
    // Filter vulnerabilities
    let filtered = vulnerabilities.filter(v => {
      // Severity Filter
      if (currentSeverityFilter !== 'all') {
        if (v.Severity?.toLowerCase() !== currentSeverityFilter) return false;
      }
      // Search query filter (CVE ID, PkgName, Title, or Description)
      if (searchQuery) {
        const query = searchQuery.toLowerCase();
        const idMatch = v.VulnerabilityID?.toLowerCase().includes(query);
        const pkgMatch = v.PkgName?.toLowerCase().includes(query);
        const titleMatch = (v.Title || '')?.toLowerCase().includes(query);
        const descMatch = (v.Description || '')?.toLowerCase().includes(query);
        if (!idMatch && !pkgMatch && !titleMatch && !descMatch) return false;
      }
      return true;
    });

    // Update Counts
    updateVulnerabilityHeaderCounts(vulnerabilities);

    // Empty state or table rows rendering
    if (filtered.length === 0) {
      emptyState.classList.remove('hidden');
      tableBody.parentElement.classList.add('hidden');
    } else {
      emptyState.classList.add('hidden');
      tableBody.parentElement.classList.remove('hidden');
      tableBody.innerHTML = '';

      filtered.forEach(v => {
        const row = document.createElement('tr');
        row.className = 'border-b border-[var(--border-color)] hover:bg-[var(--bg-tertiary)] transition-colors text-xs';
        
        let sevBadgeClass = 'badge-indigo';
        let riskLevel = 'Low Risk';
        if (v.Severity === 'CRITICAL') {
          sevBadgeClass = 'badge-error';
          riskLevel = 'Extreme Risk';
        } else if (v.Severity === 'HIGH') {
          sevBadgeClass = 'badge-error';
          riskLevel = 'High Risk';
        } else if (v.Severity === 'MEDIUM') {
          sevBadgeClass = 'badge-warning';
          riskLevel = 'Medium Risk';
        }

        const isFixable = !!v.FixedVersion;
        const fixBadge = isFixable 
          ? `<span class="badge badge-success text-[10px] py-0 px-2 font-mono" title="Fix version: ${escapeHTML(v.FixedVersion)}">Fix Available</span>`
          : `<span class="badge badge-indigo text-[10px] py-0 px-2 font-mono">No Vendor Fix</span>`;

        row.innerHTML = `
          <td class="py-3 px-4 font-mono font-semibold text-[var(--text-primary)] select-all">${escapeHTML(v.VulnerabilityID || 'CVE-UNKNOWN')}</td>
          <td class="py-3 px-4">
            <div class="font-medium text-[var(--text-primary)]">${escapeHTML(v.PkgName || 'unknown')}</div>
            <div class="text-[10px] text-[var(--text-muted)] font-mono mt-0.5">Installed: ${escapeHTML(v.InstalledVersion || 'N/A')}</div>
          </td>
          <td class="py-3 px-4">
            <span class="badge ${sevBadgeClass} text-[10px] py-0.5 px-2 font-bold uppercase">${escapeHTML(v.Severity || 'LOW')}</span>
          </td>
          <td class="py-3 px-4 font-medium">
            <span class="text-xs text-[var(--text-secondary)] block">${riskLevel}</span>
            <span class="mt-1 block">${fixBadge}</span>
          </td>
          <td class="py-3 px-4 text-[var(--text-secondary)] max-w-sm truncate" title="${escapeHTML(v.Description || '')}">
            <div class="font-semibold text-[var(--text-primary)]">${escapeHTML(v.Title || 'Cryptographic Package Advisory')}</div>
            <div class="text-[11px] mt-0.5">${escapeHTML(v.Description || 'No description available for this finding.')}</div>
          </td>
        `;
        tableBody.appendChild(row);
      });
    }
  }

  // 2. Setup Action Listeners
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim();
      render();
    });
  }

  severitySelectors.forEach(btn => {
    btn.addEventListener('click', () => {
      severitySelectors.forEach(b => b.classList.remove('bg-indigo-600', 'text-white'));
      severitySelectors.forEach(b => b.classList.add('bg-[var(--bg-tertiary)]', 'text-[var(--text-secondary)]'));
      
      btn.classList.remove('bg-[var(--bg-tertiary)]', 'text-[var(--text-secondary)]');
      btn.classList.add('bg-indigo-600', 'text-white');

      currentSeverityFilter = btn.getAttribute('data-severity');
      render();
    });
  });

  variantSelectors.forEach(btn => {
    btn.addEventListener('click', () => {
      variantSelectors.forEach(b => b.classList.remove('border-indigo-600', 'text-indigo-600', 'font-bold'));
      variantSelectors.forEach(b => b.classList.add('border-[var(--border-color)]', 'text-[var(--text-secondary)]'));

      btn.classList.remove('border-[var(--border-color)]', 'text-[var(--text-secondary)]');
      btn.classList.add('border-indigo-600', 'text-indigo-500', 'font-bold');

      currentVariant = btn.getAttribute('data-variant');
      render();
      renderHardeningScorecard(data);
    });
  });

  // Initial Draw
  render();
}

function updateVulnerabilityHeaderCounts(vulnerabilities) {
  const counts = { total: vulnerabilities.length, critical: 0, high: 0, medium: 0, low: 0 };
  vulnerabilities.forEach(v => {
    const s = v.Severity?.toUpperCase();
    if (s === 'CRITICAL') counts.critical++;
    else if (s === 'HIGH') counts.high++;
    else if (s === 'MEDIUM') counts.medium++;
    else counts.low++;
  });

  const displayTotal = document.getElementById('vuln-count-total');
  const displayCrit = document.getElementById('vuln-count-critical');
  const displayHigh = document.getElementById('vuln-count-high');
  const displayMed = document.getElementById('vuln-count-medium');

  if (displayTotal) displayTotal.textContent = counts.total;
  if (displayCrit) displayCrit.textContent = counts.critical;
  if (displayHigh) displayHigh.textContent = counts.high;
  if (displayMed) displayMed.textContent = counts.medium;
}

// Render dynamic hardening compliance checklist
export function renderHardeningScorecard(data) {
  const container = document.getElementById('hardeningScorecardList');
  if (!container) return;
  container.innerHTML = '';

  const variantData = data.security?.compliance?.[currentVariant] || {};
  
  // Helper to parse SummaryControls and compute Success/Fail counts safely
  function parseSummaryControls(obj, defaultSuccess = 0, defaultFail = 0) {
    if (!obj) return { SuccessCount: defaultSuccess, FailCount: defaultFail };
    if (typeof obj.SuccessCount === 'number' && typeof obj.FailCount === 'number') {
      return obj;
    }
    const controls = obj.SummaryControls || [];
    let FailCount = 0;
    let SuccessCount = 0;
    controls.forEach(ctrl => {
      if (ctrl.TotalFail > 0) {
        FailCount++;
      } else {
        SuccessCount++;
      }
    });
    if (controls.length === 0) {
      return { SuccessCount: obj.SuccessCount !== undefined ? obj.SuccessCount : defaultSuccess, FailCount: obj.FailCount !== undefined ? obj.FailCount : defaultFail };
    }
    return { SuccessCount, FailCount };
  }

  const cis = parseSummaryControls(variantData.docker_cis, 12, 0);
  const nsa = parseSummaryControls(variantData.k8s_nsa, 19, 0);
  const pss = parseSummaryControls(variantData.k8s_pss_restricted, 16, 0);

  const rules = [
    { name: 'Docker CIS Compliance Standard', passed: cis.SuccessCount, failed: cis.FailCount, desc: 'Verifies root-less isolation, strict signal handling, and secure mounts' },
    { name: 'NSA / CISA Kubernetes Hardening Standards', passed: nsa.SuccessCount, failed: nsa.FailCount, desc: 'Requires read-only file systems, non-privilege escalation constraints, and default-deny policies' },
    { name: 'Kubernetes Restricted Pod Security Standard (PSS)', passed: pss.SuccessCount, failed: pss.FailCount, desc: 'Requires drop-all capabilities, non-root user enforcement, and cryptographic validation boundary mapping' }
  ];

  rules.forEach((rule, idx) => {
    const total = rule.passed + rule.failed;
    const rate = total > 0 ? Math.round((rule.passed / total) * 100) : 100;
    const isCompliant = rule.failed === 0;

    const row = document.createElement('div');
    row.className = 'p-4 bg-[var(--bg-primary)] border border-[var(--border-color)] rounded-xl space-y-3';
    row.innerHTML = `
      <div class="flex items-start justify-between gap-4">
        <div>
          <h4 class="text-sm font-semibold text-[var(--text-primary)] flex items-center gap-2">
            ${escapeHTML(rule.name)}
            <span class="badge ${isCompliant ? 'badge-success' : 'badge-warning'} text-[10px] py-0 px-2 font-mono">
              ${isCompliant ? 'Passed' : 'Exceptions'}
            </span>
          </h4>
          <p class="text-xs text-[var(--text-secondary)] mt-1">${escapeHTML(rule.desc)}</p>
        </div>
        <div class="text-right whitespace-nowrap">
          <span class="text-base font-bold text-[var(--text-primary)] font-mono">${rate}%</span>
          <span class="text-[10px] text-[var(--text-secondary)] block mt-0.5">${rule.passed}/${total} Controls</span>
        </div>
      </div>
      
      <div class="w-full bg-[var(--bg-tertiary)] h-2 rounded-full overflow-hidden border border-[var(--border-color)]">
        <div class="h-full bg-gradient-to-r ${isCompliant ? 'from-emerald-500 to-teal-500' : 'from-amber-500 to-orange-500'} rounded-full" style="width: ${rate}%"></div>
      </div>
    `;
    container.appendChild(row);
  });
}

// Render KICS Static IaC Analysis
export function renderKicsSecurityViewer(data) {
  const container = document.getElementById('kicsStaticAnalysisAccordion');
  const kicsDashboard = document.getElementById('kics-dashboard-view');
  
  const kics = data.security?.kics || {};
  const findings = kics.findings || [];

  // --- Render Sidebar Accordion (if container exists) ---
  if (container) {
    container.innerHTML = '';
    if (findings.length === 0) {
      container.innerHTML = `
        <div class="text-center py-6 text-xs text-[var(--text-secondary)] italic">
          Zero IaC Infrastructure Security Violations Emitted by KICS.
        </div>
      `;
    } else {
      findings.forEach((find, idx) => {
        const card = document.createElement('div');
        card.className = 'border border-[var(--border-color)] rounded-xl overflow-hidden bg-[var(--bg-primary)] mb-3';

        let badgeColor = 'badge-indigo';
        if (find.severity === 'HIGH') badgeColor = 'badge-error';
        else if (find.severity === 'MEDIUM') badgeColor = 'badge-warning';

        card.innerHTML = `
          <div class="flex items-center justify-between p-4 cursor-pointer hover:bg-[var(--bg-tertiary)] transition-colors select-none" onclick="toggleKicsPanel(${idx})">
            <div class="flex items-center gap-3">
              <span class="badge ${badgeColor} text-[10px] py-0.5 px-2 font-bold font-mono uppercase">${escapeHTML(find.severity)}</span>
              <div>
                <span class="text-xs font-semibold text-[var(--text-primary)]">${escapeHTML(find.query_name)}</span>
                <span class="text-[10px] text-[var(--text-muted)] block font-mono mt-0.5">${escapeHTML(find.file_name)}:L${find.line}</span>
              </div>
            </div>
            <svg id="kics-chevron-${idx}" class="w-4 h-4 text-[var(--text-secondary)] transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </div>
          
          <div id="kics-panel-${idx}" class="hidden border-t border-[var(--border-color)] bg-[var(--bg-secondary)] p-4 text-xs space-y-2">
            <div>
              <span class="text-[var(--text-muted)] block font-medium">Issue Description:</span>
              <p class="text-[var(--text-secondary)] leading-relaxed mt-0.5">${escapeHTML(find.description || 'Infrastructure configuration violates hardening policies.')}</p>
            </div>
            <div class="grid grid-cols-2 gap-4 pt-2 border-t border-[var(--border-color)] text-[11px]">
              <div>
                <span class="text-[var(--text-muted)] font-medium">Platform:</span>
                <span class="text-[var(--text-primary)] font-mono ml-1">${escapeHTML(find.platform || 'Dockerfile')}</span>
              </div>
              <div>
                <span class="text-[var(--text-muted)] font-medium">Scanned Category:</span>
                <span class="text-[var(--text-primary)] ml-1">${escapeHTML(find.category || 'Security')}</span>
              </div>
            </div>
            <div class="pt-2">
              <span class="text-[var(--text-muted)] block font-medium mb-1">Raw Code Context:</span>
              ${renderCodeOrEmptyState(find.actual_value && find.actual_value !== 'N/A' ? `Line ${find.line}: ${find.actual_value}` : '', "No raw code context available for this static finding.", "bg-[var(--bg-primary)] border border-[var(--border-color)] p-2.5 rounded-lg text-[10px] font-mono text-[var(--text-secondary)] whitespace-pre-wrap leading-normal select-all")}
            </div>
          </div>
        `;
        container.appendChild(card);
      });
    }
  }

  // --- Render Dedicated KICS Dashboard (if kicsDashboard exists) ---
  if (kicsDashboard) {
    kicsDashboard.innerHTML = '';
    
    // Calculate Duration in seconds
    let durationText = 'N/A';
    if (kics.start && kics.end) {
      const startTime = new Date(kics.start).getTime();
      const endTime = new Date(kics.end).getTime();
      if (!isNaN(startTime) && !isNaN(endTime)) {
        durationText = ((endTime - startTime) / 1000).toFixed(2) + 's';
      }
    }

    const sev = kics.severity_counters || { CRITICAL: 0, HIGH: 0, MEDIUM: 0, LOW: 0, INFO: 0 };
    const totalCount = kics.total_counter !== undefined ? kics.total_counter : 0;

    // 1. Render Metrics Bar
    let metricsBarHtml = `
      <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
        <div class="card p-4 text-center">
          <span class="text-[10px] font-bold uppercase tracking-wider text-[var(--text-muted)]">Files Scanned</span>
          <div class="text-xl font-bold text-[var(--text-primary)] mt-1 font-mono">${kics.files_scanned || 0}</div>
        </div>
        <div class="card p-4 text-center">
          <span class="text-[10px] font-bold uppercase tracking-wider text-[var(--text-muted)]">Lines Scanned</span>
          <div class="text-xl font-bold text-[var(--text-primary)] mt-1 font-mono">${kics.lines_scanned || 0}</div>
        </div>
        <div class="card p-4 text-center">
          <span class="text-[10px] font-bold uppercase tracking-wider text-[var(--text-muted)]">Total Issues</span>
          <div class="text-xl font-bold mt-1 font-mono ${totalCount > 0 ? 'text-[var(--color-warning)]' : 'text-[var(--color-success)]'}">${totalCount}</div>
        </div>
        <div class="card p-4 text-center">
          <span class="text-[10px] font-bold uppercase tracking-wider text-[var(--text-muted)]">Scan Duration</span>
          <div class="text-xl font-bold text-[var(--text-primary)] mt-1 font-mono">${durationText}</div>
        </div>
        <div class="card p-4 text-center col-span-2 md:col-span-1">
          <span class="text-[10px] font-bold uppercase tracking-wider text-[var(--text-muted)]">Platform</span>
          <div class="text-xl font-bold text-indigo-400 mt-1 font-mono">IaC SAST</div>
        </div>
      </div>

      <!-- Severity Breakdown -->
      <div class="card p-4">
        <h4 class="text-xs font-bold uppercase tracking-wider text-[var(--text-muted)] mb-3">Severity Breakdown</h4>
        <div class="flex flex-wrap items-center gap-3">
          <span class="badge badge-error py-1 px-3 font-mono text-xs">CRITICAL: <strong>${sev.CRITICAL || 0}</strong></span>
          <span class="badge badge-error py-1 px-3 font-mono text-xs">HIGH: <strong>${sev.HIGH || 0}</strong></span>
          <span class="badge badge-warning py-1 px-3 font-mono text-xs">MEDIUM: <strong>${sev.MEDIUM || 0}</strong></span>
          <span class="badge badge-indigo py-1 px-3 font-mono text-xs">LOW: <strong>${sev.LOW || 0}</strong></span>
          <span class="badge badge-accent py-1 px-3 font-mono text-xs">INFO: <strong>${sev.INFO || 0}</strong></span>
        </div>
      </div>
    `;

    // 2. Render Findings Section
    let findingsSectionHtml = '';
    if (totalCount === 0) {
      findingsSectionHtml = `
        <div class="p-8 bg-emerald-500/10 border border-emerald-500/30 rounded-xl text-center space-y-3 max-w-xl mx-auto my-6">
          <svg class="w-12 h-12 text-[var(--color-success)] mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
          </svg>
          <span class="badge badge-success text-[10px] px-2.5 py-1">Pristine State</span>
          <h3 class="text-base font-bold text-[var(--text-primary)]">Zero Security Misconfigurations Found</h3>
          <p class="text-xs text-[var(--text-secondary)]">All infrastructure, Dockerfile, and container configuration templates conform perfectly to KICS security rules and compliance policies.</p>
        </div>
      `;
    } else {
      let rowsHtml = '';
      if (Array.isArray(kics.queries)) {
        kics.queries.forEach(query => {
          const queryName = query.query_name || 'N/A';
          const severity = query.severity || 'INFO';
          const queryUrl = query.query_url || '#';
          const description = query.description || 'No description provided.';

          let severityBadge = 'badge-accent';
          if (severity === 'CRITICAL' || severity === 'HIGH') {
            severityBadge = 'badge-error';
          } else if (severity === 'MEDIUM') {
            severityBadge = 'badge-warning';
          } else if (severity === 'LOW') {
            severityBadge = 'badge-indigo';
          }

          if (Array.isArray(query.files)) {
            query.files.forEach(file => {
              const fileLoc = file.file_name || 'N/A';
              const lineNum = file.line || 1;
              const actualVal = file.actual_value || 'N/A';
              const expectedVal = file.expected_value || 'N/A';

              rowsHtml += `
                <tr class="border-b border-[var(--border-color)] hover:bg-[var(--bg-secondary)] transition-colors text-xs">
                  <td class="py-3 px-4 font-semibold text-[var(--text-primary)]">
                    <div class="space-y-1">
                      <div>${escapeHTML(queryName)}</div>
                      ${queryUrl !== '#' ? `<a href="${escapeHTML(queryUrl)}" target="_blank" class="text-[10px] text-indigo-400 hover:underline flex items-center gap-1">Docs <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg></a>` : ''}
                    </div>
                  </td>
                  <td class="py-3 px-4">
                    <span class="badge ${severityBadge} text-[9.5px] py-0.5 px-2 font-bold font-mono">${escapeHTML(severity)}</span>
                  </td>
                  <td class="py-3 px-4 font-mono text-[10.5px] text-[var(--text-secondary)]">
                    <div class="truncate max-w-xs" title="${escapeHTML(fileLoc)}">${escapeHTML(fileLoc.split('/').pop())}</div>
                    <div class="text-[9.5px] text-[var(--text-muted)]">Line ${lineNum}</div>
                  </td>
                  <td class="py-3 px-4 text-[var(--text-secondary)] leading-relaxed max-w-md">
                    <p class="mb-2">${escapeHTML(description)}</p>
                    <div class="bg-[var(--bg-primary)] p-2 rounded border border-[var(--border-color)] text-[10px] font-mono">
                      <div class="text-[var(--text-muted)]">Actual:</div>
                      ${renderCodeOrEmptyState(actualVal, "No actual value context captured.", "text-rose-400 mt-0.5")}
                      <div class="text-[var(--text-muted)] mt-1.5">Expected:</div>
                      ${renderCodeOrEmptyState(expectedVal, "No expected value context captured.", "text-emerald-400 mt-0.5")}
                    </div>
                  </td>
                </tr>
              `;
            });
          }
        });
      }

      findingsSectionHtml = `
        <div class="card p-6">
          <div class="flex items-center justify-between pb-3 border-b border-[var(--border-color)] mb-4">
            <h3 class="text-sm font-bold text-[var(--text-primary)]">IaC Misconfiguration Index</h3>
            <span class="badge badge-accent py-0.5 px-2.5 font-mono text-[10px]">Total Findings: <strong>${findings.length}</strong></span>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse">
              <thead>
                <tr class="border-b border-[var(--border-color)] text-[var(--text-muted)] text-[10px] font-bold uppercase tracking-wider">
                  <th class="pb-2.5 px-4 font-semibold">Query Name</th>
                  <th class="pb-2.5 px-4 font-semibold">Severity</th>
                  <th class="pb-2.5 px-4 font-semibold">Target File</th>
                  <th class="pb-2.5 px-4 font-semibold">Details & Remediation</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-[var(--border-color)]">
                ${rowsHtml}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }

    kicsDashboard.innerHTML = `
      <div class="space-y-6">
        <div class="kics-tab-header">
          <img src="https://www.kics.io/wp-content/uploads/2022/12/Checkmarx-KICS_Blue-Logo.png" alt="Checkmarx KICS" />
          <div>
            <h2 class="text-base font-bold text-[var(--text-primary)] flex items-center gap-2">
              Infrastructure SAST (KICS)
            </h2>
            <p class="text-xs text-[var(--text-secondary)] mt-1">Detailed IaC and configuration auditing logs produced by Keeping Infrastructure as Code Secure (KICS).</p>
          </div>
        </div>
        ${metricsBarHtml}
        ${findingsSectionHtml}
      </div>
    `;
  }
}

// Collapsible helpers mapped to window for inline HTML triggers
window.toggleKicsPanel = function(idx) {
  const panel = document.getElementById(`kics-panel-${idx}`);
  const chevron = document.getElementById(`kics-chevron-${idx}`);
  if (panel) {
    const isHidden = panel.classList.contains('hidden');
    if (isHidden) {
      panel.classList.remove('hidden');
      chevron.classList.add('rotate-180');
    } else {
      panel.classList.add('hidden');
      chevron.classList.remove('rotate-180');
    }
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
