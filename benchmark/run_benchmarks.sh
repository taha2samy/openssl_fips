#!/bin/bash
set -e

RESULT_DIR="$(pwd)/bench_results"
mkdir -p "$RESULT_DIR"

docker rmi fips-bench debian-bench alpine-bench ubuntu-bench -f 2>/dev/null || true

echo "🏗️ Building Benchmark Images..."

docker build -t fips-bench - <<EOF
FROM ghcr.io/taha2samy/wolfi-openssl-fips:latest
USER root
ENTRYPOINT ["openssl"]
EOF

docker build -t debian-bench - <<EOF
FROM debian:bookworm-slim
RUN apt update && apt install -y openssl && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["openssl"]
EOF

docker build -t alpine-bench - <<EOF
FROM alpine:latest
RUN apk add --no-cache openssl
ENTRYPOINT ["openssl"]
EOF

docker build -t ubuntu-bench - <<EOF
FROM ubuntu:latest
RUN apt update && apt install -y openssl && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["openssl"]
EOF

NPROC=$(nproc)


TEST_TIME=3

echo "🚀 Running Benchmarks..."

docker run --rm --entrypoint sh fips-bench -c \
"openssl version && echo && openssl speed -multi $NPROC -seconds $TEST_TIME -evp aes-256-gcm sha256 sha512 ed25519 rsa2048" \
> "$RESULT_DIR/fips.log" 2>&1
echo "FIPS done"
docker run --rm --entrypoint sh debian-bench -c \
"openssl version && echo && openssl speed -multi $NPROC -seconds $TEST_TIME -evp aes-256-gcm sha256 sha512 ed25519 rsa2048" \
> "$RESULT_DIR/debian.log" 2>&1
echo "debian done"
docker run --rm --entrypoint sh alpine-bench -c \
"openssl version && echo && openssl speed -multi $NPROC -seconds $TEST_TIME -evp aes-256-gcm sha256 sha512 ed25519 rsa2048" \
> "$RESULT_DIR/alpine.log" 2>&1
echo "alpine done"
docker run --rm --entrypoint sh ubuntu-bench -c \
"openssl version && echo && openssl speed -multi $NPROC -seconds $TEST_TIME -evp aes-256-gcm sha256 sha512 ed25519 rsa2048" \
> "$RESULT_DIR/ubuntu.log" 2>&1
echo "ubuntu done"

echo "✅ All logs generated in $RESULT_DIR"
