// Main Orchestrator for Wolfi OpenSSL FIPS Dashboard
import { renderAESChart, renderHashChart, renderAsymmetricChart, updateChartsTheme } from './charts.js';
import { initVulnerabilityInspector, renderHardeningScorecard, renderKicsSecurityViewer } from './tables.js';
import { initTestsSuiteViewer } from './tests.js';
import { sanitizeDashboardData, checkAndRenderFeatureFallbacks } from './fallbacks.js';

let appState = null;
let currentPullSelectionType = 'tag'; // 'tag', 'floating', 'digest'

// Theme Engine setup
function initThemeEngine() {
  const themeToggle = document.getElementById('theme-toggle');
  const sunIcon = document.getElementById('sun-icon');
  const moonIcon = document.getElementById('moon-icon');
  
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  let currentTheme = 'dark'; // default
  if (savedTheme) {
    currentTheme = savedTheme;
  } else if (!systemPrefersDark) {
    currentTheme = 'light';
  }
  
  setTheme(currentTheme);
  
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const targetTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      setTheme(targetTheme);
    });
  }
  
  function switchWolfiLogo(theme) {
    const wolfiLogo = document.getElementById('wolfi-logo');
    if (wolfiLogo) {
      if (theme === 'light') {
        wolfiLogo.src = 'https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/wolfi.svg';
      } else {
        wolfiLogo.src = 'https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/wolfi-light.svg';
      }
    }
  }

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
      if (sunIcon) sunIcon.classList.remove('hidden');
      if (moonIcon) moonIcon.classList.add('hidden');
    } else {
      document.documentElement.classList.remove('dark');
      if (sunIcon) sunIcon.classList.add('hidden');
      if (moonIcon) moonIcon.classList.remove('hidden');
    }

    switchWolfiLogo(theme);
    
    // Notify charts module to update colors
    if (appState) {
      updateChartsTheme(appState);
    }
  }
}

// Global scorecards and telemetry headers rendering
function renderBaseScorecards() {
  const cveTotal = document.getElementById('scorecard-cve-total');
  const fipsTests = document.getElementById('scorecard-fips-tests');
  const complianceScore = document.getElementById('scorecard-compliance-score');
  const builderOs = document.getElementById('scorecard-builder-os');
  const builderArch = document.getElementById('scorecard-builder-arch');
  const runnerType = document.getElementById('scorecard-runner-type');
  const runDateLabel = document.getElementById('generation-date-label');

  if (runDateLabel && appState.generation_date) {
    runDateLabel.textContent = `Pipeline Run: ${appState.generation_date}`;
  }

  // Count active vulnerabilities
  const distrolessCves = appState.security?.compliance?.distroless?.vulnerabilities?.total || 0;
  const standardCves = appState.security?.compliance?.standard?.vulnerabilities?.total || 0;
  const totalCves = distrolessCves + standardCves;

  if (cveTotal) {
    cveTotal.textContent = totalCves;
    if (totalCves > 0) {
      cveTotal.classList.add('text-[var(--color-warning)]');
    }
  }

  // Count passed Pytest test runs
  const passed = appState.reports?.distroless?.summary?.passed || 0;
  const total = appState.reports?.distroless?.summary?.total || 0;
  if (fipsTests) {
    fipsTests.textContent = `${passed} / ${total}`;
  }

  // Builder host platforms
  if (builderOs) {
    builderOs.textContent = appState.hardware_context?.system || 'Linux';
  }
  if (builderArch) {
    builderArch.textContent = `(${appState.hardware_context?.architecture || 'x86_64'})`;
  }
  if (runnerType) {
    runnerType.textContent = appState.hardware_context?.runner === 'GitHub Actions CI' ? 'GH CI/CD' : 'LOCAL ENV';
  }
}

// Sidebar system packages and specs
function renderSystemBaseSpec() {
  const container = document.getElementById('sidebar-system-spec');
  if (!container) return;

  const hardware = appState.hardware_context || {};
  const specs = [
    { label: 'Host Kernel', val: hardware.kernel || '5.15.0-generic' },
    { label: 'Compiler Platform', val: 'GCC v13.2 (Wolfi-SDK)' },
    { label: 'Cores / CPU Spec', val: `${hardware.cpu_cores || 4} Cores` },
    { label: 'Total Node Memory', val: `${hardware.ram_gb || 16} GB RAM` },
    { label: 'SSL Cryptographic Boundary', val: '/usr/local/lib/ossl-modules' }
  ];

  container.innerHTML = specs.map(item => `
    <div class="flex items-center justify-between py-2 text-xs border-b border-[var(--border-color)] last:border-b-0">
      <span class="text-[var(--text-secondary)] font-medium">${item.label}</span>
      <span class="font-mono text-[var(--text-primary)] select-all">${item.val}</span>
    </div>
  `).join('');
}

// Side-by-side OpenSSL core packages
function renderOpenSSLPackageSpecs() {
  const container = document.getElementById('sidebar-package-spec');
  if (!container) return;

  const packages = appState.packages || [];
  if (packages.length === 0) {
    container.innerHTML = `<span class="italic text-[var(--text-muted)] text-xs">No core packages identified.</span>`;
    return;
  }

  container.innerHTML = packages.map(pkg => `
    <div class="flex items-center justify-between py-2 text-xs border-b border-[var(--border-color)] last:border-b-0">
      <span class="text-[var(--text-primary)] font-semibold">${pkg.name}</span>
      <span class="font-mono text-[var(--text-secondary)] bg-[var(--bg-tertiary)] border border-[var(--border-color)] px-1.5 py-0.5 rounded">${pkg.version}</span>
    </div>
  `).join('');
}

// Interactive registry copy anchoring tags selector
export function renderRegistryArtifacts() {
  const container = document.getElementById('interactiveRegistryContainer');
  if (!container) return;

  const coreVersion = appState.core_version || '3.5.5';
  const repoName = appState.repo_name || 'wolfi-openssl-fips';
  const owner = appState.owner || 'taha2samy-3';
  const registry = appState.registry || 'ghcr.io';

  const items = [
    {
      id: 'distroless',
      name: 'Distroless Variant (Minimal, Non-Root)',
      tag: `${registry}/${owner}/${repoName}:${coreVersion}-distroless`,
      floating: `${registry}/${owner}/${repoName}:latest-distroless`,
      digest: appState.artifacts?.distroless?.provenance?.digest || appState.provenance?.distroless?.digest || 'sha256:1a2b3c4d5e6f7g8h9i0j',
      provenanceUrl: appState.artifacts?.distroless?.provenance?.url || '#',
      sbomUrl: appState.artifacts?.distroless?.sbom?.url || '#',
      badge: 'badge-success',
      badgeText: 'FIPS Standard'
    },
    {
      id: 'standard',
      name: 'Standard Variant (Alpine-compatible, Busybox)',
      tag: `${registry}/${owner}/${repoName}:${coreVersion}`,
      floating: `${registry}/${owner}/${repoName}:latest`,
      digest: appState.artifacts?.standard?.provenance?.digest || appState.provenance?.standard?.digest || 'sha256:a1b2c3d4e5f6g7h8i9j0',
      provenanceUrl: appState.artifacts?.standard?.provenance?.url || '#',
      sbomUrl: appState.artifacts?.standard?.sbom?.url || '#',
      badge: 'badge-indigo',
      badgeText: 'Interactive Shell'
    },
    {
      id: 'development',
      name: 'Development Core SDK Variant',
      tag: `${registry}/${owner}/${repoName}:${coreVersion}-dev`,
      floating: `${registry}/${owner}/${repoName}:dev`,
      digest: appState.artifacts?.development?.provenance?.digest || appState.provenance?.development?.digest || 'sha256:f1e2d3c4b5a609876543',
      provenanceUrl: appState.artifacts?.development?.provenance?.url || '#',
      sbomUrl: appState.artifacts?.development?.sbom?.url || '#',
      badge: 'badge-accent',
      badgeText: 'Full Compiler Sandbox'
    }
  ];

  container.innerHTML = '';
  items.forEach(item => {
    let copyText = '';
    let displayLabel = '';
    if (currentPullSelectionType === 'tag') {
      copyText = `docker pull ${item.tag}`;
      displayLabel = `Tag: ${coreVersion}`;
    } else if (currentPullSelectionType === 'floating') {
      copyText = `docker pull ${item.floating}`;
      displayLabel = 'Tag: latest';
    } else {
      copyText = `docker pull ${registry}/${owner}/${repoName}@${item.digest}`;
      displayLabel = item.digest.substring(0, 18) + '...';
    }

    const card = document.createElement('div');
    card.className = 'border border-[var(--border-color)] p-5 rounded-xl bg-[var(--bg-secondary)] space-y-4';
    card.innerHTML = `
      <div class="flex items-center justify-between flex-wrap gap-2">
        <h4 class="text-xs font-semibold text-[var(--text-primary)] flex items-center gap-2">
          ${item.name}
          <span class="badge ${item.badge} text-[9px] py-0 px-1.5 font-bold">${item.badgeText}</span>
        </h4>
        <span class="text-[10px] text-[var(--text-muted)] font-mono">${displayLabel}</span>
      </div>
      
      <div class="flex items-center justify-between gap-3 bg-[var(--bg-primary)] p-2.5 rounded-lg border border-[var(--border-color)] font-mono text-[10.5px]">
        <span class="text-[var(--text-secondary)] select-all truncate">${copyText}</span>
        <button class="copy-btn py-1 px-2 text-[9.5px]" onclick="copyToClipboard('${copyText}', this)">Copy</button>
      </div>

      <div class="flex flex-wrap gap-3 pt-1">
        <button class="flex items-center gap-1.5 py-1 px-2.5 rounded bg-[var(--bg-primary)] border border-[var(--border-color)] text-[10.5px] text-[var(--text-secondary)] font-semibold font-mono hover:bg-[var(--bg-tertiary)] transition-colors cursor-pointer" onclick="copyToClipboard('${item.digest}', this)">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"/></svg>
          Digest: ${item.digest.substring(0, 12)}...
        </button>
        
        <a href="${item.provenanceUrl}" target="_blank" class="flex items-center gap-1.5 py-1 px-2.5 rounded bg-indigo-600/10 border border-indigo-500/30 text-[10.5px] text-indigo-400 font-semibold hover:bg-indigo-600/20 transition-colors">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
          SLSA L3 Provenance
        </a>

        <a href="${item.sbomUrl}" target="_blank" class="flex items-center gap-1.5 py-1 px-2.5 rounded bg-emerald-600/10 border border-emerald-500/30 text-[10.5px] text-emerald-400 font-semibold hover:bg-emerald-600/20 transition-colors">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
          CycloneDX SBOM
        </a>
      </div>
    `;
    container.appendChild(card);
  });
}

// Global copy trigger
window.copyToClipboard = function(text, btn) {
  navigator.clipboard.writeText(text).then(() => {
    const originalText = btn.textContent;
    btn.textContent = 'Copied!';
    btn.classList.add('bg-[var(--color-success-bg)]', 'text-[var(--color-success)]', 'border-[var(--color-success)]');
    setTimeout(() => {
      btn.textContent = originalText;
      btn.classList.remove('bg-[var(--color-success-bg)]', 'text-[var(--color-success)]', 'border-[var(--color-success)]');
    }, 1500);
  });
};

// Setup registry toggle selection buttons
function setupPullTypeSelectors() {
  const buttons = document.querySelectorAll('.pull-type-btn');
  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('bg-indigo-600', 'text-white'));
      buttons.forEach(b => b.classList.add('bg-[var(--bg-tertiary)]', 'text-[var(--text-secondary)]'));

      btn.classList.remove('bg-[var(--bg-tertiary)]', 'text-[var(--text-secondary)]');
      btn.classList.add('bg-indigo-600', 'text-white');

      currentPullSelectionType = btn.getAttribute('data-type');
      renderRegistryArtifacts();
    });
  });
}

// Handle layout tab switcher elements
function initTabs() {
  const tabButtons = document.querySelectorAll('.dashboard-tab-btn');
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      tabButtons.forEach(b => b.classList.remove('active', 'text-[var(--color-indigo)]', 'font-semibold'));
      tabButtons.forEach(b => b.classList.add('text-[var(--text-secondary)]'));

      btn.classList.add('active', 'text-[var(--color-indigo)]', 'font-semibold');
      btn.classList.remove('text-[var(--text-secondary)]');

      const targetTab = btn.getAttribute('data-tab');
      const allTabs = document.querySelectorAll('.tab-content-panel');
      allTabs.forEach(panel => {
        panel.classList.add('hidden');
      });

      const activePanel = document.getElementById(`tab-panel-${targetTab}`);
      if (activePanel) {
        activePanel.classList.remove('hidden');
      }
    });
  });
}

// Entrypoint fetcher
async function bootstrapDashboard() {
  try {
    const response = await fetch('data.json');
    if (!response.ok) {
      throw new Error(`HTTP fetch error! Status code: ${response.status}`);
    }
    const rawData = await response.json();
    appState = sanitizeDashboardData(rawData);
    window.globalDashboardState = appState; // Share globally for helper methods

    // 1. Theme Engine & Scorecards
    initThemeEngine();
    renderBaseScorecards();
    renderSystemBaseSpec();
    renderOpenSSLPackageSpecs();

    // 2. Load Charts
    renderAESChart(appState);
    renderHashChart(appState);
    renderAsymmetricChart(appState);

    // 3. Load Security Tables & Hardening Checklists
    initVulnerabilityInspector(appState);
    renderHardeningScorecard(appState);
    renderKicsSecurityViewer(appState);

    // 4. Load Pytest Forensics
    initTestsSuiteViewer(appState);

    // 5. Load Registry pull command selector
    renderRegistryArtifacts();
    setupPullTypeSelectors();

    // 6. Resilience and Fallback checks for empty/corrupted/missing telemetry
    checkAndRenderFeatureFallbacks(appState);

  } catch (err) {
    console.error('Failed to parse data.json payload:', err);
    renderErrorFallback(err);
  }
}

function renderErrorFallback(err) {
  const container = document.getElementById('tab-panel-overview');
  if (container) {
    container.innerHTML = `
      <div class="p-8 bg-red-500/10 border border-red-500/30 rounded-xl max-w-2xl mx-auto text-center space-y-3">
        <svg class="w-12 h-12 text-red-500 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
        </svg>
        <h3 class="text-base font-bold text-[var(--text-primary)]">System Aggregator Parse Failure</h3>
        <p class="text-xs text-[var(--text-secondary)]">We couldn't retrieve or parse web/data.json file. Make sure the Node data build process completed successfully.</p>
        <pre class="bg-black/40 text-left p-3 rounded-lg text-[10px] text-red-400 font-mono overflow-x-auto">${err.stack || err.message}</pre>
      </div>
    `;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  initTabs();
  bootstrapDashboard();
});
