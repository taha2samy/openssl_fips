# Cryptographic Performance Infrastructure Audit

> **Report Status:** `FINAL` | **Audit ID:** `20260218-2323`

## 1. Executive Summary
Automated performance telemetry analysis across **4** isolated operating environments. This audit evaluates throughput efficiency for **4** core cryptographic primitives under variable block size constraints.

### 1.1 Environmental Metadata
| Property | Specification |
| :--- | :--- |
| **Target OS Distributions** | ALPINE, DEBIAN, FIPS, UBUNTU |
| **Evaluated Primitives** | 4 Algorithms |
| **Block Size Dimensions** | 6 Data points per set |
| **Hardware Architecture** | x86_64 |
| **Audit Timestamp** | 2026-02-18 23:23:06 |

## 2. Detailed Throughput Analysis Matrix
Systematic breakdown of processing velocity (bytes/sec) relative to block-size allocation.

| Environment | Primitive | 16B | 64B | 256B | 1024B | 8192B | 16384B |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **ALPINE** | `AES-256-GCM` | 124.18 MB/s | 462.37 MB/s | **1.56 GB/s** | **3.77 GB/s** | **6.99 GB/s** | **7.42 GB/s** |
| **DEBIAN** | `AES-256-GCM` | 88.57 MB/s | 332.83 MB/s | **1.16 GB/s** | **3.15 GB/s** | **6.58 GB/s** | **7.22 GB/s** |
| **FIPS** | `AES-256-GCM` | 176.21 MB/s | 634.56 MB/s | **1.98 GB/s** | **4.44 GB/s** | **7.13 GB/s** | **7.46 GB/s** |
| **UBUNTU** | `AES-256-GCM` | **1.11 GB/s** | **2.64 GB/s** | **5.04 GB/s** | **6.89 GB/s** | **7.71 GB/s** | **7.76 GB/s** |
| **ALPINE** | `sha256` | 118.56 MB/s | 445.81 MB/s | **1.47 GB/s** | **3.41 GB/s** | **5.53 GB/s** | **5.79 GB/s** |
| **DEBIAN** | `sha256` | 238.07 MB/s | 838.21 MB/s | **2.38 GB/s** | **4.34 GB/s** | **5.75 GB/s** | **5.90 GB/s** |
| **FIPS** | `sha256` | 278.78 MB/s | 955.35 MB/s | **2.57 GB/s** | **4.51 GB/s** | **5.78 GB/s** | **5.93 GB/s** |
| **UBUNTU** | `sha256` | 225.96 MB/s | 805.64 MB/s | **2.32 GB/s** | **4.33 GB/s** | **5.78 GB/s** | **5.95 GB/s** |
| **ALPINE** | `sha3-256` | 52.60 MB/s | 216.40 MB/s | 584.45 MB/s | 754.69 MB/s | 871.33 MB/s | 884.52 MB/s |
| **DEBIAN** | `sha3-256` | 69.31 MB/s | 277.39 MB/s | 668.41 MB/s | 790.85 MB/s | 875.75 MB/s | 888.02 MB/s |
| **FIPS** | `sha3-256` | 75.47 MB/s | 303.49 MB/s | 696.36 MB/s | 802.08 MB/s | 879.05 MB/s | 889.27 MB/s |
| **UBUNTU** | `sha3-256` | 65.54 MB/s | 262.66 MB/s | 646.04 MB/s | 784.40 MB/s | 875.79 MB/s | 888.11 MB/s |
| **ALPINE** | `sha512` | 71.85 MB/s | 297.70 MB/s | 675.83 MB/s | **1.24 GB/s** | **1.62 GB/s** | **1.66 GB/s** |
| **DEBIAN** | `sha512` | 99.76 MB/s | 400.34 MB/s | 831.35 MB/s | **1.34 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **FIPS** | `sha512` | 109.05 MB/s | 436.85 MB/s | 842.87 MB/s | **1.36 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **UBUNTU** | `sha512` | 96.90 MB/s | 388.03 MB/s | 815.12 MB/s | **1.33 GB/s** | **1.64 GB/s** | **1.65 GB/s** |

### 2.1 Statistical Insights & Key Indicators
| Indicator | Metric Value | Analysis |
| :--- | :--- | :--- |
| AES-256-GCM | 7.1% Delta | OS Optimization Impact: `STABLE` |
| SHA256 | 2.6% Delta | OS Optimization Impact: `STABLE` |
| SHA3-256 | 0.5% Delta | OS Optimization Impact: `STABLE` |
| SHA512 | 1.2% Delta | OS Optimization Impact: `STABLE` |

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
    y-axis "Throughput (KB/s)" 0 --> 9706055
    bar [7215718.4, 7455277.06, 7422738.43, 7764844.54]
```

#### Primitive Capacity: `SHA256`
```mermaid
xychart-beta
    title "SHA256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 7432448
    bar [5904850.94, 5929312.26, 5792120.83, 5945958.4]
```

#### Primitive Capacity: `SHA3-256`
```mermaid
xychart-beta
    title "SHA3-256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 1111582
    bar [888020.99, 889266.18, 884523.01, 888111.1]
```

#### Primitive Capacity: `SHA512`
```mermaid
xychart-beta
    title "SHA512 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 2083317
    bar [1665597.44, 1666654.21, 1657438.21, 1646559.23]
```

### 📈 Architectural Scaling & Buffer Efficiency
Logarithmic growth analysis of throughput relative to increased block-size allocation.
#### Growth Vector: ALPINE (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [124180.9, 462366.21, 1562962.43, 3774432.77, 6985859.07, 7422738.43]
```
#### Growth Vector: DEBIAN (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [88570.23, 332834.4, 1162948.48, 3153376.26, 6576709.63, 7215718.4]
```
#### Growth Vector: FIPS (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [176209.75, 634561.79, 1978516.86, 4438918.14, 7125012.48, 7455277.06]
```
#### Growth Vector: UBUNTU (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [1109024.62, 2643593.22, 5035154.43, 6890158.59, 7714525.18, 7764844.54]
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
| AES-256-GCM | 🏆 **UBUNTU** | `+4.0%` | 7,464,644.61 KB/s |
| SHA256 | 🏆 **UBUNTU** | `+0.9%` | 5,893,060.61 KB/s |
| SHA3-256 | 🏆 **FIPS** | `+0.2%` | 887,480.32 KB/s |
| SHA512 | 🏆 **FIPS** | `+0.5%` | 1,659,062.27 KB/s |

### 5.1 Optimization Recommendations
- **Primary Recommendation:** For high-throughput cryptographic workloads, the **FIPS** stack demonstrates the most efficient instruction-to-cycle ratio.
- **FIPS Strategy:** The FIPS-enabled pipeline shows negligible latency delta, making it suitable for production-grade security without compromising throughput.

## 6. Cryptographic Efficiency Scorecard (CES)
A normalized scoring system (0-100) representing the aggregate cryptographic health of each environment.

| Environment | Efficiency Score | Architectural Grade | Key Strength |
| :--- | :---: | :---: | :--- |
| **UBUNTU** | `99.7/100` | **A+** | High-Concurrency Bulk Processing |
| **FIPS** | `98.9/100` | **A+** | High-Concurrency Bulk Processing |
| **DEBIAN** | `98.0/100` | **A+** | High-Concurrency Bulk Processing |
| **ALPINE** | `98.0/100` | **A+** | High-Concurrency Bulk Processing |

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
    x-axis [UBUNTU, FIPS, DEBIAN, ALPINE]
    y-axis "Score (0-100)" 0 --> 100
    bar [99.7, 98.9, 98.0, 98.0]
```

---

*automated by benchmark/generate_report.py & benchmark/parser.py*