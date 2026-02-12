# syntax=docker/dockerfile:1

ARG FIPS_VERSION=3.1.2
ARG CORE_VERSION=3.4.0
ARG BASE_IMAGE=cgr.dev/chainguard/wolfi-base:latest
ARG STATIC_IMAGE=cgr.dev/chainguard/static:latest

# -----------------------------------------------------------------------------
# Stage 1: Build FIPS Provider (OpenSSL 3.1)
# -----------------------------------------------------------------------------
FROM ${BASE_IMAGE} AS fips-builder
ARG FIPS_VERSION
RUN --mount=type=cache,target=/var/cache/apk \
    apk add build-base perl linux-headers wget ca-certificates
WORKDIR /src
RUN wget -q https://www.openssl.org/source/openssl-${FIPS_VERSION}.tar.gz || \
    wget -q https://www.openssl.org/source/old/3.1/openssl-${FIPS_VERSION}.tar.gz && \
    tar -xf openssl-${FIPS_VERSION}.tar.gz && \
    cd openssl-${FIPS_VERSION} && \
    ./Configure enable-fips && \
    make -j$(nproc)

# -----------------------------------------------------------------------------
# Stage 2: Build Core OpenSSL (OpenSSL 3.4)
# -----------------------------------------------------------------------------
FROM ${BASE_IMAGE} AS core-builder
ARG CORE_VERSION
RUN --mount=type=cache,target=/var/cache/apk \
    apk add build-base perl linux-headers wget ca-certificates zlib-dev
WORKDIR /src
RUN wget -q https://www.openssl.org/source/openssl-${CORE_VERSION}.tar.gz || \
    wget -q https://www.openssl.org/source/old/3.4/openssl-${CORE_VERSION}.tar.gz && \
    tar -xf openssl-${CORE_VERSION}.tar.gz && \
    cd openssl-${CORE_VERSION} && \
    ./Configure enable-fips shared zlib --prefix=/usr/local --openssldir=/usr/local/ssl && \
    make -j$(nproc) && \
    make install_sw install_ssldirs

# -----------------------------------------------------------------------------
# Stage 3: Integrate FIPS into Core
# -----------------------------------------------------------------------------
FROM core-builder AS fips-integrator
ARG FIPS_VERSION
COPY --from=fips-builder /src/openssl-${FIPS_VERSION}/providers/fips.so /usr/local/lib/ossl-modules/fips.so
RUN /usr/local/bin/openssl fipsinstall \
    -out /usr/local/ssl/fipsmodule.cnf \
    -module /usr/local/lib/ossl-modules/fips.so && \
    sed -i 's|# .include fipsmodule.cnf|.include /usr/local/ssl/fipsmodule.cnf|' /usr/local/ssl/openssl.cnf && \
    sed -i 's|# fips = fips_sect|fips = fips_sect|' /usr/local/ssl/openssl.cnf && \
    sed -i '/\[provider_sect\]/a base = base_sect' /usr/local/ssl/openssl.cnf && \
    sed -i 's|# activate = 1|activate = 1|g' /usr/local/ssl/openssl.cnf && \
    printf "\n[base_sect]\nactivate = 1\n" >> /usr/local/ssl/openssl.cnf && \
    sed -i 's|default = default_sect|# default = default_sect|' /usr/local/ssl/openssl.cnf

# -----------------------------------------------------------------------------
# Stage 4: Collect ONLY ESSENTIAL Runtime Dependencies
# -----------------------------------------------------------------------------
FROM ${BASE_IMAGE} AS minimal-runtime
# Install only the required libraries: zlib for compression, tzdata for time, and certs.
RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache zlib tzdata ca-certificates

# Create User
RUN addgroup -g 1000 openssl && adduser -u 1000 -G openssl -D -s /bin/sh openssl

# Prepare a clean output directory for configs and libraries
RUN mkdir -p /output/etc/ssl /output/lib /output/usr/lib

# Copy minimal required config files
COPY --from=0 /etc/passwd /etc/group /etc/nsswitch.conf /output/etc/
COPY --from=0 /etc/ssl/certs /output/etc/ssl/certs
COPY --from=0 /usr/share/zoneinfo/UTC /output/etc/localtime
RUN echo "UTC" > /output/etc/timezone

# Copy ONLY the essential shared libraries needed by OpenSSL
# We've removed libstdc++ as it's not needed.
RUN cp -L /lib/ld-linux-*.so.* /output/lib/ && \
    cp -L /usr/lib/libc.so* /output/usr/lib/ && \
    cp -L /usr/lib/libz.so* /output/usr/lib/ && \
    cp -L /usr/lib/libgcc_s.so* /output/usr/lib/ && \
    cp -L /usr/lib/libpthread.so* /output/usr/lib/ && \
    cp -L /usr/lib/libdl.so* /output/usr/lib/ && \
    cp -L /usr/lib/libm.so* /output/usr/lib/

# -----------------------------------------------------------------------------
# Stage 5: Final Image - Standard (Wolfi Base)
# -----------------------------------------------------------------------------
FROM ${BASE_IMAGE} AS openssl-standard
# Install minimal runtime dependencies using the package manager
RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache zlib tzdata ca-certificates
COPY --from=minimal-runtime /output/etc/passwd /output/etc/group /etc/
COPY --from=fips-integrator /usr/local /usr/local

ENV PATH="/usr/local/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/lib:/usr/local/lib64" \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

USER openssl
WORKDIR /home/openssl
ENTRYPOINT ["/usr/local/bin/openssl"]

# -----------------------------------------------------------------------------
# Stage 6: Final Image - Distroless (Static Base) - MINIMAL
# -----------------------------------------------------------------------------
FROM ${STATIC_IMAGE} AS openssl-distroless
# Copy all prepared configs, certs, and user info in one layer
COPY --from=minimal-runtime /output/etc /etc

# Copy all essential libraries in two layers
COPY --from=minimal-runtime /output/lib /lib
COPY --from=minimal-runtime /output/usr/lib /usr/lib

# Copy the compiled OpenSSL application
COPY --from=fips-integrator /usr/local /usr/local

ENV PATH="/usr/local/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/lib:/usr/local/lib64:/usr/lib:/lib" \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
    LANG=C.UTF-8 \
    TZ=UTC

USER openssl
WORKDIR /home/openssl
ENTRYPOINT ["/usr/local/bin/openssl"]
