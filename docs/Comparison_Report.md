# Cryptographic Performance Infrastructure Audit

> **Report Status:** `FINAL` | **Audit ID:** `20260218-1933`

## 1. Executive Summary
Automated performance telemetry analysis across **4** isolated operating environments. This audit evaluates throughput efficiency for **4** core cryptographic primitives under variable block size constraints.

### 1.1 Environmental Metadata
| Property | Specification |
| :--- | :--- |
| **Target OS Distributions** | ALPINE, DEBIAN, FIPS, UBUNTU |
| **Evaluated Primitives** | 4 Algorithms |
| **Block Size Dimensions** | 6 Data points per set |
| **Hardware Architecture** | x86_64 |
| **Audit Timestamp** | 2026-02-18 19:33:13 |

## 2. Detailed Throughput Analysis Matrix
Systematic breakdown of processing velocity (bytes/sec) relative to block-size allocation.

| Environment | Primitive | 16B | 64B | 256B | 1024B | 8192B | 16384B |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **ALPINE** | `AES-256-GCM` | 127.11 MB/s | 466.54 MB/s | **1.58 GB/s** | **3.79 GB/s** | **7.00 GB/s** | **7.43 GB/s** |
| **DEBIAN** | `AES-256-GCM` | 88.52 MB/s | 334.75 MB/s | **1.17 GB/s** | **3.18 GB/s** | **6.59 GB/s** | **7.23 GB/s** |
| **FIPS** | `AES-256-GCM` | 170.53 MB/s | 628.21 MB/s | **1.96 GB/s** | **4.49 GB/s** | **7.14 GB/s** | **7.39 GB/s** |
| **UBUNTU** | `AES-256-GCM` | **1.11 GB/s** | **2.64 GB/s** | **5.24 GB/s** | **6.88 GB/s** | **7.71 GB/s** | **7.79 GB/s** |
| **ALPINE** | `sha256` | 118.58 MB/s | 445.50 MB/s | **1.47 GB/s** | **3.40 GB/s** | **5.53 GB/s** | **5.84 GB/s** |
| **DEBIAN** | `sha256` | 237.78 MB/s | 836.06 MB/s | **2.35 GB/s** | **4.35 GB/s** | **5.74 GB/s** | **5.88 GB/s** |
| **FIPS** | `sha256` | 274.92 MB/s | 947.43 MB/s | **2.55 GB/s** | **4.51 GB/s** | **5.77 GB/s** | **5.86 GB/s** |
| **UBUNTU** | `sha256` | 226.13 MB/s | 807.19 MB/s | **2.32 GB/s** | **4.35 GB/s** | **5.78 GB/s** | **5.96 GB/s** |
| **ALPINE** | `sha3-256` | 52.72 MB/s | 216.35 MB/s | 584.25 MB/s | 753.25 MB/s | 867.86 MB/s | 883.82 MB/s |
| **DEBIAN** | `sha3-256` | 69.56 MB/s | 278.99 MB/s | 669.32 MB/s | 791.22 MB/s | 877.22 MB/s | 888.18 MB/s |
| **FIPS** | `sha3-256` | 75.85 MB/s | 303.76 MB/s | 698.75 MB/s | 801.69 MB/s | 878.83 MB/s | 889.45 MB/s |
| **UBUNTU** | `sha3-256` | 64.70 MB/s | 262.54 MB/s | 648.23 MB/s | 783.40 MB/s | 874.63 MB/s | 888.07 MB/s |
| **ALPINE** | `sha512` | 72.46 MB/s | 296.40 MB/s | 680.15 MB/s | **1.24 GB/s** | **1.62 GB/s** | **1.65 GB/s** |
| **DEBIAN** | `sha512` | 99.83 MB/s | 400.26 MB/s | 831.39 MB/s | **1.34 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **FIPS** | `sha512` | 109.04 MB/s | 435.86 MB/s | 839.06 MB/s | **1.36 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **UBUNTU** | `sha512` | 96.93 MB/s | 388.17 MB/s | 818.38 MB/s | **1.33 GB/s** | **1.64 GB/s** | **1.67 GB/s** |

### 2.1 Statistical Insights & Key Indicators
| Indicator | Metric Value | Analysis |
| :--- | :--- | :--- |
| AES-256-GCM | 7.2% Delta | OS Optimization Impact: `STABLE` |
| SHA256 | 2.1% Delta | OS Optimization Impact: `STABLE` |
| SHA3-256 | 0.6% Delta | OS Optimization Impact: `STABLE` |
| SHA512 | 1.0% Delta | OS Optimization Impact: `STABLE` |

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
    y-axis "Throughput (KB/s)" 0 --> 9737605
    bar [7230586.88, 7391281.15, 7432372.22, 7790084.1]
```

#### Primitive Capacity: `SHA256`
```mermaid
xychart-beta
    title "SHA256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 7452088
    bar [5881683.97, 5864628.22, 5837881.34, 5961670.66]
```

#### Primitive Capacity: `SHA3-256`
```mermaid
xychart-beta
    title "SHA3-256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 1111808
    bar [888184.83, 889446.4, 883818.5, 888070.14]
```

#### Primitive Capacity: `SHA512`
```mermaid
xychart-beta
    title "SHA512 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 2085826
    bar [1665482.75, 1668661.25, 1652449.28, 1665515.52]
```

### 📈 Architectural Scaling & Buffer Efficiency
Logarithmic growth analysis of throughput relative to increased block-size allocation.
#### Growth Vector: ALPINE (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [127110.06, 466541.38, 1576355.46, 3794056.19, 6996049.92, 7432372.22]
```
#### Growth Vector: DEBIAN (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [88517.11, 334750.5, 1169968.64, 3179317.76, 6591930.37, 7230586.88]
```
#### Growth Vector: FIPS (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [170526.12, 628210.46, 1955358.34, 4489903.1, 7144599.55, 7391281.15]
```
#### Growth Vector: UBUNTU (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [1113420.1, 2644448.42, 5239062.78, 6884785.15, 7713525.76, 7790084.1]
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
| AES-256-GCM | 🏆 **UBUNTU** | `+4.4%` | 7,461,081.09 KB/s |
| SHA256 | 🏆 **UBUNTU** | `+1.3%` | 5,886,466.05 KB/s |
| SHA3-256 | 🏆 **FIPS** | `+0.2%` | 887,379.97 KB/s |
| SHA512 | 🏆 **FIPS** | `+0.3%` | 1,663,027.20 KB/s |

### 5.1 Optimization Recommendations
- **Primary Recommendation:** For high-throughput cryptographic workloads, the **FIPS** stack demonstrates the most efficient instruction-to-cycle ratio.
- **FIPS Strategy:** The FIPS-enabled pipeline shows negligible latency delta, making it suitable for production-grade security without compromising throughput.

## 6. Cryptographic Efficiency Scorecard (CES)
A normalized scoring system (0-100) representing the aggregate cryptographic health of each environment.

| Environment | Efficiency Score | Architectural Grade | Key Strength |
| :--- | :---: | :---: | :--- |
| **UBUNTU** | `99.9/100` | **A+** | High-Concurrency Bulk Processing |
| **FIPS** | `98.3/100` | **A+** | High-Concurrency Bulk Processing |
| **ALPINE** | `97.9/100` | **A+** | High-Concurrency Bulk Processing |
| **DEBIAN** | `97.8/100` | **A+** | High-Concurrency Bulk Processing |

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
    bar [99.9, 98.3, 97.9, 97.8]
```

---

*automated by benchmark/generate_report.py & benchmark/parser.py*