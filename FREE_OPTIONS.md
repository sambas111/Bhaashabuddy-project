# Free Translation & Transliteration Options

## Translation (Free, No API Limits)

| Option | How | Limits |
|--------|-----|--------|
| **IndicTrans2** | Run locally or in GitHub Codespaces | None – 100% free |
| **Groq** | Cloud API | Free tier has rate limits |
| **LibreTranslate** | Self-host or their API | Limited Indic support |

**Recommended:** Use **IndicTrans2** in GitHub Codespaces (see `CODESPACE_TRANSLATE.md`). No API key, no rate limits.

## Script-Only Mode (No Translation, No API, Works on Windows)

For shared vocabulary (Sanskrit-derived words), use **script conversion** – same words, different script:

```bash
python translate_pipeline.py --target kannada --script-only
```

- Uses `indic-transliteration` (pure Python, no C++ build)
- Maps Devanagari → Kannada/Tamil/Telugu/etc. by phonetics (a, aa, i, consonants)
- No translation model, no API – instant, works on Windows

## Transliteration (Script Mapping)

Indian scripts share the same phonetic structure (a, aa, i, ii, u, consonants). The `indic-transliteration` package maps between them:

```
Devanagari (Marathi)  →  Kannada  →  same sound, different script
    नमस्कार           →  ನಮಸ್ಕಾರ
    (namaskāra)       →  (namaskāra)
```

**Script-to-script** (no translation model needed):
```python
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Devanagari → Kannada (same words, different script)
text = "नमस्कार"
out = transliterate(text, sanscript.DEVANAGARI, sanscript.KANNADA)
# → ನಮಸ್ಕಾರ

# Devanagari → Tamil, Telugu, etc.
out = transliterate(text, sanscript.DEVANAGARI, sanscript.TAMIL)
out = transliterate(text, sanscript.DEVANAGARI, sanscript.TELUGU)
```

**Script → Roman** (for pronunciation guides):
```python
out = transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
# → namaskAra
```

Supported scripts: Devanagari, Kannada, Tamil, Telugu, Malayalam, Bengali, Gujarati, Oriya, Gurmukhi.
