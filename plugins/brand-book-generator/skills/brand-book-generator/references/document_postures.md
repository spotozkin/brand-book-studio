# Document Postures — What Kind of Brand Book Is This?

The single most important structural decision, made BEFORE any layout work: what kind of
document is this brand book? Real professional brand books differ from each other at the
posture level first — a voice-led quick guide, a color-first system, a partner-governance
spec, and a one-sheet are different documents, not the same document restyled. This file
exists because the benchmark corpus (23 professional books studied) showed that section
order, chapter set, depth, and register are strategy-dependent, never fixed.

**The rule: the skill derives a recommended posture from the strategy (Step 2), then
confirms it with the person via `ask_user_input_v0` before building. Strategy proposes,
the person disposes.** Never silently default to one posture. Never present the
recommendation as the only option — offer it plus 2-3 genuinely different alternatives
that could also fit.

## The posture taxonomy

### 1. STRATEGY-LED NARRATIVE
The classic full book: opens with purpose/positioning, moves through voice to visual
system to applications. Best default for brands whose differentiation is conceptual
(mission, philosophy, heritage) rather than purely visual.
Signals: strong founding story, values-driven category (nonprofit, medical, education),
brand new to formal branding, person talks about "what we stand for."
Section spine: essence → messaging → voice → visual system → applications → governance.

### 2. VOICE-LED GUIDE
Voice and copy rules lead; visuals follow as support. Chapters open with how the brand
talks; the palette and type exist to serve the words.
Signals: personality-forward brands, content-heavy businesses (media, coaching,
newsletters), brands whose #1 asset is a recognizable way of speaking, heritage brands
with a distinctive vernacular.
Section spine: voice & vocabulary (expanded, multi-page, with rewrite examples) →
messaging → visual system (compressed) → applications.

### 3. COLOR-FIRST / VISUAL-SYSTEM-FIRST
The palette or a signature visual device IS the brand; the book opens with it.
Signals: brands with an ownable color or device (a signature hue, a container/box
device, a pattern), retail/fashion/lifestyle, brands where the person's brief centers
on "the look."
Section spine: color (expanded — families, roles, guarded colors) → mark & device →
typography → voice (compressed) → applications.

### 4. SPEC / GOVERNANCE BOOK
A compliance document: precise datums, tolerances, do/don't matrices, escalation paths.
Written for partners, franchisees, vendors, or a distributed team — not for inspiration.
Signals: multi-location businesses, licensing/partner programs, franchises, brands
handing assets to outside vendors, anyone who says "people keep getting it wrong."
Section spine: mark rules (expanded: clearspace in letterform units, minimum sizes with
declared datums, dual-tier tolerances) → color specs (per-substrate if print-heavy) →
type specs → per-asset chapters if multi-mark → do/don't register → escalation & contact.

### 5. ONE-SHEET SYSTEM OF RECORD
A single dense page (or spread) that IS the complete guide. Legitimate and professional
when the brand is simple or sits inside a house-of-brands where the corporate layer is
thin by design.
Signals: solo creators who need something usable this week, sub-brands under a strong
parent, internal project brands, anyone who picked minimum scope.
Completeness floor (non-negotiable even at one page): mark + clearspace + minimum size,
core palette with hex, primary typeface, one-line voice, one contact/escalation owner.

### 6. REBRAND-IMPLEMENTATION PACKAGE
Documents a transition, not just an end state. Versioned, change-logged, often
confidential, sometimes split by discipline (print/digital/environments).
Signals: "we're rebranding," an old identity exists and is being replaced, sunset dates
matter, multiple teams must migrate on a schedule.
Section spine: what changed & why (overlay-diff exhibit: old vs new) → new system →
sunset table (what dies, when) → migration per discipline → version control & change log.

## Deriving the recommendation

Score the strategy synthesis against the signals above. Two rules:
- **Portfolio structure trumps everything**: a branded house (one master brand) gets a
  deep single book; a house of brands gets a thin corporate layer (possibly a one-sheet)
  plus per-brand depth where it matters. Ask which structure applies whenever sub-brands,
  programs, or locations exist.
- **Audience trumps aesthetics**: a book whose primary reader is an outside vendor is a
  spec book even if the brand itself is playful. Ask who will actually open the PDF.

Present the recommendation with a one-line "because": e.g. "I'd build this as a voice-led
guide, because your differentiation is entirely in how you talk to patients — but here
are two other shapes that could work." Then let them pick.

## Completeness floor matrix

Coverage is guaranteed per posture — form is free, floors are not. Never let structural
creativity drop required content.

| Content | Narrative | Voice-led | Color-first | Spec | One-sheet | Rebrand |
|---|---|---|---|---|---|---|
| Positioning/essence | Full | Brief | Brief | One line | One line | Brief + rationale for change |
| Voice codified (not just demonstrated) | Yes | Expanded | Brief | Brief | One line | Yes |
| Mark + clearspace + min size | Yes | Yes | Yes | Expanded, datum-declared | Yes (compact) | Yes, old + new |
| Plain-language mark description | Yes | Yes | Yes | Yes | If room | Yes |
| Palette w/ hex + accessible pairings | Yes | Yes | Expanded | Yes + substrate variants | Core only | Yes |
| Typography + license source | Yes | Yes | Yes | Yes + fallback stack | Name + source | Yes |
| Do/don't guidance | Yes | Yes | Yes | Expanded register | 2-3 items | Yes |
| Applications in context | Yes | Yes | Yes | Per touchpoint matrix | Skip | Migration examples |
| Escalation/contact owner | Yes | Yes | Yes | Named | Yes | Named |
| Contrast verification | Always | Always | Always | Always | Always | Always |
| Asset/provenance index | Yes | Yes | Yes | Yes + rights expiry | Skip | Yes + version log |

Notes on the floor:
- **Floors are OUTCOMES, not sections.** Each row names a capability the reader must end
  up with, not a chapter that must exist. "Asset/provenance index: Yes" means *every
  claim and file is traceable* — satisfiable by a manifest chapter, per-page footnotes,
  swatch annotations, or a colophon (placement is seeded in `structural_seeds.md`).
  "Do/don't guidance: Yes" means *violations are detectable by a stranger* — a severity
  register, flat commandments, or rules woven into each system chapter all qualify. The
  QA question is never "does the section exist?" but "can the reader do the thing?"
- "Voice demonstration always paired with codification" — a witty book must still state
  its rules; wit alone is demonstration without governance.
- Every book names an escalation owner (a person, a role, or an inbox — "none" is a
  documented failure mode in the corpus, not an option).
- Scale the floor to the brand type: a solo dermatology practice's spec floor is not
  Calvin Klein's. Depth tiers (`asset_inventory.md`) still govern volume WITHIN the
  chosen posture; posture governs shape.

## Section-order profiles are starting points

Within a posture, reorder when the brand's logic demands it (e.g. a color-first book for
a brand whose device matters more than its hue may open with the device). The spine you
choose must be justifiable in one sentence from the strategy. If you can't write that
sentence, you've picked by habit — stop and re-derive.
