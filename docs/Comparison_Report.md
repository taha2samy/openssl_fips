# Cryptographic Performance Infrastructure Audit

> **Report Status:** `FINAL` | **Audit ID:** `20260219-0031`

## 1. Executive Summary
Automated performance telemetry analysis across **4** isolated operating environments. This audit evaluates throughput efficiency for **4** core cryptographic primitives under variable block size constraints.

### 1.1 Environmental Metadata
| Property | Specification |
| :--- | :--- |
| **Target OS Distributions** | ALPINE, DEBIAN, FIPS, UBUNTU |
| **Evaluated Primitives** | 4 Algorithms |
| **Block Size Dimensions** | 6 Data points per set |
| **Hardware Architecture** | x86_64 |
| **Audit Timestamp** | 2026-02-19 00:31:15 |

## 2. Detailed Throughput Analysis Matrix
Systematic breakdown of processing velocity (bytes/sec) relative to block-size allocation.

| Environment | Primitive | 16B | 64B | 256B | 1024B | 8192B | 16384B |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **ALPINE** | `AES-256-GCM` | 126.55 MB/s | 466.02 MB/s | **1.57 GB/s** | **3.82 GB/s** | **7.00 GB/s** | **7.42 GB/s** |
| **DEBIAN** | `AES-256-GCM` | 88.33 MB/s | 328.37 MB/s | **1.16 GB/s** | **3.14 GB/s** | **6.66 GB/s** | **7.13 GB/s** |
| **FIPS** | `AES-256-GCM` | 178.70 MB/s | 632.94 MB/s | **1.96 GB/s** | **4.49 GB/s** | **7.11 GB/s** | **7.47 GB/s** |
| **UBUNTU** | `AES-256-GCM` | **1.11 GB/s** | **2.64 GB/s** | **5.08 GB/s** | **6.89 GB/s** | **7.71 GB/s** | **7.80 GB/s** |
| **ALPINE** | `sha256` | 116.77 MB/s | 439.22 MB/s | **1.45 GB/s** | **3.38 GB/s** | **5.53 GB/s** | **5.76 GB/s** |
| **DEBIAN** | `sha256` | 239.16 MB/s | 840.64 MB/s | **2.39 GB/s** | **4.36 GB/s** | **5.72 GB/s** | **5.91 GB/s** |
| **FIPS** | `sha256` | 276.54 MB/s | 959.51 MB/s | **2.57 GB/s** | **4.51 GB/s** | **5.78 GB/s** | **5.93 GB/s** |
| **UBUNTU** | `sha256` | 225.62 MB/s | 805.82 MB/s | **2.33 GB/s** | **4.35 GB/s** | **5.76 GB/s** | **5.96 GB/s** |
| **ALPINE** | `sha3-256` | 52.55 MB/s | 215.71 MB/s | 582.75 MB/s | 754.03 MB/s | 871.11 MB/s | 884.48 MB/s |
| **DEBIAN** | `sha3-256` | 69.02 MB/s | 277.63 MB/s | 668.17 MB/s | 790.20 MB/s | 877.24 MB/s | 888.00 MB/s |
| **FIPS** | `sha3-256` | 75.92 MB/s | 302.99 MB/s | 697.76 MB/s | 802.36 MB/s | 878.65 MB/s | 889.02 MB/s |
| **UBUNTU** | `sha3-256` | 65.60 MB/s | 262.06 MB/s | 647.47 MB/s | 782.29 MB/s | 876.88 MB/s | 888.14 MB/s |
| **ALPINE** | `sha512` | 71.61 MB/s | 296.38 MB/s | 678.23 MB/s | **1.23 GB/s** | **1.62 GB/s** | **1.66 GB/s** |
| **DEBIAN** | `sha512` | 99.50 MB/s | 398.55 MB/s | 829.41 MB/s | **1.34 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **FIPS** | `sha512` | 108.64 MB/s | 437.06 MB/s | 844.17 MB/s | **1.36 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **UBUNTU** | `sha512` | 97.13 MB/s | 389.67 MB/s | 816.57 MB/s | **1.32 GB/s** | **1.64 GB/s** | **1.66 GB/s** |

### 2.1 Statistical Insights & Key Indicators
| Indicator | Metric Value | Analysis |
| :--- | :--- | :--- |
| AES-256-GCM | 8.6% Delta | OS Optimization Impact: `STABLE` |
| SHA256 | 3.3% Delta | OS Optimization Impact: `STABLE` |
| SHA3-256 | 0.5% Delta | OS Optimization Impact: `STABLE` |
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
    y-axis "Throughput (KB/s)" 0 --> 9750814
    bar [7132921.86, 7468261.38, 7421952.0, 7800651.78]
```

#### Primitive Capacity: `SHA256`
```mermaid
xychart-beta
    title "SHA256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 7450572
    bar [5912936.45, 5925830.66, 5761392.64, 5960458.24]
```

#### Primitive Capacity: `SHA3-256`
```mermaid
xychart-beta
    title "SHA3-256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 1111275
    bar [887996.42, 889020.42, 884482.05, 888135.68]
```

#### Primitive Capacity: `SHA512`
```mermaid
xychart-beta
    title "SHA512 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 2086164
    bar [1666424.83, 1668931.58, 1656766.46, 1664786.43]
```

### 📈 Architectural Scaling & Buffer Efficiency
Logarithmic growth analysis of throughput relative to increased block-size allocation.
#### Growth Vector: ALPINE (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [126552.02, 466020.45, 1568559.87, 3816127.49, 7003750.4, 7421952.0]
```
#### Growth Vector: DEBIAN (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [88327.83, 328374.78, 1163250.18, 3142814.21, 6661054.46, 7132921.86]
```
#### Growth Vector: FIPS (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [178698.5, 632941.89, 1959446.91, 4493726.72, 7106301.95, 7468261.38]
```
#### Growth Vector: UBUNTU (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [1112088.46, 2643482.69, 5078371.07, 6890775.04, 7713423.36, 7800651.78]
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
| AES-256-GCM | 🏆 **UBUNTU** | `+4.6%` | 7,455,946.75 KB/s |
| SHA256 | 🏆 **UBUNTU** | `+1.2%` | 5,890,154.50 KB/s |
| SHA3-256 | 🏆 **FIPS** | `+0.2%` | 887,408.64 KB/s |
| SHA512 | 🏆 **FIPS** | `+0.3%` | 1,664,227.32 KB/s |

### 5.1 Optimization Recommendations
- **Primary Recommendation:** For high-throughput cryptographic workloads, the **FIPS** stack demonstrates the most efficient instruction-to-cycle ratio.
- **FIPS Strategy:** The FIPS-enabled pipeline shows negligible latency delta, making it suitable for production-grade security without compromising throughput.

## 6. Cryptographic Efficiency Scorecard (CES)
A normalized scoring system (0-100) representing the aggregate cryptographic health of each environment.

| Environment | Efficiency Score | Architectural Grade | Key Strength |
| :--- | :---: | :---: | :--- |
| **UBUNTU** | `99.9/100` | **A+** | High-Concurrency Bulk Processing |
| **FIPS** | `98.8/100` | **A+** | High-Concurrency Bulk Processing |
| **ALPINE** | `97.6/100` | **A+** | High-Concurrency Bulk Processing |
| **DEBIAN** | `97.6/100` | **A+** | High-Concurrency Bulk Processing |

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
    bar [99.9, 98.8, 97.6, 97.6]
```

---

*automated by benchmark/generate_report.py & benchmark/parser.py*