# Structural Seeds — Deriving Choices From Brand Facts, Not Habit

`layout_grammar.md` gives the axes; this file gives the SEEDS. Left unconstrained, a
generator drifts to the same comfortable defaults on every axis — that drift IS the
fingerprint. Every remaining structural choice below is derived from a brand attribute
you already collected in Steps 1–2.6, so variation is *motivated* (reads as authored)
rather than random (still smells generated). If a seed rule conflicts with the brand's
own evidenced behavior, the brand's behavior wins — the seeds exist to break defaults,
not to override reality.

## Rule-tier vocabulary (do/don't register)

Never default to NEVER/AVOID/PREFER — it has appeared in consecutive outputs and is now a
known tell. Derive from formality + audience:

| Brand attribute | Tier vocabulary |
|---|---|
| Heritage / ceremonial / luxury | Commandment register, no tier labels at all — rules as flat declaratives in the brand's own liturgical voice ("The wordmark is never retyped.") |
| Playful / instructional / product-led | Permission-first: MAY / MAY NOT, or DO / DON'T with the DO wing leading |
| Vendor- or franchise-facing spec | Severity codes with consequences: PROHIBITED (triggers re-approval) / RESTRICTED (needs sign-off) / STANDARD |
| Startup / internal team | Two tiers only: "hard rules" and "judgment calls," conversational |
| Regulated (medical, financial, gov) | Compliance framing: REQUIRED / NOT PERMITTED / RECOMMENDED, citing the governing standard where one exists |

## Voice-trait count and format

Derive from how much voice VARIES across the brand's real surfaces (Step 1.5 evidence):
one register everywhere → 2–3 traits, prose not table. Distinct registers per context
(campaign vs. support vs. legal) → a register map (context → register) instead of a trait
table at all. Rich single voice → 4–6 traits, format per `layout_grammar.md` Axis 5.
**The four-row TRAIT / SOUNDS LIKE / NEVER SOUNDS LIKE table is retired as a default** —
it may appear only when trait count ≠ 4 or the column headers are rewritten in-voice.

## Rewrite examples (before/after pairs)

Vary COUNT and FORM by seed: content-heavy brand → one rewrite dissected deeply
(annotated line by line). Vendor-facing spec → 3–4 quick pairs, no commentary. Playful
brand → wrong version played for comedy. Ceremonial brand → no "before" shown at all;
only exemplary lines, because the brand would never reprint bad copy.
**The two-pairs-with-"Because:"-explanations pattern is retired as a default.**

## Provenance and asset-manifest placement

Mode B books must be traceable, but WHERE the trail lives is a seed: partner/vendor
audience → dedicated closing chapter with tables. Internal team → footnotes on the page
where each claim appears. One-sheet → a source line in the footer. Heritage/editorial →
a colophon in the brand's own voice. **Manifest-table + escalation-list + document-
control-block as a fixed closing suite is retired as a default** — each element earns its
own placement.

## Document-control furniture (version / next review / owner)

Include as a visible block only for spec, rebrand, and multi-location books — audiences
that will actually check versions. Everyone else: a one-line footer credit. A solo
creator's book does not need a "next review: January 20XX" register.

## Naming the doctrine

Concepts like the closed palette or measured contrast are required CONTENT; whether the
book NAMES its own methodology is a register choice. Brands that talk about process
(tech, design-led, instructional) may name principles — in the brand's own vocabulary,
never in this skill's (see the retired-coinage list in `anti_fingerprint_checklist.md`).
Brands that never explain themselves (luxury, heritage, minimalist) state the rule and
move on. Silence is a valid expression of rigor.

## Contrast-evidence format

The measurement always happens (`scripts/check_contrast.py`); the PRESENTATION is seeded:
spec/vendor book → full table. Design-literate internal audience → ratios annotated
directly on the palette swatches. Simple palette (≤5 pairings) → one prose sentence per
pairing. One-sheet → pass/fail glyphs only. **Full-table-followed-by-a-highlighted-
problem-callout is retired as a default beat** — if a problematic pairing exists, its
handling can live in the swatch note, the do/don't register, or a margin note instead.

## How to apply this file

At Step 5 outline time, walk the seven seeds above, write the derived choice and its
one-line justification into a short manifest comment at the top of the HTML
(`<!-- SEEDS: tiers=..., voice=..., rewrites=..., provenance=..., doccontrol=...,
doctrine=..., contrast=... -->`). The anti-fingerprint gate reads this comment; a missing
or unjustified seed is a gate failure. Two brands with genuinely similar attributes MAY
land on the same seed — that's motivated convergence, and the digest diff
(`structural_digests.md`) will still force divergence in expression.
