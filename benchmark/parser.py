#!/usr/bin/env python3
import re
import csv
import os
import glob

# --- Configuration & Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "../docs/assets/data/results.csv")  # حفظ CSV هنا

def parse_raw_logs():
    """Raw Data Extraction (Regex Engine)"""
    LOG_DIR = os.path.join(BASE_DIR, "bench_results")
    all_data = []
    log_files = glob.glob(os.path.join(LOG_DIR, "*.log"))
    
    speed_regex = r'^([a-zA-Z0-9\.-]+)\s+([\d\.]+k)\s+([\d\.]+k)\s+([\d\.]+k)\s+([\d\.]+k)\s+([\d\.]+k)\s+([\d\.]+k)'
    version_regex = r'^version:\s*([\w\.]+)'

    if not log_files:
        print("[-] No log files found in bench_results/*.log")
        return []

    for file_path in log_files:
        os_name = os.path.basename(file_path).replace('.log', '')
        current_version = "Unknown"
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                v_match = re.search(version_regex, line, re.IGNORECASE)
                if v_match:
                    current_version = v_match.group(1)
                    continue

                match = re.search(speed_regex, line)
                if match:
                    all_data.append({
                        "os": os_name,
                        "version": current_version,
                        "algorithm": match.group(1),
                        "16b": float(match.group(2).replace('k', '')),
                        "64b": float(match.group(3).replace('k', '')),
                        "256b": float(match.group(4).replace('k', '')),
                        "1024b": float(match.group(5).replace('k', '')),
                        "8192b": float(match.group(6).replace('k', '')),
                        "16384b": float(match.group(7).replace('k', ''))
                    })
    
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)

    if all_data:
        keys = all_data[0].keys()
        with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(all_data)
        print(f"[+] CSV saved to {CSV_PATH}")

    return all_data

if __name__ == "__main__":
    print("[*] Starting Benchmark Parser...")
    extracted_data = parse_raw_logs()
    
    if extracted_data:
        print(f"[+] Successfully parsed {len(extracted_data)} entries.")
    else:
        print("[-] Error: No telemetry data found.")