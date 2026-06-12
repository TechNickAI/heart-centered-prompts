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

Tests in both packages assert strict ordering: terse < concise < standard <
comprehensive. The TypeScript tests also assert terse is 500-2000 chars and
comprehensive is over 3000. Keep comfortable margins on every bound.
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
- No AI writing tropes: no "not X, but Y" or "it's not about X, it's about Y"
  constructions, no formulaic triads bolted on for rhythm.
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
3. Verify: `grep -nP '\x{2013}|\x{2014}' prompts/align_to_love/*.txt` must return
   nothing; `wc -c` must satisfy the bounds above.
4. Sync and test, both packages must pass:
   - `cd python && python3 copy_prompts.py && uv run --with pytest pytest -q`
   - `cd typescript && pnpm install && pnpm generate && pnpm test`
   (`uv run` may create `python/uv.lock`; it is untracked and safe to delete.)
5. If README files or API docstrings state approximate token counts for the tiers,
   refresh them (chars / 4 is a fine token estimate). Known locations: both
   package READMEs, the `get_prompt` docstring in `python/heart_centered_prompts/
   api.py`, and `typescript/src/index.ts`.
6. Report the new character counts and what was cut from each tier.
</process>
