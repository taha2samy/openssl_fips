# syntax=docker/dockerfile:1

ARG FIPS_VERSION=3.1.2
ARG CORE_VERSION=3.4.0
ARG BASE_IMAGE=cgr.dev/chainguard/wolfi-base:latest
ARG STATIC_IMAGE=cgr.dev/chainguard/static:latest

FROM ${BASE_IMAGE} AS fips-builder
ARG FIPS_VERSION
RUN --mount=type=cache,target=/var/cache/apk \
    apk add build-base perl linux-headers wget ca-certificates
WORKDIR /src
RUN wget -q https://www.openssl.org/source/old/3.1/openssl-${FIPS_VERSION}.tar.gz || \
    wget -q https://www.openssl.org/source/openssl-${FIPS_VERSION}.tar.gz && \
    tar -xf openssl-${FIPS_VERSION}.tar.gz && \
    cd openssl-${FIPS_VERSION} && \
    ./Configure enable-fips && \
    make -j$(nproc)

FROM ${BASE_IMAGE} AS core-builder
ARG CORE_VERSION
RUN --mount=type=cache,target=/var/cache/apk \
    apk add build-base perl linux-headers wget ca-certificates
WORKDIR /src
RUN wget -q https://www.openssl.org/source/openssl-${CORE_VERSION}.tar.gz || \
    wget -q https://www.openssl.org/source/old/3.4/openssl-${CORE_VERSION}.tar.gz && \
    tar -xf openssl-${CORE_VERSION}.tar.gz && \
    cd openssl-${CORE_VERSION} && \
    ./Configure enable-fips shared --prefix=/usr/local --openssldir=/usr/local/ssl && \
    make -j$(nproc) && \
    make install_sw install_ssldirs

FROM core-builder AS fips-integrator
ARG FIPS_VERSION
COPY --from=fips-builder /src/openssl-${FIPS_VERSION}/providers/fips.so /usr/local/lib/ossl-modules/fips.so
RUN /usr/local/bin/openssl fipsinstall \
    -out /usr/local/ssl/fipsmodule.cnf \
    -module /usr/local/lib/ossl-modules/fips.so && \
    sed -i "s|# .include fipsmodule.cnf|.include /usr/local/ssl/fipsmodule.cnf|" /usr/local/ssl/openssl.cnf && \
    sed -i 's|# fips = fips_sect|fips = fips_sect|' /usr/local/ssl/openssl.cnf

FROM ${BASE_IMAGE} AS helper
RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache libstdc++ zlib tzdata posix-libc-utils
RUN addgroup -g 1000 openssl && adduser -u 1000 -G openssl -D -s /bin/bash openssl
RUN mkdir -p /etc && touch /etc/nsswitch.conf
RUN cp /usr/share/zoneinfo/UTC /etc/localtime && echo "UTC" > /etc/timezone

FROM ${BASE_IMAGE} AS openssl-standard
RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache libgcc bash curl tzdata zlib
COPY --from=helper /etc/passwd /etc/group /etc/
COPY --from=fips-integrator /usr/local /usr/local
ENV PATH="/usr/local/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/lib:/usr/local/lib64" \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
USER openssl
WORKDIR /home/openssl
ENTRYPOINT ["/usr/local/bin/openssl"]

FROM ${STATIC_IMAGE} AS openssl-distroless
COPY --from=helper /etc/passwd /etc/group /etc/
COPY --from=helper /etc/nsswitch.conf /etc/nsswitch.conf
COPY --from=helper /etc/localtime /etc/localtime
COPY --from=helper /etc/timezone /etc/timezone
COPY --from=helper /etc/ssl/certs /etc/ssl/certs
COPY --from=helper /usr/lib/libstdc++.so* /usr/lib/
COPY --from=helper /usr/lib/libgcc_s.so* /usr/lib/
COPY --from=helper /usr/lib/libz.so* /usr/lib/
COPY --from=helper /lib/ld-linux-* /lib/ 2>/dev/null || true
COPY --from=helper /lib/libc.so* /lib/

COPY --from=fips-integrator /usr/local /usr/local

ENV PATH="/usr/local/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/lib:/usr/local/lib64:/lib:/usr/lib" \
    LANG=C.UTF-8 \
    TZ=UTC
    
USER openssl
WORKDIR /home/openssl
ENTRYPOINT ["/usr/local/bin/openssl"]