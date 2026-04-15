# One-off helper: verify all LESSONS dicts have 15–20 rows per chapter.
# Run: python _expand_urdu_s3.py

import importlib.util
import pathlib

BASE = pathlib.Path(__file__).parent
MIN_R, MAX_R = 15, 20

def load(name):
    spec = importlib.util.spec_from_file_location(name, BASE / f"{name}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for k, v in vars(m).items():
        if k.startswith("LESSONS") and isinstance(v, dict):
            return v
    return None


def main():
    for mod in [
        "urdu_lessons_s1",
        "urdu_lessons_s2a",
        "urdu_lessons_s2b",
        "urdu_lessons_s3a",
        "urdu_lessons_s3b",
        "urdu_lessons_s4",
        "urdu_lessons_s5a",
        "urdu_lessons_s5b",
    ]:
        d = load(mod)
        if not d:
            print(mod, "SKIP")
            continue
        bad = [(cid, len(rows)) for cid, rows in sorted(d.items()) if not (MIN_R <= len(rows) <= MAX_R)]
        if bad:
            print(f"{mod}: OUT OF RANGE ({len(bad)} lessons)")
            for cid, n in bad[:30]:
                print(f"  {cid}: {n} rows")
            if len(bad) > 30:
                print(f"  ... +{len(bad)-30} more")
        else:
            print(f"{mod}: OK ({len(d)} lessons, all {MIN_R}–{MAX_R} rows)")


if __name__ == "__main__":
    main()
