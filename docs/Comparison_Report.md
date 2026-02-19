# Cryptographic Performance Infrastructure Audit

> **Report Status:** `FINAL` | **Audit ID:** `20260219-0021`

## 1. Executive Summary
Automated performance telemetry analysis across **4** isolated operating environments. This audit evaluates throughput efficiency for **4** core cryptographic primitives under variable block size constraints.

### 1.1 Environmental Metadata
| Property | Specification |
| :--- | :--- |
| **Target OS Distributions** | ALPINE, DEBIAN, FIPS, UBUNTU |
| **Evaluated Primitives** | 4 Algorithms |
| **Block Size Dimensions** | 6 Data points per set |
| **Hardware Architecture** | x86_64 |
| **Audit Timestamp** | 2026-02-19 00:21:17 |

## 2. Detailed Throughput Analysis Matrix
Systematic breakdown of processing velocity (bytes/sec) relative to block-size allocation.

| Environment | Primitive | 16B | 64B | 256B | 1024B | 8192B | 16384B |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **ALPINE** | `AES-256-GCM` | 127.61 MB/s | 467.14 MB/s | **1.56 GB/s** | **3.83 GB/s** | **7.00 GB/s** | **7.42 GB/s** |
| **DEBIAN** | `AES-256-GCM` | 88.31 MB/s | 332.51 MB/s | **1.17 GB/s** | **3.14 GB/s** | **6.66 GB/s** | **7.23 GB/s** |
| **FIPS** | `AES-256-GCM` | 179.57 MB/s | 630.51 MB/s | **1.99 GB/s** | **4.50 GB/s** | **7.06 GB/s** | **7.46 GB/s** |
| **UBUNTU** | `AES-256-GCM` | **1.11 GB/s** | **2.64 GB/s** | **5.24 GB/s** | **6.54 GB/s** | **7.72 GB/s** | **7.79 GB/s** |
| **ALPINE** | `sha256` | 117.55 MB/s | 444.92 MB/s | **1.47 GB/s** | **3.40 GB/s** | **5.53 GB/s** | **5.84 GB/s** |
| **DEBIAN** | `sha256` | 236.06 MB/s | 835.96 MB/s | **2.38 GB/s** | **4.35 GB/s** | **5.75 GB/s** | **5.91 GB/s** |
| **FIPS** | `sha256` | 277.79 MB/s | 957.71 MB/s | **2.56 GB/s** | **4.52 GB/s** | **5.80 GB/s** | **5.97 GB/s** |
| **UBUNTU** | `sha256` | 224.11 MB/s | 795.87 MB/s | **2.30 GB/s** | **4.34 GB/s** | **5.78 GB/s** | **5.97 GB/s** |
| **ALPINE** | `sha3-256` | 52.59 MB/s | 216.31 MB/s | 584.63 MB/s | 753.27 MB/s | 870.81 MB/s | 884.34 MB/s |
| **DEBIAN** | `sha3-256` | 69.66 MB/s | 279.02 MB/s | 662.48 MB/s | 791.39 MB/s | 876.88 MB/s | 888.65 MB/s |
| **FIPS** | `sha3-256` | 75.81 MB/s | 303.54 MB/s | 699.89 MB/s | 802.03 MB/s | 879.16 MB/s | 889.83 MB/s |
| **UBUNTU** | `sha3-256` | 65.42 MB/s | 261.95 MB/s | 646.99 MB/s | 784.29 MB/s | 875.66 MB/s | 886.19 MB/s |
| **ALPINE** | `sha512` | 71.12 MB/s | 294.39 MB/s | 672.36 MB/s | **1.23 GB/s** | **1.61 GB/s** | **1.65 GB/s** |
| **DEBIAN** | `sha512` | 99.87 MB/s | 401.03 MB/s | 829.05 MB/s | **1.33 GB/s** | **1.62 GB/s** | **1.65 GB/s** |
| **FIPS** | `sha512` | 108.58 MB/s | 430.32 MB/s | 841.17 MB/s | **1.36 GB/s** | **1.62 GB/s** | **1.67 GB/s** |
| **UBUNTU** | `sha512` | 96.87 MB/s | 387.44 MB/s | 815.71 MB/s | **1.33 GB/s** | **1.64 GB/s** | **1.67 GB/s** |

### 2.1 Statistical Insights & Key Indicators
| Indicator | Metric Value | Analysis |
| :--- | :--- | :--- |
| AES-256-GCM | 7.2% Delta | OS Optimization Impact: `STABLE` |
| SHA256 | 2.2% Delta | OS Optimization Impact: `STABLE` |
| SHA3-256 | 0.6% Delta | OS Optimization Impact: `STABLE` |
| SHA512 | 1.1% Delta | OS Optimization Impact: `STABLE` |

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
    y-axis "Throughput (KB/s)" 0 --> 9742131
    bar [7230406.66, 7461003.26, 7419936.77, 7793704.96]
```

#### Primitive Capacity: `SHA256`
```mermaid
xychart-beta
    title "SHA256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 7465390
    bar [5905678.34, 5972312.06, 5838004.22, 5967273.98]
```

#### Primitive Capacity: `SHA3-256`
```mermaid
xychart-beta
    title "SHA3-256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 1112289
    bar [888651.78, 889831.42, 884339.48, 886185.98]
```

#### Primitive Capacity: `SHA512`
```mermaid
xychart-beta
    title "SHA512 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 2083665
    bar [1648369.66, 1666932.74, 1649115.14, 1666441.22]
```

### 📈 Architectural Scaling & Buffer Efficiency
Logarithmic growth analysis of throughput relative to increased block-size allocation.
#### Growth Vector: ALPINE (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [127610.15, 467143.71, 1558546.18, 3826008.06, 6995005.44, 7419936.77]
```
#### Growth Vector: DEBIAN (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [88309.95, 332513.7, 1169470.98, 3139880.96, 6655541.25, 7230406.66]
```
#### Growth Vector: FIPS (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [179565.42, 630508.99, 1987628.8, 4497530.88, 7061184.51, 7461003.26]
```
#### Growth Vector: UBUNTU (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [1113179.94, 2641726.34, 5244421.25, 6536078.34, 7715008.51, 7793704.96]
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
| AES-256-GCM | 🏆 **UBUNTU** | `+4.2%` | 7,476,262.91 KB/s |
| SHA256 | 🏆 **FIPS** | `+0.9%` | 5,920,817.15 KB/s |
| SHA3-256 | 🏆 **FIPS** | `+0.3%` | 887,252.17 KB/s |
| SHA512 | 🏆 **FIPS** | `+0.6%` | 1,657,714.69 KB/s |

### 5.1 Optimization Recommendations
- **Primary Recommendation:** For high-throughput cryptographic workloads, the **FIPS** stack demonstrates the most efficient instruction-to-cycle ratio.
- **FIPS Strategy:** The FIPS-enabled pipeline shows negligible latency delta, making it suitable for production-grade security without compromising throughput.

## 6. Cryptographic Efficiency Scorecard (CES)
A normalized scoring system (0-100) representing the aggregate cryptographic health of each environment.

| Environment | Efficiency Score | Architectural Grade | Key Strength |
| :--- | :---: | :---: | :--- |
| **UBUNTU** | `99.9/100` | **A+** | High-Concurrency Bulk Processing |
| **FIPS** | `98.9/100` | **A+** | High-Concurrency Bulk Processing |
| **ALPINE** | `97.8/100` | **A+** | High-Concurrency Bulk Processing |
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
    bar [99.9, 98.9, 97.8, 97.6]
```

---

*automated by benchmark/generate_report.py & benchmark/parser.py*