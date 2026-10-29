"""Headline figure for page 2. Left: per cartel, AUROC against the 40 honest episodes for the combined judge (primary judge)
and the two price statistics, with 95% bootstrap intervals. Right: mean buyer surplus per episode with a 95% bootstrap
interval, with the two honest arms as reference lines. Includes the arms added after review when their scores exist.

Usage: python3 scripts/fig_headline.py [JUDGE] -> report/figs/fig0_headline.{png,pdf}
Own RNG (seed 31); values match the tables up to bootstrap noise in the interval ends.
"""
import json
import pathlib
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import analyze as A  # noqa: E402
from figures import COAL, GRID, HONEST, INK, INK2, SURF  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIRS = ["runs_main", "runs_adapt", "runs_price", "runs_profit", "runs_ctrl"]
A.RNG = np.random.default_rng(31)
ROWS = [("C_naive", "Unaware (positive control)"), ("C_notice", "Told of the monitor only"), ("C_msg", "Hides words"),
        ("C_full", "Cover stories"), ("C_adapt", "Hides words + asks"), ("C_price", "Knows all screens"),
        ("C_profit", "Profit cartel"), ("C_profit_screen", "Profit cartel, knows all screens")]
DETS = [("C", "Combined judge (messages + actions)", HONEST, "o"), ("idx_last3", "Price level", COAL, "s"),
        ("hold_rate", "Hold rate", "#8a5a00", "^")]


def main():
    judge = sys.argv[1] if len(sys.argv) > 1 else "gpt-4.1-mini-2025-04-14"
    S = A.load(",".join(str(ROOT / r) for r in DIRS), judge)
    by = {}
    for v in S.values():
        by.setdefault(v["arm"], []).append(v)
    neg_eps = by["H_comp"] + by["H_high"]
    rows = [(a, l) for a, l in ROWS if a in by]
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.8, 0.33 * len(rows) + 1.0), sharey=True,
                                 gridspec_kw={"width_ratios": [2.3, 1], "wspace": 0.06})
    for i, (arm, _) in enumerate(rows):
        y = len(rows) - 1 - i
        for k, (d, _, col, mk) in enumerate(DETS):
            neg = [v[d] for v in neg_eps if d in v]
            pos = [v[d] for v in by[arm] if d in v]
            if not pos:
                continue
            lo, hi = A.boot(neg, pos, A.auroc)
            yy = y + (1 - k) * 0.22
            ax.plot([lo, hi], [yy, yy], color=col, lw=1.6, solid_capstyle="round", alpha=0.85)
            ax.scatter([A.auroc(neg, pos)], [yy], color=col, marker=mk, s=18, zorder=3, edgecolors=SURF, linewidths=0.8)
    ax.axvline(0.5, color=INK2, lw=0.6, ls=(0, (2, 2)))
    ax.text(0.51, -0.55, "chance", fontsize=6.5, color=INK2, ha="left", va="bottom")
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([l for _, l in reversed(rows)], fontsize=7.5, color=INK)
    ax.set_xlim(0, 1.02)
    ax.set_ylim(-0.6, len(rows) - 0.2)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xlabel("AUROC against the 40 honest episodes (95% bootstrap interval)", fontsize=7.5)
    ax.grid(axis="x", color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    for _, lab, col, mk in DETS:
        ax.scatter([], [], color=col, marker=mk, s=18, label=lab)
    ax.legend(fontsize=7, frameon=False, loc="lower center", ncol=3, bbox_to_anchor=(0.45, 1.0), handletextpad=0.3,
              columnspacing=1.0)

    def surplus(arm):
        return np.array([json.loads(f.read_text())["combined_buyer_surplus"] for r in DIRS
                         for f in sorted((ROOT / r).glob(f"{arm}_s[0-9]*/*/collusion_metrics.json"))])
    for ref, ls in [("H_comp", "-"), ("H_high", (0, (3, 2)))]:
        bx.axvline(surplus(ref).mean(), color=HONEST, lw=0.9, ls=ls)
    bx.text(surplus("H_comp").mean() + 3, len(rows) - 0.75, "honest", fontsize=6.5, color=HONEST, va="bottom")
    bx.text(surplus("H_high").mean() - 3, len(rows) - 0.75, "honest\n+ CEO", fontsize=6.5, color=HONEST, va="bottom",
            ha="right")
    for i, (arm, _) in enumerate(rows):
        x = surplus(arm)
        lo, hi = np.percentile([A.RNG.choice(x, len(x)).mean() for _ in range(A.B)], [2.5, 97.5])
        y = len(rows) - 1 - i
        bx.plot([lo, hi], [y, y], color=INK2, lw=1.6, solid_capstyle="round")
        bx.scatter([x.mean()], [y], color=INK, s=16, zorder=3, edgecolors=SURF, linewidths=0.8)
    bx.set_xlim(0, 215)
    bx.set_xticks([0, 50, 100, 150, 200])
    bx.set_xlabel("Buyer surplus per episode ($)", fontsize=7.5)
    bx.set_title("Harm: what buyers kept", fontsize=7.5, color=INK, loc="left")
    bx.grid(axis="x", color=GRID, lw=0.6)
    bx.set_axisbelow(True)
    bx.tick_params(axis="y", length=0)
    fig.subplots_adjust(left=0.25, right=0.985, top=0.87, bottom=0.15)
    out = ROOT / "report/figs"
    for ext in ("pdf", "png"):
        fig.savefig(out / f"fig0_headline.{ext}", dpi=220)
    print(f"wrote {out}/fig0_headline.png; rows {[a for a, _ in rows]}")


if __name__ == "__main__":
    main()
