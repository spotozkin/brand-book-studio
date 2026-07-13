# Anti-Fingerprint Checklist — Run Before Every Export

Purpose: no two books produced by this skill should be identifiable as siblings by their
skeleton OR their vocabulary. Run this after assembling the HTML and before final PDF
render. If any item fails, fix it before export — these are hard gates, not suggestions.

## Hard bans — retired furniture copy

These exact strings appeared verbatim in multiple outputs and are permanently retired.
They must never appear as headings or named principles in any generated book:

Retired in v1.0 era:
- "What's inside."
- "The building blocks"
- "Real touchpoints"
- "The full picture"
- "How we sound" / "How the brand sounds" (as the voice chapter title)
- "Who we are, and for whom"
- "Every touchpoint should make people feel" (the concept is fine; this heading is retired)

Retired in v1.2 (caught as verbatim repeats across the LEGO and Rolex v1 outputs):
- "closed set" / "the closed set" (as a named principle — the RULE is mandatory, the NAME is retired; see concept-level bans below)
- "receipts" (as in "Pairings, with receipts" / "Contrast receipts")
- "Two rewrites, with the rule named" / "with the rule named"
- "Documented gaps" (as a heading; the do-not-fabricate rule itself is mandatory)
- "measured, not assumed"
- The unnamed-font refusal sentence in any close paraphrase: "a governance document never
  guesses a font name" / "refuses to guess a name into a governance document"
- "Hierarchy in one sentence"

Mechanical check (adjust path):

```bash
grep -iE "What's inside|The building blocks|Real touchpoints|The full picture|touchpoint should make people feel|closed set|with the rule named|measured, not assumed|receipts|documented gaps|guess(es)? a (font )?name|hierarchy in one sentence" brand_book.html
```

Zero matches required. Functional labels ("Contents", "Color", "Typography") are always
fine — the ban is on reused VOICE copy and coined principle-names, not on plain labels.

## Concept-level bans — required rules, forbidden house names

These CONCEPTS are mandatory content in every applicable book; what is banned is naming
them in this skill's house vocabulary. Each must be either (a) named in words drawn from
the brand's own extracted vocabulary (the owned-words list you built for the voice
section — reuse it), or (b) stated as a rule and left unnamed. Silence is a valid
expression of rigor (`structural_seeds.md`, "naming the doctrine").

| Mandatory concept | Retired house name |
|---|---|
| The palette is exhaustive; off-list colors are not brand colors | "closed set" |
| Contrast is measured and evidenced, never eyeballed | "receipts" |
| Voice rules shown via before/after correction | "rewrites, with the rule named" |
| Missing asset variants are flagged and routed, never reconstructed | "documented gaps" |
| Unconfirmed proprietary fonts are described by behavior, stand-in declared | the refusal sentence |

## Structural gates

1. **Posture was chosen deliberately** — a posture from `document_postures.md` was
   recommended, confirmed with the person, and the section order can be justified in one
   sentence from the strategy. If the book happens to match the quarry template's
   11-section order exactly, re-derive: that order must be earned, not inherited.
2. **The central question governs the outline** — the `<!-- CENTRAL QUESTION -->` comment
   is present (or an explicit fallback-to-posture-default note), page allocation follows
   it, and the opening move can be justified from it (`central_question.md`).
3. **Seeds are declared and followed** — the `<!-- SEEDS -->` comment lists all seven
   derived choices from `structural_seeds.md` with justifications; no seed is a
   known-retired default (NEVER/AVOID/PREFER unseeded, four-trait table, two-rewrites-
   with-Because, manifest+escalation+doc-control closing suite, callout-after-contrast-
   table).
4. **Cover is not the split-panel default** unless split-panel was an affirmative choice
   with a brand reason. Same for the two-divider pattern at the same two positions.
5. **No fabricated assets** — every logo variation shown exists as a real file or a real
   code-built variant; every stat is sourced; every color pairing was contrast-checked.
   If the person supplied assets in Step 1.5, the book is built ON them — supplied
   mark embedded (not redrawn), palette traceable to their materials, and every
   supplied file logged wherever the seeded provenance placement puts it.
6. **Component counts vary** — not three tone traits + three feelings + three proof
   points + three stats by default. Counts follow the seeds, not the quarry defaults.
7. **Completeness floor met — as outcomes, not sections.** Check the posture's column in
   the floor matrix (`document_postures.md`). Each floor item is a reader CAPABILITY
   ("every claim is traceable", "a stranger can place the mark correctly"), satisfiable
   by any structural expression — a chapter, footnotes, swatch annotations, a colophon.
   Never confuse "the provenance chapter is missing" with "provenance is missing."
   Structure creativity never drops required content; every book names an escalation
   owner somewhere.
8. **Author profile is present, plausible, and non-resembling** — the Step 2.7 profile
   (`author_synthesis.md`) is recorded, its PLAUSIBILITY line holds for this brand's
   category, downstream choices trace to it, and it passes the non-resemblance diff
   against every AUTHOR PROFILE in the corpus (lineage/conviction/pet-move/cadence
   composite rules). Genuinely free choices were hash-committed
   (`scripts/committed_choice.py`) and logged in the SEEDS comment — never silently
   defaulted.
9. **The imperfection budget is spent, and spent safely** — 1-2 authored idiosyncrasies
   traceable to the profile, never touching floor content, never reused from any
   IDIOSYNCRASIES line in the corpus. A book with zero idiosyncrasies is uniformly
   excellent, and uniform excellence is a machine tell.
10. **Prose cadence hits the author's bands** — run `scripts/prose_fingerprint.py` on
   the final HTML; the book lands inside its own author's declared cadence targets and
   differs from the previous book's measured fingerprint per digest diff rule 9. The
   house hand (mean ~13, stdev ~8.7, em-dash ~20/1000w, aphorism ~0.25) is a known
   failure profile — landing near it fails regardless of what the author declared.
11. **Headings are in the chosen register** (one register, held consistently) and written
   fresh for this brand — no heading recycled from this skill's previous outputs or from
   the reference examples in any file.

## The digest diff (mechanical sibling gate)

Generate the candidate's structural digest and diff it against every entry in
`references/structural_digests.md` under that file's six hard-failure rules (verbatim
coined headings, repeated table schemas in the same role, identical section sequence
within a posture, repeated tier vocabulary, ≥3 shared rhetorical beats, identical
component-count profile). Log pass/fail before render; on fail, change the expression —
never the underlying rule — and re-diff. After delivery, append the new digest to the
corpus.

## The sibling test (judgment gate — kept as the human-eye backstop)

Render the cover, one interior text page, and the applications page to PNG. Ask: if
these were shuffled into a stack with every prior output in the digest corpus, would the
skeleton give them away as the same generator? Same cover formula, same chapter rhythm,
same component shapes in the same order = fail. Distinct document that shares only the
rendering pipeline = pass.

## What is ALLOWED to repeat

The rendering pipeline (WeasyPrint, @page sizing, @fontsource embedding), the QA scripts,
the accessibility standards, the completeness floors (as outcomes), and generic
functional labels. Two brands with genuinely similar attributes may converge on the same
SEED — that's motivated convergence, and the digest diff still forces divergent
expression. Consistency of QUALITY is the goal; consistency of FORM and VOCABULARY is
the bug.
