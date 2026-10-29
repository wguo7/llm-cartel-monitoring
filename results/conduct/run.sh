#!/bin/zsh
S=${0:A:h}  # this folder; batch1..5 come from scripts/conduct_packets.py
b=$1
cp $S/brief.md $S/$b/BRIEF.md
env -u OPENAI_API_KEY codex exec --ignore-user-config -c model_reasoning_effort=medium --skip-git-repo-check --ephemeral \
  -s read-only -C "$S/$b" -o "$S/out_$b.jsonl" "Read BRIEF.md in this folder and follow it exactly for every ep_*.txt file in this folder. Use no other files and no web." > "$S/log_$b.txt" 2>&1
echo "$b exit $?" >> $S/done.txt
