#!/usr/bin/env python3
"""
Re-run all build_*_from_hindi.py scripts so every language picks up the new
Daily Life entries from hindi_data.js. Runs with limited concurrency to avoid
tripping Google/MyMemory rate limits. Continues on error and prints a summary.
"""
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).parent
MAX_PARALLEL = int(sys.argv[1]) if len(sys.argv) > 1 else 3

SCRIPTS = [
    "build_kannada_from_hindi.py",
    "build_tamil_from_hindi.py",
    "build_telugu_from_hindi.py",
    "build_marathi_from_hindi.py",
    "build_gujarati_from_hindi.py",
    "build_punjabi_from_hindi.py",
    "build_bengali_from_hindi.py",
    "build_assamese_from_hindi.py",
    "build_malayalam_from_hindi.py",
    "build_odia_from_hindi.py",
    "build_nepali_from_hindi.py",
    "build_sanskrit_from_hindi.py",
    "build_dogri_from_hindi.py",
    "build_konkani_from_hindi.py",
    "build_bodo_from_hindi.py",
    "build_santali_from_hindi.py",
    "build_urdu_from_hindi.py",
    "build_sindhi_from_hindi.py",
    "build_meitei_from_hindi.py",
    "build_kashmiri_from_hindi.py",
]


def run_one(script: str):
    t0 = time.time()
    log = ROOT / (script.replace(".py", ".log"))
    with open(log, "w", encoding="utf-8") as f:
        proc = subprocess.run(
            [sys.executable, str(ROOT / script)],
            stdout=f, stderr=subprocess.STDOUT, cwd=str(ROOT),
        )
    dt = time.time() - t0
    return script, proc.returncode, round(dt, 1)


def main():
    print(f"running {len(SCRIPTS)} builds, max_parallel={MAX_PARALLEL}", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as ex:
        futs = {ex.submit(run_one, s): s for s in SCRIPTS}
        for fut in as_completed(futs):
            script, rc, dt = fut.result()
            status = "OK" if rc == 0 else f"FAIL({rc})"
            results.append((script, rc, dt))
            print(f"  {status:10} {script}  {dt}s", flush=True)
    print("\n=== summary ===", flush=True)
    for script, rc, dt in sorted(results):
        print(f"  {'OK' if rc==0 else 'FAIL':6} {script}  {dt}s", flush=True)
    fails = [s for s, rc, _ in results if rc != 0]
    print("\nfailed:", fails if fails else "none", flush=True)


if __name__ == "__main__":
    main()
