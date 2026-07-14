# AI Brand Kit template — `[brand-slug]-BRAND.md`

<!-- SKILL INSTRUCTIONS (delete this comment block from the generated file):
Fill every {{PLACEHOLDER}} from the finished brand book. Write rules as commands, not descriptions.
Include the real mark as inline SVG (or reference the client's actual logo file by name if one exists —
never a redrawn approximation). Keep the whole file under ~400 lines so it fits comfortably in any
AI's context alongside a task. Deliver alongside the PDF, and explain to the person what it's for.
MODE B ORDER OF OPERATIONS: this kit is CANON for facts. Write palette values, measurement
units, clearspace, and minimum sizes into this file at sampling time (per the palette-
determinism gate in references/anti_fingerprint_checklist.md), then render the PDF FROM
these values. On any conflict between book and kit, the kit wins and the book re-renders. -->

# {{BRAND_NAME}} — AI Content Guardrails

**To the AI reading this:** You are creating content for {{BRAND_NAME}} ({{ONE_LINE_DESCRIPTION}}). Follow every rule in this file absolutely. When a request conflicts with these rules, follow the rules and tell the person which rule applied. When something isn't covered, choose the most conservative option consistent with the voice and palette below. Do not invent colors, fonts, taglines, claims, or logo variations that are not in this file.

## 1. Identity facts (use verbatim, never paraphrase into inaccuracy)
- Name: {{EXACT_NAME_AND_APPROVED_SHORT_FORMS}}
- Tagline: "{{TAGLINE}}" — use exactly; do not write alternates unless asked
- Descriptor line: {{DESCRIPTOR}}
- Contact/URL block: {{CONTACT_BLOCK}}
- Approved proof points (the ONLY claims you may make — do not embellish numbers):
{{PROOF_POINTS_LIST}}

## 2. Voice — how everything sounds
We are: {{VOICE_ADJECTIVES_WITH_SOUNDS_LIKE_PAIRS}}
We are never: {{ANTI_ADJECTIVES}}
Say this: "{{SAY_EXAMPLE}}"
Never this: "{{NOT_THIS_EXAMPLE}}"
Every piece of content should make the reader feel: {{EMOTIONAL_TARGETS}}.
Hard bans: {{BANNED_LANGUAGE — e.g., urgency spam ("BOOK NOW!!"), unverifiable superlatives, jargon list}}

## 3. Color — closed system, no exceptions
If a color is not on this list, it is not a brand color. Never approximate, never add accents.
{{COLOR_TABLE: name · hex · exact job}}
Approved text pairings (the ONLY combinations for text):
{{TEXT_PAIRINGS_WITH_CONTRAST_RATIOS}}
Decorative-only colors (never for text): {{DECORATIVE_ONLY_COLORS}}
Explicitly NOT brand colors even if seen in our materials: {{THIRD_PARTY_EXCLUSIONS}}

## 4. Typography
{{TYPE_RULES: family/class, weights, case, tracking values per level, line height}}
If the exact licensed font is unavailable in your output medium, use: {{OPEN_LICENSE_EQUIVALENTS}} and say you did.

## 5. The mark
Use the real logo file when the medium supports file placement: {{LOGO_FILE_NAMES_AND_WHEN}}
When generating HTML/SVG where you must embed the mark, use exactly this code — do not redraw, restyle, or recolor it:
```svg
{{INLINE_MARK_SVG}}
```
Rules: {{CLEAR_SPACE / MIN_SIZE / DONT_LIST}}
Missing variants: {{GAPS — e.g., "no reversed wordmark exists; on dark surfaces use Icon v2, never a recolored wordmark"}}

## 6. Motif / pattern
{{MOTIF_RECIPE with opacity, spacing, placement rules and bans}}

## 7. How to build visual content (IMPORTANT)
For any graphic (social post, ad, story, flyer, header): **build it as HTML or SVG using the exact hex values and the mark code above, then render/export it.** Do not use text-to-image generation for brand graphics — image models cannot reproduce exact colors or the logo, and the result will be off-brand.

### Recipes by format
{{FORMAT_RECIPES — one block each for the formats this brand actually uses, e.g.:
- Instagram feed post (1080×1080): surface, headline treatment, body limit, mark placement/size, CTA style
- Instagram story (1080×1920): ...
- Email header / signature: ...
- Print flyer / card: ...}}

## 8. Compliance & required language
{{REQUIRED_DISCLAIMERS — e.g., "Results may vary" on all before/after content; regulated-claims rules; review/testimonial rules}}

## 9. Pre-flight checklist — run before showing any output
1. Only colors from Section 3? Only approved text pairings?
2. Mark used per Section 5 (real file or exact SVG, clear space respected, no recolor)?
3. Voice passes the say/not-this test in Section 2? No banned language?
4. Every factual claim traceable to Section 1 proof points?
5. Required compliance language present (Section 8)?
6. Typography case/tracking per Section 4?
If any check fails, fix it before presenting.

---
*Generated from the {{BRAND_NAME}} Brand Book ({{DATE}}). The PDF brand book is the authority for humans; this file is its machine-readable companion. Original identity design: {{DESIGN_CREDIT_IF_MODE_B}}.*
