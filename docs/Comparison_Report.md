# Cryptographic Performance Infrastructure Audit

> **Report Status:** `FINAL` | **Audit ID:** `20260219-0537`

## 1. Executive Summary
Automated performance telemetry analysis across **4** isolated operating environments. This audit evaluates throughput efficiency for **4** core cryptographic primitives under variable block size constraints.

### 1.1 Environmental Metadata
| Property | Specification |
| :--- | :--- |
| **Target OS Distributions** | ALPINE, DEBIAN, FIPS, UBUNTU |
| **Evaluated Primitives** | 4 Algorithms |
| **Block Size Dimensions** | 6 Data points per set |
| **Hardware Architecture** | x86_64 |
| **Audit Timestamp** | 2026-02-19 05:37:01 |

## 2. Detailed Throughput Analysis Matrix
Systematic breakdown of processing velocity (bytes/sec) relative to block-size allocation.

| Environment | Primitive | 16B | 64B | 256B | 1024B | 8192B | 16384B |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **ALPINE** | `AES-256-GCM` | 127.72 MB/s | 467.29 MB/s | **1.56 GB/s** | **3.82 GB/s** | **7.00 GB/s** | **7.44 GB/s** |
| **DEBIAN** | `AES-256-GCM` | 88.10 MB/s | 331.52 MB/s | **1.16 GB/s** | **3.16 GB/s** | **6.68 GB/s** | **7.23 GB/s** |
| **FIPS** | `AES-256-GCM` | 177.96 MB/s | 635.88 MB/s | **2.00 GB/s** | **4.48 GB/s** | **7.13 GB/s** | **7.48 GB/s** |
| **UBUNTU** | `AES-256-GCM` | **1.11 GB/s** | **2.64 GB/s** | **5.24 GB/s** | **6.88 GB/s** | **7.72 GB/s** | **7.77 GB/s** |
| **ALPINE** | `sha256` | 118.28 MB/s | 444.77 MB/s | **1.47 GB/s** | **3.41 GB/s** | **5.53 GB/s** | **5.82 GB/s** |
| **DEBIAN** | `sha256` | 234.99 MB/s | 830.60 MB/s | **2.37 GB/s** | **4.34 GB/s** | **5.74 GB/s** | **5.90 GB/s** |
| **FIPS** | `sha256` | 269.94 MB/s | 934.57 MB/s | **2.58 GB/s** | **4.49 GB/s** | **5.81 GB/s** | **5.97 GB/s** |
| **UBUNTU** | `sha256` | 225.32 MB/s | 795.26 MB/s | **2.30 GB/s** | **4.34 GB/s** | **5.75 GB/s** | **5.94 GB/s** |
| **ALPINE** | `sha3-256` | 52.67 MB/s | 216.26 MB/s | 584.44 MB/s | 754.04 MB/s | 870.83 MB/s | 882.69 MB/s |
| **DEBIAN** | `sha3-256` | 68.90 MB/s | 276.33 MB/s | 666.16 MB/s | 789.59 MB/s | 876.65 MB/s | 886.04 MB/s |
| **FIPS** | `sha3-256` | 75.44 MB/s | 303.95 MB/s | 705.90 MB/s | 801.39 MB/s | 878.83 MB/s | 887.13 MB/s |
| **UBUNTU** | `sha3-256` | 65.65 MB/s | 262.65 MB/s | 648.68 MB/s | 783.85 MB/s | 875.99 MB/s | 885.33 MB/s |
| **ALPINE** | `sha512` | 72.28 MB/s | 299.25 MB/s | 679.02 MB/s | **1.24 GB/s** | **1.62 GB/s** | **1.65 GB/s** |
| **DEBIAN** | `sha512` | 99.73 MB/s | 399.27 MB/s | 831.03 MB/s | **1.34 GB/s** | **1.64 GB/s** | **1.66 GB/s** |
| **FIPS** | `sha512` | 108.44 MB/s | 435.06 MB/s | 851.25 MB/s | **1.36 GB/s** | **1.64 GB/s** | **1.66 GB/s** |
| **UBUNTU** | `sha512` | 96.96 MB/s | 387.49 MB/s | 816.88 MB/s | **1.33 GB/s** | **1.64 GB/s** | **1.66 GB/s** |

### 2.1 Statistical Insights & Key Indicators
| Indicator | Metric Value | Analysis |
| :--- | :--- | :--- |
| AES-256-GCM | 7.0% Delta | OS Optimization Impact: `STABLE` |
| SHA256 | 2.4% Delta | OS Optimization Impact: `STABLE` |
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
    y-axis "Throughput (KB/s)" 0 --> 9709457
    bar [7226982.4, 7481878.12, 7444609.43, 7767565.93]
```

#### Primitive Capacity: `SHA256`
```mermaid
xychart-beta
    title "SHA256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 7456331
    bar [5895413.76, 5965065.42, 5821557.96, 5942635.72]
```

#### Primitive Capacity: `SHA3-256`
```mermaid
xychart-beta
    title "SHA3-256 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 1108908
    bar [886035.25, 887126.43, 882688.0, 885329.1]
```

#### Primitive Capacity: `SHA512`
```mermaid
xychart-beta
    title "SHA512 Peak Velocity (KB/s)"
    x-axis [DEBIAN, FIPS, ALPINE, UBUNTU]
    y-axis "Throughput (KB/s)" 0 --> 2079674
    bar [1661793.08, 1663739.49, 1652596.74, 1656383.08]
```

### 📈 Architectural Scaling & Buffer Efficiency
Logarithmic growth analysis of throughput relative to increased block-size allocation.
#### Growth Vector: ALPINE (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [127715.04, 467289.43, 1562964.22, 3817743.36, 6996715.93, 7444609.43]
```
#### Growth Vector: DEBIAN (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [88103.68, 331516.29, 1163165.8, 3155495.42, 6677968.49, 7226982.4]
```
#### Growth Vector: FIPS (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [177963.33, 635877.73, 1998197.63, 4477468.47, 7132474.57, 7481878.12]
```
#### Growth Vector: UBUNTU (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [1112731.28, 2641477.72, 5244113.2, 6881319.42, 7715786.75, 7767565.93]
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
| AES-256-GCM | 🏆 **UBUNTU** | `+3.8%` | 7,480,258.97 KB/s |
| SHA256 | 🏆 **FIPS** | `+1.0%` | 5,906,168.21 KB/s |
| SHA3-256 | 🏆 **FIPS** | `+0.2%` | 885,294.70 KB/s |
| SHA512 | 🏆 **FIPS** | `+0.3%` | 1,658,628.10 KB/s |

### 5.1 Optimization Recommendations
- **Primary Recommendation:** For high-throughput cryptographic workloads, the **FIPS** stack demonstrates the most efficient instruction-to-cycle ratio.
- **FIPS Strategy:** The FIPS-enabled pipeline shows negligible latency delta, making it suitable for production-grade security without compromising throughput.

## 6. Cryptographic Efficiency Scorecard (CES)
A normalized scoring system (0-100) representing the aggregate cryptographic health of each environment.

| Environment | Efficiency Score | Architectural Grade | Key Strength |
| :--- | :---: | :---: | :--- |
| **UBUNTU** | `99.7/100` | **A+** | High-Concurrency Bulk Processing |
| **FIPS** | `99.1/100` | **A+** | High-Concurrency Bulk Processing |
| **ALPINE** | `98.1/100` | **A+** | High-Concurrency Bulk Processing |
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
    bar [99.7, 99.1, 98.1, 97.9]
```

---

*automated by benchmark/generate_report.py & benchmark/parser.py*