#!/usr/bin/env python3
"""
BhaashaBuddy Translation Pipeline (Groq full-chapter only)

Groq does everything per chapter: translation, transliteration, and keeping English.
Input: data.json (Marathi lessons). Output: data_{target}.json (same structure, target language).

Usage:
  python translate_pipeline.py --target kannada
  python translate_pipeline.py --target kannada --limit 5
  Set GROQ_API_KEY in environment.
"""

import argparse
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent.resolve()

LANG_DISPLAY_NAMES = {
    "kannada": "Kannada", "tamil": "Tamil", "telugu": "Telugu",
    "gujarati": "Gujarati", "hindi": "Hindi", "bengali": "Bengali",
    "malayalam": "Malayalam", "marathi": "Marathi", "odia": "Odia",
}


def load_config():
    config_path = BASE / "translate_config.yaml"
    if not config_path.exists():
        return {}
    try:
        import yaml
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except ImportError:
        return {}


def _groq_full_chapter_prompt(chapter_json_str, tgt_name, target_script_name):
    """Same content as Marathi: same English, same structure. Only Marathi→target script and Marathi translit→target romanization. Do not add any new text."""
    return f"""You are a translator. You receive ONE lesson chapter as JSON from a Marathi lesson. Your output must be the SAME lesson in structure and content, with only two kinds of replacement:

WHAT TO DO:
- Keep every English sentence, phrase, and word exactly as in the input. Do not translate English. Do not add any new English or any new text.
- Replace every Marathi (Devanagari) string with the equivalent in {tgt_name} script. Use correct {tgt_name} grammar.
- Replace every Marathi transliteration (roman) with the romanization of the {tgt_name} text you wrote (e.g. mAjhA → nanna for "my" in Kannada).

WHAT NOT TO DO:
- Do not write anything that is not in the Marathi lesson. No extra explanations, no new sentences, no summaries, no commentary.
- Do not change "id", "url", or any key. Do not add or remove blocks, rows, or cells. Same number of paragraphs, same number of tables, same number of rows and columns.
- Do not translate or alter English. English stays exactly as in the input.

TABLES (same format as Marathi):
- Headers: use "English", then "{tgt_name}" or "[Label] ({tgt_name})", and "Transliteration" or "[Label] (Translit)" — same column count and order as input.
- Each row: first cell = English (copy exactly from input). Then for each language column: {tgt_name} script, then in the next cell its romanization. So: English | {tgt_name} script | Transliteration (repeated for each form if grammar table).

OUTPUT: Return ONLY the complete chapter as a single valid JSON object. No markdown, no explanation, no other text.

INPUT CHAPTER (JSON):
{chapter_json_str}

OUTPUT (JSON only):"""


def translate_chapter_with_groq(chapter, tgt_name, model=None):
    """Send one full chapter to Groq; return the translated chapter as a dict."""
    try:
        from groq import Groq
    except ImportError:
        print("Install groq: pip install groq")
        sys.exit(1)
    import os
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Set GROQ_API_KEY environment variable")
        sys.exit(1)
    client = Groq(api_key=api_key)
    model = model or "llama-3.3-70b-versatile"
    chapter_str = json.dumps(chapter, ensure_ascii=False, indent=2)
    prompt = _groq_full_chapter_prompt(chapter_str, tgt_name, tgt_name)
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        out = resp.choices[0].message.content.strip()
        if out.startswith("```"):
            out = re.sub(r"^```(?:json)?\s*", "", out)
            out = re.sub(r"\s*```\s*$", "", out)
        return json.loads(out)
    except json.JSONDecodeError as e:
        print(f"Groq returned invalid JSON for chapter id={chapter.get('id')}: {e}")
        return None
    except Exception as e:
        print(f"Groq error for chapter id={chapter.get('id')}: {e}")
        return None


def main():
    config = load_config()
    parser = argparse.ArgumentParser(description="BhaashaBuddy: translate lessons with Groq (full chapter mode)")
    parser.add_argument("--target", "-t", required=True, help="Target language (e.g. kannada, tamil)")
    parser.add_argument("--input", "-i", default="data.json", help="Input data.json")
    parser.add_argument("--output", "-o", help="Output file (default: data_{target}.json)")
    parser.add_argument("--limit", "-n", type=int, help="Limit chapters (for testing)")
    args = parser.parse_args()

    target = args.target.lower()
    tgt_name = LANG_DISPLAY_NAMES.get(target, target.title())

    input_path = BASE / args.input
    if not input_path.exists():
        print(f"Input not found: {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.limit:
        data = data[: args.limit]

    groq_model = config.get("groq_model", "llama-3.3-70b-versatile")
    print(f"Translating to {tgt_name} with Groq (full chapter mode)...")

    translated_data = []
    for i, ch in enumerate(data):
        print(f"  Chapter {i + 1}/{len(data)} (id={ch.get('id')})...")
        out = translate_chapter_with_groq(ch, tgt_name, model=groq_model)
        translated_data.append(out if out is not None else ch)

    output_path = BASE / (args.output or f"data_{target}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
