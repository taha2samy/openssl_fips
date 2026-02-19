variable "FIPS_VERSION" {
  default = "3.1.2"
}

variable "CORE_VERSION" {
  default = "3.5.5" 
}



variable "REGISTRY" {
  default = "ghcr.io"
}

variable "OWNER" {
  default = "taha2samy"
}

variable "REPO_NAME" {
  default = "wolfi-openssl-fips"
}

function "tag" {
  params = [tag_name]
  result = ["${REGISTRY}/${OWNER}/${REPO_NAME}:${tag_name}"]
}

group "default" {
  targets = ["standard", "distroless","development"]
}

target "common" {
  context    = "."
  dockerfile = "Dockerfile"
  platforms  = ["linux/amd64", "linux/arm64"]
  output = ["type=registry"]
  attest = [
    "type=sbom,generator=docker/buildkit-syft-scanner,format=cyclonedx-json",
    "type=provenance,mode=max"
  ]
args = {
  FIPS_VERSION = "${FIPS_VERSION}"
  CORE_VERSION = "${CORE_VERSION}"

  # --- Base Images ---
  BASE_IMAGE   = "${BASE_IMAGE}"
  STATIC_IMAGE = "${STATIC_IMAGE}"

  # --- Build Stage Packages (fips-builder & core-builder) ---
  BUILD_BASE_VER    = "${BUILD_BASE_VER}"
  PERL_VER          = "${PERL_VER}"
  LINUX_HEADERS_VER = "${LINUX_HEADERS_VER}"
  WGET_VER          = "${WGET_VER}"
  CA_CERTIFICATES_VER = "${CA_CERTIFICATES_VER}"

  # --- Runtime & Helper Packages (helper & openssl-standard) ---
  LIBSTDC_PLUS_PLUS_VER = "${LIBSTDC_PLUS_PLUS_VER}"
  ZLIB_VER              = "${ZLIB_VER}"
  TZDATA_VER            = "${TZDATA_VER}"
  POSIX_LIBC_UTILS_VER  = "${POSIX_LIBC_UTILS_VER}"

  # --- Dev Tools (openssl-dev) ---
  PKG_CONF_VER  = "${PKG_CONF_VER}"
  PCRE_DEV_VER  = "${PCRE_DEV_VER}"
  ZLIB_DEV_VER  = "${ZLIB_DEV_VER}"
  BASH_VER      = "${BASH_VER}"
  CURL_VER      = "${CURL_VER}"
  JQ_VER        = "${JQ_VER}"
  UNZIP_VER     = "${UNZIP_VER}"
}
}

### ---------- STANDARD IMAGE ----------
target "standard" {
  inherits = ["common"]
  target   = "openssl-standard"

  tags = concat(
    tag("${CORE_VERSION}"),
    tag("latest")
  )


cache-from = ["type=gha,scope=standard"]
cache-to   = ["type=gha,scope=standard,mode=max"]

}

### ---------- DISTROLESS IMAGE ----------
target "distroless" {
  inherits = ["common"]
  target   = "openssl-distroless"

  tags = concat(
    tag("${CORE_VERSION}-distroless"),
    tag("distroless")
  )


cache-from = ["type=gha,scope=distroless"]
cache-to   = ["type=gha,scope=distroless,mode=max"]

}

### ---------- DEV IMAGE ----------
target "development" {
  inherits = ["common"]
  target   = "openssl-dev"

  tags = concat(
    tag("${CORE_VERSION}-dev"),
    tag("dev")
  )

  cache-from = ["type=gha,scope=development"]
  cache-to   = ["type=gha,scope=development,mode=max"]
}
