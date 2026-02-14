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
RUN ldconfig
COPY --from=fips-builder /src/openssl-${FIPS_VERSION}/providers/fips.so /usr/local/lib/ossl-modules/fips.so
RUN /usr/local/bin/openssl fipsinstall \
    -module /usr/local/lib/ossl-modules/fips.so \
    -out /usr/local/ssl/fipsmodule.cnf \
    -self_test_onload \
    -hmac_key_check \
    -tdes_encrypt_disabled

COPY conf/openssl.cnf /usr/local/ssl/openssl.cnf
# RUN cat /usr/local/ssl/fipsmodule.cnf
# RUN sed -i 's/hmac-key-check = 0/hmac-key-check = 1/g' /usr/local/ssl/fipsmodule.cnf
# RUN sed -i 's/tdes-encrypt-disabled = 0/tdes-encrypt-disabled = 1/g' /usr/local/ssl/fipsmodule.cnf
# RUN sed -i 's/security-checks = 0/security-checks = 1/g' /usr/local/ssl/fipsmodule.cnf
# RUN cat /usr/local/ssl/fipsmodule.cnf


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
RUN mkdir -p /etc && touch /etc/nsswitch.conf


FROM ${BASE_IMAGE} AS openssl-standard
ARG CORE_VERSION
ARG FIPS_VERSION
LABEL org.opencontainers.image.title="Wolfi OpenSSL FIPS (Standard)" \
    org.opencontainers.image.description="FIPS 140-3 compliant OpenSSL container (standard)" \
    org.opencontainers.image.vendor="taha2samy" \
    org.opencontainers.image.core-version="${CORE_VERSION}" \
    org.opencontainers.image.fips-version="${FIPS_VERSION}" \
    org.opencontainers.image.licenses="Apache-2.0" \
    org.opencontainers.image.source="https://github.com/taha2samy/openssl_fips" 
ARG LIBSTDC_PLUS_PLUS_VER
ARG TZDATA_VER
ARG ZLIB_VER

RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache libgcc=${LIBSTDC_PLUS_PLUS_VER} tzdata=${TZDATA_VER} zlib=${ZLIB_VER}

COPY --from=helper /etc/passwd /etc/group /etc/
COPY --from=helper /etc/ssl/certs /etc/ssl/certs
COPY --from=helper /usr/share/zoneinfo/UTC /usr/share/zoneinfo/UTC
COPY --from=helper /etc/localtime /etc/localtime
COPY --from=helper /etc/timezone /etc/timezone

COPY --from=fips-integrator /usr/local/bin/openssl /usr/local/bin/openssl
COPY --from=fips-integrator /usr/local/lib/libcrypto.so.3 /usr/local/lib/
COPY --from=fips-integrator /usr/local/lib/libssl.so.3 /usr/local/lib/

RUN ln -s /usr/local/lib/libcrypto.so.3 /usr/local/lib/libcrypto.so && \
    ln -s /usr/local/lib/libssl.so.3 /usr/local/lib/libssl.so

COPY --from=fips-integrator /usr/local/lib/ossl-modules /usr/local/lib/ossl-modules
COPY --from=fips-integrator /usr/local/ssl /usr/local/ssl

ENV PATH="/usr/local/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/lib:/usr/local/lib64" \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
    OPENSSL_CONF=/usr/local/ssl/openssl.cnf \
    OPENSSL_MODULES=/usr/local/lib/ossl-modules \
    TZ=UTC


USER openssl
WORKDIR /home/openssl

HEALTHCHECK --interval=30s --timeout=3s --start-period=2s --retries=3 \
    CMD /usr/local/bin/openssl list -providers | grep -q fips || exit 1

ENTRYPOINT ["/usr/local/bin/openssl"]
FROM ${STATIC_IMAGE} AS openssl-distroless
ARG CORE_VERSION
ARG FIPS_VERSION

LABEL org.opencontainers.image.title="Wolfi OpenSSL FIPS (distroless)" \
    org.opencontainers.image.description="FIPS 140-3 compliant OpenSSL container (distroless)" \
    org.opencontainers.image.vendor="taha2samy" \
    org.opencontainers.image.core-version="${CORE_VERSION}" \
    org.opencontainers.image.fips-version="${FIPS_VERSION}" \
    org.opencontainers.image.licenses="Apache-2.0" \
    org.opencontainers.image.source="https://github.com/taha2samy/openssl_fips" 

COPY --from=openssl-standard /etc/passwd /etc/group /etc/
COPY --from=openssl-standard /etc/ssl/certs /etc/ssl/certs
COPY --from=openssl-standard /etc/localtime /etc/localtime
COPY --from=openssl-standard /etc/timezone /etc/timezone
COPY --from=openssl-standard /usr/share/zoneinfo/UTC /usr/share/zoneinfo/UTC

COPY --from=openssl-standard /usr/lib/libgcc_s.so* /usr/lib/
COPY --from=openssl-standard /usr/lib/libz.so* /usr/lib/
COPY --from=openssl-standard /lib/ld-linux-* /lib/
COPY --from=openssl-standard /lib/libc.so* /lib/

COPY --from=openssl-standard /usr/local/bin/openssl /usr/local/bin/openssl
COPY --from=openssl-standard /usr/local/lib/libcrypto.so* /usr/local/lib/
COPY --from=openssl-standard /usr/local/lib/libssl.so* /usr/local/lib/
COPY --from=openssl-standard /usr/local/lib/ossl-modules /usr/local/lib/ossl-modules
COPY --from=openssl-standard /usr/local/ssl /usr/local/ssl
COPY --from=helper /etc/nsswitch.conf /etc/nsswitch.conf
COPY --from=openssl-standard /usr/lib/libnss_dns.so* /usr/lib/
COPY --from=openssl-standard /usr/lib/libnss_files.so* /usr/lib/

ENV PATH="/usr/local/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/lib:/lib:/usr/lib" \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
    OPENSSL_CONF=/usr/local/ssl/openssl.cnf \
    OPENSSL_MODULES=/usr/local/lib/ossl-modules \
    LANG=C.UTF-8 \
    TZ=UTC

USER openssl
WORKDIR /home/openssl

HEALTHCHECK --interval=30s --timeout=3s --start-period=2s --retries=3 \
    CMD ["/usr/local/bin/openssl", "sha256", "/dev/null"]

ENTRYPOINT ["/usr/local/bin/openssl"]