#!/usr/bin/env python3
"""Put letter grids into blocks (before the word table) so the app actually renders them."""
import json, sys
from pathlib import Path

BASE = Path(__file__).parent.resolve()

GRIDS = {

501: [
    {
        "type": "table",
        "heading": "Vowels (Iyek Ipee)",
        "headers": ["Letter", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ꯑ", "a"],
            ["ꯏ", "i"],
            ["ꯎ", "u"],
        ]
    },
    {
        "type": "table",
        "heading": "Consonants (Iyek Ipee)",
        "headers": ["Letter", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ꯀ", "ka"],
            ["ꯁ", "sa"],
            ["ꯂ", "la"],
            ["ꯃ", "ma"],
            ["ꯄ", "pa"],
            ["ꯅ", "na"],
            ["ꯆ", "cha"],
            ["ꯇ", "ta"],
            ["ꯈ", "kha"],
            ["ꯉ", "nga"],
            ["ꯊ", "tha"],
            ["ꯋ", "wa"],
            ["ꯌ", "ya"],
            ["ꯍ", "ha"],
            ["ꯐ", "pha"],
            ["ꯒ", "ga"],
            ["ꯓ", "jha"],
            ["ꯔ", "ra"],
            ["ꯕ", "ba"],
            ["ꯖ", "ja"],
            ["ꯗ", "da"],
            ["ꯘ", "gha"],
            ["ꯙ", "dha"],
            ["ꯚ", "bha"],
        ]
    },
],

502: [
    {
        "type": "table",
        "heading": "Independent Vowels",
        "headers": ["Letter", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ꯑ", "a"],
            ["ꯏ", "i"],
            ["ꯎ", "u"],
        ]
    },
    {
        "type": "table",
        "heading": "Core Consonants",
        "headers": ["Letter", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ꯀ", "ka"],
            ["ꯁ", "sa"],
            ["ꯂ", "la"],
            ["ꯃ", "ma"],
            ["ꯄ", "pa"],
            ["ꯅ", "na"],
            ["ꯆ", "cha"],
            ["ꯇ", "ta"],
            ["ꯈ", "kha"],
            ["ꯉ", "nga"],
            ["ꯊ", "tha"],
            ["ꯋ", "wa"],
            ["ꯌ", "ya"],
            ["ꯍ", "ha"],
            ["ꯐ", "pha"],
        ]
    },
    {
        "type": "table",
        "heading": "Extended Consonants (for loanwords)",
        "headers": ["Letter", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ꯒ", "ga"],
            ["ꯓ", "jha"],
            ["ꯔ", "ra"],
            ["ꯕ", "ba"],
            ["ꯖ", "ja"],
            ["ꯗ", "da"],
            ["ꯘ", "gha"],
            ["ꯙ", "dha"],
            ["ꯚ", "bha"],
        ]
    },
],

503: [
    {
        "type": "table",
        "heading": "Vowel Signs (Cheitap Iyek)",
        "headers": ["Sign", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ꯥ", "aa"],
            ["ꯤ", "i"],
            ["ꯨ", "u"],
            ["ꯦ", "e"],
            ["ꯣ", "o"],
            ["ꯧ", "ou"],
            ["ꯩ", "ei"],
            ["ꯪ", "ng"],
        ]
    },
    {
        "type": "table",
        "heading": "Combined with ꯀ (ka)",
        "headers": ["Combined", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ꯀ", "ka"],
            ["ꯀꯥ", "kaa"],
            ["ꯀꯤ", "ki"],
            ["ꯀꯨ", "ku"],
            ["ꯀꯦ", "ke"],
            ["ꯀꯣ", "ko"],
            ["ꯀꯧ", "kou"],
            ["ꯀꯩ", "kei"],
            ["ꯀꯪ", "kang"],
        ]
    },
    {
        "type": "table",
        "heading": "Combined with ꯃ (ma)",
        "headers": ["Combined", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ꯃ", "ma"],
            ["ꯃꯥ", "maa"],
            ["ꯃꯤ", "mi"],
            ["ꯃꯨ", "mu"],
            ["ꯃꯦ", "me"],
            ["ꯃꯣ", "mo"],
            ["ꯃꯧ", "mou"],
            ["ꯃꯩ", "mei"],
            ["ꯃꯪ", "mang"],
        ]
    },
],

505: [
    {
        "type": "table",
        "heading": "Final Consonants (Lonsum Iyek)",
        "headers": ["Letter", "Transliteration"],
        "speakCol": 0,
        "rows": [
            ["ꯛ", "k (final)"],
            ["ꯜ", "l (final)"],
            ["ꯝ", "m (final)"],
            ["ꯞ", "p (final)"],
            ["ꯟ", "n (final)"],
            ["ꯠ", "t (final)"],
            ["ꯡ", "ng (final)"],
            ["ꯢ", "i (final)"],
        ]
    },
],

}

def main():
    path = BASE / "data_meitei.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    updated = 0
    for chapter in data:
        cid = chapter["id"]
        if cid in GRIDS:
            existing_blocks = chapter.get("blocks", [])
            chapter["blocks"] = GRIDS[cid] + existing_blocks
            chapter.pop("tables", None)
            updated += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sys.stdout.buffer.write(f"Moved grids into blocks for {updated} lessons\n".encode("utf-8"))

if __name__ == "__main__":
    main()
