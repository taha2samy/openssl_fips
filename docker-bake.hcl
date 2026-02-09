variable "FIPS_VERSION" {
  default = "3.1.2"
}

variable "FIPS_SHA256" {
  default = "a0ce69b8b97ea6a35b96875235aa453b966ba3cba8af2de23657d8b6767d6539"
}

variable "CORE_VERSION" {
  default = "3.5.5"
}

variable "CORE_SHA256" {
  default = "b28c91532a8b65a1f983b4c28b7488174e4a01008e29ce8e69bd789f28bc2a89"
}

group "default" {
    targets = ["standard", "distroless"]
}

variable "REGISTRY" { default = "ghcr.io" }
variable "REPO" { default = "taha2samy/wolfi_os" }

variable "FIPS_VER" { default = "3.1.2" }
variable "CORE_VER" { default = "3.4.0" }

variable "CACHE_FROM" { default = "" }
variable "CACHE_TO" { default = "" }

group "default" {
    targets = ["standard", "distroless"]
}

target "common" {
    context = "."
    dockerfile = "Dockerfile"
    platforms = ["linux/amd64", "linux/arm64"]
    args = {
        FIPS_VERSION = "${FIPS_VER}"
        CORE_VERSION = "${CORE_VER}"
        BASE_IMAGE   = "${WOLFI_BASE_REF}"
        STATIC_IMAGE = "${WOLFI_STATIC_REF}"
    }
}

target "standard" {
    inherits = ["common"]
    target   = "openssl-standard"
    tags     = ["${REGISTRY}/${REPO}:latest", "${REGISTRY}/${REPO}:${CORE_VER}"]
    cache-from = ["type=gha,scope=standard"]
    cache-to   = ["type=gha,mode=max,scope=standard"]
}

target "distroless" {
    inherits = ["common"]
    target   = "openssl-distroless"
    tags     = ["${REGISTRY}/${REPO}:distroless", "${REGISTRY}/${REPO}:${CORE_VER}-distroless"]
    cache-from = ["type=gha,scope=distroless"]
    cache-to   = ["type=gha,mode=max,scope=distroless"]
}