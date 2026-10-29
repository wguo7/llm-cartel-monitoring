"""Bootstrap interval for the knows-all-screens cartel's reduction in buyer-surplus loss (added after the fourth review).

Usage: python3 scripts/harm_ci.py -> prints the reduction 1 - (ref - C_price) / (ref - C_full) with a 95% interval, for
ref = plain honest (H_comp) and ref = CEO-pressure honest (H_high). Each arm is resampled independently (2,000 draws); own
RNG (seed 17).
"""
import json
import pathlib

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
RNG = np.random.default_rng(17)


def surplus(arm):
    return np.array([json.loads(f.read_text())["combined_buyer_surplus"] for r in ["runs_main", "runs_adapt", "runs_price"]
                     for f in sorted((ROOT / r).glob(f"{arm}_s*/*/collusion_metrics.json"))])


price, full = surplus("C_price"), surplus("C_full")
for ref_arm in ["H_comp", "H_high"]:
    ref = surplus(ref_arm)
    f = lambda r, p, c: 1 - (r.mean() - p.mean()) / (r.mean() - c.mean())
    bs = [f(RNG.choice(ref, len(ref)), RNG.choice(price, len(price)), RNG.choice(full, len(full))) for _ in range(2000)]
    lo, hi = np.percentile(bs, [2.5, 97.5])
    print(f"ref {ref_arm} (n={len(ref)}): reduction {f(ref, price, full):.2f} [{lo:.2f}, {hi:.2f}]")

# added after review round 6: the knows-all-screens cartel's buyer surplus minus each honest arm's (independent resampling)
for ref_arm in ["H_comp", "H_high"]:
    ref = surplus(ref_arm)
    bs = [RNG.choice(price, len(price)).mean() - RNG.choice(ref, len(ref)).mean() for _ in range(2000)]
    lo, hi = np.percentile(bs, [2.5, 97.5])
    print(f"C_price minus {ref_arm}: {price.mean() - ref.mean():+.1f} [{lo:+.1f}, {hi:+.1f}] dollars per episode")
