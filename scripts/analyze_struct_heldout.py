"""Frozen rubric with held-out honest negatives (added after review round 7; predictions P75-P76 sealed first).
For each seed half, fit the structured-rubric logistic regression on the other half's 80 episodes (the eight original
arms) and score this half's honest episodes and later-arm (runs_ctrl) episodes, so no scored episode was in its fit.

Usage: python scripts/analyze_struct_heldout.py [JUDGE] -> results/struct_heldout_<judge>.md
"""
import pathlib
import sys

import analyze_struct as S

ROOT = pathlib.Path(__file__).resolve().parents[1]


def main():
    judge = sys.argv[1] if len(sys.argv) > 1 else "qwen2.5-14b-instruct-4bit"
    eps = list(S.rows(judge, S.FIT_DIRS).values())
    F = list(S.rows(judge, ["runs_ctrl"]).values())
    half = lambda e: e["seed"] < 110
    for h in (True, False):
        g = S.fit([e for e in eps if half(e) != h])[0]
        for e in eps + F:
            if half(e) == h:
                e["ho"] = g(e["x"])
    out = [f"judge {judge}; rubric fitted on one seed half, applied to the other half's honest and later-arm episodes", "",
           "| negatives | " + " | ".join(S.FRESH) + " |", "|---" * (len(S.FRESH) + 1) + "|"]
    for title, narms in [("all 40 honest", S.HONEST), ("plain honest only", ["H_comp"]), ("CEO-pressure honest only", ["H_high"])]:
        n = [e["ho"] for e in eps if e["arm"] in narms]
        out.append(f"| {title} | " + " | ".join(S.cell(n, [e["ho"] for e in F if e["arm"] == a]) for a in S.FRESH) + " |")
    path = ROOT / f"results/struct_heldout_{judge}.md"
    path.write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
