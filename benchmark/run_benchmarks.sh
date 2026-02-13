#!/bin/bash
set -e

echo "🧹 Cleaning old benchmark images..."
docker rmi fips-bench debian-bench -f 2>/dev/null || true

RESULT_DIR="$(pwd)/bench_results"
mkdir -p "$RESULT_DIR"

echo "🏗️ Building FIPS-Bench (Wolfi)..."
docker build -t fips-bench - <<EOF
FROM ghcr.io/taha2samy/wolfi-openssl-fips:latest
USER root
ENTRYPOINT ["openssl"]
EOF

echo "🏗️ Building Debian-Bench..."
docker build -t debian-bench - <<EOF
FROM debian:bookworm-slim
RUN apt update && apt install -y openssl && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["openssl"]
EOF

NPROC=$(nproc)
SECONDS_of_test=20

echo "🚀 Running FIPS Benchmark ($NPROC cores, $SECONDS_of_test sec)..."
docker run --rm fips-bench speed -multi $NPROC -seconds $SECONDS_of_test -evp aes-256-gcm sha256 sha512 ed25519 rsa2048 > "$RESULT_DIR/fips.log" 2>&1
echo $SECONDS_of_test heeeeeeeeeeeeeeeeeeeeeeeeeeeee
echo "🚀 Running Debian Benchmark ($NPROC cores, $SECONDS_of_test sec)..."
docker run --rm debian-bench speed -multi $NPROC -seconds $SECONDS_of_test -evp aes-256-gcm sha256 sha512 ed25519 rsa2048 > "$RESULT_DIR/debian.log" 2>&1

echo "✅ All logs generated in $RESULT_DIR"