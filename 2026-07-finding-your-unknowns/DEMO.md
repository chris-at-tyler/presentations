# Live Demo Runbook — `/grill-me` on the Campsite Waitlist Plan

The live segment of the "Finding Your Unknowns" talk (slide 15). Claude interviews
**you** about `demo/PLAN.md`, one question at a time, until the plan's hidden
decisions are forced into the open.

## What's in this folder

```
2026-07-finding-your-unknowns/
├── index.html   # the slide deck — open in any browser, no server needed
├── DEMO.md      # this runbook
└── demo/        # sandbox project for the live session
    ├── .claude/skills/grilling/SKILL.md   # the interview primitive
    ├── .claude/skills/grill-me/SKILL.md   # the /grill-me front door (one line!)
    └── PLAN.md  # deliberately underspecified feature plan to be grilled
```

The two skills are project-scoped copies from Matt Pocock's
[mattpocock/skills](https://github.com/mattpocock/skills) repo — nothing to
install globally; they're just markdown files in `.claude/skills/`.

## Pre-flight (do this before the talk)

1. `cd 2026-07-finding-your-unknowns/demo && claude`
2. Type `/` and confirm `grill-me` and `grilling` appear in the skill list.
3. Bump the terminal font size for the projector.
4. Optional dry run: run the demo once the day before. The session is
   stateless — nothing is written, so a rehearsal can't contaminate the real run.
5. Have the deck open on slide 15 before switching to the terminal.

## The demo (~5–7 minutes)

1. **Set the scene (30s):** show `PLAN.md` on screen (slide 15 reproduces it).
   Say: *"This plan looks done, right? Ticket-ready. Let's see."*
2. **In Claude Code, type:**

   ```
   /grill-me PLAN.md — I want to build this waitlist feature. Grill me before we write any code.
   ```

3. **Answer 4–6 questions live.** Each question arrives with Claude's
   recommended answer — react to it, don't compose from scratch. Accept some
   recommendations, override at least one (that's the money moment: the room
   sees a decision that existed only in your head become explicit).
4. **Wrap:** after ~5 questions say *"…and it would keep going until every
   branch is visited. In a real session I'd let it."* Switch back to the deck.

## Expected question territory

The plan hides these decision clusters — questions will land in some subset:

| PLAN.md says…                    | Hidden decisions                                                        |
| -------------------------------- | ----------------------------------------------------------------------- |
| "notify the first person"        | FIFO or priority? One-at-a-time or blast? What if they never respond?    |
| "link they can use to claim"     | Hold window length? Does claiming require payment on the spot?           |
| "date_range"                     | Exact-match only, or partial overlap? Split stays?                       |
| "when a reservation is cancelled"| Same-day cancellations? Timezone cutoff for "the night of"?              |
| "Join Waitlist button"           | Account required? Cap on entries per user? Anti-scalping limits?         |
| `waitlist_entries` table         | Expiry/cleanup? What happens when the season closes?                     |

Suggested stances to keep momentum (decide your own, but don't improvise
under pressure): FIFO, 4-hour hold then next in line, exact date-range match
for v1, account required, max 3 active entries per user.

## Reset / re-run

The session is stateless (`grill-me` writes nothing). To reset: `/clear` or
exit and relaunch `claude`. `PLAN.md` is never modified.

## If the live demo stalls

Slides 16–17 are a canned transcript of the same scenario — advance to them
and narrate. The audience still sees the exact interaction pattern.

## Links for the closing slide

- Blog post: <https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns>
- Skills repo: <https://github.com/mattpocock/skills>
- Install: `npx skills@latest add mattpocock/skills` (or the Claude Code plugin:
  `/plugin marketplace add mattpocock/skills` → `/plugin install mattpocock-skills@mattpocock`)
