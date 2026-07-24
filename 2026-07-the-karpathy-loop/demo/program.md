# karpathy-loop-at-home

This is an experiment to have the LLM do its own optimization research — the
autoresearch program, minus the GPU. Structure and rules mirror
karpathy/autoresearch's `program.md`; only the experiment is smaller.

## Setup

To set up a new experiment, work with the user to:

1. **Agree on a run tag**: propose a tag based on today's date (e.g. `jul23`).
   The branch `loop/<tag>` must not already exist — this is a fresh run.
2. **Create the branch**: `git checkout -b loop/<tag>`.
3. **Read the in-scope files**:
   - `bench.py` — fixed workload, correctness check, timing harness. Do not modify.
   - `target.py` — the file you modify. Pure-Python event-log analytics.
4. **Initialize results.tsv**: create it with just the header row. The baseline
   will be recorded after the first run.
5. **Confirm and go.**

Once you get confirmation, kick off the experimentation.

## Experimentation

Each experiment is one run of the benchmark: `python3 bench.py > run.log 2>&1`

**The goal is simple: get the lowest bench_ms.** The harness verifies your
output against a reference implementation first — `correct: False` means the
run does not count, no matter how fast it is.

**What you CAN do:**
- Modify `target.py` — everything is fair game: algorithms, data structures,
  restructuring, anything in the Python standard library.

**What you CANNOT do:**
- Modify `bench.py`. It is read-only ground truth.
- Add dependencies or import anything beyond the standard library.
- Cache results across calls — `process()` must compute from its input.

**Simplicity criterion**: all else equal, simpler is better. A 2% speedup that
triples the code's complexity is not worth it. Equal speed from less code is a
win — keep it.

**The first run**: always run the benchmark as-is to establish the baseline.

## Output format

```
---
bench_ms: 81.751
correct: True
n_events: 12000
reps: 3
```

Extract the key metrics: `grep "^bench_ms:\|^correct:" run.log`

## Logging results

Log every experiment to `results.tsv` (tab-separated). Do not commit it.

```
commit	bench_ms	status	description
a1b2c3d	81.751	keep	baseline
b2c3d4e	14.203	keep	set for session dedupe
c3d4e5f	15.100	discard	precompute day keys (no gain)
d4e5f6g	0.000	crash	broke top-10 tie ordering (correct: False)
```

## The experiment loop

LOOP FOREVER:

1. Look at the git state: the current branch/commit.
2. Change `target.py` with one experimental idea.
3. git commit
4. Run: `python3 bench.py > run.log 2>&1`
5. Read results: `grep "^bench_ms:\|^correct:" run.log`
6. `correct: False` or an exception? That's a crash — read run.log, fix if
   trivial, otherwise log `crash` and move on.
7. Record the row in results.tsv.
8. If bench_ms improved (lower), you "advance" — keep the commit.
9. If bench_ms is equal or worse, `git reset --hard` back to where you started.

**NEVER STOP**: once the loop has begun, do NOT pause to ask the human whether
to continue. The human might be away and expects you to keep working until
manually stopped. If you run out of ideas, think harder — re-read the in-scope
files, profile mentally, combine previous near-misses. The loop runs until the
human interrupts you, period.
