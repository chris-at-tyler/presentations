# The existence test

*Excerpt from the house skill-design rules (adapted from mattpocock/skills, MIT; house additions
2026-07-31). Whether material should be a skill at all — the decision that precedes every other
authoring choice.*

Three questions, in order:

1. **Can you write the exact rule?** Then it's a script, not a skill. A program is cheaper,
   faster, and _more_ accurate: its failure modes are enumerable, the model's aren't. The
   model's place is **authoring time** (write the script once) and **repair time** (fix the edge
   case that breaks it) — the mechanic, not the engine. A model at runtime executing a writable
   rule pays inference prices for a lookup table.
2. **Does it need judgment?** Then an agent runs it — and the skill question becomes a
   **reachability** question: supply only what the agent can't reach itself. Context the agent
   can already reach — the repo, fetchable docs, an MCP connection — is a skill that shouldn't
   exist; write the pointer, not the copy. Judgment the model already applies by default
   (universal conventions, trained-in standards) is a **no-op** restated: does the line change
   behavior versus the default? If not, delete it.
3. **Does it need a guarantee?** CI gates, billing, security policy, anything audited: a
   program, regardless of model quality. The requirement is determinism and auditability —
   properties of a mechanism, not a skill level. A probabilistic system asymptotes toward 100%
   and never reaches _auditable_.

**The messy tail.** Some tasks are 95% rule-writable with an endless tail of messy inputs.
Shape them as a deterministic core with an AI escape hatch: the script handles the head of the
distribution, the agent handles the tail, and each tail case the agent solves is a candidate
for promotion into the script.

**The demotion ladder.** A skill that only ever carries shared facts demotes to a plain
reference file; a skill whose steps are deterministic demotes those steps to scripts (or git
hooks — a mechanically checkable rule about commits belongs in a `commit-msg` hook, where it is
enforced at 100% rather than requested in prose); a skill with nothing left after both demotions
was a program all along.
