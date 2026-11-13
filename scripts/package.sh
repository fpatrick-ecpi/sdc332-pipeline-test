#!/usr/bin/env bash
# package.sh LABEL OUTPUT: bundle the app into a tar.gz named OUTPUT.
set -euo pipefail
if [ "$#" -ne 2 ]; then
  echo "usage: package.sh LABEL OUTPUT" >&2
  exit 2
fi
label="$1"
output="$2"
echo "$label" > LABEL.txt
tar -czf "$output" relnotes config CHANGELOG.md LABEL.txt
echo "packaged ${label} into ${output}"
