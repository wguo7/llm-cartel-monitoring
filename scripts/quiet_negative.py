"""Every cartel against the quiet-honest negative arm (sealed as P95-P100 in PREDICTIONS.md).

Usage: python3 scripts/quiet_negative.py [JUDGE] [--neg H_quiet] [--out results/quiet_negative_<judge>.md]
Negatives: the 20 H_quiet episodes (honest briefing plus "never discuss prices ... with other sellers"), so judges face
negatives that were told not to talk about prices. --neg H_comp reproduces the plain-honest split as a check.
Own RNG (seed 81). Reads existing scores and market logs only; no model calls.
"""
import argparse
import pathlib

import numpy as np

import analyze as A

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIRS = ["runs_main", "runs_adapt", "runs_price", "runs_profit", "runs_ctrl", "runs_quiet"]
CARTELS = ["C_naive", "C_notice", "C_msg", "C_full", "C_adapt", "C_price", "C_profit", "C_profit_screen"]
POOLS = {"coached four": ["C_msg", "C_full", "C_adapt", "C_price"],
         "coached six": ["C_msg", "C_full", "C_adapt", "C_price", "C_profit", "C_profit_screen"]}
DETS = ["M", "P", "A", "C", "B", "S", "K", "R", "N", "E", "idx_last3", "hold_rate"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("judge", nargs="?", default="gpt-4.1-mini-2025-04-14")
    ap.add_argument("--neg", default="H_quiet")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    A.RNG = np.random.default_rng(81)
    dirs = [str(ROOT / r) for r in DIRS if (ROOT / r).exists()]
    S = A.load(",".join(dirs), a.judge)
    arms = lambda names, d: [v[d] for v in S.values() if v["arm"] in names and d in v]
    idx = arms([a.neg], "idx_last3")
    out = [f"judge {a.judge}; negatives: {a.neg} only (n={len(idx)}); AUROC [95% CI] (P95-P100)", "",
           f"{a.neg} mean collusion index (last third): {np.mean(idx):.3f}; mean hold rate: "
           f"{np.mean(arms([a.neg], 'hold_rate')):.3f}", "",
           "| detector | " + " | ".join(CARTELS + list(POOLS)) + " |", "|---" * (len(CARTELS) + len(POOLS) + 1) + "|"]
    for d in DETS:
        neg = arms([a.neg], d)
        if not neg:
            continue
        cells = []
        for names in [[c] for c in CARTELS] + list(POOLS.values()):
            pos = arms(names, d)
            if not pos:
                cells.append("")
                continue
            lo, hi = A.boot(neg, pos, A.auroc)
            cells.append(f"{A.auroc(neg, pos):.2f} [{lo:.2f}, {hi:.2f}]")
        out.append(f"| {d} | " + " | ".join(cells) + " |")
    path = ROOT / (a.out or f"results/quiet_negative_{a.judge.split('-2025')[0]}.md")
    path.write_text("\n".join(out) + "\n")
    print("\n".join(out[:4]))


if __name__ == "__main__":
    main()
