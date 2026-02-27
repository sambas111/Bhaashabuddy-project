# Translate in Google Colab

Use Colab (free GPU) to run IndicTrans2—no API limits, no local setup.

## Quick Start

1. **Open Colab:** [Open translate_colab.ipynb in Colab](https://colab.research.google.com/github/sambas111/Bhaashabuddy-project/blob/translation-pipeline/translate_colab.ipynb)

   Or: Upload `translate_colab.ipynb` to Colab manually.

2. **Runtime → Run all** (or run cells one by one)

3. **Download** the output files when done:
   - `data_kannada.json`
   - `phrases_kannada.json`
   - `dictionary_kannada.json`

4. **Add to your project** – copy the downloaded files into your local `Bhaashabuddy-project` folder.

## Change Target Language

Edit the cell:
```python
TARGET = "kannada"  # or tamil, telugu, hindi, bengali, gujarati, malayalam, odia, punjabi...
```

## Test First (5 chapters)

```python
LIMIT = 5  # Quick test
```

Set `LIMIT = 0` for full translation.

## Repo

[github.com/sambas111/Bhaashabuddy-project (translation-pipeline branch)](https://github.com/sambas111/Bhaashabuddy-project/tree/translation-pipeline)
