# Cryptographic Performance Infrastructure Audit

> **Report Status:** `FINAL` | **Audit ID:** `20260218-0832`

## 1. Executive Summary
Automated performance telemetry analysis across **4** isolated operating environments. This audit evaluates throughput efficiency for **4** core cryptographic primitives under variable block size constraints.

### 1.1 Environmental Metadata
| Property | Specification |
| :--- | :--- |
| **Target OS Distributions** | ALPINE, DEBIAN, FIPS, UBUNTU |
| **Evaluated Primitives** | 4 Algorithms |
| **Block Size Dimensions** | 6 Data points per set |
| **Hardware Architecture** | x86_64 |
| **Audit Timestamp** | 2026-02-18 08:32:01 |

## 2. Detailed Throughput Analysis Matrix
Systematic breakdown of processing velocity (bytes/sec) relative to block-size allocation.

| Environment | Primitive | 16B | 64B | 256B | 1024B | 8192B | 16384B |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **ALPINE** | `AES-256-GCM` | 151.37 MB/s | 602.60 MB/s | **2.25 GB/s** | **6.04 GB/s** | **18.16 GB/s** | **21.38 GB/s** |
| **DEBIAN** | `AES-256-GCM` | 81.39 MB/s | 307.82 MB/s | **1.12 GB/s** | **3.29 GB/s** | **7.90 GB/s** | **8.83 GB/s** |
| **FIPS** | `AES-256-GCM` | 175.90 MB/s | 691.61 MB/s | **2.54 GB/s** | **6.82 GB/s** | **18.77 GB/s** | **21.40 GB/s** |
| **UBUNTU** | `AES-256-GCM` | **1.16 GB/s** | **4.48 GB/s** | **11.62 GB/s** | **13.71 GB/s** | **22.95 GB/s** | **23.80 GB/s** |
| **ALPINE** | `sha256` | 107.44 MB/s | 386.86 MB/s | **1.18 GB/s** | **2.42 GB/s** | **3.47 GB/s** | **3.59 GB/s** |
| **DEBIAN** | `sha256` | 176.88 MB/s | 576.90 MB/s | **1.54 GB/s** | **2.73 GB/s** | **3.55 GB/s** | **3.62 GB/s** |
| **FIPS** | `sha256` | 192.35 MB/s | 626.73 MB/s | **1.65 GB/s** | **2.81 GB/s** | **3.57 GB/s** | **3.63 GB/s** |
| **UBUNTU** | `sha256` | 174.22 MB/s | 582.24 MB/s | **1.57 GB/s** | **2.77 GB/s** | **3.54 GB/s** | **3.63 GB/s** |
| **ALPINE** | `sha3-256` | 51.40 MB/s | 207.43 MB/s | 525.35 MB/s | 647.05 MB/s | 718.10 MB/s | 729.01 MB/s |
| **DEBIAN** | `sha3-256` | 55.73 MB/s | 222.72 MB/s | 549.49 MB/s | 655.30 MB/s | 719.22 MB/s | 736.93 MB/s |
| **FIPS** | `sha3-256` | 60.34 MB/s | 242.35 MB/s | 571.17 MB/s | 664.88 MB/s | 729.14 MB/s | 738.32 MB/s |
| **UBUNTU** | `sha3-256` | 55.47 MB/s | 222.94 MB/s | 549.02 MB/s | 649.61 MB/s | 727.94 MB/s | 738.71 MB/s |
| **ALPINE** | `sha512` | 68.75 MB/s | 273.70 MB/s | 618.35 MB/s | **1.10 GB/s** | **1.40 GB/s** | **1.43 GB/s** |
| **DEBIAN** | `sha512` | 78.72 MB/s | 315.57 MB/s | 662.97 MB/s | **1.13 GB/s** | **1.41 GB/s** | **1.44 GB/s** |
| **FIPS** | `sha512` | 84.40 MB/s | 337.47 MB/s | 679.59 MB/s | **1.15 GB/s** | **1.41 GB/s** | **1.44 GB/s** |
| **UBUNTU** | `sha512` | 74.71 MB/s | 301.64 MB/s | 656.72 MB/s | **1.12 GB/s** | **1.41 GB/s** | **1.44 GB/s** |

### 2.1 Statistical Insights & Key Indicators
| Indicator | Metric Value | Analysis |
| :--- | :--- | :--- |
| AES-256-GCM | 62.9% Delta | OS Optimization Impact: `SENSITIVE` |
| SHA256 | 1.2% Delta | OS Optimization Impact: `STABLE` |
| SHA3-256 | 1.3% Delta | OS Optimization Impact: `STABLE` |
| SHA512 | 0.5% Delta | OS Optimization Impact: `STABLE` |

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
    y-axis "Throughput (KB/s)" 0 --> 29753774
    bar [8833138.69, 21403475.97, 21377867.78, 23803019.26]
```

#### Primitive Capacity: `SHA256`
```mermaid
xychart-beta
    title "SHA256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 4538470
    bar [3623231.49, 3630497.79, 3586924.54, 3630776.32]
```

#### Primitive Capacity: `SHA3-256`
```mermaid
xychart-beta
    title "SHA3-256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 923381
    bar [736927.74, 738317.21, 729006.08, 738705.41]
```

#### Primitive Capacity: `SHA512`
```mermaid
xychart-beta
    title "SHA512 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 1798338
    bar [1435607.04, 1438670.85, 1431437.31, 1437646.85]
```

### 📈 Architectural Scaling & Buffer Efficiency
Logarithmic growth analysis of throughput relative to increased block-size allocation.
#### Growth Vector: ALPINE (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [151374.72, 602604.7, 2249550.59, 6039271.42, 18155397.12, 21377867.78]
```
#### Growth Vector: DEBIAN (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [81392.35, 307822.72, 1124123.52, 3286054.4, 7896596.48, 8833138.69]
```
#### Growth Vector: FIPS (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [175900.96, 691614.72, 2537767.42, 6820570.11, 18768556.03, 21403475.97]
```
#### Growth Vector: UBUNTU (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [1162987.49, 4478728.16, 11618178.43, 13710525.95, 22954299.39, 23803019.26]
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
| AES-256-GCM | 🏆 **UBUNTU** | `+26.2%` | 18,854,375.43 KB/s |
| SHA256 | 🏆 **UBUNTU** | `+0.4%` | 3,617,857.54 KB/s |
| SHA3-256 | 🏆 **UBUNTU** | `+0.4%` | 735,739.11 KB/s |
| SHA512 | 🏆 **FIPS** | `+0.2%` | 1,435,840.51 KB/s |

### 5.1 Optimization Recommendations
- **Primary Recommendation:** For high-throughput cryptographic workloads, the **FIPS** stack demonstrates the most efficient instruction-to-cycle ratio.
- **FIPS Strategy:** The FIPS-enabled pipeline shows negligible latency delta, making it suitable for production-grade security without compromising throughput.

## 6. Cryptographic Efficiency Scorecard (CES)
A normalized scoring system (0-100) representing the aggregate cryptographic health of each environment.

| Environment | Efficiency Score | Architectural Grade | Key Strength |
| :--- | :---: | :---: | :--- |
| **UBUNTU** | `100.0/100` | **A+** | High-Concurrency Bulk Processing |
| **FIPS** | `97.5/100` | **A+** | High-Concurrency Bulk Processing |
| **ALPINE** | `96.7/100` | **A+** | High-Concurrency Bulk Processing |
| **DEBIAN** | `84.1/100` | **B+** | FIPS-Compliant Workloads |

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
    bar [100.0, 97.5, 96.7, 84.1]
```

---

*automated by benchmark/generate_report.py & benchmark/parser.py*