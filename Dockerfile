# syntax=docker/dockerfile:1

ARG FIPS_VERSION=3.1.2
ARG FIPS_SHA256=a0ce69b8b97ea6a35b96875235aa453b966ba3cbb8b8c726fa6964861eb696f5
ARG CORE_VERSION=3.5.0
ARG CORE_SHA256=97dfd412e8b233a7f7d1f55a73e61c31405e5d36e2f1e1498e5e9559e38e1b69
ARG INSTALL_PREFIX=/usr/local
ARG OPENSSLDIR=/usr/local/ssl

FROM cgr.dev/chainguard/wolfi-base AS build-base
RUN --mount=type=cache,target=/var/cache/apk \
    apk add build-base perl linux-headers wget ca-certificates

FROM build-base AS fips-builder
ARG FIPS_VERSION
ARG FIPS_SHA256
WORKDIR /src
RUN wget -q https://www.openssl.org/source/openssl-${FIPS_VERSION}.tar.gz && \
    #echo "${FIPS_SHA256}  openssl-${FIPS_VERSION}.tar.gz" | sha256sum -c - && \
    tar -xf openssl-${FIPS_VERSION}.tar.gz && \
    cd openssl-${FIPS_VERSION} && \
    ./Configure enable-fips && \
    make

FROM build-base AS core-builder
ARG CORE_VERSION
ARG CORE_SHA256
ARG INSTALL_PREFIX
ARG OPENSSLDIR
WORKDIR /src
RUN wget -q https://www.openssl.org/source/openssl-${CORE_VERSION}.tar.gz && \
    #echo "${CORE_SHA256}  openssl-${CORE_VERSION}.tar.gz" | sha256sum -c - && \
    tar -xf openssl-${CORE_VERSION}.tar.gz && \
    cd openssl-${CORE_VERSION} && \
    ./Configure enable-fips shared --prefix=${INSTALL_PREFIX} --openssldir=${OPENSSLDIR} && \
    make && \
    make install_sw install_ssldirs

FROM core-builder AS fips-integrator
ARG FIPS_VERSION
ARG CORE_VERSION
ARG INSTALL_PREFIX
ARG OPENSSLDIR
COPY --from=fips-builder /src/openssl-${FIPS_VERSION}/providers/fips.so ${INSTALL_PREFIX}/lib/ossl-modules/fips.so
# Install FIPS config
RUN ${INSTALL_PREFIX}/bin/openssl fipsinstall \
    -out ${OPENSSLDIR}/fipsmodule.cnf \
    -module ${INSTALL_PREFIX}/lib/ossl-modules/fips.so && \
    chmod 644 ${OPENSSLDIR}/fipsmodule.cnf
# Patch openssl.cnf to include fipsmodule.cnf and activate the provider
RUN sed -i "s|# .include fipsmodule.cnf|.include ${OPENSSLDIR}/fipsmodule.cnf|" ${OPENSSLDIR}/openssl.cnf && \
    sed -i 's|# fips = fips_sect|fips = fips_sect|' ${OPENSSLDIR}/openssl.cnf

FROM cgr.dev/chainguard/wolfi-base
ARG INSTALL_PREFIX
RUN --mount=type=cache,target=/var/cache/apk \
    apk add libgcc
COPY --from=fips-integrator ${INSTALL_PREFIX} ${INSTALL_PREFIX}
ENV PATH="${INSTALL_PREFIX}/bin:${PATH}"
ENV LD_LIBRARY_PATH="${INSTALL_PREFIX}/lib:${INSTALL_PREFIX}/lib64"
ENTRYPOINT ["openssl"]
CMD ["list", "-provider-path", "/usr/local/lib/ossl-modules", "-provider", "fips", "-providers"]