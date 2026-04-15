# -*- coding: utf-8 -*-
"""
Set English column in data_kashmiri.json from data_maithili.json for every
English/Maithili table, row-aligned by lesson + table order.

- Kashmiri + transliteration default to existing data_kashmiri.json.
- If Maithili has fewer rows in a table (alphabet lessons 501–509), extra rows
  keep the previous English (Kashmiri unchanged).
- Lessons 510–542: optional overrides for Kashmiri from kashmiri_maithili_s2_pairs.KS_RO
  when row counts match.

Run: py -3 apply_maithili_english_all_kashmiri.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAI = ROOT / "data_maithili.json"
KSH = ROOT / "data_kashmiri.json"

EMT = ("English", "Maithili", "Transliteration")
EKT = ("English", "Kashmiri", "Transliteration")


def _emt_blocks(lesson: dict) -> list[dict]:
    out: list[dict] = []
    for key in ("tables", "blocks"):
        for b in lesson.get(key) or []:
            if tuple(b.get("headers") or ()) == EMT:
                out.append(b)
    return out


def _ekt_blocks(lesson: dict) -> list[dict]:
    out: list[dict] = []
    for key in ("tables", "blocks"):
        for b in lesson.get(key) or []:
            if tuple(b.get("headers") or ()) == EKT:
                out.append(b)
    return out


def main() -> None:
    from kashmiri_maithili_s2_pairs import KS_RO

    maithili = json.loads(MAI.read_text(encoding="utf-8"))
    kashmiri = json.loads(KSH.read_text(encoding="utf-8"))
    m_by_id = {x["id"]: x for x in maithili}
    changed = 0

    for les in kashmiri:
        lid = les["id"]
        mles = m_by_id.get(lid)
        if not mles:
            continue
        m_blks = _emt_blocks(mles)
        k_blks = _ekt_blocks(les)
        if len(m_blks) != len(k_blks):
            raise RuntimeError(
                f"lesson {lid}: EMT block count {len(m_blks)} != EKT {len(k_blks)}"
            )

        for bi, (mb, kb) in enumerate(zip(m_blks, k_blks)):
            mrows = mb.get("rows") or []
            krows = kb.get("rows") or []
            m_eng = [r[0] for r in mrows]
            new_rows: list[list[str]] = []

            use_s2_pairs = lid in KS_RO and len(m_eng) == len(krows) == len(KS_RO[lid])

            for j, kr in enumerate(krows):
                if len(kr) < 3:
                    raise RuntimeError(f"lesson {lid} row {j} expected 3 cols")
                old_en, ks, ro = kr[0], kr[1], kr[2]

                if use_s2_pairs:
                    ks, ro = KS_RO[lid][j][0], KS_RO[lid][j][1]
                    en = m_eng[j]
                elif j < len(m_eng):
                    en = m_eng[j]
                else:
                    en = old_en

                new_rows.append([en, ks, ro])

            if new_rows != krows:
                kb["rows"] = new_rows
                changed += 1

    KSH.write_text(json.dumps(kashmiri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated English from Maithili in", changed, "lessons (tables patched where rows differed)")


if __name__ == "__main__":
    main()
