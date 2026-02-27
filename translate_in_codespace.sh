#!/bin/bash
# Run this in GitHub Codespaces (Linux) to translate using IndicTransToolkit.
# Output: data_{lang}.json, phrases_{lang}.json, dictionary_{lang}.json
# Download these files and add them to your local project.

set -e
cd "$(dirname "$0")"
TARGET="${1:-kannada}"
LIMIT="${2:-}"  # Optional: e.g. 5 for testing with 5 chapters

echo "=== BhaashaBuddy Translation in Codespaces ==="
echo "Target: $TARGET"
echo ""

# Install dependencies (Codespaces has Linux - no C++ Build Tools needed)
pip install -q indictranstoolkit transformers torch indic-transliteration pyyaml

# Run translation with IndicTrans2
if [ -n "$LIMIT" ]; then
  python translate_pipeline.py --target "$TARGET" --backend indic_trans2 --limit "$LIMIT"
else
  python translate_pipeline.py --target "$TARGET" --backend indic_trans2
fi

echo ""
echo "=== Done! Output files ==="
ls -la data_*.json phrases_*.json dictionary_*.json 2>/dev/null || true
echo ""
echo "Download these files to your local project."
