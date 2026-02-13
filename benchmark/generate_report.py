import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "bench_results")
OUTPUT_PATH = os.path.join(BASE_DIR, "..", "Comparison_Report.md")

def parse_file(filepath):
    data = {}
    if not os.path.exists(filepath): return None
    
    with open(filepath, "r") as f:
        content = f.read()
        lines = content.splitlines()
        
        for line in lines:
            line = line.strip()
            
            if "rsa" in line and "2048" in line:
                nums = re.findall(r"([0-9]{2,}\.[0-9]+|[0-9]{3,})", line)
                if len(nums) >= 2:
                    data["rsa_sign"] = float(nums[-2])
                    data["rsa_verify"] = float(nums[-1])

            if "Ed25519" in line and "sign" in line:
                nums = re.findall(r"([0-9]{2,}\.[0-9]+|[0-9]{3,})", line)
                if len(nums) >= 2:
                    data["ed25519_sign"] = float(nums[-2])
                    data["ed25519_verify"] = float(nums[-1])

            if any(x in line for x in ["AES-256-GCM", "sha256", "sha512"]):
                parts = line.split()
                if len(parts) > 2 and any(p.endswith('k') for p in parts):
                    val = float(parts[-1].replace('k', ''))
                    if "AES-256-GCM" in line: data["aes_throughput"] = val
                    elif "sha256" in line: data["sha256"] = val
                    elif "sha512" in line: data["sha512"] = val
    return data

fips = parse_file(os.path.join(LOG_DIR, "fips.log"))
debian = parse_file(os.path.join(LOG_DIR, "debian.log"))

if not fips or not debian:
    exit(1)

report = [
    "# 🚀 Ultimate FIPS vs Standard Performance Report\n",
    "| Algorithm Metric | FIPS (Wolfi 3.5) | Standard (Debian 3.0) | % Diff |",
    "| :--- | :---: | :---: | :---: |"
]

metrics = [
    ("RSA 2048 Sign (ops/s)", "rsa_sign"),
    ("RSA 2048 Verify (ops/s)", "rsa_verify"),
    ("Ed25519 Sign (ops/s)", "ed25519_sign"),
    ("Ed25519 Verify (ops/s)", "ed25519_verify"),
    ("AES-256-GCM (16k block)", "aes_throughput"),
    ("SHA-256 (16k block)", "sha256"),
    ("SHA-512 (16k block)", "sha512")
]

for label, key in metrics:
    fv, dv = fips.get(key, 0.0), debian.get(key, 0.0)
    diff = ((fv - dv) / dv * 100) if dv > 0 else 0
    report.append(f"| {label} | {fv:,.1f} | {dv:,.1f} | {diff:+.2f}% |")

with open(OUTPUT_PATH, "w") as f:
    f.write("\n".join(report))

print(f"⭐ Report Successfully Generated at: {os.path.abspath(OUTPUT_PATH)}")