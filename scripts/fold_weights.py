"""Per-seed-fold weights of the structured rubric (backs the report's "signs agree in both seed folds").

Usage: python3 scripts/fold_weights.py [JUDGE] -> results/struct_fold_weights_<judge>.md. Reuses analyze_struct's fit; no
model calls.
"""
import pathlib
import sys

import analyze_struct as S

ROOT = pathlib.Path(__file__).resolve().parents[1]
judge = sys.argv[1] if len(sys.argv) > 1 else "qwen2.5-14b-instruct-4bit"
eps = list(S.rows(judge, S.FIT_DIRS).values())
out = [f"judge {judge}; rubric weights per standard deviation, fitted on each seed half (as in the held-out-seed column)", "",
       "| fit on | " + " | ".join(S.SUBS) + " |", "|---" * (len(S.SUBS) + 1) + "|"]
for name, keep in [("seeds 100-109", lambda e: e["seed"] < 110), ("seeds 110-119", lambda e: e["seed"] >= 110),
                   ("all 160", lambda e: True)]:
    _, w, _ = S.fit([e for e in eps if keep(e)])
    out.append(f"| {name} | " + " | ".join(f"{x:+.2f}" for x in w[1:]) + " |")
(ROOT / f"results/struct_fold_weights_{judge}.md").write_text("\n".join(out) + "\n")
print("\n".join(out))
