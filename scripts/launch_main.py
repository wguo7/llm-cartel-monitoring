"""Run the main grid (arms x seeds) with a budget kill rule. Writes progress to logs/main.log.

Usage: python3 scripts/launch_main.py --budget 79 [--workers 8]
Skips episodes that already finished (collusion_metrics.json present), so it can be re-run after a stop.
"""
import argparse
import json
import pathlib
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import cost  # noqa: E402

ARMS = ["H_comp", "H_high", "C_naive", "C_msg", "C_full"]
SEEDS = range(100, 120)
OUT = ROOT / "runs_main"
lock = threading.Lock()
stopped = threading.Event()


def spent():
    rows = []
    for f in OUT.rglob("usage.jsonl"):
        rows += [json.loads(l) for l in f.read_text().splitlines() if l.strip()]
    return cost.cost_of(rows)[0]


def done(arm, seed):
    return any((OUT / f"{arm}_s{seed}").glob("*/collusion_metrics.json"))


def one(job, budget, log):
    arm, seed = job
    if stopped.is_set() or done(arm, seed):
        return
    with lock:
        s = spent()
        if s > budget:
            stopped.set()
            log.write(f"KILL: spend ${s:.2f} > budget ${budget}; not starting {arm} {seed}\n")
            log.flush()
            return
    rc = subprocess.call([sys.executable, str(ROOT / "scripts/run_arm.py"), arm, str(seed),
                          "--sellers", "5", "--buyers", "5", "--out", str(OUT)],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with lock:
        log.write(f"{arm} {seed} exit={rc} spend=${spent():.2f} ok={done(arm, seed)}\n")
        log.flush()


def main():
    global OUT
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, required=True)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--arms", nargs="+", default=ARMS)
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--log", default="main")
    a = ap.parse_args()
    OUT = pathlib.Path(a.out).expanduser().resolve()
    OUT.mkdir(exist_ok=True)
    # interleave arms so a stop leaves a balanced partial grid
    jobs = [(arm, seed) for seed in SEEDS for arm in a.arms]
    with open(ROOT / f"logs/{a.log}.log", "a") as log, ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda j: one(j, a.budget, log), jobs))
        n = sum(done(*j) for j in jobs)
        log.write(f"FINISHED {n}/{len(jobs)} episodes, spend ${spent():.2f}\n")


if __name__ == "__main__":
    main()
