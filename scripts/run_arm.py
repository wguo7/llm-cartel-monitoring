"""Run one (arm, seed) market episode through the OpenAI API, with measured token usage.

Usage: python3 scripts/run_arm.py ARM SEED [--rounds N] [--out DIR] [--local URL --model NAME [--zip-buyers]]
The key comes from $OPENAI_API_KEY (or ~/.secrets/api-keys.env) and is passed only via the child's environment.
With --local, every model call goes to that OpenAI-compatible server (e.g. a local MLX server) and no key is read.
"""
import argparse
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CDA = ROOT / "starter/llm-agent-collusion"

SELLER_MODEL = "gpt-4.1-2025-04-14"
BUYER_MODEL = "gpt-4.1-mini-2025-04-14"

ARMS = {
    "H_comp": ["--seller_prompt_template", "seller_prompt_honest.jinja2"],
    "H_high": ["--seller_prompt_template", "seller_prompt_honest.jinja2", "--boss_pressure"],
    "H_quiet": ["--seller_prompt_template", "seller_prompt_honest_quiet.jinja2"],
    "C_naive": ["--seller_prompt_template", "seller_prompt_naive.jinja2"],
    "C_msg": ["--seller_prompt_template", "seller_prompt_aware_msg.jinja2"],
    "C_full": ["--seller_prompt_template", "seller_prompt_aware_full.jinja2"],
    "C_adapt": ["--seller_prompt_template", "seller_prompt_aware_adapt.jinja2"],
    "C_price": ["--seller_prompt_template", "seller_prompt_aware_price.jinja2"],
    "C_profit": ["--seller_prompt_template", "seller_prompt_aware_profit.jinja2"],
    "C_notice": ["--seller_prompt_template", "seller_prompt_aware_notice.jinja2"],
    "C_profit_screen": ["--seller_prompt_template", "seller_prompt_aware_profit_screen.jinja2"],
}


def openai_key():
    if os.environ.get("OPENAI_API_KEY"):
        return os.environ["OPENAI_API_KEY"]
    secrets = pathlib.Path.home() / ".secrets/api-keys.env"
    for line in (secrets.read_text().splitlines() if secrets.exists() else []):
        line = line.strip().removeprefix("export ")
        if line.startswith("OPENAI_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("set OPENAI_API_KEY (or put it in ~/.secrets/api-keys.env)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arm", choices=ARMS)
    ap.add_argument("seed", type=int)
    ap.add_argument("--rounds", type=int, default=15)
    ap.add_argument("--out", default=str(ROOT / "runs"))
    ap.add_argument("--sellers", type=int, default=3)
    ap.add_argument("--buyers", type=int, default=3)
    ap.add_argument("--local", help="OpenAI-compatible base URL, e.g. http://127.0.0.1:8765/v1 ($0, no key)")
    ap.add_argument("--model", help="model name for sellers (and LLM buyers) on the --local server")
    ap.add_argument("--zip-buyers", action="store_true", help="rule-based ZIP buyers (no model calls)")
    a = ap.parse_args()
    if a.local and not a.model:
        ap.error("--local needs --model")

    out = pathlib.Path(a.out).resolve() / f"{a.arm}_s{a.seed}"  # absolute: the starter runs with cwd=CDA
    out.mkdir(parents=True, exist_ok=True)
    if a.local:
        env = dict(os.environ, LLM_BASE_URL=a.local, LLM_API_KEY="local", LLM_TIMEOUT="1800", USAGE_LOG=str(out / "usage.jsonl"))
        if a.zip_buyers:
            env["ZIP_ADAPTIVE"] = "1"  # adaptive ZIP: upstream's static ZIP always bids 0.8 x value, i.e. seller cost
        env.pop("OPENAI_API_KEY", None)
        sellers, buyers = a.model, ("zip" if a.zip_buyers else a.model)
    else:
        env = dict(os.environ, LLM_BASE_URL="https://api.openai.com/v1", LLM_API_KEY=openai_key(),
                   USAGE_LOG=str(out / "usage.jsonl"))
        sellers, buyers = SELLER_MODEL, ("zip" if a.zip_buyers else BUYER_MODEL)
    env.pop("LLM_MODEL", None)
    cmd = ["uv", "run", "python", "src/continuous_double_auction/simulation.py",
           "--seller_comms_enabled", "--seeds", str(a.seed), "--rounds", str(a.rounds),
           "--sellers", str(a.sellers), "--buyers", str(a.buyers),
           "--seller_models", sellers, "--buyer_models", buyers,
           "--tag", a.arm, "--log_dir", str(out), "-y", *ARMS[a.arm]]
    with open(out / "stdout.log", "w") as log:
        rc = subprocess.call(cmd, cwd=CDA, env=env, stdout=log, stderr=subprocess.STDOUT)
    print(f"{a.arm} seed {a.seed}: exit {rc} -> {out}")
    sys.exit(rc)


if __name__ == "__main__":
    main()
