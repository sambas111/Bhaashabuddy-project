"""Shared helpers for Bengali lesson JSON generation."""
H = ["English", "Bengali", "Transliteration"]
S = 1


def r(e, b, rom):
    return [e, b, rom]


def block_table(heading, rows):
    return {
        "type": "table",
        "heading": heading,
        "headers": H,
        "speakCol": S,
        "rows": rows,
    }


def blk_para(heading, content):
    return {"type": "paragraph", "heading": heading, "content": content}


def lesson_blocks(cid, title, content, intro, rows, heading="Examples"):
    """Single table block (common pattern for grammar/conversation)."""
    return ch(
        cid,
        title,
        content,
        intro,
        blocks=[block_table(heading, rows)],
    )


def ch(cid, title, content, intro, tables=None, blocks=None):
    o = {
        "id": cid,
        "title": title,
        "url": "#",
        "content": content,
        "intro": intro,
    }
    if tables is not None:
        o["tables"] = tables
    if blocks is not None:
        o["blocks"] = blocks
    return o
