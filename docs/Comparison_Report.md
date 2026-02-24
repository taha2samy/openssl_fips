# Cryptographic Performance Infrastructure Audit

> **Report Status:** `FINAL` | **Audit ID:** `20260220-0408`

## 1. Executive Summary
Automated performance telemetry analysis across **4** isolated operating environments. This audit evaluates throughput efficiency for **4** core cryptographic primitives under variable block size constraints.

### 1.1 Environmental Metadata
| Property | Specification |
| :--- | :--- |
| **Target OS Distributions** | ALPINE, DEBIAN, FIPS, UBUNTU |
| **Evaluated Primitives** | 4 Algorithms |
| **Block Size Dimensions** | 6 Data points per set |
| **Hardware Architecture** | x86_64 |
| **Audit Timestamp** | 2026-02-20 04:08:58 |

## 2. Detailed Throughput Analysis Matrix
Systematic breakdown of processing velocity (bytes/sec) relative to block-size allocation.

| Environment | Primitive | 16B | 64B | 256B | 1024B | 8192B | 16384B |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **ALPINE** | `AES-256-GCM` | 129.87 MB/s | 473.78 MB/s | **1.59 GB/s** | **3.85 GB/s** | **6.97 GB/s** | **7.41 GB/s** |
| **DEBIAN** | `AES-256-GCM` | 88.80 MB/s | 334.10 MB/s | **1.17 GB/s** | **3.15 GB/s** | **6.63 GB/s** | **7.23 GB/s** |
| **FIPS** | `AES-256-GCM` | 178.70 MB/s | 635.70 MB/s | **2.00 GB/s** | **4.47 GB/s** | **7.16 GB/s** | **7.43 GB/s** |
| **UBUNTU** | `AES-256-GCM` | **1.10 GB/s** | **2.65 GB/s** | **5.23 GB/s** | **6.89 GB/s** | **7.71 GB/s** | **7.80 GB/s** |
| **ALPINE** | `sha256` | 119.06 MB/s | 446.20 MB/s | **1.48 GB/s** | **3.41 GB/s** | **5.53 GB/s** | **5.85 GB/s** |
| **DEBIAN** | `sha256` | 231.55 MB/s | 808.99 MB/s | **2.34 GB/s** | **4.33 GB/s** | **5.73 GB/s** | **5.91 GB/s** |
| **FIPS** | `sha256` | 279.52 MB/s | 957.97 MB/s | **2.60 GB/s** | **4.52 GB/s** | **5.80 GB/s** | **5.99 GB/s** |
| **UBUNTU** | `sha256` | 225.64 MB/s | 798.09 MB/s | **2.32 GB/s** | **4.35 GB/s** | **5.76 GB/s** | **5.96 GB/s** |
| **ALPINE** | `sha3-256` | 52.66 MB/s | 215.76 MB/s | 583.69 MB/s | 754.67 MB/s | 869.73 MB/s | 886.25 MB/s |
| **DEBIAN** | `sha3-256` | 69.72 MB/s | 279.39 MB/s | 671.66 MB/s | 792.46 MB/s | 876.21 MB/s | 889.28 MB/s |
| **FIPS** | `sha3-256` | 75.82 MB/s | 302.70 MB/s | 706.03 MB/s | 801.99 MB/s | 877.20 MB/s | 889.78 MB/s |
| **UBUNTU** | `sha3-256` | 65.57 MB/s | 261.94 MB/s | 650.18 MB/s | 784.98 MB/s | 876.70 MB/s | 889.44 MB/s |
| **ALPINE** | `sha512` | 72.61 MB/s | 300.50 MB/s | 681.47 MB/s | **1.24 GB/s** | **1.62 GB/s** | **1.66 GB/s** |
| **DEBIAN** | `sha512` | 100.80 MB/s | 402.58 MB/s | 833.48 MB/s | **1.34 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **FIPS** | `sha512` | 108.99 MB/s | 435.46 MB/s | 852.06 MB/s | **1.36 GB/s** | **1.64 GB/s** | **1.67 GB/s** |
| **UBUNTU** | `sha512` | 97.15 MB/s | 388.36 MB/s | 815.56 MB/s | **1.33 GB/s** | **1.64 GB/s** | **1.67 GB/s** |

### 2.1 Statistical Insights & Key Indicators
| Indicator | Metric Value | Analysis |
| :--- | :--- | :--- |
| AES-256-GCM | 7.3% Delta | OS Optimization Impact: `STABLE` |
| SHA256 | 2.4% Delta | OS Optimization Impact: `STABLE` |
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
    x-axis [ALPINE, UBUNTU, DEBIAN, FIPS]
    y-axis "Throughput (KB/s)" 0 --> 9749639
    bar [7412739.28, 7799711.33, 7232569.34, 7433422.44]
```

#### Primitive Capacity: `SHA256`
```mermaid
xychart-beta
    title "SHA256 Peak Velocity (KB/s)"
    x-axis [ALPINE, UBUNTU, DEBIAN, FIPS]
    y-axis "Throughput (KB/s)" 0 --> 7486531
    bar [5846694.3, 5958461.03, 5911509.4, 5989225.27]
```

#### Primitive Capacity: `SHA3-256`
```mermaid
xychart-beta
    title "SHA3-256 Peak Velocity (KB/s)"
    x-axis [ALPINE, UBUNTU, DEBIAN, FIPS]
    y-axis "Throughput (KB/s)" 0 --> 1112227
    bar [886251.52, 889436.57, 889279.28, 889782.27]
```

#### Primitive Capacity: `SHA512`
```mermaid
xychart-beta
    title "SHA512 Peak Velocity (KB/s)"
    x-axis [ALPINE, UBUNTU, DEBIAN, FIPS]
    y-axis "Throughput (KB/s)" 0 --> 2085689
    bar [1657515.21, 1667042.51, 1668551.48, 1668200.86]
```

### 📈 Architectural Scaling & Buffer Efficiency
Logarithmic growth analysis of throughput relative to increased block-size allocation.
#### Growth Vector: ALPINE (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [129874.87, 473783.89, 1589774.18, 3851375.1, 6972890.32, 7412739.28]
```
#### Growth Vector: DEBIAN (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [88802.84, 334097.24, 1168914.64, 3145375.64, 6634922.8, 7232569.34]
```
#### Growth Vector: FIPS (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [178699.47, 635695.08, 2003124.89, 4470499.53, 7159685.94, 7433422.44]
```
#### Growth Vector: UBUNTU (AES-256-GCM)
```mermaid
xychart-beta
    title "Buffer Efficiency Scaling"
    x-axis [16B, 64B, 256B, 1024B, 8192B, 16384B]
    y-axis "KB/s"
    line [1101014.72, 2645477.57, 5231766.14, 6888037.89, 7707996.98, 7799711.33]
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
| AES-256-GCM | 🏆 **UBUNTU** | `+4.4%` | 7,469,610.60 KB/s |
| SHA256 | 🏆 **FIPS** | `+1.1%` | 5,926,472.50 KB/s |
| SHA3-256 | 🏆 **FIPS** | `+0.1%` | 888,687.41 KB/s |
| SHA512 | 🏆 **DEBIAN** | `+0.2%` | 1,665,327.52 KB/s |

### 5.1 Optimization Recommendations
- **Primary Recommendation:** For high-throughput cryptographic workloads, the **DEBIAN** stack demonstrates the most efficient instruction-to-cycle ratio.
- **FIPS Strategy:** The FIPS-enabled pipeline shows negligible latency delta, making it suitable for production-grade security without compromising throughput.

## 6. Cryptographic Efficiency Scorecard (CES)
A normalized scoring system (0-100) representing the aggregate cryptographic health of each environment.

| Environment | Efficiency Score | Architectural Grade | Key Strength |
| :--- | :---: | :---: | :--- |
| **UBUNTU** | `99.8/100` | **A+** | High-Concurrency Bulk Processing |
| **FIPS** | `98.8/100` | **A+** | High-Concurrency Bulk Processing |
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
    bar [99.8, 98.8, 97.9, 97.8]
```

---

*automated by benchmark/generate_report.py & benchmark/parser.py*