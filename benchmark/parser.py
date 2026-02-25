#!/usr/bin/env python3
import re
import csv
import json
import os
import glob
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(ROOT_DIR)

from scripts.logger import log, group_start, group_end, notice

LOG_DIR = os.path.join(SCRIPT_DIR, "bench_results")
REPORTS_DIR = os.path.join(ROOT_DIR, "reports")
CSV_PATH = os.path.join(ROOT_DIR, "reports","results.csv")
JSON_PATH = os.path.join(REPORTS_DIR, "benchmark_data.json")

def parse_raw_logs():
    all_data = []
    log_files = glob.glob(os.path.join(LOG_DIR, "*.log"))
    
    speed_regex = r'^([a-zA-Z0-9\.-]+)\s+([\d\.]+k)\s+([\d\.]+k)\s+([\d\.]+k)\s+([\d\.]+k)\s+([\d\.]+k)\s+([\d\.]+k)'
    version_regex = r'^version:\s*([\w\.]+)'

    if not log_files:
        log.error(f"No log files found in {LOG_DIR}")
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
    
    if all_data:
        os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
        keys = all_data[0].keys()
        with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(all_data)
        notice(f"CSV data synced to docs")

    return all_data

def transform_to_json(data):
    structured = {"metadata": {}, "metrics": {}}
    for entry in data:
        algo, os_name, ver = entry['algorithm'], entry['os'], entry['version']
        if os_name not in structured["metadata"]:
            structured["metadata"][os_name] = {"openssl_version": ver}
        if algo not in structured["metrics"]:
            structured["metrics"][algo] = {}
        structured["metrics"][algo][os_name] = [
            entry['16b'], entry['64b'], entry['256b'], 
            entry['1024b'], entry['8192b'], entry['16384b']
        ]
    return structured

if __name__ == "__main__":
    group_start("Benchmark Telemetry Processor")
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    extracted = parse_raw_logs()
    if not extracted:
        log.error("Parsing failed: Check if benchmark logs exist.")
        sys.exit(1)

    try:
        with open(JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(transform_to_json(extracted), f, indent=4)
        notice(f"Benchmark JSON updated successfully")
    except Exception as e:
        log.error(f"IO Error: {str(e)}")
        sys.exit(1)
        
    log.info(f"Processed {len(extracted)} metrics across {len(set(d['os'] for d in extracted))} environments.")
    group_end()