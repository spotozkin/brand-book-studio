# Structural Digests — The Cross-Book Differential

The sibling test in `anti_fingerprint_checklist.md` is a judgment call; this file is the
mechanical version. Every book this skill has shipped gets a DIGEST — a compact record of
its skeleton. Before rendering a new book, generate the candidate's digest and diff it
against every digest below. This corpus is append-only: after each delivered book, the
skill writes the new digest and tells the person to commit it to the repo copy so the
corpus grows with the portfolio.

## The digest schema

Record for every book:

```
BOOK: <brand> · <date> · v<n>
POSTURE / CENTRAL QUESTION: <one line each>
COVER: <archetype + one detail>
SECTION SEQUENCE: <functional labels, in order>
HEADING REGISTER: <register + 2 example headings verbatim>
COINED HEADINGS/PHRASES: <every non-functional heading and named principle, verbatim>
TABLE SCHEMAS: <column headers + which section each table sits in>
RULE TIERS: <the vocabulary used>
COMPONENT COUNTS: <voice traits / rewrites / tiers / palette size>
RHETORICAL BEATS: <recurring moves — e.g. "callout after contrast table",
  "unnamed-font refusal paragraph", "closing document-control block">
AUTHOR PROFILE: <handle · lineage · era · convictions ·  blind spot · pet move —
  verbatim from Step 2.7, references/author_synthesis.md>
IDIOSYNCRASIES: <the 1-2 authored quirks spent from the imperfection budget>
PROSE FINGERPRINT: <output of scripts/prose_fingerprint.py on the final HTML —
  mean/stdev · em-dash/1000w · colon/1000w · aphorism · long-sentence>
```

## Diff rules — hard failures

Comparing candidate vs. any single corpus entry:

1. **Any verbatim non-functional heading or coined phrase match** → fail. (Functional
   labels — "Contents", "Color", "Typography" — never count.)
2. **Same table schema (same column headers) in the same section role** → fail. Same
   DATA is fine; the schema must be re-expressed (different columns, prose, annotations
   on swatches, etc. — see `structural_seeds.md`).
3. **Identical section sequence** for books of the same posture → fail; re-derive from
   the central question.
4. **Same rule-tier vocabulary as the immediately previous book** → fail (earlier books:
   allowed only if seeded from genuinely similar brand attributes, justified in the
   SEEDS comment).
5. **Three or more shared rhetorical beats** with any one corpus entry → fail. One or two
   shared beats across a portfolio is normal authorship; three is a skeleton.
6. **Identical component-count profile** (traits/rewrites/tiers all equal) with the
   immediately previous book → fail unless seeded.
7. **Author-profile resemblance** → fail per the non-resemblance rules in
   `author_synthesis.md`: lineage matching the previous book; more than one shared
   conviction with any entry; any reused pet move or blind spot; or matching any entry
   on two or more of {lineage, conviction, pet move, cadence band}.
8. **Reused idiosyncrasy** — any quirk from any IDIOSYNCRASIES line reappearing → fail.
9. **Prose-cadence match** — run `scripts/prose_fingerprint.py` on the candidate HTML.
   The book must land inside its own author's declared cadence bands, AND differ from
   the immediately previous book's measured fingerprint on at least two of {sentence
   mean, em-dash rate, aphorism ratio, long-sentence ratio} by a meaningful margin
   (>15% relative or >2 words for the mean). Both v1 baseline entries below fail this
   against each other — that is the house hand this rule exists to break.

Run the coined-phrase portion mechanically (grep the candidate HTML for every string in
every corpus entry's COINED line plus the retired list in
`anti_fingerprint_checklist.md`); the rest is a structured comparison you perform
against this file. Log the result (pass, or what failed and what was changed) before
render.

## Corpus

### BOOK: Rolex (Mode B test) · Jul 2026 · v1
POSTURE / CENTRAL QUESTION: spec-adjacent codification · (pre-dates Step 2.6; implicitly
"protecting restraint from marketing enthusiasm")
COVER: full-field typographic, deep green, letterspaced small caps
SECTION SEQUENCE: reading guide → color → mark → letterforms → voice → proof-point record
→ imagery registers → annotated applications → severity register → custody
(manifest + escalation + document control)
HEADING REGISTER: in-voice reverent declaratives — "One green, held for a century" ·
"Reverence, measured out in short sentences"
COINED HEADINGS/PHRASES: "the closed set" · "Pairings, with receipts" · "Two rewrites,
with the rule named" · "Documented gaps" · "On the site but not of the brand" · "the
severity register" · "Custody" · "The gold demotion"
TABLE SCHEMAS: contrast (TEXT ON SURFACE / RATIO / VERDICT / USE, in color) · voice
(TRAIT / SOUNDS LIKE / NEVER SOUNDS LIKE) · proof points (YEAR / PROOF POINT / SOURCE) ·
manifest (ASSET / SOURCE / LICENSE-STATUS / ADDED, in custody)
RULE TIERS: NEVER / AVOID / PREFER
COMPONENT COUNTS: 4 traits / 2 rewrites / 3 tiers / 10 colors
RHETORICAL BEATS: closed-set doctrine stated on palette page · demotion callout after
contrast table · unnamed-font refusal + @fontsource stand-in paragraph · rewrite pairs
with "Because:" explanations · documented-gaps-do-not-reconstruct rule · owner escalation
ending at document owner · closing document-control block (version / next review /
companion file)
AUTHOR PROFILE: none — pre-dates Step 2.7 (house hand, unsynthesized)
IDIOSYNCRASIES: none budgeted — uniformly rigorous throughout (itself a tell)
PROSE FINGERPRINT: mean 12.9 / stdev 8.7 · em-dash 19.8/1000w · colon 11.9/1000w ·
aphorism 0.27 · long-sentence 0.10 (measured from body prose)

### BOOK: LEGO (Mode B test) · Jul 2026 · v1
POSTURE / CENTRAL QUESTION: working reference / spec · (pre-dates Step 2.6; implicitly
"keeping own colors sovereign amid licensed-partner artwork")
COVER: full-field brand yellow, logo tile top-left, plain metadata row
SECTION SEQUENCE: read-this-first → color core → color interface → mark → mark rules →
typography → voice → applications (touchpoint matrix) → governance → assets & provenance
→ dark closer quote page with document-control row
HEADING REGISTER: in-voice questions — "What yellow is LEGO yellow, exactly?" · "Who do
you ask when this book runs out?"
COINED HEADINGS/PHRASES: "the closed set" · "Contrast receipts — measured, not assumed"
· "Two rewrites, with the rule named" · "the archaeology trail" · "Hierarchy in one
sentence" · "read a row, build the thing"
TABLE SCHEMAS: contrast (PAIRING / RATIO / WCAG AA VERDICT, in color) · voice (TRAIT /
SOUNDS LIKE / NEVER SOUNDS LIKE) · touchpoint matrix (TOUCHPOINT / SURFACE / MARK / TYPE
/ COLOR LOGIC) · manifest (FILE / WHAT IT IS / SOURCE / STATUS) · fact sources (CLAIM /
WHERE)
RULE TIERS: NEVER / AVOID / PREFER + bounded MAY
COMPONENT COUNTS: 4 traits / 2 rewrites / 3(+1) tiers / 4+3 colors
RHETORICAL BEATS: closed-set doctrine stated on palette page · inherited-pairing callout
after contrast table · unnamed-font refusal + @fontsource stand-in paragraph · rewrite
pairs with "Because:" explanations · no-variant-do-not-fabricate rule · owner escalation
ending at document owner · closing document-control block (version / owner / next review)
AUTHOR PROFILE: none — pre-dates Step 2.7 (house hand, unsynthesized)
IDIOSYNCRASIES: none budgeted — uniformly rigorous throughout (itself a tell)
PROSE FINGERPRINT: mean 13.6 / stdev 8.7 · em-dash 20.4/1000w · colon 6.6/1000w ·
aphorism 0.24 · long-sentence 0.10 (measured from body prose)

### Cross-corpus note
The two entries above share SEVEN beats, three verbatim coinages, and a near-identical
prose fingerprint (sentence stdev identical at 8.7; em-dash rate within 0.6/1000w;
aphorism ratio within 0.03) — they are the known-cloned pair and the reason this file
exists. Any candidate matching either on the diff rules is reproducing the exact failure
this gate was built to catch. Their shared cadence is the HOUSE HAND: rule 9's baseline.

### Precedent lineages (pending)
When the 23-book professional benchmark corpus is digested into this file (from the
maintained benchmark notes — see `author_synthesis.md`, "Precedent lineages"), those
entries are ANCHORS, not bans: author lineages sample FROM them, and the diff rules
above apply only among this skill's own outputs, never against the professional corpus.

## Appending a new digest

After delivery, write the new book's digest in the schema above, append it here (in the
working copy), and include the updated file in anything shipped back to the person with
a one-line reminder to commit it. A corpus that doesn't grow protects nothing.
