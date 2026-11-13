#!/usr/bin/env bash
# Smoke check: /health must answer 200 within 20 seconds.
set -euo pipefail
url="${1:-http://localhost:8000}"
for _ in $(seq 1 20); do
  if body="$(curl -fsS "$url/health" 2>/dev/null)"; then
    echo "smoke: GET /health -> 200 ${body}"
    echo "smoke: $(curl -fsS "$url/" | head -n 1)"
    exit 0
  fi
  sleep 1
done
echo "smoke: FAILED, /health did not answer 200 at ${url}"
exit 1
