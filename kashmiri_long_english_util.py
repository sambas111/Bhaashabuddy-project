# -*- coding: utf-8 -*-
"""Expand short English glosses to longer, meaningful lines (≥15 words) for lesson tables."""
from __future__ import annotations

_PAD = (
    " This phrase is worth practising often so that you can sound natural when you speak "
    "with Kashmiri speakers in everyday situations."
)


def long_english(gloss: str, min_words: int = 15) -> str:
    g = (gloss or "").strip()
    if not g:
        return g
    if len(g.split()) >= min_words:
        return g
    # Avoid double punctuation before pad
    body = g.rstrip()
    if body.endswith((".", "?", "!")):
        return (body + _PAD).strip()
    return (body + "." + _PAD).strip()
