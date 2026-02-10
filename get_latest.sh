#!/bin/bash
set -e
OUTFILE="versions.hcl"
echo "" > "$OUTFILE"
declare -A IMAGES
IMAGES=(
  ["STATIC_IMAGE"]="chainguard/static"
  ["BASE_IMAGE"]="chainguard/wolfi-base"
)
for var in "${!IMAGES[@]}"; do
  image="${IMAGES[$var]}"
  digest=$(docker manifest inspect "$image:latest" | jq -r '.config.digest // .manifests[0].digest' 2>/dev/null || \
           docker pull "$image:latest" >/dev/null && docker inspect --format='{{index .RepoDigests 0}}' "$image:latest" | cut -d'@' -f2)
  if [ -z "$digest" ] || [ "$digest" == "null" ]; then exit 1; fi
  cat >> "$OUTFILE" <<EOL
variable "$var" {
  default = "$image@$digest"
}
EOL
done
