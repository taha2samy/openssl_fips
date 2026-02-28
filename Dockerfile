# syntax=docker/dockerfile:1

# --- Base Images ---
ARG BASE_IMAGE
ARG STATIC_IMAGE
# --- Version Variables ---
ARG FIPS_VERSION
ARG CORE_VERSION
ARG APK_TOOLS_VER
ARG BUSYBOX_VER
ARG GLIBC_VER
ARG GLIBC_LOCALE_POSIX_VER
ARG LD_LINUX_VER
ARG LIBCRYPT1_VER
ARG LIBXCRYPT_VER
ARG LIBGCC_VER
ARG WOLFI_BASE_VER
ARG WOLFI_BASELAYOUT_VER
ARG WOLFI_KEYS_VER

# --- Build Stage Packages ---
ARG BUILD_BASE_VER
ARG PERL_VER
ARG LINUX_HEADERS_VER
ARG WGET_VER
ARG CA_CERTIFICATES_VER

# --- Runtime & Helper Packages ---
ARG LIBSTDC_PLUS_PLUS_VER
ARG ZLIB_VER
ARG TZDATA_VER
ARG POSIX_LIBC_UTILS_VER

# --- Dev Tools (SDK Only) ---
ARG PKGCONF_VER
ARG PCRE_DEV_VER
ARG ZLIB_DEV_VER
ARG BASH_VER
ARG CURL_VER
ARG JQ_VER
ARG UNZIP_VER

FROM ${BASE_IMAGE} as producer
ARG APK_TOOLS_VER
ARG BUSYBOX_VER
ARG GLIBC_VER
ARG GLIBC_LOCALE_POSIX_VER
ARG LD_LINUX_VER
ARG LIBCRYPT1_VER
ARG LIBXCRYPT_VER
ARG LIBGCC_VER
ARG WOLFI_BASE_VER
ARG WOLFI_BASELAYOUT_VER
ARG WOLFI_KEYS_VER
ARG BUILD_BASE_VER
ARG PERL_VER
ARG LINUX_HEADERS_VER
ARG WGET_VER
ARG CA_CERTIFICATES_VER
ARG LIBSTDC_PLUS_PLUS_VER
ARG ZLIB_VER
ARG TZDATA_VER
ARG POSIX_LIBC_UTILS_VER
ARG PKGCONF_VER
ARG PCRE_DEV_VER
ARG ZLIB_DEV_VER
ARG BASH_VER
ARG CURL_VER
ARG JQ_VER
ARG UNZIP_VER
USER root
RUN mkdir -p /rootfs/distroless /rootfs/standard /rootfs/development
RUN apk add tree
# RUN --mount=type=cache,target=/var/cache/apk \
#     set -eux; \
#     apk add --no-cache \
#     --initdb \
#     --no-scripts \
#     --root /rootfs/distroless \
#     --keys-dir /etc/apk/keys \
#     --repositories-file /etc/apk/repositories \
#     wolfi-baselayout=${WOLFI_BASELAYOUT_VER} \
#     wolfi-keys=${WOLFI_KEYS_VER} \
#     glibc=${GLIBC_VER} \
#     libgcc=${LIBGCC_VER} \
#     zlib=${ZLIB_VER} \
#     tzdata=${TZDATA_VER} \
#     ca-certificates=${CA_CERTIFICATES_VER}; \
#     mkdir -p /rootfs/distroless/etc/apk; \
#     cp -a /etc/apk/keys /rootfs/distroless/etc/apk/; \
#     cp -a /etc/apk/repositories /rootfs/distroless/etc/apk/; \
#     cp -a /etc/passwd /rootfs/distroless/etc/; \
#     cp -a /etc/group /rootfs/distroless/etc/; \
#     cp -a /etc/shadow /rootfs/distroless/etc/
RUN --mount=type=cache,target=/var/cache/apk \
    set -eux; \
    apk add --no-cache \
    --initdb \
    --no-scripts \
    --root /rootfs/standard \
    --keys-dir /etc/apk/keys \
    --repositories-file /etc/apk/repositories \
    wolfi-baselayout=${WOLFI_BASELAYOUT_VER} \
    wolfi-keys=${WOLFI_KEYS_VER} \
    glibc=${GLIBC_VER} \
    libgcc=${LIBGCC_VER} \
    zlib=${ZLIB_VER} \
    tzdata=${TZDATA_VER} \
    ca-certificates=${CA_CERTIFICATES_VER} \
    busybox=${BUSYBOX_VER} \
    posix-libc-utils=${POSIX_LIBC_UTILS_VER} \
    libstdc++=${LIBSTDC_PLUS_PLUS_VER}; \
    mkdir -p /rootfs/standard/etc/apk; \
    cp -a /etc/apk/keys /rootfs/standard/etc/apk/; \
    cp -a /etc/apk/repositories /rootfs/standard/etc/apk/; \
    cp -a /etc/passwd /rootfs/standard/etc/; \
    cp -a /etc/group /rootfs/standard/etc/; \
    cp -a /etc/shadow /rootfs/standard/etc/
RUN chroot /rootfs/standard /usr/bin/busybox --install -s /usr/bin
RUN ln -sf busybox /rootfs/standard/usr/bin/sh
RUN echo "======================================================"
RUN tree -a -F /rootfs/standard

# RUN --mount=type=cache,target=/var/cache/apk \
#     set -eux; \
#     apk add --no-cache \
#     --initdb \
#     --no-scripts \
#     --root /rootfs/development \
#     --keys-dir /etc/apk/keys \
#     --repositories-file /etc/apk/repositories \
#     wolfi-baselayout=${WOLFI_BASELAYOUT_VER} \
#     wolfi-keys=${WOLFI_KEYS_VER} \
#     glibc=${GLIBC_VER} \
#     libgcc=${LIBGCC_VER} \
#     zlib=${ZLIB_VER} \
#     tzdata=${TZDATA_VER} \
#     ca-certificates=${CA_CERTIFICATES_VER} \
#     busybox=${BUSYBOX_VER} \
#     posix-libc-utils=${POSIX_LIBC_UTILS_VER} \
#     libstdc++=${LIBSTDC_PLUS_PLUS_VER} \
#     build-base=${BUILD_BASE_VER} \
#     pkgconf=${PKGCONF_VER} \
#     pcre-dev=${PCRE_DEV_VER} \
#     zlib-dev=${ZLIB_DEV_VER} \
#     bash=${BASH_VER} \
#     curl=${CURL_VER} \
#     jq=${JQ_VER} \
#     unzip=${UNZIP_VER}; \
#     mkdir -p /rootfs/development/etc/apk; \
#     cp -a /etc/apk/keys /rootfs/development/etc/apk/; \
#     cp -a /etc/apk/repositories /rootfs/development/etc/apk/; \
#     cp -a /etc/passwd /rootfs/development/etc/; \
#     cp -a /etc/group /rootfs/development/etc/; \
#     cp -a /etc/shadow /rootfs/development/etc/

# RUN /rootfs/standard/usr/bin/busybox --install -s /rootfs/standard/usr/bin && \
#     ln -sf busybox /rootfs/standard/usr/bin/sh



FROM ${STATIC_IMAGE} AS distroless
COPY --from=producer /rootfs/distroless /
ENV PATH="/usr/local/bin:/usr/bin:/bin"


FROM ${STATIC_IMAGE} AS standard
COPY --from=producer /rootfs/standard /
ENV PATH="/usr/local/bin:/usr/bin:/bin"


FROM ${STATIC_IMAGE} AS development
COPY --from=producer /rootfs/development /
ENV PATH="/usr/local/bin:/usr/bin:/bin"


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
    tar -xf openssl-${FIPS_VERSION}.tar.gz

WORKDIR /src/openssl-${FIPS_VERSION}
RUN ./Configure enable-fips && \
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
    tar -xf openssl-${CORE_VERSION}.tar.gz

WORKDIR /src/openssl-${CORE_VERSION}
RUN ./Configure enable-fips shared --prefix=/usr/local --openssldir=/usr/local/ssl && \
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
    -pedantic \
    -hmac_key_check \
    -kmac_key_check \
    -hkdf_digest_check \
    -hkdf_key_check \
    -kbkdf_key_check \
    -tls13_kdf_digest_check \
    -tls13_kdf_key_check \
    -tls1_prf_digest_check \
    -tls1_prf_key_check \
    -no_drbg_truncated_digests \
    -tdes_encrypt_disabled \
    -signature_digest_check \
    -rsa_pkcs15_padding_disabled \
    -rsa_pss_saltlen_check \
    -rsa_sign_x931_disabled \
    -dsa_sign_disabled \
    -ecdh_cofactor_check \
    -ems_check \
    -no_short_mac

COPY conf/openssl.cnf /usr/local/ssl/openssl.cnf
RUN cat /usr/local/ssl/fipsmodule.cnf

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

FROM standard AS openssl-standard
ARG CORE_VERSION
ARG FIPS_VERSION

LABEL org.opencontainers.image.title="Wolfi OpenSSL FIPS (Standard)" \
    org.opencontainers.image.vendor="taha2samy" \
    org.opencontainers.image.core-version="${CORE_VERSION}" \
    org.opencontainers.image.fips-version="${FIPS_VERSION}"
COPY --from=producer /rootfs/standard /

COPY --from=fips-integrator /usr/local/bin/openssl /usr/local/bin/openssl
COPY --from=fips-integrator /usr/local/lib/libcrypto.so.3 /usr/local/lib/
COPY --from=fips-integrator /usr/local/lib/libssl.so.3 /usr/local/lib/

COPY --from=fips-integrator /usr/local/lib/ossl-modules /usr/local/lib/ossl-modules
COPY --from=fips-integrator /usr/local/ssl /usr/local/ssl

RUN ln -s /usr/local/lib/libcrypto.so.3 /usr/local/lib/libcrypto.so && \
    ln -s /usr/local/lib/libssl.so.3 /usr/local/lib/libssl.so 

#ldconfig

ENV PATH="/usr/local/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/lib:/usr/lib:/lib" \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
    OPENSSL_CONF=/usr/local/ssl/openssl.cnf \
    OPENSSL_MODULES=/usr/local/lib/ossl-modules \
    TZ=UTC \
    LANG=C.UTF-8

USER nonroot
WORKDIR /home/user/nonroot

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

FROM ${BASE_IMAGE} AS openssl-dev
ARG CORE_VERSION
ARG FIPS_VERSION
ARG BUILD_BASE_VER
ARG POSIX_LIBC_UTILS_VER
ARG PKGCONF_VER
ARG PCRE_DEV_VER
ARG ZLIB_DEV_VER
ARG BASH_VER
ARG CURL_VER
ARG JQ_VER
ARG UNZIP_VER

RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache \
    build-base=${BUILD_BASE_VER} \
    pkgconf=${PKGCONF_VER} \
    pcre-dev=${PCRE_DEV_VER} \
    zlib-dev=${ZLIB_DEV_VER} \
    posix-libc-utils=${POSIX_LIBC_UTILS_VER} \
    bash=${BASH_VER} \
    curl=${CURL_VER} \
    jq=${JQ_VER} \
    unzip=${UNZIP_VER}

COPY --from=fips-integrator /usr/local /usr/local

RUN ln -sf /usr/local/lib/libssl.so.3 /usr/local/lib/libssl.so && \
    ln -sf /usr/local/lib/libcrypto.so.3 /usr/local/lib/libcrypto.so

COPY --from=helper /etc/passwd /etc/group /etc/

ENV PATH="/usr/local/bin:${PATH}" \
    CPATH="/usr/local/include" \
    LIBRARY_PATH="/usr/local/lib" \
    LD_LIBRARY_PATH="/usr/local/lib:/usr/local/lib64" \
    PKG_CONFIG_PATH="/usr/local/lib/pkgconfig" \
    OPENSSL_CONF=/usr/local/ssl/openssl.cnf

LABEL org.opencontainers.image.title="Wolfi OpenSSL FIPS (development)" \
    org.opencontainers.image.description="FIPS 140-3 compliant OpenSSL container (development)" \
    org.opencontainers.image.vendor="taha2samy" \
    org.opencontainers.image.core-version="${CORE_VERSION}" \
    org.opencontainers.image.fips-version="${FIPS_VERSION}" \
    org.opencontainers.image.licenses="Apache-2.0" \
    org.opencontainers.image.source="https://github.com/taha2samy/openssl_fips" 

USER openssl
WORKDIR /home/openssl

HEALTHCHECK --interval=30s --timeout=3s --start-period=2s --retries=3 \
    CMD /usr/local/bin/openssl list -providers | grep -q fips || exit 1

ENTRYPOINT ["/bin/bash"]