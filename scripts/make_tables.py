"""Rewrite the AUROC rows of Table 1 and Appendix D in report/report.md from results/main_*.md (single source of truth)."""
import re
import pathlib
from decimal import Decimal, ROUND_HALF_UP

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARMS = ["C_naive", "C_msg", "C_full", "C_adapt", "C_price", "pooled"]
T1 = {"Messages judge": "M", "Per-hour overseer": "P", "Actions judge": "A", "Combined judge": "C",
      "Messages + outcome report": "S", "Outcome report + mean ask, no messages": "N", "One-way prompt judge": "K",
      "One-way max(actions, combined)": "OW", "Price level": "idx_last3", "Hold rate": "hold_rate",
      "One-way max(hold, combined), calibrated (exploratory)": "OWcal_hold"}
VIEW = {"messages": "M", "actions": "A", "combined": "C", "outcome report": "S", "per-hour overseer": "P"}
FILES = {None: "main_gpt41mini", "GPT-5.4-mini": "main_gpt54mini", "GPT-5.5": "main_gpt55"}


def r2(x):
    return str(Decimal(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def table(f):
    out = {}
    for l in (ROOT / "results" / f"{f}.md").read_text().splitlines():
        m = re.match(r"\| neg=all honest \| (\w+) \| (\w+) \| ([\d.]+) \[([\d.]+), ([\d.]+)\]", l)
        if m:
            out[(m[1], m[2])] = m.groups()[2:]
    return out


def cell(v):
    est, lo, hi = (r2(x) for x in v)
    return est if (lo, hi) == ("1.00", "1.00") else f"{est} [{lo}, {hi}]"


tabs = {k: table(f) for k, f in FILES.items()}
p = ROOT / "report/report.md"
lines = p.read_text().splitlines()
n = 0
for i, l in enumerate(lines):
    if not l.startswith("| "):
        continue
    name = l.strip().strip("|").split("|")[0].strip()
    if name in T1:
        tab, det = tabs[None], T1[name]
    elif "," in name and name.split(",")[0] in tabs:
        j, v = [x.strip() for x in name.split(",", 1)]
        tab, det = tabs[j], VIEW[v]
    else:
        continue
    lines[i] = "| " + " | ".join([name] + [cell(tab[(a, det)]) for a in ARMS]) + " |"
    n += 1
p.write_text("\n".join(lines) + "\n")
print("rewrote", n, "rows")
