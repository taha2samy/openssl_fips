import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const ROOT_DIR = path.resolve(__dirname, '..');
const REPORTS_DIR = path.join(ROOT_DIR, 'reports');
const METADATA_DIR = path.join(ROOT_DIR, 'all-metadata');
const OUTPUT_FILE = path.join(__dirname, 'data.json');

// Helper to parse simple CSV into structured objects on-the-fly
function parseCSV(content) {
  if (!content) return [];
  const lines = content.split('\n').map(l => l.trim()).filter(l => l.length > 0);
  if (lines.length < 2) return [];

  // Helper to split a CSV line properly handling quoted values
  const splitLine = (line) => {
    const result = [];
    let current = '';
    let inQuotes = false;
    for (let i = 0; i < line.length; i++) {
      const char = line[i];
      if (char === '"') {
        inQuotes = !inQuotes;
      } else if (char === ',' && !inQuotes) {
        result.push(current.trim());
        current = '';
      } else {
        current += char;
      }
    }
    result.push(current.trim());
    return result;
  };

  const headers = splitLine(lines[0]);
  const result = [];

  for (let i = 1; i < lines.length; i++) {
    const row = splitLine(lines[i]);
    const obj = {};
    headers.forEach((h, index) => {
      let val = row[index] || '';
      // Remove enclosing quotes if any
      if (val.startsWith('"') && val.endsWith('"')) {
        val = val.substring(1, val.length - 1);
      }
      if (val !== '' && !isNaN(val)) {
        val = Number(val);
      }
      obj[h] = val;
    });
    result.push(obj);
  }
  return result;
}

// Helper to parse HCL and extract variable defaults
function parseHCL(content) {
  const result = {};
  // Match variable blocks: variable "NAME" { ... }
  const varRegex = /variable\s+"([^"]+)"\s*\{([^}]+)\}/gs;
  let match;
  while ((match = varRegex.exec(content)) !== null) {
    const varName = match[1];
    const blockContent = match[2];
    // Match default value which could be in quotes, e.g. default = "value"
    const defaultMatch = /default\s*=\s*(?:"([^"]+)"|'([^']+)'|([^\s}]+))/.exec(blockContent);
    if (defaultMatch) {
      const val = defaultMatch[1] || defaultMatch[2] || defaultMatch[3];
      result[varName] = val;
    }
  }
  return result;
}

// Helper to load JSON safely
function loadJSON(filePath) {
  if (!fs.existsSync(filePath)) {
    return null;
  }
  try {
    const raw = fs.readFileSync(filePath, 'utf-8');
    return JSON.parse(raw);
  } catch (err) {
    console.error(`Error parsing JSON from ${filePath}:`, err.message);
    return null;
  }
}

// Helper to extract Trivy CVE totals
function getVulnerabilityCounts(scan) {
  const counts = { critical: 0, high: 0, medium: 0, low: 0, total: 0 };
  if (!scan || !scan.Results) return counts;
  scan.Results.forEach(res => {
    if (res.Vulnerabilities) {
      res.Vulnerabilities.forEach(vuln => {
        counts.total++;
        const sev = (vuln.Severity || '').toLowerCase();
        if (counts[sev] !== undefined) {
          counts[sev]++;
        }
      });
    }
  });
  return counts;
}

// Main builder automation engine
function runAutomationPipeline() {
  const startTime = Date.now();
  console.log('\x1b[36m%s\x1b[0m', '🚀 Starting Wolfi OpenSSL FIPS Automated Build Pipeline...');

  // 1. Parse HCL variables dynamically from the root workspace
  let bakeVars = {};
  let versionVars = {};
  let parsedHclFiles = 0;

  const bakePath = path.join(ROOT_DIR, 'docker-bake.hcl');
  if (fs.existsSync(bakePath)) {
    bakeVars = parseHCL(fs.readFileSync(bakePath, 'utf-8'));
    parsedHclFiles++;
  }

  const versionsPath = path.join(ROOT_DIR, 'versions.hcl');
  if (fs.existsSync(versionsPath)) {
    versionVars = parseHCL(fs.readFileSync(versionsPath, 'utf-8'));
    parsedHclFiles++;
  }

  // 2. Extracted packages from versions.hcl
  const packages = Object.entries(versionVars)
    .filter(([key]) => key !== 'BASE_IMAGE' && key !== 'STATIC_IMAGE')
    .map(([key, value]) => ({
      name: key.replace('_VER', '').replace(/_/g, ' ').toLowerCase()
        .replace(/\b\w/g, c => c.toUpperCase()),
      version: value
    }));

  // Standard compliance and security template structure
  const compliance = {
    standard: {
      vulnerabilities: { total: 0, critical: 0, high: 0, medium: 0, low: 0 },
      raw_scan: { Results: [] },
      docker_cis: { SuccessCount: 0, FailCount: 0 },
      k8s_nsa: { SuccessCount: 0, FailCount: 0 },
      k8s_pss_restricted: { Summary: { SuccessCount: 0, FailCount: 0 } }
    },
    distroless: {
      vulnerabilities: { total: 0, critical: 0, high: 0, medium: 0, low: 0 },
      raw_scan: { Results: [] },
      docker_cis: { SuccessCount: 0, FailCount: 0 },
      k8s_nsa: { SuccessCount: 0, FailCount: 0 },
      k8s_pss_restricted: { Summary: { SuccessCount: 0, FailCount: 0 } }
    },
    development: {
      vulnerabilities: { total: 0, critical: 0, high: 0, medium: 0, low: 0 },
      raw_scan: { Results: [] },
      docker_cis: { SuccessCount: 0, FailCount: 0 },
      k8s_nsa: { SuccessCount: 0, FailCount: 0 },
      k8s_pss_restricted: { Summary: { SuccessCount: 0, FailCount: 0 } }
    }
  };

  const reports = {
    distroless: { summary: { passed: 0, failed: 0, duration: 0, total: 0 }, tests: [], environment: {} },
    standard: { summary: { passed: 0, failed: 0, duration: 0, total: 0 }, tests: [], environment: {} }
  };

  const provenance = {
    distroless: { digest: 'N/A', url: '#', sbom_url: '#' },
    standard: { digest: 'N/A', url: '#', sbom_url: '#' },
    development: { digest: 'N/A', url: '#', sbom_url: '#' }
  };

  let kicsReport = { total_results: 0, severity_counters: { HIGH: 0, MEDIUM: 0, LOW: 0, INFO: 0 }, queries: [] };
  let summaryReport = { summary: { statistic: { passed: 0, failed: 0, broken: 0, total: 0 } } };
  
  let rawBenchmarks = {
    metadata: { fips: { openssl_version: 'N/A' } },
    metrics: {}
  };

  let resultsCsv = [];
  let signaturesCsv = [];

  // Metrics fallbacks
  const expectedAlgorithms = ['AES-256-GCM', 'sha256', 'sha512', 'sha3-256'];
  expectedAlgorithms.forEach(algo => {
    rawBenchmarks.metrics[algo] = {
      fips: [0, 0, 0, 0, 0, 0],
      ubuntu: [0, 0, 0, 0, 0, 0],
      debian: [0, 0, 0, 0, 0, 0],
      alpine: [0, 0, 0, 0, 0, 0]
    };
  });

  // Automated Directory Crawling: reports/
  let discoveredFiles = [];
  let trivyScansCount = 0;
  let csvCount = 0;
  let pytestCount = 0;
  let iacCount = 0;
  let attestationCount = 0;

  if (fs.existsSync(REPORTS_DIR)) {
    try {
      const filesInReports = fs.readdirSync(REPORTS_DIR);
      filesInReports.forEach(filename => {
        const filePath = path.join(REPORTS_DIR, filename);
        discoveredFiles.push(filename);

        // A. Match Trivy Compliance and Security JSONs
        const trivyMatch = /^(standard|distroless|development)-(security-full|docker-cis_full|k8s-nsa_full|k8s-pss-restricted_full)\.json$/.exec(filename);
        if (trivyMatch) {
          const variant = trivyMatch[1];
          const scanType = trivyMatch[2];
          const jsonData = loadJSON(filePath);
          trivyScansCount++;

          if (jsonData) {
            if (scanType === 'security-full') {
              compliance[variant].raw_scan = jsonData;
              compliance[variant].vulnerabilities = getVulnerabilityCounts(jsonData);
            } else if (scanType === 'docker-cis_full') {
              compliance[variant].docker_cis = jsonData.Summary || jsonData;
            } else if (scanType === 'k8s-nsa_full') {
              compliance[variant].k8s_nsa = jsonData.Summary || jsonData;
            } else if (scanType === 'k8s-pss-restricted_full') {
              compliance[variant].k8s_pss_restricted = jsonData.Summary || jsonData;
            }
          }
          return;
        }

        // B. Match Attestation Details / Provenance
        const attestationMatch = /^(distroless|standard|development)_attestation_details\.json$/.exec(filename);
        if (attestationMatch) {
          const variant = attestationMatch[1];
          const jsonData = loadJSON(filePath);
          attestationCount++;
          if (jsonData) {
            provenance[variant] = {
              digest: jsonData.provenance?.digest || 'N/A',
              url: jsonData.provenance?.url || '#',
              sbom_url: jsonData.sbom?.url || '#'
            };
          }
          return;
        }

        // C. Match Pytest validation reports
        const pytestMatch = /^report_(distroless|standard)\.json$/.exec(filename);
        if (pytestMatch) {
          const variant = pytestMatch[1];
          const jsonData = loadJSON(filePath);
          pytestCount++;
          if (jsonData) {
            reports[variant] = jsonData;
          }
          return;
        }

        // D. Match KICS report
        if (filename === 'kics-report.json') {
          const jsonData = loadJSON(filePath);
          iacCount++;
          if (jsonData) {
            kicsReport = jsonData;
            // Map queries to a flattened findings array
            const findings = [];
            if (Array.isArray(jsonData.queries)) {
              jsonData.queries.forEach(query => {
                if (Array.isArray(query.files)) {
                  query.files.forEach(file => {
                    findings.push({
                      query_name: query.query_name,
                      query_id: query.query_id,
                      query_url: query.query_url,
                      severity: query.severity,
                      platform: query.platform,
                      category: query.category,
                      description: query.description,
                      file_name: file.file_name,
                      line: file.line,
                      actual_value: file.actual_value,
                      expected_value: file.expected_value
                    });
                  });
                }
              });
            }
            kicsReport.findings = findings;
            console.log(`[BUILD] ✔ Loaded KICS Report (${kicsReport.total_counter || 0} findings)`);
          }
          return;
        }

        // E. Match Benchmark Data JSON
        if (filename === 'benchmark_data.json') {
          const jsonData = loadJSON(filePath);
          if (jsonData) {
            rawBenchmarks = jsonData;
          }
          return;
        }

        // F. Match summary.json
        if (filename === 'summary.json') {
          const jsonData = loadJSON(filePath);
          if (jsonData) {
            summaryReport = jsonData;
          }
          return;
        }

        // G. Match Benchmark CSVs
        if (filename === 'results.csv') {
          resultsCsv = parseCSV(fs.readFileSync(filePath, 'utf-8'));
          csvCount++;
          return;
        }
        if (filename === 'signatures.csv') {
          signaturesCsv = parseCSV(fs.readFileSync(filePath, 'utf-8'));
          csvCount++;
          return;
        }
      });
    } catch (err) {
      console.error('⚠️ Error scanning reports directory:', err.message);
    }
  }

  // 4. Gather all-metadata folder content
  const allMetadataFiles = {};
  let metadataCount = 0;
  if (fs.existsSync(METADATA_DIR)) {
    try {
      const files = fs.readdirSync(METADATA_DIR);
      files.forEach(file => {
        if (file.endsWith('.json')) {
          const content = loadJSON(path.join(METADATA_DIR, file));
          if (content) {
            allMetadataFiles[path.basename(file, '.json')] = content;
            metadataCount++;
          }
        }
      });
    } catch (err) {
      console.error('⚠️ Error listing all-metadata files:', err.message);
    }
  }

  // Function to safely load metadata file
  function loadMetadata(filename) {
    const filePath = path.join(METADATA_DIR, filename);
    if (fs.existsSync(filePath)) {
      try {
        return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
      } catch (e) {
        console.warn(`[BUILD] Warning: Failed to parse ${filename}`);
      }
    }
    return {
      provenance: { digest: 'N/A', url: '#' },
      sbom: { url: '#' }
    };
  }

  // Build the standardized compiled schema
  const unifiedData = {
    project_name: process.env.PROJECT_NAME || 'Wolfi OpenSSL FIPS',
    owner: bakeVars.OWNER || 'taha2samy-3',
    repo_name: bakeVars.REPO_NAME || 'wolfi-openssl-fips',
    registry: bakeVars.REGISTRY || 'ghcr.io',
    core_version: bakeVars.CORE_VERSION || '3.5.5',
    fips_version: bakeVars.FIPS_VERSION || '3.1.2',
    base_image: versionVars.BASE_IMAGE || 'N/A',
    static_image: versionVars.STATIC_IMAGE || 'N/A',
    generation_date: process.env.GENERATION_DATE || new Date().toISOString().split('T')[0],
    
    // Map metadata into data.artifacts payload
    artifacts: {
      standard: loadMetadata('standard_attestation_details.json'),
      distroless: loadMetadata('distroless_attestation_details.json'),
      development: loadMetadata('development_attestation_details.json')
    },
    
    // System tests stats
    test_stats: summaryReport.summary?.statistic || { passed: 0, failed: 0, broken: 0, total: 0 },
    
    // Reports and functional test results
    reports: reports,

    // Security & Compliance findings
    security: {
      kics: kicsReport,
      compliance: compliance
    },
    kics_report: kicsReport,

    // Performance metrics
    benchmarks: rawBenchmarks,
    bench_results_raw: resultsCsv,
    bench_signatures_raw: signaturesCsv,

    // Metadata & Supply Chain
    provenance: provenance,
    
    // Extracted packages from versions.hcl
    packages: packages,

    // Embedded hardware context for CI runs
    hardware_context: {
      system: process.platform === 'win32' ? 'Windows' : process.platform === 'darwin' ? 'macOS' : 'Linux',
      release: 'Kernel Release',
      architecture: process.arch,
      cpu_cores: 4,
      ram_gb: 16,
      runner: process.env.CI ? 'GitHub Actions CI' : 'Local Runner'
    },

    // Metadata collection
    all_metadata: allMetadataFiles
  };

  // Write compiled output file to target
  fs.mkdirSync(path.dirname(OUTPUT_FILE), { recursive: true });
  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(unifiedData, null, 2), 'utf-8');

  // Print a clean, gorgeous build log summary
  const durationMs = Date.now() - startTime;
  console.log('\n\x1b[32m%s\x1b[0m', '───────────────────────────────────────────────────────────────────');
  console.log('\x1b[32m%s\x1b[0m', `✔ Compiled successfully in ${durationMs}ms`);
  console.log('\x1b[32m%s\x1b[0m', '───────────────────────────────────────────────────────────────────');
  console.log(`✔ Auto-discovered & parsed HCL variables:  ${parsedHclFiles} files`);
  console.log(`✔ Auto-discovered Trivy security scans:   ${trivyScansCount} scans`);
  console.log(`✔ Auto-discovered Pytest execution:       ${pytestCount} reports`);
  console.log(`✔ Auto-discovered IaC diagnostics:        ${iacCount} logs`);
  console.log(`✔ Auto-discovered Attestation sets:       ${attestationCount} bundles`);
  console.log(`✔ Auto-discovered Supply chain metadata:  ${metadataCount} items`);
  console.log(`✔ Parsed dynamic CSV benchmark tables:    ${csvCount} sheets`);
  console.log(`✔ Standardized and generated state file:  web/data.json`);
  console.log('\x1b[32m%s\x1b[0m', '───────────────────────────────────────────────────────────────────\n');
}

runAutomationPipeline();
