# reveal-single-file template

Produces a **single self-contained `index.html`** deck — reveal.js 5.2.1 and the
speaker-notes plugin inlined, zero network dependencies, presentable by
double-clicking the file. Extracted from the 2026-07 "Finding Your Unknowns" talk.

## Usage

```bash
cp -R templates/reveal-single-file 2026-09-my-talk
cd 2026-09-my-talk
# 1. parts/slides.html — your content (three example slides show the components)
# 2. parts/theme.css   — colors/typography (palette is WCAG AA on the dark bg)
# 3. parts/top.html    — <title>
./assemble.sh          # → index.html
```

Keep `parts/` + `vendor/` committed alongside the generated `index.html` so the
deck can be edited and reassembled later.

## How it fits together

`assemble.sh` concatenates, in order: `parts/top.html` (doctype → `<style>`) ·
`vendor/reveal.css` · `parts/theme.css` · `parts/slides.html` (`</style>` →
slides → `<script>`) · `vendor/reveal.js` · script-tag break · `vendor/notes.js`
· `parts/bottom.html` (`Reveal.initialize`, edit config here).

Gotcha baked into the script: inlining only works while the vendored JS contains
no literal `</script>` sequence (true for reveal.js 5.2.x); assemble.sh fails
loudly if a future vendor bump breaks that. `vendor/notes.js` embeds the whole
speaker view, so `S` works offline.

## Presenting

Arrows navigate · `S` speaker view + notes · `F` fullscreen · `Esc` overview ·
URL hash deep-links to a slide (`index.html#/12`).
