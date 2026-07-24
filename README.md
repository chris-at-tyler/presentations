# Presentations

Consolidated home for demos, decks, and talks. Each talk lives in its own
date-prefixed folder and is fully self-contained — open its `index.html` in a
browser to present; no server, build step, or network required.

**Live site:** <https://chris-at-tyler.github.io/presentations/> (GitHub Pages
from `main`; this repo is public — keep talk content public-safe).

## Talks

| Date    | Talk                                                       | Audience                    | Live demo | Notes                       |
| ------- | ---------------------------------------------------------- | --------------------------- | --------- | --------------------------- |
| 2026-07 | [Finding Your Unknowns](2026-07-finding-your-unknowns/)    | Tyler Tech lunch-and-learn  | ✅ `/grill-me` | Runbook in `DEMO.md`   |
| 2026-07 | [Writing Great Skills](2026-07-writing-great-skills/)      | Tyler Tech lunch-and-learn (part 2) | ✅ skill makeover | Runbook in `DEMO.md` |

## Conventions

- **Folder naming:** `YYYY-MM-topic-slug/` — sorts chronologically.
- **Self-contained decks:** single-file HTML with all assets inlined (see
  `templates/reveal-single-file/`). Presentable from a file:// URL, offline.
- **`DEMO.md`:** any talk with a live-demo segment ships a runbook — pre-flight
  checklist, exact prompts/commands, expected behavior, timing, reset steps,
  and a fallback plan.
- **Demo sandboxes:** live-demo working directories (e.g. `demo/`) are committed
  with the talk, including any `.claude/skills/` they depend on, so the demo
  runs identically years later.

## Starting a new talk

```bash
cp -R templates/reveal-single-file 2026-09-my-next-talk
cd 2026-09-my-next-talk
# edit parts/slides.html (content) and parts/theme.css (look)
./assemble.sh          # → index.html
```

Then add the talk to the table above and to the root `index.html` landing page
— pushing to `main` publishes it on the live site.

Presenting: arrow keys to navigate, `S` for speaker view with notes, `F` for
fullscreen, `Esc` for slide overview.
