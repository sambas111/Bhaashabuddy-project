# Merge odia_mid_a.txt + odia_mid_b.txt into populate_odia_s2.py (lessons 512-542).
from pathlib import Path

BASE = Path(__file__).parent.resolve()
MID = (BASE / "odia_mid_a.txt").read_text(encoding="utf-8").rstrip() + "\n\n" + (
    BASE / "odia_mid_b.txt"
).read_text(encoding="utf-8").rstrip()
p = BASE / "populate_odia_s2.py"
t = p.read_text(encoding="utf-8")
i = t.find("\n# ━━━ 519: Simple Past Tense")
j = t.find("\n}  # end LESSONS")
if i == -1 or j == -1:
    raise SystemExit(f"markers not found: i={i} j={j}")
p.write_text(t[:i] + "\n" + MID + t[j:], encoding="utf-8")
print("Merged odia_mid_a + odia_mid_b into populate_odia_s2.py")
