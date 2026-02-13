#!/usr/bin/env python3
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "bench_results")
OUTPUT_PATH = os.path.join(BASE_DIR, "..", "Comparison_Report.md")

def parse_file(filepath):
    data = {}
    if not os.path.exists(filepath): return None
    with open(filepath, "r") as f:
        lines = f.readlines()
        version = re.search(r"\d+\.\d+\.\d+", lines[0]).group(0)
        data["version"] = version
        for line in lines:
            line = line.strip()
            if "rsa" in line and "2048" in line and "bits" in line:
                nums = re.findall(r"(\d+\.\d+)", line)
                if len(nums) >= 4:
                    data["rsa_sign"] = float(nums[-4]) if len(nums) > 4 else float(nums[-2])
                    data["rsa_verify"] = float(nums[-3]) if len(nums) > 4 else float(nums[-1])
            
            if "Ed25519" in line and ("sign" in line or "verify" in line or "EdDSA" in line):
                nums = re.findall(r"(\d+\.\d+)", line)
                if len(nums) >= 2:
                    data["ed25519_sign"] = float(nums[-2])
                    data["ed25519_verify"] = float(nums[-1])

            if any(x in line for x in ["AES-256-GCM", "sha256", "sha512"]):
                parts = line.split()
                if len(parts) > 2 and any(p.endswith('k') for p in parts):
                    val = float(parts[-1].replace('k', ''))
                    if "AES-256-GCM" in line: data["aes"] = val
                    elif "sha256" in line: data["sha256"] = val
                    elif "sha512" in line: data["sha512"] = val
    return data

systems = {
    "FIPS (Wolfi)": "fips.log",
    "Debian": "debian.log",
    "Alpine": "alpine.log",
    "Ubuntu": "ubuntu.log"
}

results = {name: parse_file(os.path.join(LOG_DIR, file)) for name, file in systems.items()}
results = {k: v for k, v in results.items() if v}

metrics = [
    ("OpenSSL Version", "version"),
    ("RSA 2048 Sign", "rsa_sign"),
    ("RSA 2048 Verify", "rsa_verify"),
    ("Ed25519 Sign", "ed25519_sign"),
    ("Ed25519 Verify", "ed25519_verify"),
    ("AES-256-GCM", "aes"),
    ("SHA-256", "sha256"),
    ("SHA-512", "sha512")
]

header = "| Metric | Unit | " + " | ".join(results.keys()) + " |"
separator = "| :--- | :---: | " + " | ".join([":---:"] * len(results)) + " |"
report = [
    "# 🛡️ Multi-OS OpenSSL Performance Comparison",
    "\nThis report compares the performance of **FIPS-validated OpenSSL (Wolfi OS)** against standard OpenSSL implementations in common Linux distributions.",
    "\n" + header,
    separator
]

for label, key in metrics:
    unit = "ops/s" if "Sign" in label or "Verify" in label else "kB/s" if "Version" not in label else ""
    row = f"| {label} | {unit} | "
    vals = []
    for sys in results:
        v = results[sys].get(key, 0.0)
        if key == "version":
            vals.append(v)

        else:
            vals.append(f"{v:,.1f}")
    row += " | ".join(vals) + " |"
    report.append(row)

report.extend([
    "\n## 📘 Metric Definitions",
    "\n### 1. Asymmetric Cryptography (RSA & Ed25519)",
    "- **Unit:** `ops/s` (Operations per second).",
    "- **Meaning:** How many digital signatures or verifications the CPU can perform in one second. Higher is better.",
    "- **Sign vs. Verify:** Signing usually requires more computational power than verification (especially in RSA), which is why verification numbers are significantly higher.",
    "\n### 2. Symmetric Encryption (AES-256-GCM)",
    "- **Unit:** `kB/s` (Kilobytes processed per second).",
    "- **Block Size:** Tested with `16k` blocks to simulate large data transfers (e.g., VPN, HTTPS).",
    "- **Meaning:** The volume of data the system can encrypt/decrypt per second. High numbers indicate efficient use of Hardware Acceleration (like Intel AES-NI).",
    "\n### 3. Hashing (SHA-256 & SHA-512)",
    "- **Unit:** `kB/s` (Kilobytes hashed per second).",
    "- **Meaning:** Speed of generating data integrity checksums. Wolfi (FIPS) may show improvements here due to newer OpenSSL 3.5 optimizations.",
    "\n---",
    "\n> **Note:** Performance differences are influenced by OpenSSL versions (Wolfi uses 3.5.x while Debian/Ubuntu use 3.0.x) and compiler optimizations (e.g., `-O3` vs `-O2`)."
])

with open(OUTPUT_PATH, "w") as f:
    f.write("\n".join(report))