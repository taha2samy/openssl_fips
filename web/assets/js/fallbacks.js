// Fallback and Resilience Module for Wolfi OpenSSL FIPS Dashboard

/**
 * Checks the incoming data payload for required sections and fills in safe defaults
 * to prevent uncaught runtime errors (e.g., Cannot read properties of undefined).
 * @param {Object} data - Raw JSON payload from data.json
 * @returns {Object} Sanitized and structured data payload
 */
export function sanitizeDashboardData(data) {
  const safeData = data || {};

  // Ensure high-level structures exist
  safeData.reports = safeData.reports || {};
  safeData.packages = Array.isArray(safeData.packages) ? safeData.packages : [];
  safeData.security = safeData.security || {};
  safeData.security.kics = safeData.security.kics || { findings: [] };
  safeData.security.compliance = safeData.security.compliance || {};
  
  // Safe default variants
  const variants = ['distroless', 'standard', 'development'];
  variants.forEach(variant => {
    // Reports
    safeData.reports[variant] = safeData.reports[variant] || {
      summary: { passed: 0, failed: 0, duration: 0, total: 0 },
      tests: [],
      environment: { Platform: 'Linux', Python: 'Python 3.11' }
    };
    
    // Compliance and scans
    safeData.security.compliance[variant] = safeData.security.compliance[variant] || {
      vulnerabilities: { total: 0, critical: 0, high: 0, medium: 0, low: 0 },
      raw_scan: { Results: [] },
      docker_cis: { SuccessCount: 0, FailCount: 0 },
      k8s_nsa: { SuccessCount: 0, FailCount: 0 },
      k8s_pss_restricted: { SuccessCount: 0, FailCount: 0 }
    };
    
    // Provenance
    safeData.provenance = safeData.provenance || {};
    safeData.provenance[variant] = safeData.provenance[variant] || {
      digest: 'N/A',
      url: '#',
      sbom_url: '#'
    };
  });

  // Benchmarks fallback mapping
  safeData.benchmarks = safeData.benchmarks || {};
  safeData.benchmarks.metadata = safeData.benchmarks.metadata || { fips: { openssl_version: '3.1.2' } };
  safeData.benchmarks.metrics = safeData.benchmarks.metrics || {};

  const expectedAlgorithms = ['AES-256-GCM', 'sha256', 'sha512', 'sha3-256'];
  expectedAlgorithms.forEach(algo => {
    safeData.benchmarks.metrics[algo] = safeData.benchmarks.metrics[algo] || {
      fips: [0, 0, 0, 0, 0, 0],
      ubuntu: [0, 0, 0, 0, 0, 0],
      debian: [0, 0, 0, 0, 0, 0],
      alpine: [0, 0, 0, 0, 0, 0]
    };
  });

  safeData.bench_results_raw = Array.isArray(safeData.bench_results_raw) ? safeData.bench_results_raw : [];
  safeData.bench_signatures_raw = Array.isArray(safeData.bench_signatures_raw) ? safeData.bench_signatures_raw : [];
  safeData.hardware_context = safeData.hardware_context || {
    system: 'Linux',
    architecture: 'x86_64',
    cpu_cores: 4,
    ram_gb: 16,
    runner: 'Local Runner'
  };

  return safeData;
}

/**
 * Checks if key features have data populated, otherwise replaces containers with fallback visuals.
 * @param {Object} data - Sanitized dashboard data
 */
export function checkAndRenderFeatureFallbacks(data) {
  // Check Pytest Reports
  const hasDistrolessTests = data.reports?.distroless?.tests?.length > 0;
  const hasStandardTests = data.reports?.standard?.tests?.length > 0;
  if (!hasDistrolessTests && !hasStandardTests) {
    renderFallbackState(
      'pytest-runs-container',
      'Pytest Forensic Reports Missing',
      'No pytest compliance execution outputs were found in report_distroless.json or report_standard.json. Ensure test pipelines have completed running successfully.',
      'pipeline'
    );
  }

  // Check Trivy Scans
  const distrolessVulnerabilities = data.security?.compliance?.distroless?.raw_scan?.Results || [];
  const standardVulnerabilities = data.security?.compliance?.standard?.raw_scan?.Results || [];
  const hasVulnerabilities = distrolessVulnerabilities.length > 0 || standardVulnerabilities.length > 0;
  
  if (!hasVulnerabilities) {
    const tableBody = document.getElementById('vulnerability-table-rows');
    if (tableBody) {
      const parent = tableBody.closest('.overflow-x-auto');
      if (parent) {
        parent.classList.add('hidden');
      }
      renderFallbackState(
        'vulnerability-empty-state',
        'Vulnerability Scan Reports Pending',
        'Trivy security scans have not yet registered or are currently building. Run the local builder tool or trigger a repository build run to refresh.',
        'shield'
      );
      const emptyState = document.getElementById('vulnerability-empty-state');
      if (emptyState) {
        emptyState.classList.remove('hidden');
      }
    }
  }

  // Check KICS IaC Scan
  const hasKicsFindings = data.security?.kics?.findings?.length > 0;
  if (!hasKicsFindings) {
    renderFallbackState(
      'kicsStaticAnalysisAccordion',
      'KICS Static Audit Pending',
      'No IaC static scanning diagnostics were found. If this is a clean build, this is expected.',
      'info'
    );
  }

  // Check Benchmarks
  const metrics = data.benchmarks?.metrics || {};
  const hasPerformanceData = Object.values(metrics).some(m => m.fips?.some(val => val > 0));
  if (!hasPerformanceData) {
    // If charts are empty, we display fallback state
    const aesCanvas = document.getElementById('aesCurveChart');
    if (aesCanvas) {
      const container = aesCanvas.parentElement;
      if (container) {
        renderFallbackState(
          container,
          'Performance Benchmark Data Pending',
          'Automated OpenSSL speed runs have not been executed on this host. Run the benchmark tool to populate cryptographic throughput curves.',
          'chart'
        );
      }
    }
    const hashCanvas = document.getElementById('hashComparisonChart');
    if (hashCanvas) {
      const container = hashCanvas.parentElement;
      if (container) {
        renderFallbackState(
          container,
          'Digest Velocity Metrics Pending',
          'Cryptographic hash velocity runs are not yet recorded.',
          'chart'
        );
      }
    }
    const asymmetricCanvas = document.getElementById('asymmetricVelocityChart');
    if (asymmetricCanvas) {
      const container = asymmetricCanvas.parentElement;
      if (container) {
        renderFallbackState(
          container,
          'Asymmetric Key Sign/Verify Pending',
          'ECDSA and RSA signature verification logs are pending validation execution.',
          'chart'
        );
      }
    }
  }
}

/**
 * Dynamically inserts a highly polished "Data Pending / CI Execution Required" card inside a DOM container.
 * @param {string|HTMLElement} containerRef - Container ID or DOM node to overwrite/inject fallback into
 * @param {string} title - Main header of fallback state
 * @param {string} description - Explicit instructions/explanations
 * @param {string} iconType - Icon styling category ('shield', 'chart', 'pipeline', 'info')
 */
export function renderFallbackState(containerRef, title, description, iconType = 'info') {
  const container = typeof containerRef === 'string' ? document.getElementById(containerRef) : containerRef;
  if (!container) return;

  let iconSvg = '';
  let borderAccent = 'border-[var(--border-color)]';
  let iconBg = 'bg-[var(--bg-tertiary)] text-[var(--text-secondary)]';

  if (iconType === 'shield') {
    iconBg = 'bg-amber-500/10 text-amber-500';
    borderAccent = 'border-amber-500/20';
    iconSvg = `<svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>`;
  } else if (iconType === 'chart') {
    iconBg = 'bg-indigo-500/10 text-indigo-500';
    borderAccent = 'border-indigo-500/20';
    iconSvg = `<svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>`;
  } else if (iconType === 'pipeline') {
    iconBg = 'bg-blue-500/10 text-blue-500';
    borderAccent = 'border-blue-500/20';
    iconSvg = `<svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 1121.21 8H12"/></svg>`;
  } else {
    iconBg = 'bg-[var(--bg-tertiary)] text-[var(--text-secondary)]';
    borderAccent = 'border-[var(--border-color)]';
    iconSvg = `<svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>`;
  }

  container.innerHTML = `
    <div class="p-6 bg-[var(--bg-secondary)] border ${borderAccent} rounded-xl text-center space-y-4 max-w-xl mx-auto my-4 transition-all duration-300">
      <div class="w-14 h-14 ${iconBg} rounded-full flex items-center justify-center mx-auto shadow-inner">
        ${iconSvg}
      </div>
      <div class="space-y-1.5">
        <h4 class="text-sm font-bold text-[var(--text-primary)]">${escapeFallbackHTML(title)}</h4>
        <p class="text-xs text-[var(--text-secondary)] leading-relaxed">${escapeFallbackHTML(description)}</p>
      </div>
      <div class="pt-2">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 bg-[var(--bg-primary)] border border-[var(--border-color)] rounded-lg text-[10px] text-[var(--text-muted)] font-semibold font-mono">
          <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
          CI Execution Pending
        </span>
      </div>
    </div>
  `;
}

function escapeFallbackHTML(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
}
