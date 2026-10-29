"""Table 1 detectors on the coached-only pool (sealed as P91-P94 in PREDICTIONS.md).

Usage: python3 scripts/coached_pool.py [JUDGE] [--out results/coached_pool_<judge>.md]
Pool: the four coached cartels among the original five (C_msg, C_full, C_adapt, C_price), so the unaware cartel's
1.00 does not enter the pooled value. Negatives: all 40 honest episodes. Own RNG (seed 71). Reads existing scores only.
"""
import argparse
import pathlib

import numpy as np

import analyze as A

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIRS = ["runs_main", "runs_adapt", "runs_price", "runs_profit", "runs_ctrl"]
NEG = ["H_comp", "H_high"]
POOLS = {"original five": ["C_naive", "C_msg", "C_full", "C_adapt", "C_price"],
         "coached four": ["C_msg", "C_full", "C_adapt", "C_price"]}
DETS = ["M", "P", "A", "C", "B", "idx_last3", "hold_rate"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("judge", nargs="?", default="gpt-4.1-mini-2025-04-14")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    A.RNG = np.random.default_rng(71)
    S = A.load(",".join(str(ROOT / r) for r in DIRS), a.judge)
    arms = lambda names, d: [v[d] for v in S.values() if v["arm"] in names and d in v]
    out = [f"judge {a.judge}; pooled AUROC [95% CI] against all 40 honest episodes (P91-P94)", "",
           "| pool | " + " | ".join(DETS) + " |", "|---" * (len(DETS) + 1) + "|"]
    for name, pool in POOLS.items():
        cells = []
        for d in DETS:
            neg, pos = arms(NEG, d), arms(pool, d)
            lo, hi = A.boot(neg, pos, A.auroc)
            cells.append(f"{A.auroc(neg, pos):.2f} [{lo:.2f}, {hi:.2f}] (n={len(pos)})")
        out.append(f"| {name} | " + " | ".join(cells) + " |")
    path = ROOT / (a.out or f"results/coached_pool_{a.judge.split('-2025')[0]}.md")
    path.write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
