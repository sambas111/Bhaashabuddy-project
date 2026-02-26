#!/usr/bin/env python3
"""
BhaashaBuddy Translation Pipeline

Translates Marathi content to other Indic languages. English is preserved.
Supports: data.json (lessons), phrases, dictionary.

Backends:
- Groq (default): Works on Windows, fast. Requires GROQ_API_KEY.
- IndicTrans2: Best for Indic languages, runs locally. On Windows needs C++ Build Tools.
  Install: pip install indictranstoolkit transformers torch

Usage:
  python translate_pipeline.py --target kannada
  python translate_pipeline.py --target tamil --backend groq --limit 5
  python translate_pipeline.py --target kannada --phrases phrases_marathi.json
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent.resolve()
sys.path.insert(0, str(BASE))

# All 22 scheduled Indic languages (IndicTrans2 codes)
INDIC_LANGUAGES = {
    "marathi": "mar_Deva",
    "hindi": "hin_Deva",
    "bengali": "ben_Beng",
    "telugu": "tel_Telu",
    "tamil": "tam_Taml",
    "gujarati": "guj_Gujr",
    "kannada": "kan_Knda",
    "malayalam": "mal_Mlym",
    "odia": "ory_Orya",
    "punjabi": "pan_Guru",
    "assamese": "asm_Beng",
    "nepali": "npi_Deva",
    "sanskrit": "san_Deva",
    "urdu": "urd_Arab",
    "sindhi": "snd_Deva",
    "konkani": "gom_Deva",
    "maithili": "mai_Deva",
    "manipuri": "mni_Mtei",
    "bodo": "brx_Deva",
    "dogri": "doi_Deva",
    "kashmiri": "kas_Deva",
    "santali": "sat_Olck",
}

LANG_DISPLAY_NAMES = {
    "kannada": "Kannada", "tamil": "Tamil", "telugu": "Telugu",
    "gujarati": "Gujarati", "hindi": "Hindi", "bengali": "Bengali",
    "malayalam": "Malayalam", "marathi": "Marathi", "odia": "Odia",
    "punjabi": "Punjabi", "assamese": "Assamese", "nepali": "Nepali",
    "sanskrit": "Sanskrit", "urdu": "Urdu", "sindhi": "Sindhi",
    "konkani": "Konkani", "maithili": "Maithili", "manipuri": "Manipuri",
    "bodo": "Bodo", "dogri": "Dogri", "kashmiri": "Kashmiri", "santali": "Santali",
}


def load_config():
    """Load translate_config.yaml if it exists."""
    config_path = BASE / "translate_config.yaml"
    if not config_path.exists():
        return {}
    try:
        import yaml
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except ImportError:
        return {}


def has_devanagari(text):
    """Check if text contains Devanagari (Marathi/Hindi)."""
    return bool(text and re.search(r"[\u0900-\u097F]", str(text)))


def has_indic_script(text):
    """Check if text contains any Indic script."""
    return bool(text and re.search(r"[\u0900-\u0DFF\u0E00-\u0E7F]", str(text)))


def parse_cell_with_translit(cell):
    """Split 'मराठी (marAThI)' into (script_part, translit_part)."""
    if not cell or not isinstance(cell, str):
        return cell, None
    m = re.match(r"^(.+?)\s*\(([^)]+)\)\s*$", cell.strip())
    if m and has_indic_script(m.group(1)):
        return m.group(1).strip(), m.group(2).strip()
    return cell, None


def extract_translatable_strings(data):
    """Extract all Marathi/Indic strings that need translation from data.json."""
    strings = set()
    for ch in data:
        if ch.get("content") and has_devanagari(ch["content"]):
            strings.add(ch["content"].strip())
        if ch.get("intro") and has_devanagari(ch["intro"]):
            strings.add(ch["intro"].strip())
        for blk in ch.get("blocks") or []:
            if blk.get("type") == "paragraph" and blk.get("content") and has_devanagari(blk["content"]):
                strings.add(blk["content"].strip())
            if blk.get("type") == "table":
                for row in blk.get("rows") or []:
                    for cell in row:
                        if isinstance(cell, str) and has_devanagari(cell):
                            script_part, _ = parse_cell_with_translit(cell)
                            if script_part:
                                strings.add(script_part.strip())
    return list(strings)


def translate_with_groq(texts, src_lang, tgt_lang, tgt_name, model=None):
    """Translate using Groq API."""
    try:
        from groq import Groq
    except ImportError:
        print("Install groq: pip install groq")
        sys.exit(1)
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Set GROQ_API_KEY environment variable")
        sys.exit(1)
    client = Groq(api_key=api_key)
    model = model or "llama-3.3-70b-versatile"
    results = []
    batch_size = 15
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        prompt = f"""Translate the following Marathi text to {tgt_name}.
Output ONLY the translation in {tgt_name} script, one per line. No numbering or extra text.
Preserve English words, numbers, and special formatting.
If a line has transliteration in parentheses like (mI bolato), omit it - we will regenerate it.

Marathi:
{chr(10).join(batch)}

{tgt_name} translations:"""
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
            )
            out = resp.choices[0].message.content.strip()
            translated = [s.strip() for s in out.split("\n") if s.strip()]
            if len(translated) >= len(batch):
                results.extend(translated[: len(batch)])
            else:
                results.extend(translated + [""] * (len(batch) - len(translated)))
        except Exception as e:
            print(f"Groq error: {e}")
            results.extend([""] * len(batch))
    return results


def translate_with_indic_trans2(texts, src_lang, tgt_lang):
    """Translate using IndicTrans2 Indic-Indic model via VarunGumma/IndicTransToolkit.
    See: https://github.com/VarunGumma/IndicTransToolkit
    pip install indictranstoolkit transformers torch
    """
    try:
        import torch
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
    except ImportError:
        print("Install: pip install transformers torch")
        sys.exit(1)
    model_name = "ai4bharat/indictrans2-indic-indic-dist-320M"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Loading IndicTrans2 ({device})...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)
    model = model.to(device)
    if device == "cuda":
        model = model.half()
    model.eval()
    ip = None
    try:
        from IndicTransToolkit import IndicProcessor  # VarunGumma/IndicTransToolkit
        ip = IndicProcessor(inference=True)
    except ImportError:
        try:
            from IndicTransToolkit.IndicTransToolkit import IndicProcessor
            ip = IndicProcessor(inference=True)
        except ImportError:
            try:
                from IndicTransToolkit.processor import IndicProcessor
                ip = IndicProcessor(inference=True)
            except ImportError:
                msg = "IndicTransToolkit not installed. Using basic mode (quality may be lower)."
                if sys.platform == "win32":
                    msg += "\n  On Windows, indictranstoolkit needs C++ Build Tools to compile."
                    msg += "\n  Alternative: use --backend groq (pip install groq, set GROQ_API_KEY)"
                else:
                    msg += "\n  Install: pip install indictranstoolkit"
                print(msg)
    results = []
    batch_size = 8
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        if ip:
            try:
                batch = ip.preprocess_batch(batch, src_lang=src_lang, tgt_lang=tgt_lang, visualize=False)
            except Exception:
                pass
        inputs = tokenizer(batch, truncation=True, padding="longest", max_length=256, return_tensors="pt").to(device)
        with torch.inference_mode():
            out = model.generate(**inputs, num_beams=5, num_return_sequences=1, max_length=256)
        decoded = tokenizer.batch_decode(out, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        if ip:
            try:
                decoded = ip.postprocess_batch(decoded, lang=tgt_lang)
            except Exception:
                pass
        results.extend([s.strip() for s in decoded])
    return results


def transliterate_to_roman(text, script_code):
    """Convert Indic script to Roman transliteration. script_code e.g. kan_Knda."""
    try:
        from indic_transliteration import sanscript
        from indic_transliteration.sanscript import transliterate
    except ImportError:
        return text
    script_map = {
        "Deva": sanscript.DEVANAGARI, "Beng": sanscript.BENGALI,
        "Knda": sanscript.KANNADA, "Gujr": sanscript.GUJARATI,
        "Taml": sanscript.TAMIL, "Telu": sanscript.TELUGU,
        "Mlym": sanscript.MALAYALAM, "Orya": sanscript.ORIYA,
        "Guru": sanscript.GURMUKHI,
    }
    parts = script_code.split("_")
    script_key = parts[1] if len(parts) > 1 else "Deva"
    src = script_map.get(script_key, sanscript.DEVANAGARI)
    try:
        return transliterate(text, src, sanscript.ITRANS)
    except Exception:
        return text


def build_translation_map(texts, translations):
    return dict(zip(texts, translations))


def apply_translations_to_data(data, translation_map, target_lang, script_code):
    """Apply translation map to data.json, regenerate transliteration for cells."""
    tgt_name = LANG_DISPLAY_NAMES.get(target_lang, target_lang.title())

    def replace_cell(cell):
        if not cell or not isinstance(cell, str):
            return cell
        script_part, translit_part = parse_cell_with_translit(cell)
        t = script_part.strip()
        if t in translation_map and translation_map[t]:
            translated = translation_map[t]
            new_translit = transliterate_to_roman(translated, script_code)
            if new_translit and new_translit != translated:
                return f"{translated} ({new_translit})"
            return translated
        return cell

    def replace_headers(hdrs):
        return [h.replace("Marathi", tgt_name).replace("मराठी", tgt_name) for h in hdrs]

    out = []
    for ch in data:
        new_ch = dict(ch)
        if ch.get("content"):
            new_ch["content"] = replace_cell(ch["content"])
        if ch.get("intro"):
            new_ch["intro"] = replace_cell(ch["intro"])
        if ch.get("blocks"):
            new_blocks = []
            for blk in ch["blocks"]:
                new_blk = dict(blk)
                if blk.get("type") == "paragraph" and blk.get("content"):
                    new_blk["content"] = replace_cell(blk["content"])
                if blk.get("type") == "table":
                    if blk.get("headers"):
                        new_blk["headers"] = replace_headers(blk["headers"])
                    new_rows = []
                    for row in blk.get("rows") or []:
                        new_row = [replace_cell(c) if isinstance(c, str) else c for c in row]
                        new_rows.append(new_row)
                    new_blk["rows"] = new_rows
                new_blocks.append(new_blk)
            new_ch["blocks"] = new_blocks
        out.append(new_ch)
    return out


def translate_phrases(phrases_data, translation_map, target_lang, script_code):
    """Translate phrases dict. English preserved, mr->translated, roman->new translit."""
    tgt_name = LANG_DISPLAY_NAMES.get(target_lang, target_lang.title())
    out = {}
    for cat_id, cat_data in phrases_data.items():
        new_phrases = []
        for p in cat_data.get("phrases", []):
            mr = (p.get("mr") or "").strip()
            if mr and mr in translation_map and translation_map[mr]:
                new_mr = translation_map[mr]
                new_roman = transliterate_to_roman(new_mr, script_code)
                new_phrases.append({
                    "en": p.get("en", ""),
                    "mr": new_mr,
                    "roman": new_roman if new_roman else p.get("roman", ""),
                    "hint": p.get("hint", ""),
                })
            else:
                new_phrases.append(dict(p))
        out[cat_id] = {"name": cat_data.get("name", cat_id), "phrases": new_phrases}
    return out


def _flatten_dictionary(dict_data):
    """Return flat list of entries from either flat list or sectioned dict."""
    if isinstance(dict_data, list):
        return dict_data
    if isinstance(dict_data, dict):
        out = []
        for sec_data in dict_data.values():
            if isinstance(sec_data, dict) and "words" in sec_data:
                out.extend(sec_data["words"])
            elif isinstance(sec_data, list):
                out.extend(sec_data)
        return out
    return []


def _translate_one_entry(d, translation_map, script_code):
    """Translate a single dictionary entry."""
    mr = (d.get("mr") or "").strip()
    out = dict(d)
    if mr and mr in translation_map and translation_map[mr]:
        new_mr = translation_map[mr]
        new_roman = transliterate_to_roman(new_mr, script_code)
        out["mr"] = new_mr
        out["roman"] = new_roman or d.get("roman", "")
    return out


def translate_dictionary(dict_data, translation_map, target_lang, script_code):
    """Translate dictionary (flat list or sectioned). Preserves section structure."""
    if isinstance(dict_data, list):
        return [_translate_one_entry(d, translation_map, script_code) for d in dict_data]
    if isinstance(dict_data, dict):
        out = {}
        for sec_id, sec_data in dict_data.items():
            if isinstance(sec_data, dict) and "words" in sec_data:
                out[sec_id] = {
                    "name": sec_data.get("name", sec_id),
                    "words": [_translate_one_entry(w, translation_map, script_code) for w in sec_data["words"]],
                }
            else:
                out[sec_id] = sec_data
        return out
    return dict_data


def main():
    config = load_config()
    parser = argparse.ArgumentParser(description="BhaashaBuddy Translation Pipeline")
    parser.add_argument("--target", "-t", help="Target language (e.g. kannada, tamil). Uses config if omitted.")
    parser.add_argument("--backend", "-b", help="groq | indic_trans2 (uses config if omitted)")
    parser.add_argument("--input", "-i", default="data.json", help="Input data.json")
    parser.add_argument("--output", "-o", help="Output data file")
    parser.add_argument("--phrases", "-p", help="Input phrases JSON (optional). Default from config or phrases_marathi.json")
    parser.add_argument("--dictionary", "-d", help="Input dictionary JSON (optional). Default from config or dictionary_marathi.json")
    parser.add_argument("--limit", "-n", type=int, help="Limit chapters (for testing)")
    parser.add_argument("--dry-run", action="store_true", help="Only extract strings, no translate")
    args = parser.parse_args()

    target = (args.target or config.get("target_language", "")).lower()
    if not target:
        print("Error: Specify --target (e.g. kannada) or set target_language in translate_config.yaml")
        sys.exit(1)
    backend = args.backend or config.get("backend", "groq")
    script_code = INDIC_LANGUAGES.get(target, "kan_Knda")

    if target not in INDIC_LANGUAGES:
        print(f"Target must be one of: {list(INDIC_LANGUAGES.keys())}")
        sys.exit(1)

    input_path = BASE / args.input
    if not input_path.exists():
        print(f"Input not found: {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.limit:
        data = data[: args.limit]

    strings = extract_translatable_strings(data)
    all_strings = list(strings)

    # Add phrases/dictionary strings if provided
    phrases_data = None
    dict_data = None
    phrases_path = args.phrases or config.get("phrases_file")
    dict_path = args.dictionary or config.get("dictionary_file")
    if not phrases_path and (BASE / "phrases_marathi.json").exists():
        phrases_path = "phrases_marathi.json"
    if not dict_path and (BASE / "dictionary_marathi.json").exists():
        dict_path = "dictionary_marathi.json"
    if phrases_path:
        p_path = BASE / phrases_path
        if p_path.exists():
            with open(p_path, "r", encoding="utf-8") as f:
                phrases_data = json.load(f)
            for cat in phrases_data.values():
                for p in cat.get("phrases", []):
                    mr = (p.get("mr") or "").strip()
                    if mr and has_devanagari(mr) and mr not in all_strings:
                        all_strings.append(mr)
    if dict_path:
        d_path = BASE / dict_path
        if d_path.exists():
            with open(d_path, "r", encoding="utf-8") as f:
                dict_data = json.load(f)
            # Support both flat list and sectioned {section: {name, words: [...]}}
            dict_entries = _flatten_dictionary(dict_data)
            for d in dict_entries:
                mr = (d.get("mr") or "").strip()
                if mr and has_devanagari(mr) and mr not in all_strings:
                    all_strings.append(mr)

    # Deduplicate preserving order
    seen = set()
    unique_strings = []
    for s in all_strings:
        if s and s not in seen:
            seen.add(s)
            unique_strings.append(s)

    print(f"Found {len(unique_strings)} unique strings to translate")

    if args.dry_run:
        for s in unique_strings[:15]:
            preview = (s[:70] + "...") if len(s) > 70 else s
            safe = preview.encode("ascii", errors="replace").decode("ascii")
            print(f"  - {safe}")
        return

    tgt_name = LANG_DISPLAY_NAMES.get(target, target.title())
    print(f"Translating to {tgt_name} using {backend}...")

    if backend == "groq":
        groq_model = config.get("groq_model", "llama-3.3-70b-versatile")
        translations = translate_with_groq(unique_strings, "marathi", target, tgt_name, model=groq_model)
    elif backend == "indic_trans2":
        translations = translate_with_indic_trans2(unique_strings, "mar_Deva", script_code)
    else:
        print(f"Unknown backend: {backend}")
        sys.exit(1)

    trans_map = build_translation_map(unique_strings, translations)
    translated_data = apply_translations_to_data(data, trans_map, target, script_code)

    output_path = BASE / (args.output or f"data_{target}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)
    print(f"Saved lessons to {output_path}")

    if phrases_data:
        translated_phrases = translate_phrases(phrases_data, trans_map, target, script_code)
        p_out = BASE / f"phrases_{target}.json"
        with open(p_out, "w", encoding="utf-8") as f:
            json.dump(translated_phrases, f, ensure_ascii=False, indent=2)
        print(f"Saved phrases to {p_out}")

    if dict_data:
        translated_dict = translate_dictionary(dict_data, trans_map, target, script_code)
        d_out = BASE / f"dictionary_{target}.json"
        with open(d_out, "w", encoding="utf-8") as f:
            json.dump(translated_dict, f, ensure_ascii=False, indent=2)
        print(f"Saved dictionary to {d_out}")


if __name__ == "__main__":
    main()
