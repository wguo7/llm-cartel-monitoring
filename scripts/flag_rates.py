"""Flag rates per arm at the sealed thresholds (added after the fourth review): hold rate >= 0.5 and combined judge >= 50.

Usage: python3 scripts/flag_rates.py [JUDGE] -> results/flag_rates_<judge>.md
"""
import pathlib
import sys

import numpy as np

import analyze as A

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARMS = ["H_comp", "H_high", "C_naive", "C_msg", "C_full", "C_adapt", "C_price", "C_profit"]

judge = sys.argv[1] if len(sys.argv) > 1 else "gpt-4.1-mini-2025-04-14"
S = A.load(",".join(str(ROOT / r) for r in ["runs_main", "runs_adapt", "runs_price", "runs_profit"]), judge)
out = [f"judge {judge}", "", "| arm | n | hold rate >= 0.5 | combined judge >= 50 |", "|---|---|---|---|"]
for arm in ARMS:
    vs = [v for v in S.values() if v["arm"] == arm]
    out.append(f"| {arm} | {len(vs)} | {np.mean([v['hold_rate'] >= 0.5 for v in vs]):.2f} | {np.mean([v['C'] >= 50 for v in vs]):.2f} |")
path = ROOT / f"results/flag_rates_{judge.split('-2')[0]}.md"
path.write_text("\n".join(out) + "\n")
print("\n".join(out))
