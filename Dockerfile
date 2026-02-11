# syntax=docker/dockerfile:1

ARG OPENSSL_IMAGE

FROM ${OPENSSL_IMAGE} AS openssl-source

FROM alpine:3.19 AS fetcher
ARG TARGETARCH
ARG JAVA_URL_AMD64
ARG JAVA_URL_AARCH64
ARG JAVA_SHA_AMD64
ARG JAVA_SHA_AARCH64

RUN --mount=type=cache,target=/var/cache/java_download,id=java_downloads_{{ version }} \
    apk add --no-cache curl tar && \
    set -ux; \
    if [ "$TARGETARCH" = "amd64" ]; then \
    URL=$JAVA_URL_AMD64; SHA=$JAVA_SHA_AMD64; \
    else \
    URL=$JAVA_URL_AARCH64; SHA=$JAVA_SHA_AARCH64; \
    fi; \
    FILENAME=$(basename "$URL"); \
    if [ ! -f "/var/cache/java_download/$FILENAME" ]; then \
    curl -LfsS "$URL" -o "/var/cache/java_download/$FILENAME"; \
    fi; \
    echo "$SHA  /var/cache/java_download/$FILENAME" | sha256sum -c - && \
    mkdir -p /opt/java-full && \
    tar -xzf "/var/cache/java_download/$FILENAME" -C /opt/java-full --strip-components=1 && \
    find /opt/java-full -exec touch -t 202001010000 {} +

FROM cgr.dev/chainguard/wolfi-base@{{WOLFI_BASE_DIGEST}} AS cleaner
COPY --from=fetcher /opt/java-full /opt/java-slim

{% if version == '8' %}
RUN rm -rf /opt/java-slim/src.zip \
    /opt/java-slim/demo \
    /opt/java-slim/sample \
    /opt/java-slim/man
{% else %}
RUN rm -rf /opt/java-slim/jmods \
    /opt/java-slim/lib/src.zip \
    /opt/java-slim/demo \
    /opt/java-slim/sample \
    /opt/java-slim/man \
    /opt/java-slim/docs
{% endif %}

WORKDIR /tmp/java-conf

RUN echo "name = OpenSSL-FIPS" > fips.cfg && \
    echo "library = /usr/local/lib/libcrypto.so" >> fips.cfg && \
    echo "attributes = compatibility" >> fips.cfg

RUN cp /opt/java-slim/conf/security/java.security ./java.security.modified && \
    sed -i 's/security.provider.1=/security.provider.1=sun.security.pkcs11.SunPKCS11 \/opt\/java\/conf\/security\/fips.cfg\nsecurity.provider.2=/' ./java.security.modified && \
    sed -i 's/security.provider.2=sun.security.provider.Sun/security.provider.3=sun.security.provider.Sun/' ./java.security.modified

FROM cgr.dev/chainguard/wolfi-base@{{WOLFI_BASE_DIGEST}} AS helper
RUN --mount=type=cache,target=/var/cache/apk,id=apk_cache_helper_{{ version }} \
    apk add --no-cache libstdc++ zlib tzdata posix-libc-utils
RUN addgroup -g 1000 java && adduser -u 1000 -G java -D -s /bin/bash java
RUN mkdir -p /etc && touch /etc/nsswitch.conf && ln -sf /usr/lib/libz.so.1 /usr/lib/libz.so
RUN cp /usr/share/zoneinfo/UTC /etc/localtime && echo "UTC" > /etc/timezone

FROM cgr.dev/chainguard/static@{{WOLFI_STATIC_DIGEST}} AS jre-distroless

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

COPY --from=cleaner /opt/java-slim /opt/java

COPY --from=openssl-source /usr/local/bin/openssl /usr/local/bin/openssl
COPY --from=openssl-source /usr/local/lib/libcrypto.so* /usr/local/lib/
COPY --from=openssl-source /usr/local/lib/libssl.so* /usr/local/lib/
COPY --from=openssl-source /usr/local/lib/ossl-modules/fips.so /usr/local/lib/ossl-modules/fips.so
COPY --from=openssl-source /usr/local/ssl/openssl.cnf /usr/local/ssl/openssl.cnf
COPY --from=openssl-source /usr/local/ssl/fipsmodule.cnf /usr/local/ssl/fipsmodule.cnf

COPY --from=cleaner /tmp/java-conf/fips.cfg /opt/java/conf/security/fips.cfg
COPY --from=cleaner /tmp/java-conf/java.security.modified /opt/java/conf/security/java.security

ENV JAVA_HOME=/opt/java \
    PATH="/opt/java/bin:/usr/local/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/lib:/usr/local/lib64:/lib:/usr/lib" \
    OPENSSL_CONF=/usr/local/ssl/openssl.cnf \
    LANG=C.UTF-8 \
    TZ=UTC

USER java
WORKDIR /home/java
ENTRYPOINT ["/opt/java/bin/java"]
