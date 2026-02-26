# Translate in GitHub Codespaces (IndicTransToolkit)

Use GitHub Codespaces to run IndicTransToolkit on Linux—no C++ Build Tools, no Groq API limits.

## Setup

1. **Open your repo in Codespaces**
   - GitHub → Your repo → Code → Codespaces → Create codespace
   - Or: `gh codespace create` from the repo

2. **Ensure these files exist in the project:**
   - `data.json` (lessons)
   - `phrases_marathi.json` (optional)
   - `dictionary_marathi.json` (optional)

## Run Translation

**Single language (e.g. Kannada):**
```bash
chmod +x translate_in_codespace.sh
./translate_in_codespace.sh kannada
```

**Test with 5 chapters first:**
```bash
./translate_in_codespace.sh kannada 5
```

**Multiple languages:**
```bash
chmod +x translate_all_codespace.sh
./translate_all_codespace.sh kannada,tamil,telugu
```

**Many languages:**
```bash
./translate_all_codespace.sh kannada,tamil,telugu,hindi,bengali,gujarati,malayalam,odia,punjabi
```

## Output Files

After running, you'll have:
- `data_kannada.json`, `data_tamil.json`, ...
- `phrases_kannada.json`, `phrases_tamil.json`, ...
- `dictionary_kannada.json`, `dictionary_tamil.json`, ...

## Download to Local

1. In Codespaces: right-click file → Download
2. Or: Files panel → right-click → Download
3. Or use `gh codespace cp` to copy files out

Place the downloaded files in your local `Bhaashabuddy-project` folder.

## Add to App

After copying files locally, add the language to `app.js` LANGUAGES and `index.html` (see TRANSLATE_README.md).
