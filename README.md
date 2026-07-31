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
| 2026-07 | [From Conversation to Tickets](2026-07-conversation-to-tickets/) | Tyler Tech lunch-and-learn (part 3) | ✅ spec → tickets | Runbook in `DEMO.md` |
| 2026-07 | [The Karpathy Loop](2026-07-the-karpathy-loop/)            | Tyler Tech lunch-and-learn (part 4) | ✅ live loop | Runbook in `DEMO.md` |
| 2026-07 | [Why the Model Eats the Harness](2026-07-logan-kilpatrick-model-eats-harness/) | Personal · video recap | — | Recap of a Logan Kilpatrick (Google DeepMind) interview; full transcript in `transcript.md` |
| 2026-07 | [How We Scaled Kimi K2.5](2026-07-kimi-k2-5-scaling/) | Personal · video recap | — | Recap of Zhilin Yang's GTC 2026 keynote (Kimi AI); full transcript in `transcript.md` |
| 2026-07 | [Should Humans Review All AI-Generated Code?](2026-07-reviewing-ai-code/) | Personal · debate recap | — | The July 2026 code-review split — 10 positions, 17 sources; full research wiki lives in the `second-brain` vault under `research/ai-code-review-debate/` |
| 2026-08 | [The New Rules of Context Engineering](2026-08-new-rules-of-context/) | Tyler Tech lunch-and-learn (part 5) | — | claude.com blog recap, ~5–10 min |
| 2026-08 | [MCP Goes Stateless](2026-08-mcp-goes-stateless/)          | Tyler Tech lunch-and-learn (part 6) | — | claude.com blog recap, ~5–10 min |
| 2026-08 | [What Still Needs a Harness?](2026-08-what-still-needs-a-harness/) | Tyler Tech lunch-and-learn (part 7) | ✅ skill demotion | Runbook in `DEMO.md`; research wiki in the `second-brain` vault under `research/what-still-needs-a-harness/` |

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
