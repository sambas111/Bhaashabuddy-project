# -*- coding: utf-8 -*-
"""
Apply long English (≥15 words) plus aligned Kashmiri + roman from:
- kashmiri_lesson_overrides.LESSON_ROWS (priority)
- kashmiri_maithili_s2_pairs.KS_RO for lessons 510–542 when row counts match
- Else Maithili EMT gloss + existing Kashmiri EKT columns (English replaced only)

Run: py -3 apply_kashmiri_full_enrichment.py
"""
from __future__ import annotations

import json
from pathlib import Path

from kashmiri_lesson_overrides import LESSON_ROWS
from kashmiri_long_english_util import long_english
from kashmiri_maithili_s2_pairs import KS_RO

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
    maithili = json.loads(MAI.read_text(encoding="utf-8"))
    kashmiri = json.loads(KSH.read_text(encoding="utf-8"))
    m_by_id = {x["id"]: x for x in maithili}
    patched = 0

    for les in kashmiri:
        lid = les["id"]
        mles = m_by_id.get(lid)
        if not mles:
            continue
        m_blks = _emt_blocks(mles)
        k_blks = _ekt_blocks(les)
        if len(m_blks) != len(k_blks):
            raise RuntimeError(f"lesson {lid}: EMT block count {len(m_blks)} != EKT {len(k_blks)}")

        # Full table override (one or more blocks)
        if lid in LESSON_ROWS:
            flat = LESSON_ROWS[lid]
            if len(k_blks) == 1:
                k_blks[0]["rows"] = [
                    [long_english(r[0]), r[1], r[2]] for r in flat
                ]
                patched += 1
                continue
            idx = 0
            for mb, kb in zip(m_blks, k_blks):
                n = len(mb.get("rows") or [])
                chunk = flat[idx : idx + n]
                kb["rows"] = [[long_english(r[0]), r[1], r[2]] for r in chunk]
                idx += n
            if idx != len(flat):
                raise RuntimeError(
                    f"lesson {lid}: LESSON_ROWS length {len(flat)} != EMT rows sum {idx}"
                )
            patched += 1
            continue

        for bi, (mb, kb) in enumerate(zip(m_blks, k_blks)):
            mrows = mb.get("rows") or []
            krows = kb.get("rows") or []
            m_eng = [r[0] for r in mrows]
            use_s2 = (
                lid in KS_RO
                and len(m_eng) == len(krows) == len(KS_RO[lid])
            )
            new_rows: list[list[str]] = []
            for j, kr in enumerate(krows):
                if len(kr) < 3:
                    raise RuntimeError(f"lesson {lid} row {j} expected 3 cols")
                old_en, ks, ro = kr[0], kr[1], kr[2]
                gloss = m_eng[j] if j < len(m_eng) else old_en
                if use_s2:
                    ks, ro = KS_RO[lid][j][0], KS_RO[lid][j][1]
                en_out = long_english(gloss)
                new_rows.append([en_out, ks, ro])
            kb["rows"] = new_rows
            patched += 1

    KSH.write_text(
        json.dumps(kashmiri, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("Patched EKT blocks in", patched, "lesson-block pairs; wrote", KSH.name)


if __name__ == "__main__":
    main()
