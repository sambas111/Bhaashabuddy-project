# BhaashaBuddy Translation Pipeline

Translate Marathi content to any of the **22 scheduled Indic languages**. English is preserved; Marathi text is translated and transliteration is regenerated.

## Quick Start: Change Language & Translate

1. Edit `translate_config.yaml` and set `target_language: kannada` (or tamil, telugu, etc.)
2. Run: `python translate_pipeline.py`
3. Output: `data_kannada.json`, `phrases_kannada.json`, `dictionary_kannada.json`

No need to pass `--target` every time—just change the config.

**Default backend:** Groq (works on Windows). Use `--backend indic_trans2` for local translation (Linux/Mac, or Windows with C++ Build Tools).

## Supported Languages

| Language | Code | Script |
|----------|------|--------|
| Kannada | kannada | Kannada |
| Tamil | tamil | Tamil |
| Telugu | telugu | Telugu |
| Hindi | hindi | Devanagari |
| Gujarati | gujarati | Gujarati |
| Bengali | bengali | Bengali |
| Malayalam | malayalam | Malayalam |
| Odia | odia | Odia |
| Punjabi | punjabi | Gurmukhi |
| Assamese | assamese | Bengali |
| Nepali | nepali | Devanagari |
| Sanskrit | sanskrit | Devanagari |
| Urdu | urdu | Arabic |
| Sindhi | sindhi | Devanagari |
| Konkani | konkani | Devanagari |
| Maithili | maithili | Devanagari |
| Manipuri | manipuri | Meitei |
| Bodo | bodo | Devanagari |
| Dogri | dogri | Devanagari |
| Kashmiri | kashmiri | Devanagari |
| Santali | santali | Ol Chiki |

## Quick Start

### 1. Install Dependencies

**Windows (recommended: use Groq):**
```bash
pip install -r requirements-translate-windows.txt
# Or: pip install groq pyyaml indic-transliteration
# Set GROQ_API_KEY, then run with default backend
```

**Linux/Mac (IndicTrans2 or Groq):**
```bash
pip install -r requirements-translate.txt
```

For IndicTrans2 on Linux/Mac (no API key):
```bash
pip install indictranstoolkit transformers torch
```
Note: On Windows, indictranstoolkit requires [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) to compile.

### 2. Translate Lessons (data.json)

**Using Groq (recommended for speed):**
```bash
set GROQ_API_KEY=your_api_key_here
python translate_pipeline.py --target kannada
```

**Using IndicTrans2 (best quality for Indic languages):**
```bash
python translate_pipeline.py --target kannada --backend indic_trans2
```

### 3. Output

- `data_kannada.json` – Translated lessons (chapters)
- `phrases_kannada.json` – If you pass `--phrases phrases_marathi.json`
- `dictionary_kannada.json` – If you pass `--dictionary dictionary_marathi.json`

## Options

| Flag | Description |
|------|-------------|
| `--target`, `-t` | Target language (required) |
| `--backend`, `-b` | `groq` or `indic_trans2` |
| `--input`, `-i` | Input data.json path |
| `--output`, `-o` | Output file path |
| `--phrases`, `-p` | Input phrases JSON |
| `--dictionary`, `-d` | Input dictionary JSON |
| `--limit`, `-n` | Limit chapters (for testing) |
| `--dry-run` | Only list strings, no translation |

## Examples

```bash
# Translate to Kannada with Groq (fast)
python translate_pipeline.py -t kannada -b groq

# Translate to Tamil with IndicTrans2 (best quality)
python translate_pipeline.py -t tamil -b indic_trans2

# Test with 5 chapters only
python translate_pipeline.py -t kannada --limit 5

# Translate lessons + phrases + dictionary
python translate_pipeline.py -t kannada -p phrases_marathi.json -d dictionary_marathi.json
```

## Adding a New Language to the App

After translation:

1. Copy `data_kannada.json` to the project
2. Copy `lessons_structure.json` to `lessons_structure_kannada.json` (structure is same)
3. Add the language to `LANGUAGES` in `app.js`:

```javascript
kannada: {
  name: "Kannada",
  code: "kn",
  subtitle: "ಕನ್ನಡ ಕಲಿಯಿರಿ",
  scriptFont: "'Noto Sans Kannada', sans-serif",
  speechLang: "kn-IN",
  dataSource: "learnmarathiwithkaushik.com",
  hasLessons: true,
  dataFile: "data_kannada.json",
  structureFile: "lessons_structure_kannada.json",
  PHRASES: KANNADA_PHRASES,  // from phrases_kannada.json
  DICTIONARY: KANNADA_DICTIONARY  // from dictionary_kannada.json
}
```

4. Add Kannada to the language selection screen in `index.html`

## Config File

Create `translate_config.yaml` to set defaults:

```yaml
target_language: kannada
backend: groq
```

## Words Section & Dictionary Sections

Words are organized into sections (Reading, Writing, Numbers, Animals, etc.) in the Words tab.

### Build sectioned dictionary

```bash
python build_dictionary_sections.py
```

Creates `dictionary_marathi.json` with sections. To embed into app.js:

```bash
python embed_dictionary_sections.py
```

Or use `--from extracted_phrases.json` to build from extracted phrases (preserves category from lessons).

### Batch translate to all 22 languages

```bash
python translate_all.py
python translate_all.py --languages kannada,tamil,telugu
python translate_all.py --limit 2   # Test with 2 chapters
```

## References

- [IndicTransToolkit](https://github.com/VarunGumma/IndicTransToolkit) – Toolkit used for IndicTrans2 (pip: indictranstoolkit)
- [IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) – Translation models for 22 Indic languages
- [IndicTrans2 HuggingFace](https://huggingface.co/ai4bharat/indictrans2-indic-indic-dist-320M)
