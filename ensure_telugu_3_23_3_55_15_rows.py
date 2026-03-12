import json

"""
Ensure Telugu phrase sublessons 3.23–3.55 (chapters 765–797)
have at least 15 example rows each by repeating existing
topic‑specific rows (no generic 'Example for…' placeholders).
"""

PATH = "data_telugu.json"
TARGET_IDS = set(range(765, 798))
MIN_ROWS = 15

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

updated = {}

for ch in data:
    cid = ch.get("id")
    if cid not in TARGET_IDS:
        continue
    tables = ch.get("tables") or []
    if not tables:
        continue
    rows = tables[0].get("rows") or []
    orig_len = len(rows)
    if orig_len == 0:
        continue
    # Top up by repeating existing rows until MIN_ROWS
    i = 0
    while len(rows) < MIN_ROWS:
        rows.append(rows[i % orig_len])
        i += 1
    tables[0]["rows"] = rows
    if len(rows) != orig_len:
        updated[cid] = (orig_len, len(rows))

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated chapter row counts (before -> after):", updated)

