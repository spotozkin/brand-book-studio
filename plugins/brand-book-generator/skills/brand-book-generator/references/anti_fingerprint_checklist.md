# Anti-Fingerprint Checklist — Run Before Every Export

Purpose: no two books produced by this skill should be identifiable as siblings by their
skeleton. Run this after assembling the HTML and before final PDF render. If any item
fails, fix it before export — these are hard gates, not suggestions.

## Hard bans — retired furniture copy

These exact strings appeared verbatim in multiple early outputs and are permanently
retired. They must never appear as headings in any generated book:

- "What's inside."
- "The building blocks"
- "Real touchpoints"
- "The full picture"
- "How we sound" / "How the brand sounds" (as the voice chapter title)
- "Who we are, and for whom"
- "Every touchpoint should make people feel" (the concept is fine; this heading is retired)

Mechanical check (adjust path):

```bash
grep -iE "What's inside|The building blocks|Real touchpoints|The full picture|touchpoint should make people feel" brand_book.html
```

Zero matches required. Functional labels ("Contents", "Color", "Typography") are always
fine — the ban is on reused VOICE copy, not on plain labels.

## Structural gates

1. **Posture was chosen deliberately** — a posture from `document_postures.md` was
   recommended, confirmed with the person, and the section order can be justified in one
   sentence from the strategy. If the book happens to match the quarry template's
   11-section order exactly, re-derive: that order must be earned, not inherited.
2. **Cover is not the split-panel default** unless split-panel was an affirmative choice
   with a brand reason. Same for the two-divider pattern at the same two positions.
3. **No fabricated assets** — every logo variation shown exists as a real file or a real
   code-built variant; every stat is sourced; every color pairing was contrast-checked.
   If the person supplied assets in Step 1.5, the book is built ON them — supplied
   mark embedded (not redrawn), palette traceable to their materials, and every
   supplied file logged in the asset manifest.
4. **Component counts vary** — not three tone traits + three feelings + three proof
   points + three stats by default. At least one count differs from the quarry defaults
   for a reason.
5. **Completeness floor met** — check the posture's column in the floor matrix
   (`document_postures.md`). Structure creativity never drops required content. Every
   book names an escalation owner somewhere.
6. **Headings are in the chosen register** (one register, held consistently) and written
   fresh for this brand — no heading recycled from this skill's previous outputs or from
   the reference examples in any file.

## The sibling test (judgment gate)

Render the cover, one interior text page, and the applications page to PNG. Ask: if
these were shuffled into a stack with the LEGO and Rolex reference outputs, would the
skeleton give them away as the same generator? Same cover formula, same chapter rhythm,
same component shapes in the same order = fail. Distinct document that shares only the
rendering pipeline = pass.

## What is ALLOWED to repeat

The rendering pipeline (WeasyPrint, @page sizing, @fontsource embedding), the QA scripts,
the accessibility standards, the completeness floors, and generic functional labels.
Consistency of QUALITY is the goal; consistency of FORM is the bug.
