# Section 3: Phrases & sentence structures (chapterIds 543–596). Eighteen examples each:
# English gloss, Assamese sentence, ITRANS-style transliteration (matches assamese_phrases_rows.py).
from assamese_lesson_helpers import ch, r, block_table
from assamese_phrases_meta import META
from assamese_phrases_rows import ROWS


def _b(cid: int, title: str, content: str, intro: str, rows: list, heading: str = "Examples") -> dict:
    return ch(cid, title, content, intro, blocks=[block_table(heading, rows)])


def add_chapters_543_596(out: list) -> None:
    """Append lessons 543–596 from curated ROWS + META (Assamese)."""
    for cid in range(543, 597):
        m = META[cid]
        rows = [r(en, asm, rom) for en, asm, rom in ROWS[cid]]
        out.append(_b(cid, m["title"], m["content"], m["intro"], rows))
