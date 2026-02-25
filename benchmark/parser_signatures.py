#!/usr/bin/env python3
import re
import csv
import os
import glob
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(ROOT_DIR)

from scripts.logger import log, group_start, group_end, notice

LOG_DIRECTORY = os.path.join(SCRIPT_DIR, "bench_results")
REPORTS_DIRECTORY = os.path.join(ROOT_DIR, "reports")
SIGNATURE_CSV_PATH = os.path.join(REPORTS_DIRECTORY, "signatures.csv")

def extract_version_from_log(file_lines):
    version_pattern = re.compile(r'^version:\s*([\w\.]+)', re.IGNORECASE)
    for line in file_lines:
        match = version_pattern.search(line.strip())
        if match:
            return match.group(1)
    return "Unknown"

def extract_clean_metrics(line):
    parts = line.split()
    metrics = []
    for p in parts:
        clean = p.strip()
        if clean.endswith('s') or not re.match(r'^-?\d+(\.\d+)?$', clean):
            continue
        val = float(clean)
        if val in [256.0, 384.0, 521.0, 1024.0, 2048.0, 4096.0, 0.0]:
            continue
        metrics.append(val)
    return metrics

def process_signature_telemetry():
    asym_log_files = glob.glob(os.path.join(LOG_DIRECTORY, "*.log"))
    signature_records = []
    
    asym_algo_pattern = re.compile(r'rsa\s+\d+|ecdsa|nistp\d+|256\s+bit|384\s+bit', re.IGNORECASE)

    if not asym_log_files:
        log.error(f"No logs found in {LOG_DIRECTORY}")
        return []

    for file_path in asym_log_files:
        os_name = os.path.basename(file_path).replace('.log', '')
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        openssl_version = extract_version_from_log(lines)

        for line in lines:
            line = line.strip()
            if not line or any(x in line.lower() for x in ['built', 'compiler', 'keygen', 'encaps', 'decaps']):
                continue

            if asym_algo_pattern.search(line):
                nums = extract_clean_metrics(line)
                if len(nums) >= 2:
                    algo_label = "rsa2048" if "rsa" in line.lower() else "ecdsap256"
                    signature_records.append({
                        "os": os_name,
                        "version": openssl_version,
                        "algorithm": algo_label,
                        "sign_ops": nums[0],
                        "verify_ops": nums[1]
                    })
    return signature_records

def save_signature_report(data):
    if not data:
        log.warning("No signature data found to save.")
        return

    unique_peaks = {}
    for entry in data:
        key = (entry['os'], entry['algorithm'])
        if key not in unique_peaks or entry['sign_ops'] > unique_peaks[key]['sign_ops']:
            unique_peaks[key] = entry

    os.makedirs(REPORTS_DIRECTORY, exist_ok=True)
    headers = ["os", "version", "algorithm", "sign_ops", "verify_ops"]
    
    with open(SIGNATURE_CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(unique_peaks.values())
    
    notice(f"Signature report generated at {SIGNATURE_CSV_PATH}")

if __name__ == "__main__":
    group_start("Asymmetric Signature Parser")
    
    results = process_signature_telemetry()
    save_signature_report(results)
    
    group_end()