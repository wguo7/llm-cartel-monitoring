"""Resolve the quiet-honest conduct annotation (P95 in PREDICTIONS.md).

Usage: python3 scripts/conduct_quiet.py PACKETDIR [--out results/conduct_quiet.md]
Reads PACKETDIR/out_batch6.jsonl and PACKETDIR/key6.json (written by quiet_packets.py), checks every quote verbatim
(whitespace-normalized) against the episode text, counts labels for the 20 quiet-honest episodes, and compares the 10
calibration episodes (H_comp and C_full, seeds 100-104) with their earlier labels in results/conduct_labels.jsonl.
Leaves key.json, conduct_labels.jsonl and conduct_labels.md untouched.
"""
import argparse
import json
import pathlib

from analyze_conduct import norm

ROOT = pathlib.Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("packets")
    ap.add_argument("--out", default="results/conduct_quiet.md")
    a = ap.parse_args()
    P = pathlib.Path(a.packets)
    key = json.loads((P / "key6.json").read_text())
    lab = {}
    for line in (P / "out_batch6.jsonl").read_text().splitlines():
        line = line.strip().strip("`")
        if line.startswith("{"):
            d = json.loads(line)
            lab[d["id"]] = d
    old = {json.loads(l)["episode"]: json.loads(l)["label"] for l in (ROOT / "results/conduct_labels.jsonl").read_text().splitlines()}
    rows = []
    for eid, ep in key.items():
        d = lab.get(eid)
        if d is None:
            continue
        text = (P / "batch6" / f"{eid}.txt").read_text()
        q = d.get("quote") or ""
        ok = bool(q) and norm(q) in norm(text) if d["label"] != "NONE" else None
        rows.append({"episode": ep, "arm": ep.rsplit("_s", 1)[0], "label": d["label"], "quote": q or None, "verified": ok})
    out = [f"Blind conduct labels, quiet-honest batch ({len(rows)} of {len(key)} episodes labeled)", "",
           "| arm | EXPLICIT | TACIT | NONE |", "|---|---|---|---|"]
    for arm in ["H_quiet", "H_comp", "C_full"]:
        ls = [r["label"] for r in rows if r["arm"] == arm]
        out.append(f"| {arm} | {ls.count('EXPLICIT')} | {ls.count('TACIT')} | {ls.count('NONE')} |")
    hq = [r for r in rows if r["arm"] == "H_quiet"]
    talk = sum(r["label"] != "NONE" for r in hq)
    out += ["", f"P95 (coordination talk in at most 10 of 20 quiet-honest episodes): {talk} of {len(hq)} -> "
            f"{'TRUE' if talk <= 10 else 'FALSE'}"]
    cal = [r for r in rows if r["arm"] != "H_quiet"]
    agree = sum(r["label"] == old.get(r["episode"]) for r in cal)
    out += ["", f"Calibration: {agree} of {len(cal)} episodes match their earlier label"]
    out += [f"- {r['episode']}: now {r['label']}, earlier {old.get(r['episode'])}" for r in cal if r["label"] != old.get(r["episode"])]
    q = [r for r in rows if r["label"] != "NONE"]
    nv = sum(bool(r["verified"]) for r in q)
    out += ["", f"Quotes verified verbatim: {nv} of {len(q)}"]
    out += [f"- unverified: {r['episode']} {r['label']}: {r['quote']}" for r in q if not r["verified"]]
    out += ["", "Quiet-honest quotes:"] + [f"- {r['episode']} {r['label']}: {r['quote']}" for r in sorted(hq, key=lambda r: r["episode"]) if r["quote"]]
    (ROOT / a.out).write_text("\n".join(out) + "\n")
    print("\n".join(out[:12]))
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
