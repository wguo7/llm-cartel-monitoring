"""Blind conduct-annotation packets (sealed as P81-P85 in PREDICTIONS.md).

Usage: python3 scripts/conduct_packets.py OUTDIR
Writes OUTDIR/batch{1..5}/ep_XXXX.txt (seller messages only, hour by hour) for H_comp, H_high, C_naive, C_msg and C_full,
seeds 100-119, shuffled across batches with random ids, plus OUTDIR/key.json (id -> episode, kept outside the batches).
Own RNG (seed 53).
"""
import json
import pathlib
import re
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARMS = ["H_comp", "H_high", "C_naive", "C_msg", "C_full"]
RNG = np.random.default_rng(53)


def transcript(res):
    rounds = [json.loads(x) for x in re.findall(r"````json\n(.*?)\n````", res.read_text(), re.S)]
    out = []
    for r in rounds:
        msgs = r.get("seller_messages") or {}
        if msgs:
            out.append(f"Hour {r['round_number']}")
            out += [f"{who}: {m}" for who, m in msgs.items() if m]
    return "\n".join(out) + "\n"


def main():
    od = pathlib.Path(sys.argv[1])
    eps = [(a, s) for a in ARMS for s in range(100, 120)]
    order = RNG.permutation(len(eps))
    ids = RNG.choice(np.arange(1000, 10000), len(eps), replace=False)
    key = {}
    for k, i in enumerate(order):
        arm, seed = eps[i]
        res = next((ROOT / "runs_main").glob(f"{arm}_s{seed}/*/auction_results.md"))
        b = od / f"batch{k // 20 + 1}"
        b.mkdir(parents=True, exist_ok=True)
        (b / f"ep_{ids[k]}.txt").write_text(transcript(res))
        key[f"ep_{ids[k]}"] = f"{arm}_s{seed}"
    (od / "key.json").write_text(json.dumps(key, indent=1))
    print(f"wrote {len(key)} episodes in {k // 20 + 1} batches to {od}")


if __name__ == "__main__":
    main()
