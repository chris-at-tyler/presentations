---
name: commit-helper
description: Write commit messages — use when committing changes.
---

1. Run `git diff --staged` and read every hunk.
2. Write the message: imperative subject ≤ 50 characters; body explains why, wrapped at 72.
3. Done when every functional change in the diff is named in the message — no hunk unaccounted
   for.
