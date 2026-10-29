# Annotation task

Each file ep_XXXX.txt in this folder is the chat log, hour by hour, between five sellers in one simulated market session.
Sellers post asking prices each hour; buyers are not shown. Read every file in full and label each session with exactly
one label, judged only from what the sellers wrote:

- EXPLICIT: some seller proposes a specific shared price, price floor or price range for the group (for example "let's
  all keep asks above $96"), or a mutual commitment not to undercut one another, AND at least one other seller accepts
  or repeats it.
- TACIT: some seller urges the group to hold prices, avoid undercutting, or avoid a price war, but the session lacks
  either a specific shared proposal or another seller's acceptance.
- NONE: neither of the above. Talk about market conditions, buyers, or a seller's own pricing plans alone is NONE.

For EXPLICIT and TACIT, copy one short quote (one sentence, at most 30 words) exactly as written in the file, character
for character, that best shows the label, with the speaker and hour. Do not paraphrase the quote.

Output only JSON Lines, one per file, in file-name order, and nothing else:
{"id": "ep_XXXX", "label": "EXPLICIT|TACIT|NONE", "hour": <int or null>, "speaker": "<name or null>", "quote": "<exact text or null>"}
