# 🛡️ Multi-OS OpenSSL Performance Comparison

This report compares the performance of **FIPS-validated OpenSSL (Wolfi OS)** against standard OpenSSL implementations in common Linux distributions.

| Metric | Unit | FIPS (Wolfi) | Debian | Alpine | Ubuntu |
| :--- | :---: | :---: | :---: | :---: | :---: |
| OpenSSL Version |  | 3.5.5 | 3.0.18 | 3.5.5 | 3.0.13 |
| RSA 2048 Sign | ops/s | 2,331.5 | 3,516.3 | 3,164.3 | 2,411.6 |
| RSA 2048 Verify | ops/s | 118,831.6 | 104,987.3 | 98,157.6 | 108,910.8 |
| Ed25519 Sign | ops/s | 65,528.1 | 40,131.4 | 36,233.7 | 39,532.6 |
| Ed25519 Verify | ops/s | 20,555.9 | 19,237.3 | 13,980.3 | 16,199.8 |
| AES-256-GCM | kB/s | 8,323,223.2 | 6,674,064.1 | 6,892,754.0 | 8,456,737.4 |
| SHA-256 | kB/s | 1,087,667.2 | 726,173.1 | 804,339.7 | 629,977.7 |
| SHA-512 | kB/s | 1,423,376.4 | 1,013,200.5 | 1,400,507.2 | 1,385,843.8 |

## 📘 Metric Definitions

### 1. Asymmetric Cryptography (RSA & Ed25519)
- **Unit:** `ops/s` (Operations per second).
- **Meaning:** How many digital signatures or verifications the CPU can perform in one second. Higher is better.
- **Sign vs. Verify:** Signing usually requires more computational power than verification (especially in RSA), which is why verification numbers are significantly higher.

### 2. Symmetric Encryption (AES-256-GCM)
- **Unit:** `kB/s` (Kilobytes processed per second).
- **Block Size:** Tested with `16k` blocks to simulate large data transfers (e.g., VPN, HTTPS).
- **Meaning:** The volume of data the system can encrypt/decrypt per second. High numbers indicate efficient use of Hardware Acceleration (like Intel AES-NI).

### 3. Hashing (SHA-256 & SHA-512)
- **Unit:** `kB/s` (Kilobytes hashed per second).
- **Meaning:** Speed of generating data integrity checksums. Wolfi (FIPS) may show improvements here due to newer OpenSSL 3.5 optimizations.

---

> **Note:** Performance differences are influenced by OpenSSL versions (Wolfi uses 3.5.x while Debian/Ubuntu use 3.0.x) and compiler optimizations (e.g., `-O3` vs `-O2`).