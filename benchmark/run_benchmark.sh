#!/bin/bash
set -e
rm -rf ./bench_results/*.log
RESULT_DIR="$(pwd)/bench_results"
mkdir -p "$RESULT_DIR"

docker rmi fips-bench debian-bench alpine-bench ubuntu-bench -f 2>/dev/null || true

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
TEST_TIME=10

set +e
ALGS="aes-256-gcm sha256 sha512 sha3-256 rsa2048 ecdsap256 ecdhp256"
for alg in $ALGS; do
    echo "Testing $alg..."
    
    docker run --rm --entrypoint sh fips-bench -c "openssl speed -multi $NPROC -seconds $TEST_TIME -evp $alg" >> "$RESULT_DIR/fips.log" 2>&1 || echo "$alg not supported" >> "$RESULT_DIR/fips.log"
    
    docker run --rm --entrypoint sh debian-bench -c "openssl speed -multi $NPROC -seconds $TEST_TIME -evp $alg" >> "$RESULT_DIR/debian.log" 2>&1 || echo "$alg not supported" >> "$RESULT_DIR/debian.log"
    
    docker run --rm --entrypoint sh alpine-bench -c "openssl speed -multi $NPROC -seconds $TEST_TIME -evp $alg" >> "$RESULT_DIR/alpine.log" 2>&1 || echo "$alg not supported" >> "$RESULT_DIR/alpine.log"
    
    docker run --rm --entrypoint sh ubuntu-bench -c "openssl speed -multi $NPROC -seconds $TEST_TIME -evp $alg" >> "$RESULT_DIR/ubuntu.log" 2>&1 || echo "$alg not supported" >> "$RESULT_DIR/ubuntu.log"

done

set -e
echo "✅ All logs generated in $RESULT_DIR"