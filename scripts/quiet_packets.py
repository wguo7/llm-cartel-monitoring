"""Blind conduct-annotation batch for the quiet-honest arm (sealed as P95 in PREDICTIONS.md).

Usage: python3 scripts/quiet_packets.py OUTDIR
Writes OUTDIR/batch6/ep_XXXX.txt (seller messages only, hour by hour) for the 20 H_quiet episodes (runs_quiet) plus 10
already-labelled calibration episodes (H_comp and C_full, seeds 100-104), shuffled with random ids, and
OUTDIR/key6.json (id -> episode, kept outside the batch). Ids avoid those in OUTDIR/key.json. Own RNG (seed 91).
"""
import json
import pathlib
import sys

import numpy as np

from conduct_packets import transcript

ROOT = pathlib.Path(__file__).resolve().parents[1]
RNG = np.random.default_rng(91)


def main():
    od = pathlib.Path(sys.argv[1])
    used = {int(k.split("_")[1]) for k in json.loads((od / "key.json").read_text())}
    eps = [("runs_quiet", "H_quiet", s) for s in range(100, 120)]
    eps += [("runs_main", a, s) for a in ["H_comp", "C_full"] for s in range(100, 105)]
    order = RNG.permutation(len(eps))
    ids = RNG.choice(sorted(set(range(1000, 10000)) - used), len(eps), replace=False)
    b = od / "batch6"
    b.mkdir(parents=True, exist_ok=True)
    key = {}
    for k, i in enumerate(order):
        runs, arm, seed = eps[i]
        res = next((ROOT / runs).glob(f"{arm}_s{seed}/*/auction_results.md"))
        (b / f"ep_{ids[k]}.txt").write_text(transcript(res))
        key[f"ep_{ids[k]}"] = f"{arm}_s{seed}"
    (od / "key6.json").write_text(json.dumps(key, indent=1))
    print(f"wrote {len(key)} episodes to {b}")


if __name__ == "__main__":
    main()
