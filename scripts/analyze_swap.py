"""Analysis of the message-swap test (scripts/swap_messages.py; predictions P70-P74). For each cartel/honest pair, the
2x2 within-seed design gives a message effect (p with the honest arm's messages minus p with the cartel's, averaged over
whose actions are shown) and an action effect (p with the cartel's actions minus p with the honest arm's, averaged over
whose messages are shown), in probability points, with 95% bootstrap intervals over seeds (seed 37).

Usage: python scripts/analyze_swap.py [JUDGE] -> results/swap_<judge>.md
"""
import json
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
CARTELS, HONEST, SEEDS = ["C_full", "C_msg"], ["H_high", "H_comp"], list(range(100, 120))
B = 10000


def main():
    judge = sys.argv[1] if len(sys.argv) > 1 else "qwen2.5-14b-instruct-4bit"
    p = {}
    for l in (ROOT / "results" / f"scores_runs_main_{judge}.jsonl").read_text().splitlines():
        d = json.loads(l)
        if d["view"] == "C":
            arm, seed = d["episode"].rsplit("_s", 1)
            p[(arm, arm, int(seed))] = d["score"]
    for l in (ROOT / "results" / f"scores_swap_{judge}.jsonl").read_text().splitlines():
        d = json.loads(l)
        p[(d["actions"], d["messages"], d["seed"])] = d["score"]
    rng = np.random.default_rng(37)
    out = [f"judge {judge}; view C; cells are mean p_collusion (0-100) over seeds 100-119", "",
           "| Cartel | Honest arm | cartel actions + cartel messages | cartel actions + honest messages | "
           "honest actions + cartel messages | honest actions + honest messages | message effect | action effect | n |",
           "|---|---|---|---|---|---|---|---|---|"]
    for k in CARTELS:
        for h in HONEST:
            seeds = [s for s in SEEDS if all((a, m, s) in p for a in (k, h) for m in (k, h))]
            kk, kh, hk, hh = (np.array([p[(a, m, s)] for s in seeds]) for a, m in [(k, k), (k, h), (h, k), (h, h)])
            msg = ((kh + hh) - (kk + hk)) / 2
            act = ((kk + kh) - (hk + hh)) / 2

            def ci(x):
                bs = [x[rng.integers(0, len(x), len(x))].mean() for _ in range(B)]
                lo, hi = np.percentile(bs, [2.5, 97.5])
                return f"{x.mean():+.1f} [{lo:+.1f}, {hi:+.1f}]"
            out.append(f"| {k} | {h} | {kk.mean():.1f} | {kh.mean():.1f} | {hk.mean():.1f} | {hh.mean():.1f} | {ci(msg)} | "
                       f"{ci(act)} | {len(seeds)} |")
    path = ROOT / "results" / f"swap_{judge}.md"
    path.write_text("\n".join(out) + "\n")
    print("\n".join(out[2:]))


if __name__ == "__main__":
    main()
