#!/bin/bash
set -e
OUTFILE="versions.hcl"
echo "" > "$OUTFILE"

declare -A IMAGES
IMAGES=(
  ["STATIC_IMAGE"]="cgr.dev/chainguard/static"
  ["BASE_IMAGE"]="cgr.dev/chainguard/wolfi-base"
)

for var in "${!IMAGES[@]}"; do
  image="${IMAGES[$var]}"
  
  digest=$(skopeo inspect docker://"$image:latest" | jq -r '.Digest')

  if [ -z "$digest" ] || [ "$digest" == "null" ]; then
    echo "Error: Could not find digest for $image"
    exit 1
  fi

  cat >> "$OUTFILE" <<EOL
variable "$var" {
  default = "$image@$digest"
}

EOL
done
