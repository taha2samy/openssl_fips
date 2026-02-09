#!/bin/bash
OUTFILE="versions.hcl"
echo "" > "$OUTFILE"

declare -A IMAGES
IMAGES=(
  ["STATIC_IMAGE"]="chainguard/wolfi-base"
  ["BASE_IMAGE"]="chainguard/wolfi-base"
)

for var in "${!IMAGES[@]}"; do
  image="${IMAGES[$var]}"
  digest=$(docker pull "$image:latest" > /dev/null && docker inspect --format='{{index .RepoDigests 0}}' "$image:latest" | cut -d'@' -f2)
  cat >> "$OUTFILE" <<EOL
variable "$var" {
  default = "$image@$digest"
}

EOL
done
