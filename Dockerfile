# syntax=docker/dockerfile:1

ARG FIPS_VERSION
ARG CORE_VERSION
ARG BASE_IMAGE=cgr.dev/chainguard/wolfi-base:latest
ARG STATIC_IMAGE=cgr.dev/chainguard/static:latest
ARG BUILD_BASE_VER
ARG PERL_VER
ARG LINUX_HEADERS_VER
ARG WGET_VER
ARG CA_CERTIFICATES_VER
ARG LIBSTDC_PLUS_PLUS_VER
ARG ZLIB_VER
ARG TZDATA_VER
ARG POSIX_LIBC_UTILS_VER
FROM ${BASE_IMAGE} AS fips-builder
ARG BUILD_BASE_VER
ARG PERL_VER
ARG LINUX_HEADERS_VER
ARG WGET_VER
ARG CA_CERTIFICATES_VER
ARG FIPS_VERSION
RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache \
    build-base=${BUILD_BASE_VER} \
    perl=${PERL_VER} \
    linux-headers=${LINUX_HEADERS_VER} \
    wget=${WGET_VER} \
    ca-certificates=${CA_CERTIFICATES_VER}

WORKDIR /src
RUN wget -q https://www.openssl.org/source/old/3.1/openssl-${FIPS_VERSION}.tar.gz || \
    wget -q https://www.openssl.org/source/openssl-${FIPS_VERSION}.tar.gz && \
    tar -xf openssl-${FIPS_VERSION}.tar.gz && \
    cd openssl-${FIPS_VERSION} && \
    ./Configure enable-fips && \
    make -j$(nproc)

FROM ${BASE_IMAGE} AS core-builder
ARG CORE_VERSION
ARG BUILD_BASE_VER
ARG PERL_VER
ARG LINUX_HEADERS_VER
ARG WGET_VER
ARG CA_CERTIFICATES_VER
RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache \
    build-base=${BUILD_BASE_VER} \
    perl=${PERL_VER} \
    linux-headers=${LINUX_HEADERS_VER} \
    wget=${WGET_VER} \
    ca-certificates=${CA_CERTIFICATES_VER}
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
    sed -i 's|# \.include fipsmodule.cnf|.include /usr/local/ssl/fipsmodule.cnf|' /usr/local/ssl/openssl.cnf && \
    sed -i 's|# fips = fips_sect|fips = fips_sect\nbase = base_sect|' /usr/local/ssl/openssl.cnf && \
    sed -i 's|# activate = 1|activate = 1|g' /usr/local/ssl/openssl.cnf && \
    printf "\n[base_sect]\nactivate = 1\n" >> /usr/local/ssl/openssl.cnf && \
    sed -i 's|default = default_sect|# default = default_sect|' /usr/local/ssl/openssl.cnf

FROM ${BASE_IMAGE} AS helper
ARG LIBSTDC_PLUS_PLUS_VER
ARG ZLIB_VER
ARG TZDATA_VER
ARG POSIX_LIBC_UTILS_VER
RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache libstdc++=${LIBSTDC_PLUS_PLUS_VER} zlib=${ZLIB_VER} tzdata=${TZDATA_VER} posix-libc-utils=${POSIX_LIBC_UTILS_VER}
RUN addgroup -g 1000 openssl && adduser -u 1000 -G openssl -D -s /bin/bash openssl
RUN mkdir -p /etc && touch /etc/nsswitch.conf
RUN cp /usr/share/zoneinfo/UTC /etc/localtime && echo "UTC" > /etc/timezone

FROM ${BASE_IMAGE} AS openssl-standard
ARG LIBSTDC_PLUS_PLUS_VER
ARG TZDATA_VER
ARG ZLIB_VER
RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache libgcc=${LIBSTDC_PLUS_PLUS_VER} tzdata=${TZDATA_VER} zlib=${ZLIB_VER}
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
COPY --from=helper /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=helper /etc/localtime /etc/localtime
COPY --from=helper /etc/timezone /etc/timezone
COPY --from=helper /etc/ssl/certs /etc/ssl/certs
COPY --from=helper /usr/lib/libstdc++.so* /usr/lib/
COPY --from=helper /usr/lib/libgcc_s.so* /usr/lib/
COPY --from=helper /usr/lib/libz.so* /usr/lib/
COPY --from=helper /usr/lib/libc.so* /usr/lib/
COPY --from=helper /usr/lib/libpthread.so* /usr/lib/
COPY --from=helper /usr/lib/libm.so* /usr/lib/
COPY --from=helper /usr/lib/libdl.so* /usr/lib/
COPY --from=helper /usr/lib/librt.so* /usr/lib/
COPY --from=helper /lib/ld-linux-* /lib/

COPY --from=fips-integrator /usr/local /usr/local

ENV PATH="/usr/local/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/lib:/usr/local/lib64:/lib:/usr/lib" \
    LANG=C.UTF-8 \
    TZ=UTC

USER openssl
WORKDIR /home/openssl
ENTRYPOINT ["/usr/local/bin/openssl"]
