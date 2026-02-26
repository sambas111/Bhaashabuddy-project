#!/bin/bash
# Run in GitHub Codespaces to translate to multiple languages using IndicTransToolkit.
# Usage: ./translate_all_codespace.sh [lang1,lang2,...]
# Example: ./translate_all_codespace.sh kannada,tamil,telugu
# Example: ./translate_all_codespace.sh  (translates to all 22 languages - takes hours)

set -e
cd "$(dirname "$0")"
LANGS="${1:-kannada,tamil,telugu,hindi,bengali,gujarati,malayalam,odia,punjabi}"

echo "=== BhaashaBuddy Batch Translation in Codespaces ==="
echo "Languages: $LANGS"
echo ""

pip install -q indictranstoolkit transformers torch indic-transliteration pyyaml

IFS=',' read -ra LANG_ARRAY <<< "$LANGS"
for lang in "${LANG_ARRAY[@]}"; do
  lang=$(echo "$lang" | xargs)
  [ -z "$lang" ] && continue
  if [ "$lang" = "marathi" ]; then
    echo "Skipping marathi (source)"
    continue
  fi
  echo ""
  echo "=== Translating to $lang ==="
  python translate_pipeline.py --target "$lang" --backend indic_trans2 || true
done

echo ""
echo "=== All done! Output files ==="
ls -la data_*.json phrases_*.json dictionary_*.json 2>/dev/null || true
echo ""
echo "Download these files to your local project."
