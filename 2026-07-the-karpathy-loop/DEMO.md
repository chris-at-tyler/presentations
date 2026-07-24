# Live Demo Runbook — Karpathy Loop at Home

The live segment of "The Karpathy Loop" (part 4). An agent runs the real
autoresearch loop shape — edit, commit, benchmark, keep or reset — on a
GPU-free target: a naive Python analytics function with ~86× of headroom.

## What's in this folder

```
2026-07-the-karpathy-loop/
├── index.html    # the slide deck — open in any browser, no server needed
├── DEMO.md       # this runbook
├── parts/ vendor/ assemble.sh   # deck source (edit parts/, run ./assemble.sh)
└── demo/         # the loop sandbox (copied out before running — see below)
    ├── bench.py     # fixed harness = prepare.py (correctness check + timing)
    ├── target.py    # the file the agent edits = train.py (deliberately naive)
    └── program.md   # the loop instructions = Karpathy's program.md, adapted
```

Measured on this machine: baseline **81.8 ms**, fully optimized **0.95 ms** —
plenty of distinct keep/discard beats between them (session set, Counter,
single pass, sort-based top-10).

## Pre-flight (do this before the talk)

The loop commits and resets with git, so it must NOT run inside the
presentations repo. Copy the sandbox out and give it its own repo:

```bash
rm -rf /tmp/karpathy-loop && cp -R demo /tmp/karpathy-loop
cd /tmp/karpathy-loop && git init -q && git add -A && git commit -qm "initial"
claude
```

Then in the session, type `/` once to make sure you're in a clean context, and
bump the terminal font. Sanity check beforehand: `python3 bench.py` should
print `bench_ms: ~80` and `correct: True`.

Permissions: the README's "disable all permissions" is the overnight mode. For
a projector demo, accept-edits mode is plenty — the agent only touches
target.py and runs python3/git.

## The demo (~6–8 minutes)

1. **Set the scene (30s):** *"Same three files as Karpathy's repo — a harness I
   can't touch, a target file the agent owns, and a program.md. The metric is
   milliseconds instead of validation loss. Watch the loop."*
2. **Type Karpathy's README prompt, verbatim:**

   ```
   Hi have a look at program.md and let's kick off a new experiment! let's do the setup first.
   ```

3. **Approve the setup** (branch + results.tsv + baseline plan), then let it
   loop. Narrate the beats as they land:
   - baseline logged (~80 ms)
   - first big win (session list → set, or Counter) — **keep, branch advances**
   - a discard or crash — **git reset, loop continues** (this is the money
     moment: failure costs nothing but one commit)
   - `cat results.tsv` — the experiment ledger growing
4. **Interrupt it** after 3–4 cycles (Esc): *"and per program.md it would never
   stop — that's the point. On Karpathy's H100 this exact shape ran ~100
   experiments a night on a real GPT."*
5. **Show** `git log --oneline` — kept experiments only; discards left no trace.

## Reset / re-run

`rm -rf /tmp/karpathy-loop` and redo pre-flight. The committed `demo/` folder
is never touched by the run.

## If the live demo stalls

The three slides after the demo-intro are the canned fallback: the adapted
program.md, a results.tsv mid-run, and the git-log-as-ledger shot. Advance and
narrate.

## Links for the closing slide

- Repo: <https://github.com/karpathy/autoresearch> (local clone: `third-party/autoresearch`)
- Parts 1–3: <https://chris-at-tyler.github.io/presentations/>
