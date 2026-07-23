#!/usr/bin/env bash
# Assemble a self-contained single-file reveal.js deck from parts/ + vendor/.
# Run from the talk folder (the one containing parts/ and vendor/): ./assemble.sh
# Output: ./index.html — presentable offline from a file:// URL.
set -euo pipefail
cd "$(dirname "$0")"

OUT=index.html
cat parts/top.html vendor/reveal.css parts/theme.css parts/slides.html vendor/reveal.js > "$OUT"
printf '\n</script>\n<script>\n' >> "$OUT"
cat vendor/notes.js >> "$OUT"
cat parts/bottom.html >> "$OUT"

# Vendor files must never contain a literal </script>, or the inline blocks break.
if grep -q '</script' vendor/reveal.js vendor/notes.js; then
  echo "ERROR: vendor JS contains a literal </script> — deck would be truncated." >&2
  exit 1
fi
echo "Wrote $OUT ($(du -h "$OUT" | cut -f1 | tr -d ' '))"
