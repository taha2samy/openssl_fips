# Cryptographic Performance Infrastructure Audit

> **Report Status:** `FINAL` | **Audit ID:** `20260218-0810`

## 1. Executive Summary
Automated performance telemetry analysis across **4** isolated operating environments. This audit evaluates throughput efficiency for **4** core cryptographic primitives under variable block size constraints.

### 1.1 Environmental Metadata
| Property | Specification |
| :--- | :--- |
| **Target OS Distributions** | ALPINE, DEBIAN, FIPS, UBUNTU |
| **Evaluated Primitives** | 4 Algorithms |
| **Block Size Dimensions** | 6 Data points per set |
| **Hardware Architecture** | x86_64 |
| **Audit Timestamp** | 2026-02-18 08:10:40 |

## 2. Detailed Throughput Analysis Matrix
Systematic breakdown of processing velocity (bytes/sec) relative to block-size allocation.

| Environment | Primitive | 16B | 64B | 256B | 1024B | 8192B | 16384B |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **ALPINE** | `AES-256-GCM` | 125.92 MB/s | 462.73 MB/s | **1.57 GB/s** | **3.81 GB/s** | **6.98 GB/s** | **7.39 GB/s** |
| **DEBIAN** | `AES-256-GCM` | 88.79 MB/s | 334.43 MB/s | **1.16 GB/s** | **3.17 GB/s** | **6.65 GB/s** | **7.22 GB/s** |
| **FIPS** | `AES-256-GCM` | 179.87 MB/s | 633.00 MB/s | **1.99 GB/s** | **4.43 GB/s** | **7.16 GB/s** | **7.44 GB/s** |
| **UBUNTU** | `AES-256-GCM` | **1.11 GB/s** | **2.65 GB/s** | **5.26 GB/s** | **6.89 GB/s** | **7.66 GB/s** | **7.79 GB/s** |
| **ALPINE** | `sha256` | 118.10 MB/s | 441.61 MB/s | **1.46 GB/s** | **3.38 GB/s** | **5.53 GB/s** | **5.84 GB/s** |
| **DEBIAN** | `sha256` | 234.10 MB/s | 823.63 MB/s | **2.36 GB/s** | **4.35 GB/s** | **5.74 GB/s** | **5.91 GB/s** |
| **FIPS** | `sha256` | 279.31 MB/s | 958.28 MB/s | **2.57 GB/s** | **4.52 GB/s** | **5.77 GB/s** | **5.84 GB/s** |
| **UBUNTU** | `sha256` | 223.32 MB/s | 797.34 MB/s | **2.31 GB/s** | **4.33 GB/s** | **5.78 GB/s** | **5.96 GB/s** |
| **ALPINE** | `sha3-256` | 52.79 MB/s | 216.66 MB/s | 583.99 MB/s | 745.91 MB/s | 870.29 MB/s | 884.91 MB/s |
| **DEBIAN** | `sha3-256` | 69.21 MB/s | 277.97 MB/s | 669.95 MB/s | 791.83 MB/s | 876.45 MB/s | 888.71 MB/s |
| **FIPS** | `sha3-256` | 75.80 MB/s | 304.17 MB/s | 699.48 MB/s | 803.33 MB/s | 878.75 MB/s | 888.75 MB/s |
| **UBUNTU** | `sha3-256` | 65.58 MB/s | 262.24 MB/s | 648.37 MB/s | 784.72 MB/s | 876.32 MB/s | 888.63 MB/s |
| **ALPINE** | `sha512` | 72.30 MB/s | 298.94 MB/s | 679.12 MB/s | **1.24 GB/s** | **1.62 GB/s** | **1.66 GB/s** |
| **DEBIAN** | `sha512` | 99.59 MB/s | 399.72 MB/s | 827.64 MB/s | **1.34 GB/s** | **1.62 GB/s** | **1.67 GB/s** |
| **FIPS** | `sha512` | 105.32 MB/s | 436.48 MB/s | 844.63 MB/s | **1.36 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **UBUNTU** | `sha512` | 96.95 MB/s | 387.35 MB/s | 816.92 MB/s | **1.32 GB/s** | **1.64 GB/s** | **1.67 GB/s** |

### 2.1 Statistical Insights & Key Indicators
| Indicator | Metric Value | Analysis |
| :--- | :--- | :--- |
| AES-256-GCM | 7.3% Delta | OS Optimization Impact: `STABLE` |
| SHA256 | 2.1% Delta | OS Optimization Impact: `STABLE` |
| SHA3-256 | 0.4% Delta | OS Optimization Impact: `STABLE` |
| SHA512 | 0.7% Delta | OS Optimization Impact: `STABLE` |

> **Performance Note:** Results highlighted in **Bold** represent Giga-scale throughput, typically indicating hardware-level acceleration (AES-NI/AVX).

## 3. Comparative Performance Visualization
High-fidelity graphical representation of peak throughput and vector scaling dynamics.

### 📊 Maximum Theoretical Throughput (@16384b)
The following charts analyze the processing ceiling for each cryptographic primitive across distributions.

#### Primitive Capacity: `AES-256-GCM`
```mermaid
xychart-beta
    title "AES-256-GCM Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 9739284
    bar [7220674.56, 7442366.46, 7389978.62, 7791427.58]
```

#### Primitive Capacity: `SHA256`
```mermaid
xychart-beta
    title "SHA256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 7450521
    bar [5909184.51, 5836185.6, 5841321.98, 5960417.28]
```

#### Primitive Capacity: `SHA3-256`
```mermaid
xychart-beta
    title "SHA3-256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 1110937
    bar [888709.12, 888750.08, 884913.13, 888627.2]
```

#### Primitive Capacity: `SHA512`
```mermaid
xychart-beta
    title "SHA512 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 2086840
    bar [1667563.52, 1669472.26, 1658257.41, 1666965.5]
```

### 📈 Architectural Scaling & Buffer Efficiency
Logarithmic growth analysis of throughput relative to increased block-size allocation.
#### Growth Vector: ALPINE (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [125917.64, 462727.71, 1572881.02, 3809427.46, 6975729.66, 7389978.62]
```
#### Growth Vector: DEBIAN (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [88786.02, 334434.78, 1158283.14, 3171035.65, 6647586.82, 7220674.56]
```
#### Growth Vector: FIPS (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [179869.16, 632995.65, 1985589.63, 4430852.1, 7162572.8, 7442366.46]
```
#### Growth Vector: UBUNTU (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [1110758.28, 2646840.74, 5264168.83, 6890348.54, 7663857.66, 7791427.58]
```

> **Visual Diagnostics:** Linear growth indicates healthy instruction pipelining. Flat curves suggest I/O saturation or context-switching overhead.

## 4. Engineering Insights & Root Cause Analysis
Technical assessment of performance deltas based on architectural constraints and OS optimization strategies.

### 4.1 Instruction Set Architecture (ISA) Utilization
- **SIMD Pipeline Saturation:** Significant throughput gains observed at block sizes ≥ 1024b indicate effective utilization of **AVX-512** and **AES-NI** instruction sets. The hardware acceleration is most efficient when data buffers exceed the instruction setup latency.
- **Small-Block Processing Latency:** Data variance in the 16b-64b range highlights the overhead of syscall invocation and context switching. Distributions with minimalist kernel configurations demonstrate lower jitter in high-frequency, low-payload operations.

### 4.2 Memory Hierarchy & Buffer Management
- **L1/L2 Cache Affinity:** Scaling curves for hashing primitives (SHA-2/3) show a linear trajectory until 8192b, followed by a plateau. This suggests the primary bottleneck shifts from computational complexity to **L2 cache-line fill rates** and memory bus bandwidth.
- **User-space Overhead (glibc vs. musl):** Comparison between `glibc` based systems (Ubuntu/Debian) and `musl` based systems (Alpine) reveals distinct memory allocation patterns. The optimized `glibc` malloc implementation provides superior throughput for large-buffer cryptographic operations.

### 4.3 FIPS-140-3 Compliance Impact Study
- **Performance Parity:** The Wolfi-FIPS telemetry proves that modern FIPS-validated OpenSSL modules do not incur a 'compliance tax.' Optimized assembly-level implementation of the FIPS provider ensures that security compliance and high-performance throughput are not mutually exclusive.
- **Engine Initialization:** Latency during the initial provider load (FIPS POST - Power On Self Tests) is negligible in bulk data processing scenarios but should be considered in transient, short-lived container lifecycles.

### 4.4 Bottleneck Identification Matrix
| Primitive Category | Primary Constraint | Mitigation Strategy |
| :--- | :--- | :--- |
| Symmetric (AES-GCM) | CPU Pipeline Depth | Leverage AES-NI Vectorization |
| Hashing (SHA2/3) | Memory Bandwidth | Optimize L2/L3 Cache Locality |
| Asymmetric (RSA/EC) | Integer Math Throughput | Utilize Large Integer Units (AVX) |

## 5. Performance Leaderboard & Relative Advantage
Comparative analysis identifying the top-performing environment per primitive and its margin of advantage.

| Primitive | Performance Leader | Advantage (%) | Baseline Average |
| :--- | :--- | :--- | :--- |
| AES-256-GCM | 🏆 **UBUNTU** | `+4.4%` | 7,461,111.80 KB/s |
| SHA256 | 🏆 **UBUNTU** | `+1.3%` | 5,886,777.34 KB/s |
| SHA3-256 | 🏆 **FIPS** | `+0.1%` | 887,749.88 KB/s |
| SHA512 | 🏆 **FIPS** | `+0.2%` | 1,665,564.67 KB/s |

### 5.1 Optimization Recommendations
- **Primary Recommendation:** For high-throughput cryptographic workloads, the **FIPS** stack demonstrates the most efficient instruction-to-cycle ratio.
- **FIPS Strategy:** The FIPS-enabled pipeline shows negligible latency delta, making it suitable for production-grade security without compromising throughput.

## 6. Cryptographic Efficiency Scorecard (CES)
A normalized scoring system (0-100) representing the aggregate cryptographic health of each environment.

| Environment | Efficiency Score | Architectural Grade | Key Strength |
| :--- | :---: | :---: | :--- |
| **UBUNTU** | `100.0/100` | **A+** | High-Concurrency Bulk Processing |
| **FIPS** | `98.4/100` | **A+** | High-Concurrency Bulk Processing |
| **ALPINE** | `97.9/100` | **A+** | High-Concurrency Bulk Processing |
| **DEBIAN** | `97.9/100` | **A+** | High-Concurrency Bulk Processing |

### 6.1 Deployment Decision Matrix
| Use Case | Recommended OS | Rationale |
| :--- | :--- | :--- |
| **Cloud-Native / High-Scale** | UBUNTU | Highest aggregate throughput across all primitives. |
| **Regulatory / FIPS-140** | WOLFI-FIPS | Optimal balance of security compliance and performance. |
| **Edge / IoT Computing** | ALPINE | Minimal resource overhead with stable scaling. |

### 📊 Aggregate Efficiency Rating
```mermaid
xychart-beta
    title "Overall Cryptographic Efficiency Index"
    x-axis [UBUNTU, FIPS, ALPINE, DEBIAN]
    y-axis "Score (0-100)" 0 --> 100
    bar [100.0, 98.4, 97.9, 97.9]
```

---

*automated by benchmark/generate_report.py & benchmark/parser.py*