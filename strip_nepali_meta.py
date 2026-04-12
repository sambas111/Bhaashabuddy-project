# -*- coding: utf-8 -*-
"""Remove instructional meta-wrappers from English/Nepali/transliteration lesson rows."""
import json
import re
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data_nepali.json"

PREFIX_EN_CONV = "In Nepali conversation, you might say: "
PREFIX_EN_ASK = "When you talk to someone in Nepal, you might ask: "
PREFIX_EN_VOCAB = re.compile(
    r'^When you learn Nepali vocabulary, "([^"]+)" is a useful word to remember\.$'
)
PREFIX_EN_TO = "To express this idea in Nepali, you might say: "

PREFIX_NE_CONV = "दैनिक कुराकानीमा यो प्रयोग गर्न सकिन्छ: "
PREFIX_NE_ASK = "कसैसँग कुरा गर्दा यसरी सोध्न सकिन्छ: "
PREFIX_NE_TO = "यो अर्थ नेपालीमा यसरी भन्न सकिन्छ: "

PREFIX_TR_CONV = "dainika kurākānīmā yo prayog garna sakncha: "
PREFIX_TR_ASK = "kasai-saṃga kurā gardā yasari sodhna sakncha: "
PREFIX_TR_TO = "yo artha nepālīmā yasari bhanna sakncha: "

RE_VOCAB_NE = re.compile(r"^(.+?) शब्द सिक्न उपयोगी छ।$")
RE_VOCAB_TR = re.compile(r"^(.+?) śabda sikna upayogī cha$")


def strip_row(en: str, ne: str, tr: str) -> tuple[str, str, str]:
    en = en.strip()
    ne = ne.strip()
    tr = tr.strip()

    m = PREFIX_EN_VOCAB.match(en)
    if m:
        en_word = m.group(1)
        mne = RE_VOCAB_NE.match(ne)
        mtr = RE_VOCAB_TR.match(tr)
        if mne and mtr:
            return en_word.strip(), mne.group(1).strip(), mtr.group(1).strip()

    if en.startswith(PREFIX_EN_ASK):
        return (
            en[len(PREFIX_EN_ASK) :].strip(),
            ne.replace(PREFIX_NE_ASK, "", 1).strip(),
            tr.replace(PREFIX_TR_ASK, "", 1).strip(),
        )

    if en.startswith(PREFIX_EN_TO):
        return (
            en[len(PREFIX_EN_TO) :].strip(),
            ne.replace(PREFIX_NE_TO, "", 1).strip(),
            tr.replace(PREFIX_TR_TO, "", 1).strip(),
        )

    if en.startswith(PREFIX_EN_CONV):
        return (
            en[len(PREFIX_EN_CONV) :].strip(),
            ne.replace(PREFIX_NE_CONV, "", 1).strip(),
            tr.replace(PREFIX_TR_CONV, "", 1).strip(),
        )

    return en, ne, tr


def process_tables(obj):
    if isinstance(obj, dict):
        headers = obj.get("headers")
        if (
            headers == ["English", "Nepali", "Transliteration"]
            and "rows" in obj
            and isinstance(obj["rows"], list)
        ):
            new_rows = []
            for row in obj["rows"]:
                if (
                    isinstance(row, list)
                    and len(row) == 3
                    and all(isinstance(x, str) for x in row)
                ):
                    en, ne, tr = strip_row(row[0], row[1], row[2])
                    new_rows.append([en, ne, tr])
                else:
                    new_rows.append(row)
            obj["rows"] = new_rows
        for v in obj.values():
            process_tables(v)
    elif isinstance(obj, list):
        for item in obj:
            process_tables(item)


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    data = deepcopy(data)
    process_tables(data)
    DATA.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("Stripped meta prefixes from", DATA)


if __name__ == "__main__":
    main()
