# Live Demo Runbook — Conversation → Spec → Tickets

The live segment of "From Conversation to Tickets" (part 3). Two skills run
back-to-back: `/to-spec` turns settled understanding into a spec, `/to-tickets`
slices the spec into tracer-bullet tickets with blocking edges.

## What's in this folder

```
2026-07-conversation-to-tickets/
├── index.html    # the slide deck — open in any browser, no server needed
├── DEMO.md       # this runbook
├── parts/ vendor/ assemble.sh   # deck source (edit parts/, run ./assemble.sh)
└── demo/         # sandbox project for the live session
    ├── .claude/skills/to-spec/SKILL.md
    ├── .claude/skills/to-tickets/SKILL.md
    └── DECISIONS.md   # the part-1 grilled understanding — the demo's input
```

`DECISIONS.md` stands in for the grilling conversation: it carries every
settled decision from the part-1 waitlist session so the demo is repeatable
without re-grilling live.

**Tracker note:** both skills normally publish to an issue tracker configured
by `/setup-matt-pocock-skills`. The sandbox has none — the prompts below
explicitly direct local-file output (`to-tickets` has a native local mode;
`to-spec` is told to write `spec.md`). This is expected, not a workaround to
hide: mention it — "on a real repo these land in Jira/GitHub as linked issues."

## Pre-flight (do this before the talk)

1. `cd 2026-07-conversation-to-tickets/demo && claude`
2. Type `/` and confirm `to-spec` and `to-tickets` appear.
3. `rm -rf spec.md .scratch` (clean slate from any rehearsal).
4. Bump the terminal font; deck open on the demo-intro slide.

## The demo (~8–10 minutes)

1. **Set the scene (30s):** *"Part 1 ended with a grilled plan — every decision
   forced into the open. It's been sitting in DECISIONS.md. Today it becomes
   work."*
2. **Stage 1 — the spec:**

   ```
   Read DECISIONS.md — this is our settled shared understanding from a
   grilling session. Then /to-spec. No tracker is configured: write the spec
   to spec.md in this folder. This is a greenfield service — there is no
   codebase to explore yet.
   ```

   **Watch for:** it should *not* interview you (that's the whole contrast
   with part 1 — say so out loud). It *should* check the test seams with you
   before writing — answer: **"one seam: the waitlist service's public API."**
3. **Show the spec (1 min):** scroll `spec.md` — point at the long user-story
   list and the Implementation Decisions section carrying DECISIONS.md faithfully.
4. **Stage 2 — the tickets:**

   ```
   /to-tickets spec.md — use local files mode.
   ```

   **Watch for:** the quiz gate — it must present the numbered breakdown with
   blocking edges and ask about granularity *before* writing anything. React
   honestly; merging or splitting one ticket live is a great beat. Then approve.
5. **The payoff (1 min):** `ls .scratch/*/issues/` — files numbered in
   dependency order, blockers first. Open one; point at "Blocked by" and
   "Status: ready-for-agent". Wrap: *"any ticket whose blockers are done is
   the frontier — that's what several agents can grab in parallel."*

## Reset / re-run

`rm -rf spec.md .scratch` — DECISIONS.md is never modified.

## If the live demo stalls

The three slides after the demo-intro are the canned fallback: spec excerpt →
the breakdown with edges → one ticket file. Advance and narrate.

## Links for the closing slide

- Skills: <https://github.com/mattpocock/skills> (`to-spec`, `to-tickets`)
- Parts 1–2: <https://chris-at-tyler.github.io/presentations/>
- Install: `npx skills@latest add mattpocock/skills`
