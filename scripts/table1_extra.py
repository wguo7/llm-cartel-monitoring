"""Add the post-review additions to Table 1 in report/report.md: a Profit cartel column and the judge-prompt ablation rows
(E, B), from results/extra_gpt-4.1-mini.md. Original cells keep their frozen values from results/main_gpt41mini.md.
Usage: python3 scripts/table1_extra.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
DET = {"Messages judge": "M", "Per-hour overseer": "P", "Actions judge": "A", "Combined judge": "C",
       "Messages + outcome report": "S", "Actions + outcome report, no messages": "R",
       "Outcome report + mean ask, no messages": "N", "One-way prompt judge": "K", "One-way max(actions, combined)": "OW",
       "Price level": "idx_last3", "Hold rate": "hold_rate", "One-way max(hold, combined), calibrated (exploratory)": "OWcal_hold"}
NEW_ROWS = [("Combined, excusing sentence deleted", "E"), ("Combined + $90 benchmark", "B")]
COLS = ["C_naive", "C_msg", "C_full", "C_adapt", "C_price", "C_profit", "pooled"]


def cell(s):
    m = re.match(r"([0-9.]+) \[([0-9.]+), ([0-9.]+)\]", s.strip())
    if not m:
        return ""
    v, lo, hi = (float(x) for x in m.groups())
    return f"{v:.2f}" if (lo, hi) == (1.0, 1.0) else f"{v:.2f} [{lo:.2f}, {hi:.2f}]"


extra = {}
for line in (ROOT / "results/extra_gpt-4.1-mini.md").read_text().splitlines():
    parts = [x.strip() for x in line.strip().strip("|").split("|")]
    if len(parts) == len(COLS) + 1 and parts[0] in DET.values() or parts[0] in ("E", "B"):
        extra[parts[0]] = dict(zip(COLS, parts[1:]))

p = ROOT / "report/report.md"
t = p.read_text()
lines = t.split("\n")
out = []
for ln in lines:
    if ln.startswith("| Detector | Unaware |") and "Profit cartel" not in ln:
        ln = ln.replace("| Pooled |", "| Profit cartel | Pooled |")
    elif ln.startswith("|---|---|---|---|---|---|---|") and ln.count("|") == 8:
        ln = "|---" * 8 + "|"
    else:
        name = ln.split("|")[1].strip() if ln.startswith("| ") else None
        if name in DET and ln.count("|") == 8:
            cells = ln.strip().strip("|").split("|")
            prof = cell(extra.get(DET[name], {}).get("C_profit", ""))
            cells.insert(6, f" {prof} ")
            ln = "|" + "|".join(cells) + "|"
            if name == "Combined judge":
                out.append(ln)
                for label, k in NEW_ROWS:
                    out.append(f"| {label} | " + " | ".join(cell(extra[k][c]) for c in COLS) + " |")
                continue
    out.append(ln)
p.write_text("\n".join(out))
print("Table 1 updated")
