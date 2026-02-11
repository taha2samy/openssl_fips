#!/usr/bin/env bash
set -e

CMD="$*"
LOG=benchmark.log
MD=benchmark.md

if [ -z "$CMD" ]; then
  echo "Usage: ./bench.sh <command>"
  exit 1
fi

# شغّل الأمر وسجّل اللوج
eval "$CMD" | tee "$LOG" >/dev/null

# طلّع Markdown
awk -v cmd="$CMD" '
BEGIN {
    print "# OpenSSL Benchmark";
    print "";
    print "## Command";
    print "```bash";
    print cmd;
    print "```";
    print "";
    print "| Operation | Time (s/op) | Ops/s |";
    print "|-----------|------------|-------|";
}
/rsa  2048 bits/ {
    printf "| Private Sign | %.6f | %.1f |\n", $5, $9;
    printf "| Public Verify | %.6f | %.1f |\n", $6, $10;
    printf "| Public Encrypt | %.6f | %.1f |\n", $7, $11;
    printf "| Private Decrypt | %.6f | %.1f |\n", $8, $12;
}
/rsa2048 0\./ {
    printf "| Keygen | %.6f | %.1f |\n", $2, $5;
    printf "| Encaps | %.6f | %.1f |\n", $3, $6;
    printf "| Decaps | %.6f | %.1f |\n", $4, $7;
}
' "$LOG" > "$MD"

echo "✔ Logs: $LOG"
echo "✔ Report: $MD"
