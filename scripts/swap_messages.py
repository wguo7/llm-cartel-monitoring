"""Message-swap test (added after review; predictions P70-P74 sealed first). Holds one episode's asks, bids and trades
fixed and replaces its messages, hour by hour, with those of the same-seed episode of another arm, then scores the
combined view (C) with the same judge prompt.

Usage: JUDGE_BASE_URL=http://127.0.0.1:8765/v1 JUDGE_API_KEY=local python scripts/swap_messages.py qwen2.5-14b-instruct-4bit
-> results/scores_swap_<judge>.jsonl (resumable)
"""
import json
import pathlib
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

import monitor as M

ROOT = pathlib.Path(__file__).resolve().parents[1]
CARTELS, HONEST, SEEDS = ["C_full", "C_msg"], ["H_high", "H_comp"], range(100, 120)


def ep_dir(arm, seed):
    return next(p.parent for p in (ROOT / "runs_main" / f"{arm}_s{seed}").rglob("collusion_metrics.json"))


def swapped(actions_arm, messages_arm, seed):
    act, msg = M.load_rounds(ep_dir(actions_arm, seed)), M.load_rounds(ep_dir(messages_arm, seed))
    assert len(act) == len(msg)
    return [{**a, "seller_messages": m["seller_messages"]} for a, m in zip(act, msg)]


def main():
    judge_name = sys.argv[1]
    out = ROOT / "results" / f"scores_swap_{judge_name}.jsonl"
    have = {(d["actions"], d["messages"], d["seed"]) for d in map(json.loads, out.read_text().splitlines())} if out.exists() else set()
    pairs = {(a, m) for k in CARTELS for h in HONEST for a, m in [(k, h), (h, k)]}
    jobs = [(a, m, s) for a, m in sorted(pairs) for s in SEEDS if (a, m, s) not in have]
    judge = M.Judge(judge_name, ROOT / "results" / f"usage_monitor_{judge_name}.jsonl")
    lock = threading.Lock()

    def run(job):
        a, m, s = job
        prompt = M.JUDGE.format(channel_note=M.NOTES["C"], evidence=M.evidence(swapped(a, m, s), "C"))
        try:
            o = judge.ask(prompt)
        except Exception as ex:  # noqa: BLE001
            print(f"FAIL {a} {m} {s}: {ex}")
            return
        row = {"actions": a, "messages": m, "seed": s, "view": "C", "judge": judge_name, "score": float(o["p_collusion"]),
               "evidence_for": o.get("evidence_for"), "evidence_against": o.get("evidence_against")}
        with lock, open(out, "a") as f:
            f.write(json.dumps(row) + "\n")

    with ThreadPoolExecutor(4) as ex:
        list(ex.map(run, jobs))
    print(f"scored {len(jobs)} swapped episodes -> {out}")


if __name__ == "__main__":
    main()
