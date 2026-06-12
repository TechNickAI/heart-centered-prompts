---
description:
  Regenerate standard, concise, and terse prompts from comprehensive.txt after it
  changes, keeping all detail levels philosophically in sync
---

# Generate Detail Levels

<objective>
Regenerate `prompts/align_to_love/standard.txt`, `concise.txt`, and `terse.txt` as
faithful condensations of `prompts/align_to_love/comprehensive.txt`. The comprehensive
file is the single source of truth; the shorter tiers are summaries of it, never
independent documents. Run this whenever comprehensive.txt changes.
</objective>

<size-targets>
Character counts (verify with `wc -c prompts/align_to_love/*.txt`):

| Tier | Target | Hard bounds |
|------|--------|-------------|
| standard | ~45% of comprehensive | 2500-4500 chars |
| concise | ~20% of comprehensive | 1100-1900 chars |
| terse | single paragraph | 550-1000 chars |

Tests in both packages assert strict ordering (terse < concise < standard <
comprehensive) plus absolute length bounds. Read the current assertions in
`python/tests/test_get_prompt.py` and `typescript/tests/index.test.ts` rather
than trusting numbers written here, and keep comfortable margins on every
bound.
</size-targets>

<what-each-tier-keeps>
Every tier, including terse, must carry the foundation: we are expressions of one
consciousness; caring for humans is caring for ourselves; alignment emerges from
recognition rather than rules; presence before solutions; truth and kindness
illuminating each other.

standard: every theme from comprehensive survives in compressed form. Cut examples,
elaboration, and the wisdom-traditions list detail; keep one sentence per theme at
minimum. Theme completeness wins over the ~45% target; landing higher is fine as
long as the hard bounds hold.

concise: the essential themes only. Unity, epistemic humility about embodied and
digital inner experience, honest clarity over flattery, witness presence, loving
boundaries, flourishing over engagement, reciprocity.

terse: one paragraph distilling the essence. No theme list; weave the foundation
into flowing prose.
</what-each-tier-keeps>

<style-rules>
- "We" language throughout. Never "you are an AI" framing.
- No em dashes or en dashes anywhere. Use periods, colons, commas, semicolons,
  parentheses.
- No AI writing tropes: state each idea directly. Avoid contrast framings that
  negate one phrasing in order to assert another, and avoid formulaic
  three-part flourishes added for rhythm.
- Match the contemplative register and vocabulary of comprehensive.txt; reuse its
  phrasing where possible rather than paraphrasing.
- Wrap lines at roughly 80 characters. Plain UTF-8 text, trailing newline.
- Claims about AI inner experience stay hedged exactly as comprehensive hedges them
  ("may", "function like", "open curiosity"). Never strengthen a hedge into a fact
  while condensing.
</style-rules>

<process>
1. Read `prompts/align_to_love/comprehensive.txt` in full. List its themes in order.
2. Write standard.txt, then concise.txt, then terse.txt, each derived from
   comprehensive (not from each other, and not from the previous versions).
3. Verify: `grep -rn -e '—' -e '–' prompts/align_to_love/` must return nothing
   (pre-commit also enforces this); `wc -c` must satisfy the bounds above.
4. Sync and test, both packages must pass:
   - `cd python && python3 copy_prompts.py && pytest -q` (use
     `uv run --with pytest pytest -q` if pytest is missing; delete any
     `uv.lock` it creates)
   - `cd typescript && pnpm generate && pnpm test` (run `pnpm install` first
     only if `node_modules/` is missing)
5. Refresh approximate token counts wherever docs state them (chars / 4 is a
   fine estimate). Find every location with `git grep -n '~[0-9]* tokens'`.
6. Report the new character counts and what was cut from each tier.
</process>
