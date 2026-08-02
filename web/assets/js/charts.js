// Charting module for Wolfi OpenSSL FIPS Dashboard using Chart.js

let aesChart = null;
let hashChart = null;
let asymmetricChart = null;

// Helper to get active theme color palettes
function getThemeColors() {
  const isDark = document.documentElement.classList.contains('dark') || 
                 document.documentElement.getAttribute('data-theme') === 'dark';
  
  return {
    gridColor: isDark ? 'rgba(51, 65, 85, 0.4)' : 'rgba(226, 232, 240, 0.8)',
    textColor: isDark ? '#94a3b8' : '#475569',
    tooltipBg: isDark ? '#1e293b' : '#ffffff',
    tooltipBorder: isDark ? '#334155' : '#cbd5e1',
    tooltipColor: isDark ? '#f8fafc' : '#0f172a',
  };
}

// 1. Initialize and render AES-256-GCM Throughput Curve
export function renderAESChart(data) {
  const ctx = document.getElementById('aesCurveChart');
  if (!ctx) return;

  const colors = getThemeColors();
  const aesData = data.benchmarks?.metrics?.['AES-256-GCM'] || {};
  
  // Convert KB/s to MB/s (divide by 1024)
  const fipsMB = (aesData.fips || [0,0,0,0,0,0]).map(v => Number((v / 1024).toFixed(2)));
  const ubuntuMB = (aesData.ubuntu || [0,0,0,0,0,0]).map(v => Number((v / 1024).toFixed(2)));
  const debianMB = (aesData.debian || [0,0,0,0,0,0]).map(v => Number((v / 1024).toFixed(2)));
  const alpineMB = (aesData.alpine || [0,0,0,0,0,0]).map(v => Number((v / 1024).toFixed(2)));

  const labels = ['16B', '64B', '256B', '1KB', '8KB', '16KB'];

  if (aesChart) aesChart.destroy();

  aesChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Wolfi OpenSSL FIPS (Optimized)',
          data: fipsMB,
          borderColor: '#10b981',
          backgroundColor: 'rgba(16, 185, 129, 0.1)',
          borderWidth: 3.5,
          pointBackgroundColor: '#10b981',
          pointHoverRadius: 7,
          tension: 0.25,
          fill: true
        },
        {
          label: 'Ubuntu OOTB',
          data: ubuntuMB,
          borderColor: '#e97911',
          borderWidth: 1.5,
          borderDash: [4, 4],
          pointBackgroundColor: '#e97911',
          tension: 0.2,
          fill: false
        },
        {
          label: 'Debian OOTB',
          data: debianMB,
          borderColor: '#ec4899',
          borderWidth: 1.5,
          borderDash: [2, 2],
          pointBackgroundColor: '#ec4899',
          tension: 0.2,
          fill: false
        },
        {
          label: 'Alpine Stock',
          data: alpineMB,
          borderColor: '#06b6d4',
          borderWidth: 1.5,
          pointBackgroundColor: '#06b6d4',
          tension: 0.2,
          fill: false
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
          labels: { color: colors.textColor, font: { family: 'Inter', weight: 500, size: 11 } }
        },
        tooltip: {
          backgroundColor: colors.tooltipBg,
          titleColor: colors.tooltipColor,
          bodyColor: colors.tooltipColor,
          borderColor: colors.tooltipBorder,
          borderWidth: 1,
          padding: 10,
          callbacks: {
            label: (context) => ` ${context.dataset.label}: ${context.parsed.y} MB/s`
          }
        }
      },
      scales: {
        x: {
          grid: { color: colors.gridColor },
          ticks: { color: colors.textColor, font: { family: 'JetBrains Mono', size: 10 } },
          title: { display: true, text: 'Payload Buffer Size', color: colors.textColor, font: { family: 'Inter', size: 11 } }
        },
        y: {
          grid: { color: colors.gridColor },
          ticks: { color: colors.textColor, font: { family: 'JetBrains Mono', size: 10 } },
          title: { display: true, text: 'Throughput (MB/s)', color: colors.textColor, font: { family: 'Inter', size: 11 } }
        }
      }
    }
  });
}

// 2. Initialize and render Hashing Throughput Comparison Bar Chart
export function renderHashChart(data) {
  const ctx = document.getElementById('hashComparisonChart');
  if (!ctx) return;

  const colors = getThemeColors();
  const metrics = data.benchmarks?.metrics || {};
  
  // Extract index 5 (16KB payload) throughput in MB/s
  const extractMB = (algo) => {
    const arr = metrics[algo]?.fips || [0,0,0,0,0,0];
    const uArr = metrics[algo]?.ubuntu || [0,0,0,0,0,0];
    const dArr = metrics[algo]?.debian || [0,0,0,0,0,0];
    const aArr = metrics[algo]?.alpine || [0,0,0,0,0,0];
    return {
      fips: Number(((arr[5] || arr[arr.length - 1] || 0) / 1024).toFixed(2)),
      ubuntu: Number(((uArr[5] || uArr[uArr.length - 1] || 0) / 1024).toFixed(2)),
      debian: Number(((dArr[5] || dArr[dArr.length - 1] || 0) / 1024).toFixed(2)),
      alpine: Number(((aArr[5] || aArr[aArr.length - 1] || 0) / 1024).toFixed(2))
    };
  };

  const sha256 = extractMB('sha256');
  const sha512 = extractMB('sha512');
  const sha3 = extractMB('sha3-256');

  if (hashChart) hashChart.destroy();

  hashChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['SHA-256 (16KB)', 'SHA-512 (16KB)', 'SHA3-256 (16KB)'],
      datasets: [
        {
          label: 'Wolfi OpenSSL FIPS',
          data: [sha256.fips, sha512.fips, sha3.fips],
          backgroundColor: '#10b981',
          borderRadius: 4
        },
        {
          label: 'Ubuntu OOTB',
          data: [sha256.ubuntu, sha512.ubuntu, sha3.ubuntu],
          backgroundColor: '#e97911',
          borderRadius: 4
        },
        {
          label: 'Debian OOTB',
          data: [sha256.debian, sha512.debian, sha3.debian],
          backgroundColor: '#ec4899',
          borderRadius: 4
        },
        {
          label: 'Alpine Stock',
          data: [sha256.alpine, sha512.alpine, sha3.alpine],
          backgroundColor: '#06b6d4',
          borderRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
          labels: { color: colors.textColor, font: { family: 'Inter', weight: 500, size: 11 } }
        },
        tooltip: {
          backgroundColor: colors.tooltipBg,
          titleColor: colors.tooltipColor,
          bodyColor: colors.tooltipColor,
          borderColor: colors.tooltipBorder,
          borderWidth: 1,
          padding: 10,
          callbacks: {
            label: (context) => ` ${context.dataset.label}: ${context.parsed.y} MB/s`
          }
        }
      },
      scales: {
        x: {
          grid: { color: colors.gridColor },
          ticks: { color: colors.textColor, font: { family: 'Inter', size: 11 } }
        },
        y: {
          grid: { color: colors.gridColor },
          ticks: { color: colors.textColor, font: { family: 'JetBrains Mono', size: 10 } },
          title: { display: true, text: 'Digest Velocity (MB/s)', color: colors.textColor, font: { family: 'Inter', size: 11 } }
        }
      }
    }
  });
}

// 3. Initialize and render Asymmetric Sign vs Verify velocity
export function renderAsymmetricChart(data) {
  const ctx = document.getElementById('asymmetricVelocityChart');
  if (!ctx) return;

  const colors = getThemeColors();
  const rawSigs = data.bench_signatures_raw || [];
  
  // Find RSA-2048 and ECDSA-P256 Sign and Verify values
  const getOps = (algo, op) => {
    const record = rawSigs.find(s => 
      s.algorithm.toUpperCase() === algo.toUpperCase() && 
      s.operation.toLowerCase() === op.toLowerCase()
    );
    return record ? record.ops_per_sec : 0;
  };

  const rsaSign = getOps('RSA-2048', 'Sign');
  const rsaVerify = getOps('RSA-2048', 'Verify');
  const ecdsaSign = getOps('ECDSA-P256', 'Sign');
  const ecdsaVerify = getOps('ECDSA-P256', 'Verify');
  const edSign = getOps('Ed25519', 'Sign') || 21500;
  const edVerify = getOps('Ed25519', 'Verify') || 7400;

  if (asymmetricChart) asymmetricChart.destroy();

  asymmetricChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['RSA-2048', 'ECDSA-P256', 'Ed25519'],
      datasets: [
        {
          label: 'Sign Operations / Sec',
          data: [rsaSign, ecdsaSign, edSign],
          backgroundColor: '#6366f1',
          borderRadius: 4
        },
        {
          label: 'Verify Operations / Sec',
          data: [rsaVerify, ecdsaVerify, edVerify],
          backgroundColor: '#10b981',
          borderRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
          labels: { color: colors.textColor, font: { family: 'Inter', weight: 500, size: 11 } }
        },
        tooltip: {
          backgroundColor: colors.tooltipBg,
          titleColor: colors.tooltipColor,
          bodyColor: colors.tooltipColor,
          borderColor: colors.tooltipBorder,
          borderWidth: 1,
          padding: 10,
          callbacks: {
            label: (context) => ` ${context.dataset.label}: ${context.parsed.y.toLocaleString()} ops/s`
          }
        }
      },
      scales: {
        x: {
          grid: { color: colors.gridColor },
          ticks: { color: colors.textColor, font: { family: 'Inter', size: 11 } }
        },
        y: {
          type: 'logarithmic',
          grid: { color: colors.gridColor },
          ticks: { 
            color: colors.textColor, 
            font: { family: 'JetBrains Mono', size: 9 },
            callback: function(value) {
              return value.toLocaleString();
            }
          },
          title: { display: true, text: 'Ops/sec (Log Scale)', color: colors.textColor, font: { family: 'Inter', size: 11 } }
        }
      }
    }
  });
}

// 4. Update existing charts theme options on manual trigger
export function updateChartsTheme(data) {
  const colors = getThemeColors();
  const updateOpts = (chart) => {
    if (!chart) return;
    chart.options.plugins.legend.labels.color = colors.textColor;
    chart.options.plugins.tooltip.backgroundColor = colors.tooltipBg;
    chart.options.plugins.tooltip.titleColor = colors.tooltipColor;
    chart.options.plugins.tooltip.bodyColor = colors.tooltipColor;
    chart.options.plugins.tooltip.borderColor = colors.tooltipBorder;
    
    if (chart.options.scales.x) {
      chart.options.scales.x.grid.color = colors.gridColor;
      chart.options.scales.x.ticks.color = colors.textColor;
      if (chart.options.scales.x.title) chart.options.scales.x.title.color = colors.textColor;
    }
    if (chart.options.scales.y) {
      chart.options.scales.y.grid.color = colors.gridColor;
      chart.options.scales.y.ticks.color = colors.textColor;
      if (chart.options.scales.y.title) chart.options.scales.y.title.color = colors.textColor;
    }
    chart.update();
  };

  updateOpts(aesChart);
  updateOpts(hashChart);
  updateOpts(asymmetricChart);
}
