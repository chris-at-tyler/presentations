# Demo runbook — the skill demotion

The live segment for slide 14: apply the existence test to part 2's *finished* `commit-helper`
skill and watch it dissolve into a git hook plus nothing.

## What's in this folder

```
demo/
  .claude/skills/commit-helper/SKILL.md   part 2's end state — the GOOD 9-line version
  existence-test.md                       the three tests (excerpt of the house rules)
  src/inventory.py                        a toy module so there's something real to stage
```

The sandbox is self-contained: the skill and the test doc it needs are committed with the talk,
so the demo runs identically years later.

## Pre-flight (do this before the talk)

1. Copy the sandbox out of the repo so the live run can't dirty the talk folder:
   ```bash
   rm -rf /tmp/harness-demo && cp -R demo /tmp/harness-demo && cd /tmp/harness-demo
   ```
2. Give it its own git repo with one commit and one *staged* change (so
   `git diff --staged` has content if Claude explores):
   ```bash
   git init -q && git add -A && git commit -qm "Initial commit"
   sed -i '' 's/safety_factor: float = 1.5/safety_factor: float = 2.0/' src/inventory.py
   git add src/inventory.py
   ```
3. Launch `claude` in `/tmp/harness-demo`, confirm the `commit-helper` skill is listed
   (`/skills` or ask "what skills do you have?"). Leave the session open, terminal font sized
   for the room.
4. Have slide 15 (the fallback) ready in the speaker view.

## The demo (~5 minutes)

Paste the prompt (also shown on slide 14):

> Read existence-test.md, then apply it to .claude/skills/commit-helper/SKILL.md line by line:
> which lines are a program, which are judgment the model already has, which are knowledge it
> couldn't know? Extract anything deterministic into a git hook. Tell me what's left.

Expected behavior, in roughly this order:

1. Reads both files; classifies the three steps: hunk-reading = judgment it already does,
   the ≤50/72 rule = mechanically checkable, the "every change named" criterion = trained-in
   convention.
2. Writes `.git/hooks/commit-msg` (subject-length check, maybe the 72-wrap too) and marks it
   executable.
3. Delivers the verdict: knowledge residue is empty — the skill can be deleted; a real house
   rule (ticket prefix, sign-off trailer) would be the only thing worth keeping.

Room beats: before pasting, ask for predictions — "this is the skill part 2 was proud of; what
survives?" After the verdict, demo the hook working: `git commit -m "this subject line is
definitely much longer than fifty characters"` → rejected, every time, no tokens.

If Claude keeps a 1–2 line residual skill instead of deleting: that's a fine outcome — point at
the judgment call and move on. The demo's claim is the decomposition, not the exact line count.

## Reset / re-run

```bash
cd /tmp/harness-demo && git checkout -- . && rm -f .git/hooks/commit-msg
sed -i '' 's/safety_factor: float = 2.0/safety_factor: float = 1.5/' src/inventory.py 2>/dev/null
sed -i '' 's/safety_factor: float = 1.5/safety_factor: float = 2.0/' src/inventory.py
git add src/inventory.py
```
(Or just `rm -rf /tmp/harness-demo` and redo pre-flight — it's 20 seconds.)

## If the live demo stalls

Slide 15 is the full result: the line-by-line classification, the generated hook, and the
"34 → 9 → 0" arc. Narrate it as "here's what the run produces" — the punchline (a well-written
skill can still be a skill that shouldn't exist) needs no terminal.

## Links for the closing slide

- Part 2 deck: `chris-at-tyler.github.io/presentations/2026-07-writing-great-skills`
- Kilpatrick interview: `youtube.com/watch?v=cMAs8z2dehs`
- Anthropic post: `claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models`
- The Bitter Lesson: `incompleteideas.net/IncIdeas/BitterLesson.html`
