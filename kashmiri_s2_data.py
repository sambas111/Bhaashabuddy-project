# -*- coding: utf-8 -*-
"""
Topic-specific rows for Kashmiri section 2 (lessons 510–542).

English strings match `data_maithili.json` section 2 (exported in `_maithili_s2_english.json`); Kashmiri + roman are faithful translations in `kashmiri_maithili_s2_pairs.py`.
Sources: O. N. Koul, The Kashmiri Language: A Grammatical Sketch (ikashmir.net/onkoul);
Modern Kashmiri Grammar (kashmirculturaltrust.in); Wikivoyage Kashmiri phrasebook; koshur.org course notes.
Roman follows common academic Kashmiri transliteration (long vowels as a:, etc.).
Devanagari is a practical gloss for learners (Kashmiri in Devanagari orthography).
"""
from __future__ import annotations

import json
from pathlib import Path

from kashmiri_maithili_s2_pairs import KS_RO

# Helper: [English, Kashmiri Devanagari, Roman transliteration]


def R(e: str, ks: str, ro: str) -> list[str]:
    return [e, ks, ro]


_ROOT = Path(__file__).resolve().parent
_ENGLISH_BY_LESSON: dict[int, list[str]] = {
    x["id"]: x["english"]
    for x in json.loads((_ROOT / "_maithili_s2_english.json").read_text(encoding="utf-8"))
}


def _rows(n: int) -> list[list[str]]:
    ens = _ENGLISH_BY_LESSON[n]
    pairs = KS_RO[n]
    if len(ens) != len(pairs):
        raise ValueError(f"lesson {n}: english {len(ens)} vs kashmiri {len(pairs)}")
    return [R(e, ks, ro) for e, (ks, ro) in zip(ens, pairs)]


L510 = _rows(510)
L511 = _rows(511)
L512 = _rows(512)
L513 = _rows(513)
L514 = _rows(514)
L515 = _rows(515)
L516 = _rows(516)
L517 = _rows(517)
L518 = _rows(518)
L519 = _rows(519)
L520 = _rows(520)
L521 = _rows(521)
L522 = _rows(522)
L523 = _rows(523)
L524 = _rows(524)
L525 = _rows(525)
L526 = _rows(526)
L527 = _rows(527)
L528 = _rows(528)
L529 = _rows(529)
L530 = _rows(530)
L531 = _rows(531)
L532 = _rows(532)
L533 = _rows(533)
L534 = _rows(534)
L535 = _rows(535)
L536 = _rows(536)
L537 = _rows(537)
L538 = _rows(538)
L539 = _rows(539)
L540 = _rows(540)
L541 = _rows(541)
L542 = _rows(542)


PATCH: dict[int, dict[str, list[list[str]]]] = {
    510: {"Pronoun and article examples": L510},
    511: {"Respectful and plural forms": L511},
    512: {"Verb examples in sentences": L512},
    513: {"Simple present sentences": L513},
    514: {'"To be" in present': L514},
    515: {"Present continuous sentences": L515},
    516: {"Simple future sentences": L516},
    517: {"Future continuous examples": L517},
    518: {"Simple past (no object)": L518},
    519: {"Simple past (with object)": L519},
    520: {'Past "to be" and state': L520},
    521: {"Exceptional verb past forms": L521},
    522: {"Past continuous sentences": L522},
    523: {"Perfect tense examples": L523},
    524: {"Preposition / postposition examples": L524},
    525: {'"To" in sentences': L525},
    526: {"Person as object": L526},
    527: {"My / Your / His / Her": L527},
    528: {"Questions in Kashmiri": L528},
    529: {"Negative present": L529},
    530: {"Negative past": L530},
    531: {"Negative future": L531},
    532: {"Nouns, gender and number": L532},
    533: {"Nouns with prepositions": L533},
    534: {"Similar prepositions": L534},
    535: {"Case usage": L535},
    536: {"Commands and requests": L536},
    537: {"Time words and sentences": L537},
    538: {"Causative verb examples": L538},
    539: {"Agreement examples": L539},
    540: {"Perfect second style": L540},
    541: {"Perfect continuous": L541},
    542: {"No/not vs don't want": L542},
}
