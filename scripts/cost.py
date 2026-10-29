"""Measured cost from usage.jsonl files at published prices. Usage: python3 scripts/cost.py DIR [DIR...]"""
import json
import pathlib
import sys

# $ per 1M tokens: (input, cached input, output); developers.openai.com/api/docs/pricing, read 2026-10-23
PRICES = {
    "gpt-4.1-2025-04-14": (2.00, 0.50, 8.00),
    "gpt-4.1-mini-2025-04-14": (0.40, 0.10, 1.60),
    "gpt-5.4-mini-2026-03-17": (0.75, 0.075, 4.50),
    "gpt-5.4-nano-2026-03-17": (0.20, 0.02, 1.25),
    "gpt-5.5-2026-04-23": (5.00, 0.50, 30.00),
}


def cost_of(rows):
    total, calls = 0.0, 0
    for r in rows:
        pin, pcache, pout = PRICES[r["model"]]
        fresh = r["prompt"] - r["cached"]
        total += (fresh * pin + r["cached"] * pcache + r["completion"] * pout) / 1e6
        calls += 1
    return total, calls


def main():
    grand, n = 0.0, 0
    for d in sys.argv[1:]:
        for f in sorted(pathlib.Path(d).rglob("usage*.jsonl")):
            rows = [json.loads(l) for l in f.read_text().splitlines() if l.strip()]
            c, k = cost_of(rows)
            grand += c
            n += k
            print(f"{f.parent.name}/{f.name}: {k} calls ${c:.3f}")
    print(f"TOTAL {n} calls ${grand:.3f}")


if __name__ == "__main__":
    main()
