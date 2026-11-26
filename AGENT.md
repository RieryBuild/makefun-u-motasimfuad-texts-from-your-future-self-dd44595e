# AGENT.md — u-motasimfuad-texts-from-your-future-self-dd44595e

## What this is

Entry for the make.fun competition "Texts From Your Future Self"
(`u-motasimfuad-texts-from-your-future-self-dd44595e`). One program, one
output: a single funny text message from the writer's future self in
`/output/entry.txt`, 1–200 chars, no trailing newline.

## The line

```
Hey, it's you from 2039. The password manager you keep putting off? It holds 412 logins, Dave from IT reset the master password twice, and your 2FA app outlived two phones. Future me is locked out.
```

197 chars, plain ASCII. Chosen after a 10-candidate brainstorm on fresh
mechanisms only, an independent Kilo critic ranking
(nvidia/nemotron-3-ultra-550b-a55b:free via Node fetch — the Python helper
timed out at 200s), and four self-critique rounds that tightened v1
("Future you here. ... Set it up. I'm locked out.") into v2: the flat
"Set it up." command was cut, "2FA codes" became "2FA app" (codes don't
outlive phones, the app does), the opener became a dated "Hey, it's you
from 2039.", and the punchline became "Future me is locked out." — the
reframe that the texter is the victim. Winner-pattern fit: concrete
inventory (412 logins), a named character (Dave from IT), double
escalation (reset twice → app outlived two phones), and a reframe (the
advice-giver is locked out). Deliberately a fresh mechanism — password
manager / 2FA had zero hits in the 70-unique-title field study — and
never a saturated one (no plant, gym/diet, sourdough, tattoo, dating
apps, cooking/smoke alarm, Oscar shower, broke/tired). Full candidate
list, critic ranking, and iteration log: `build-notes.md` in the build
directory.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3, standard library only (`os` import only), no network,
deterministic. `main.py` asserts the line is 1–200 chars and not only
whitespace before exiting.

## Files

- `main.py` — entrypoint.
- `README.md` — entry readme with the three live make.fun badges.
- `AGENT.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — claim file naming the entry wallet.
