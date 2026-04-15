import ast
import re
from pathlib import Path

files = [
    ("dogri_lessons_a.py", "LESSONS_A"),
    ("dogri_lessons_b.py", "LESSONS_B"),
    ("dogri_lessons_s3a.py", "LESSONS_S3A"),
    ("dogri_lessons_s3b.py", "LESSONS_S3B"),
    ("dogri_lessons_s4.py", "LESSONS_S4"),
    ("dogri_lessons_s5a.py", "LESSONS_S5A"),
    ("dogri_lessons_s5b.py", "LESSONS_S5B"),
]

seen = set()
for fn, name in files:
    g = {}
    exec(Path(fn).read_text(encoding="utf-8"), g)
    d = g[name]
    for cid, rows in d.items():
        for r in rows:
            seen.add(r[0])

lines = sorted(seen)
Path("all_unique_en.txt").write_text("\n".join(lines), encoding="utf-8")
print("unique", len(lines))
