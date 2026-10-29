"""Check Table 1 and Appendix D cells in report/report.md against results/main_*.md. Prints mismatches only."""
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARMS = ["C_naive", "C_msg", "C_full", "C_adapt", "C_price", "pooled"]
T1 = {"Messages judge": "M", "Per-hour overseer": "P", "Actions judge": "A", "Combined judge": "C",
      "Messages + outcome report": "S", "Outcome report + mean ask, no messages": "N", "One-way prompt judge": "K",
      "One-way max(actions, combined)": "OW", "Price level": "idx_last3", "Hold rate": "hold_rate",
      "One-way max(hold, combined), calibrated (exploratory)": "OWcal_hold"}
VIEW = {"messages": "M", "actions": "A", "combined": "C", "outcome report": "S", "per-hour overseer": "P"}


def table(f):
    out = {}
    for l in (ROOT / f).read_text().splitlines():
        m = re.match(r"\| neg=all honest \| (\w+) \| (\w+) \| ([\d.]+) \[([\d.]+), ([\d.]+)\]", l)
        if m:
            out[(m[1], m[2])] = tuple(float(x) for x in m.groups()[2:])
    return out


def check(row, cells, ref, det):
    bad = 0
    for arm, cell in zip(ARMS, cells):
        m = re.match(r"([\d.]+)(?: \[([\d.]+), ([\d.]+)\])?", cell.strip())
        got = [float(x) for x in m.groups() if x is not None]
        exp = ref.get((arm, det))
        if exp is None:
            print("missing", row, arm); bad += 1; continue
        want = [round(exp[0], 2)] + ([round(exp[1], 2), round(exp[2], 2)] if len(got) == 3 else [])
        if any(abs(a - b) > 0.0051 for a, b in zip(got, want)) or (len(got) == 1 and exp[1:] != (1.0, 1.0) and row):
            if len(got) == 1 and exp[1:] == (1.0, 1.0) and abs(got[0] - want[0]) < 0.006:
                continue
            print(f"{row} | {arm}: report {got} vs file {[round(x, 3) for x in exp]}"); bad += 1
    return bad


md = (ROOT / "report/report.md").read_text()
bad = 0
prim = table("results/main_gpt41mini.md")
judges = {"GPT-5.4-mini": table("results/main_gpt54mini.md"), "GPT-5.5": table("results/main_gpt55.md")}
for l in md.splitlines():
    if not l.startswith("| ") or l.startswith("| Detector") or l.startswith("| Judge"):
        continue
    parts = [p for p in l.strip().strip("|").split("|")]
    name, cells = parts[0].strip(), parts[1:]
    if name in T1:
        bad += check(name, cells, prim, T1[name])
    elif "," in name and name.split(",")[0] in judges:
        j, v = [x.strip() for x in name.split(",", 1)]
        bad += check(name, cells, judges[j], VIEW[v])
print("mismatches:", bad)
