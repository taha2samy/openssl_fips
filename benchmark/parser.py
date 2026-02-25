#!/usr/bin/env python3
import re
import csv
import os
import glob
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from scripts.logger import log
except ImportError:
    import logging as log
    log.basicConfig(level=log.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH_THROUGHPUT =  "./reports/results.csv"
CSV_PATH_SIGNATURES = "./reports/signatures.csv"

def get_os_version(os_name):
    if os_name in ["fips", "alpine"]:
        return "3.5.5"
    if os_name == "debian":
        return "3.0.18"
    if os_name == "ubuntu":
        return "3.0.13"
    log.warning(f"Version mapping missing for OS: {os_name}")
    return "Unknown"

def identify_and_clean_algo(line):
    line_lower = line.lower()
    if "rsa" in line_lower: return "rsa2048"
    if "ecdsa" in line_lower or "nistp256" in line_lower: return "ecdsap256"
    return line.split()[0].upper().replace(':', '')

def extract_perf_numbers(line):
    parts = line.split()
    nums = []
    for p in parts:
        clean = p.strip().replace('k', '')
        if clean.endswith('s') or not re.match(r'^-?\d+(\.\d+)?$', clean):
            continue
        val = float(clean)
        if val in [16.0, 64.0, 256.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 0.0]:
            continue
        nums.append(val)
    return nums

def parse_raw_logs():
    LOG_DIR = os.path.join(BASE_DIR, "bench_results")
    throughput_data = []
    signature_data = []
    
    log_files = glob.glob(os.path.join(LOG_DIR, "*.log"))

    if not log_files:
        log.error("No log files found.")
        return

    log.info("Parsing telemetry with fixed version mapping...")

    for file_path in log_files:
        os_name = os.path.basename(file_path).replace('.log', '')
        current_version = get_os_version(os_name)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or any(x in line.lower() for x in ['built', 'compiler', 'options', 'cpuinfo', 'keygen', 'encaps', 'decaps', 'encrypt', 'decrypt', 'encr', 'decr']):
                        continue

                    if line.startswith(('+', 'Forked', 'Got:', 'version:')):
                        continue

                    nums = extract_perf_numbers(line)
                    if not nums: continue

                    algo = identify_and_clean_algo(line)

                    if len(nums) == 6:
                        throughput_data.append({
                            "os": os_name,
                            "version": current_version,
                            "algorithm": algo,
                            "16b": nums[0], "64b": nums[1], "256b": nums[2],
                            "1024b": nums[3], "8192b": nums[4], "16384b": nums[5]
                        })
                    
                    elif len(nums) >= 2:
                        signature_data.append({
                            "os": os_name,
                            "version": current_version,
                            "algorithm": algo,
                            "sign_ops": nums[0],
                            "verify_ops": nums[1]
                        })

        except Exception as e:
            log.error(f"Error parsing {os_name}: {str(e)}")
    
    os.makedirs(os.path.dirname(CSV_PATH_THROUGHPUT), exist_ok=True)

    if throughput_data:
        with open(CSV_PATH_THROUGHPUT, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=throughput_data[0].keys())
            writer.writeheader()
            writer.writerows(throughput_data)

    if signature_data:
        unique_sigs = {}
        for entry in signature_data:
            key = (entry['os'], entry['algorithm'])
            if key not in unique_sigs or entry['sign_ops'] > unique_sigs[key]['sign_ops']:
                unique_sigs[key] = entry
        
        with open(CSV_PATH_SIGNATURES, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=signature_data[0].keys())
            writer.writeheader()
            writer.writerows(unique_sigs.values())

    log.info("CSVs regenerated successfully with correct versions.")

if __name__ == "__main__":
    parse_raw_logs()