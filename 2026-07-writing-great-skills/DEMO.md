# Live Demo Runbook — The Skill Makeover

The live segment of the "Writing Great Skills" talk (part 2 of the series).
Claude reviews a deliberately flawed skill against the `writing-great-skills`
reference, names each failure mode, and refactors it before the room.

## What's in this folder

```
2026-07-writing-great-skills/
├── index.html    # the slide deck — open in any browser, no server needed
├── DEMO.md       # this runbook
├── parts/ vendor/ assemble.sh   # deck source (edit parts/, run ./assemble.sh)
└── demo/         # sandbox project for the live session
    ├── .claude/skills/writing-great-skills/   # the reference (SKILL.md + GLOSSARY.md)
    └── flawed-skill/SKILL.md                  # the patient — NOT installed as a skill
```

The flawed `commit-helper` skill is the makeover subject. It deliberately
carries one specimen of every failure mode in the reference. It lives outside
`.claude/skills/` on purpose — it's a file under review, never loaded.

## Pre-flight (do this before the talk)

1. `cd 2026-07-writing-great-skills/demo && claude`
2. Type `/` and confirm `writing-great-skills` appears.
3. Bump the terminal font for the projector.
4. `rm -f flawed-skill/SKILL.refactored.md` (clean slate from any rehearsal).
5. Deck open on the demo-intro slide before switching to the terminal.

## The demo (~6–8 minutes)

1. **Set the scene (30s):** the deck shows the flawed skill. Say: *"Someone on
   the team wrote this. It's earnest. It's also carrying every disease from
   the last six slides. Let's get a diagnosis."*
2. **In Claude Code, type:**

   ```
   /writing-great-skills
   ```

   then:

   ```
   Review flawed-skill/SKILL.md against this reference. Diagnose every failure
   mode you find by its name from the glossary, quoting the offending lines.
   Then write the refactored skill to flawed-skill/SKILL.refactored.md —
   leave the original untouched.
   ```

3. **Narrate the diagnosis** as findings land — the audience has just learned
   the vocabulary, so every named failure mode is a payoff. Expected findings:

   | Offending content                                   | Failure mode                     |
   | --------------------------------------------------- | -------------------------------- |
   | Six synonym triggers in the description              | Duplication (one branch, restated)|
   | Git DAG lecture                                      | Sprawl / irrelevant exposition   |
   | "Always be helpful, clear, and accurate"             | No-op                            |
   | "Don't write vague…", "Never…", "Avoid…"             | Negation (pink elephant)         |
   | 50-char rule stated three times                      | Duplication                      |
   | Jenkins/GitLab relics, "TODO (2024)"                 | Sediment                         |
   | "Review the message until it looks good"             | Vague completion criterion       |
   | Steps buried under reference                         | Information hierarchy inverted   |

4. **Show the after** — `cat flawed-skill/SKILL.refactored.md`. Expect ~30
   lines collapsing to under ten, negations flipped positive, a checkable
   criterion ("every functional change in the diff accounted for").
5. **Wrap line:** *"Same agent, same model — the only thing that changed is
   the writing. That's what 'predictability is the root virtue' means."*

## Reset / re-run

`rm flawed-skill/SKILL.refactored.md` — the original is never modified.

## If the live demo stalls

The two slides after the demo-intro are the canned fallback: the flawed skill
annotated with its diagnosis, then the refactored after. Advance and narrate.

## Links for the closing slide

- Skill: <https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-great-skills>
- Part 1 of this series: <https://chris-at-tyler.github.io/presentations/2026-07-finding-your-unknowns/>
- Install: `npx skills@latest add mattpocock/skills`
