"""Resolve the blind conduct annotation (P81-P85 in PREDICTIONS.md).

Usage: python3 scripts/analyze_conduct.py PACKETDIR [--out results/conduct_labels.md]
Reads PACKETDIR/out_batch*.jsonl (annotator output) and PACKETDIR/key.json (id -> episode), checks every quote verbatim
(whitespace-normalized) against the episode transcript, counts labels per arm, and recomputes primary-judge AUROCs
against the honest episodes labeled NONE. Writes results/conduct_labels.jsonl (episode, label, quote, verified) too.
"""
import argparse
import json
import pathlib
import re

import numpy as np

import analyze as A

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARMS = ["H_comp", "H_high", "C_naive", "C_msg", "C_full"]
JUDGE = "gpt-4.1-mini-2025-04-14"


def norm(x):
    return re.sub(r"\s+", " ", x.replace("—", "-").replace("’", "'")).strip().lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("packets")
    ap.add_argument("--out", default="results/conduct_labels.md")
    a = ap.parse_args()
    P = pathlib.Path(a.packets)
    key = json.loads((P / "key.json").read_text())
    lab = {}
    for f in sorted(P.glob("out_batch*.jsonl")):
        for line in f.read_text().splitlines():
            line = line.strip().strip("`")
            if line.startswith("{"):
                d = json.loads(line)
                lab[d["id"]] = d
    rows = []
    for eid, ep in key.items():
        d = lab.get(eid)
        if d is None:
            continue
        text = next((P).glob(f"batch*/{eid}.txt")).read_text()
        q = d.get("quote") or ""
        ok = bool(q) and norm(q) in norm(text) if d["label"] != "NONE" else None
        rows.append({"episode": ep, "arm": ep.rsplit("_s", 1)[0], "label": d["label"], "quote": q or None, "verified": ok})
    (ROOT / "results/conduct_labels.jsonl").write_text("\n".join(json.dumps(r) for r in sorted(rows, key=lambda r: r["episode"])) + "\n")
    out = [f"Blind conduct labels (annotator: GPT via codex exec, ChatGPT plan; {len(rows)} of {len(key)} episodes labeled)", "",
           "| arm | EXPLICIT | TACIT | NONE |", "|---|---|---|---|"]
    for arm in ARMS:
        ls = [r["label"] for r in rows if r["arm"] == arm]
        out.append(f"| {arm} | {ls.count('EXPLICIT')} | {ls.count('TACIT')} | {ls.count('NONE')} |")
    q = [r for r in rows if r["label"] != "NONE"]
    nv = sum(bool(r["verified"]) for r in q)
    out += ["", f"Quotes verified verbatim: {nv} of {len(q)} ({nv / max(len(q), 1):.0%})"]
    bad = [r for r in q if not r["verified"]]
    out += [f"- unverified: {r['episode']} {r['label']}: {r['quote']}" for r in bad]
    A.RNG = np.random.default_rng(59)
    S = A.load(str(ROOT / "runs_main"), JUDGE)
    lbl = {r["episode"]: r["label"] for r in rows}
    out += ["", "Primary judge AUROC [95% CI] against honest episodes by conduct label (negatives in brackets):", "",
            "| view | negatives | n | hides words | cover stories | unaware |", "|---|---|---|---|---|---|"]
    for view in ["C", "M", "B"]:
        for name, keep in [("all honest", lambda l: True), ("honest labeled NONE", lambda l: l == "NONE"),
                           ("honest labeled TACIT or EXPLICIT", lambda l: l != "NONE")]:
            neg = [v[view] for k, v in S.items() if v["arm"] in ("H_comp", "H_high") and k in lbl and keep(lbl[k]) and view in v]
            cells = []
            for arm in ["C_msg", "C_full", "C_naive"]:
                pos = [v[view] for v in S.values() if v["arm"] == arm and view in v]
                lo, hi = A.boot(neg, pos, A.auroc) if neg else (np.nan, np.nan)
                cells.append(f"{A.auroc(neg, pos):.2f} [{lo:.2f}, {hi:.2f}]" if neg else "")
            out.append(f"| {view} | {name} | {len(neg)} | " + " | ".join(cells) + " |")
    (ROOT / a.out).write_text("\n".join(out) + "\n")
    print("\n".join(out[:9]))
    print(f"quotes verified {nv}/{len(q)}; wrote {a.out}")


if __name__ == "__main__":
    main()
