#!/usr/bin/env bash
# Download the Kokoro-82M ONNX voice model (~350 MB) used for the natural voices.
set -euo pipefail
DIR="${1:-$(dirname "$0")/models}"
mkdir -p "$DIR"
BASE=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -f "$DIR/$f" ] || curl -L --fail -o "$DIR/$f" "$BASE/$f"
done
echo "Models ready in $DIR"
