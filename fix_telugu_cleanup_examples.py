import json

"""
Remove generic 'Example for ...' placeholder rows from Telugu phrase chapters
765–797 so that only meaningful topic‑specific sentences remain.
"""

PATH = "data_telugu.json"

TARGET_IDS = set(range(765, 798))


def is_placeholder_row(row):
    if not isinstance(row, list) or not row:
        return False
    eng = str(row[0]).strip()
    tel = str(row[1]).strip() if len(row) > 1 else ""
    return eng.startswith("Example for") or eng.startswith("Example ") or "ఉదాహరణ" in tel


with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

removed_counts = {}

for ch in data:
    cid = ch.get("id")
    if cid not in TARGET_IDS:
        continue
    tables = ch.get("tables") or []
    if not tables:
        continue
    rows = tables[0].get("rows") or []
    new_rows = [r for r in rows if not is_placeholder_row(r)]
    removed = len(rows) - len(new_rows)
    if removed > 0:
        tables[0]["rows"] = new_rows
        removed_counts[cid] = removed

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Removed placeholder rows in chapters:", removed_counts)

