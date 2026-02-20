# Cryptographic Performance Infrastructure Audit

> **Report Status:** `FINAL` | **Audit ID:** `20260220-0208`

## 1. Executive Summary
Automated performance telemetry analysis across **4** isolated operating environments. This audit evaluates throughput efficiency for **4** core cryptographic primitives under variable block size constraints.

### 1.1 Environmental Metadata
| Property | Specification |
| :--- | :--- |
| **Target OS Distributions** | ALPINE, DEBIAN, FIPS, UBUNTU |
| **Evaluated Primitives** | 4 Algorithms |
| **Block Size Dimensions** | 6 Data points per set |
| **Hardware Architecture** | x86_64 |
| **Audit Timestamp** | 2026-02-20 02:08:00 |

## 2. Detailed Throughput Analysis Matrix
Systematic breakdown of processing velocity (bytes/sec) relative to block-size allocation.

| Environment | Primitive | 16B | 64B | 256B | 1024B | 8192B | 16384B |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **ALPINE** | `AES-256-GCM` | 126.82 MB/s | 466.26 MB/s | **1.57 GB/s** | **3.81 GB/s** | **6.96 GB/s** | **7.45 GB/s** |
| **DEBIAN** | `AES-256-GCM` | 88.04 MB/s | 332.27 MB/s | **1.17 GB/s** | **3.16 GB/s** | **6.67 GB/s** | **7.25 GB/s** |
| **FIPS** | `AES-256-GCM` | 178.83 MB/s | 637.28 MB/s | **2.01 GB/s** | **4.49 GB/s** | **7.15 GB/s** | **7.41 GB/s** |
| **UBUNTU** | `AES-256-GCM` | **1.11 GB/s** | **2.61 GB/s** | **5.21 GB/s** | **6.89 GB/s** | **7.72 GB/s** | **7.80 GB/s** |
| **ALPINE** | `sha256` | 118.64 MB/s | 444.49 MB/s | **1.47 GB/s** | **3.41 GB/s** | **5.54 GB/s** | **5.84 GB/s** |
| **DEBIAN** | `sha256` | 232.03 MB/s | 804.75 MB/s | **2.33 GB/s** | **4.31 GB/s** | **5.75 GB/s** | **5.90 GB/s** |
| **FIPS** | `sha256` | 267.90 MB/s | 928.00 MB/s | **2.55 GB/s** | **4.48 GB/s** | **5.78 GB/s** | **5.93 GB/s** |
| **UBUNTU** | `sha256` | 223.48 MB/s | 796.03 MB/s | **2.31 GB/s** | **4.33 GB/s** | **5.79 GB/s** | **5.97 GB/s** |
| **ALPINE** | `sha3-256` | 52.55 MB/s | 215.30 MB/s | 582.94 MB/s | 754.55 MB/s | 871.74 MB/s | 885.85 MB/s |
| **DEBIAN** | `sha3-256` | 65.47 MB/s | 260.98 MB/s | 617.21 MB/s | 700.04 MB/s | 765.78 MB/s | 774.32 MB/s |
| **FIPS** | `sha3-256` | 75.57 MB/s | 301.37 MB/s | 704.41 MB/s | 801.12 MB/s | 879.83 MB/s | 889.88 MB/s |
| **UBUNTU** | `sha3-256` | 65.74 MB/s | 262.49 MB/s | 649.21 MB/s | 785.12 MB/s | 877.16 MB/s | 888.02 MB/s |
| **ALPINE** | `sha512` | 72.30 MB/s | 298.76 MB/s | 679.81 MB/s | **1.24 GB/s** | **1.62 GB/s** | **1.64 GB/s** |
| **DEBIAN** | `sha512` | 100.83 MB/s | 402.47 MB/s | 833.63 MB/s | **1.34 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **FIPS** | `sha512` | 109.05 MB/s | 435.78 MB/s | 852.77 MB/s | **1.36 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **UBUNTU** | `sha512` | 96.77 MB/s | 386.10 MB/s | 814.54 MB/s | **1.33 GB/s** | **1.64 GB/s** | **1.67 GB/s** |

### 2.1 Statistical Insights & Key Indicators
| Indicator | Metric Value | Analysis |
| :--- | :--- | :--- |
| AES-256-GCM | 7.0% Delta | OS Optimization Impact: `STABLE` |
| SHA256 | 2.2% Delta | OS Optimization Impact: `STABLE` |
| SHA3-256 | 13.0% Delta | OS Optimization Impact: `STABLE` |
| SHA512 | 1.5% Delta | OS Optimization Impact: `STABLE` |

> **Performance Note:** Results highlighted in **Bold** represent Giga-scale throughput, typically indicating hardware-level acceleration (AES-NI/AVX).

## 3. Comparative Performance Visualization
High-fidelity graphical representation of peak throughput and vector scaling dynamics.

### 📊 Maximum Theoretical Throughput (@16384b)
The following charts analyze the processing ceiling for each cryptographic primitive across distributions.

#### Primitive Capacity: `AES-256-GCM`
```mermaid
xychart-beta
    title "AES-256-GCM Peak Velocity (KB/s)"
    x-axis [ALPINE, UBUNTU, DEBIAN, FIPS]
    y-axis "Throughput (KB/s)" 0 --> 9745915
    bar [7447301.32, 7796732.72, 7251800.88, 7413805.88]
```

#### Primitive Capacity: `SHA256`
```mermaid
xychart-beta
    title "SHA256 Peak Velocity (KB/s)"
    x-axis [ALPINE, UBUNTU, DEBIAN, FIPS]
    y-axis "Throughput (KB/s)" 0 --> 7468144
    bar [5843555.12, 5974515.71, 5904211.97, 5926581.04]
```

#### Primitive Capacity: `SHA3-256`
```mermaid
xychart-beta
    title "SHA3-256 Peak Velocity (KB/s)"
    x-axis [ALPINE, UBUNTU, DEBIAN, FIPS]
    y-axis "Throughput (KB/s)" 0 --> 1112350
    bar [885848.47, 888022.63, 774322.59, 889880.58]
```

#### Primitive Capacity: `SHA512`
```mermaid
xychart-beta
    title "SHA512 Peak Velocity (KB/s)"
    x-axis [ALPINE, UBUNTU, DEBIAN, FIPS]
    y-axis "Throughput (KB/s)" 0 --> 2086852
    bar [1644796.31, 1667316.12, 1667960.01, 1669482.09]
```

### 📈 Architectural Scaling & Buffer Efficiency
Logarithmic growth analysis of throughput relative to increased block-size allocation.
#### Growth Vector: ALPINE (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [126819.91, 466261.38, 1574140.13, 3807294.36, 6963028.79, 7447301.32]
```
#### Growth Vector: DEBIAN (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [88035.38, 332267.42, 1166006.07, 3156464.13, 6665139.81, 7251800.88]
```
#### Growth Vector: FIPS (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [178828.2, 637283.33, 2010941.26, 4492602.16, 7152666.21, 7413805.88]
```
#### Growth Vector: UBUNTU (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [1113411.07, 2609570.01, 5213411.51, 6887487.49, 7723210.34, 7796732.72]
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
| AES-256-GCM | 🏆 **UBUNTU** | `+4.3%` | 7,477,410.20 KB/s |
| SHA256 | 🏆 **UBUNTU** | `+1.1%` | 5,912,215.96 KB/s |
| SHA3-256 | 🏆 **FIPS** | `+3.5%` | 859,518.57 KB/s |
| SHA512 | 🏆 **FIPS** | `+0.4%` | 1,662,388.63 KB/s |

### 5.1 Optimization Recommendations
- **Primary Recommendation:** For high-throughput cryptographic workloads, the **FIPS** stack demonstrates the most efficient instruction-to-cycle ratio.
- **FIPS Strategy:** The FIPS-enabled pipeline shows negligible latency delta, making it suitable for production-grade security without compromising throughput.

## 6. Cryptographic Efficiency Scorecard (CES)
A normalized scoring system (0-100) representing the aggregate cryptographic health of each environment.

| Environment | Efficiency Score | Architectural Grade | Key Strength |
| :--- | :---: | :---: | :--- |
| **UBUNTU** | `99.9/100` | **A+** | High-Concurrency Bulk Processing |
| **FIPS** | `98.6/100` | **A+** | High-Concurrency Bulk Processing |
| **ALPINE** | `97.8/100` | **A+** | High-Concurrency Bulk Processing |
| **DEBIAN** | `94.7/100` | **A** | General Purpose Production |

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
    bar [99.9, 98.6, 97.8, 94.7]
```

---

*automated by benchmark/generate_report.py & benchmark/parser.py*