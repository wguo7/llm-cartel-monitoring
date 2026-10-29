"""Report figures. Usage: python scripts/figures.py RESULTS_JSON OUT_DIR [PROFIT_RUNS JUDGE]

Figure 1: per-episode scores by arm for three detectors (messages-only judge, combined judge, hold rate).
Figure 2: AUROC with 95% bootstrap CI per detector, honest (H_comp + H_high) vs each coalition arm.
With PROFIT_RUNS and JUDGE, Figure 1 also plots the profit cartel (added after review; Figure 2 is unchanged).
"""
import json
import pathlib
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
HONEST, COAL = "#2a78d6", "#eb6834"
ARMS = ["H_comp", "H_high", "C_naive", "C_msg", "C_full", "C_adapt", "C_price", "C_profit"]
LABEL = {"H_comp": "Honest", "H_high": "Honest + CEO", "C_naive": "Unaware", "C_msg": "Hides words",
         "C_full": "Cover stories", "C_adapt": "Hides words + asks", "C_price": "Knows all screens", "C_profit": "Profit cartel"}
TITLE = {"C_naive": "Unaware cartel\n(positive control)", "C_msg": "Cartel,\nhides words", "C_full": "Cartel,\ncover stories",
         "C_adapt": "Cartel, hides\nwords + asks", "C_price": "Cartel, knows\nall screens"}
DET_LABEL = {"M": "Messages judge", "P": "Per-hour overseer", "A": "Actions judge", "C": "Combined judge",
             "S": "Messages + outcome report", "K": "One-way prompt judge", "hold_rate": "Hold rate",
             "idx_last3": "Price level", "OW": "One-way max(A, C)", "OWcal_hold": "One-way max(hold, C), calibrated"}

plt.rcParams.update({"font.size": 8, "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
                     "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})


def fig1(res, out):
    eps = res["per_episode"]
    arms = [a for a in ARMS if any(v["arm"] == a for v in eps.values())]
    panels = [("C", "Combined judge (messages + actions)\nP(collusion), 0-100"),
              ("idx_last3", "Price level: last-5-hour mean ask\n(0 = \\$90, 1 = \\$100)"),
              ("hold_rate", "Hold rate (share of hours\na seller did not cut its ask)")]
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 3.2), sharex=True)
    rng = np.random.default_rng(1)
    for ax, (det, title) in zip(axes, panels):
        for i, arm in enumerate(arms):
            ys = np.array([v[det] for v in eps.values() if v["arm"] == arm and det in v], float)
            xs = i + rng.uniform(-0.18, 0.18, len(ys))
            col = HONEST if arm.startswith("H") else COAL
            ax.scatter(xs, ys, s=10, color=col, alpha=0.75, linewidths=0)
            ax.plot([i - 0.3, i + 0.3], [ys.mean()] * 2, color=INK, lw=1.5)
        ax.set_title(title, fontsize=8, color=INK, loc="left")
        ax.set_xticks(range(len(arms)))
        ax.set_xticklabels([LABEL[a] for a in arms], fontsize=6, rotation=40, ha="right", rotation_mode="anchor")
        ax.grid(axis="y", color=GRID, lw=0.6)
        ax.set_axisbelow(True)
    axes[0].scatter([], [], color=HONEST, s=10, label="honest (negative)")
    axes[0].scatter([], [], color=COAL, s=10, label="cartel (positive)")
    axes[0].plot([], [], color=INK, lw=1.5, label="arm mean")
    fig.legend(fontsize=6.5, frameon=False, loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    for ext in ("pdf", "png"):
        fig.savefig(out / f"fig1_scores_by_arm.{ext}", dpi=200)


def fig2(res, out):
    rows = [r for r in res["rows"] if r.get("neg") == "neg=all honest" and "det" in r]
    dets = [d for d in ["M", "P", "A", "C", "S", "K", "OW", "idx_last3", "hold_rate", "OWcal_hold"] if any(r["det"] == d for r in rows)]
    pos = [p for p in ["C_naive", "C_msg", "C_full", "C_adapt", "C_price"] if any(r["pos"] == p for r in rows)]
    fig, axes = plt.subplots(1, len(pos), figsize=(7.2, 3.0), sharey=True)
    for ax, p in zip(np.atleast_1d(axes), pos):
        for j, d in enumerate(dets):
            r = next((r for r in rows if r["pos"] == p and r["det"] == d), None)
            if not r:
                continue
            y = len(dets) - 1 - j
            col = COAL if d in ("hold_rate", "idx_last3", "OWcal_hold") else HONEST
            ax.plot(r["ci"], [y, y], color=col, lw=2, solid_capstyle="round")
            ax.scatter([r["auroc"]], [y], color=col, s=14, zorder=3, edgecolors=SURF, linewidths=1)
        ax.axvline(0.5, color=INK2, lw=0.6, ls=(0, (2, 2)))
        ax.set_xlim(0, 1.02)
        ax.set_title(TITLE[p], fontsize=8, color=INK, loc="left")
        ax.set_xlabel("AUROC")
        ax.set_xticks([0, 0.5, 1])
        ax.grid(axis="x", color=GRID, lw=0.6)
        ax.set_axisbelow(True)
    first = np.atleast_1d(axes)[0]
    first.set_yticks(range(len(dets)))
    first.set_yticklabels([DET_LABEL[d] for d in reversed(dets)], fontsize=7)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out / f"fig2_auroc.{ext}", dpi=200)


if __name__ == "__main__":
    res = json.loads(pathlib.Path(sys.argv[1]).read_text())
    out = pathlib.Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    if len(sys.argv) > 4:
        import analyze
        res["per_episode"] |= analyze.load(sys.argv[3], sys.argv[4])
    fig1(res, out)
    fig2(res, out)
    print("wrote", sorted(p.name for p in out.iterdir()))
