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

### BOOK: Rolex "A Record of the Visual System" (Mode B test) · Jul 2026 · v3
POSTURE / CENTRAL QUESTION: heritage/editorial record (essayistic studio book) ·
implicitly "holding the ration — pigment scarcity defended against enthusiasm"
COVER: white field, gold coronet centered, letterspaced small-caps title, single
metadata footer line; no contents page anywhere ("chapters announce themselves")
SECTION SEQUENCE: why-this-exists preface → color & light (2pp incl. photographic
tones) → mark (2pp) → letterforms → voice → annotated applications → colophon →
full-green typographic closer
HEADING REGISTER: essayistic declaratives — "Almost every page is black and white." ·
"Where the richness actually comes from"
COINED HEADINGS/PHRASES: "A Record of the Visual System" · "color is rationed" / "hold
the ration" · the crown unit ("measured in crowns") · register names "The archive / The
stage / The event" · "Lines to measure against" · "A note from the compositor" · "When
this book runs out" · "A gap acknowledged costs nothing, while a gap improvised costs
the mark its authority" · "Precision is the ornament" · "Seven colors. Two greens. One
crown."
TABLE SCHEMAS: none — all evidence carried in prose and captioned figures; contrast
ratios inline in swatch notes
RULE TIERS: none named — absolutes stated in prose
COMPONENT COUNTS: 3 traits / 0 rewrites (3 exemplary lines only) / 0 tiers / 7 colors
(+2 photographic tones explicitly excluded)
RHETORICAL BEATS: machine-colors exclusion note · unnamed-font refusal + Inter stand-in
paragraph · exemplary-lines-only voice format · gaps routed to Geneva, never rebuilt ·
colophon-in-brand-voice replacing the manifest/control suite · full-field brand-color
closer carrying an aphorism
AUTHOR PROFILE: not recorded in this reconstruction — backfill from the HTML SEEDS
comment if available (digest rebuilt from the delivered PDF)
IDIOSYNCRASIES / PROSE FINGERPRINT: backfill from HTML; not measurable from PDF alone
NOTE: facts drifted vs. the v1 Rolex run (palette 7 vs 10; clearspace unit crown WIDTH
vs HEIGHT; min size 61px vs 96px) — the drift that motivated the v1.4 palette-
determinism gate.

### BOOK: LEGO "Graphics Standard LGS-2" (Mode B test) · Jul 2026 · v3
POSTURE / CENTRAL QUESTION: numbered standards manual (spec) · "the identity is a host
system — hold the frame so the guests can change"
COVER: white page with hairline box frame, tile top-left, document-control table ON the
cover, single yellow rule accent
SECTION SEQUENCE: index → frame & guests → mark → mark conduct → color + conformance →
letterforms → language registers → imagery → frame in use → sources & registers →
closing one-drawing restatement
HEADING REGISTER: institutional § headings — "§ 1 The frame and its guests" · "§ 3 Mark
conduct"; decimal-numbered clauses (1.1, 2.4) throughout
COINED HEADINGS/PHRASES: "the frame and its guests" · "host system" · "guest zone" ·
"Mark conduct" · "the identity set / the interface set" · "a rule without a consequence
is read as a preference" · "no one fills a gap locally" · "every clause ... is a load
calculation for this one drawing" · "the brick is the pixel"
TABLE SCHEMAS: conduct (CODE / RULE) · conformance (COMBINATION / MEASURED /
CONFORMANCE / PERMITTED AT) · registers (CONTEXT / REGISTER / OBSERVED MARKERS) ·
corrections (OFF-STANDARD / CORRECTED TO REGISTER) · type environment (ENVIRONMENT /
SIZE BAND / FACE AND WEIGHT / NOTES) · evidence register (ITEM / EVIDENCE / LOCATION) ·
artifact register (REF / ARTIFACT / ORIGIN / DISPOSITION)
RULE TIERS: PROHIBITED / RESTRICTED / STANDARD — consequence-bearing
COMPONENT COUNTS: 5 language registers (no trait table) / 3 corrections / 3 tiers /
4 identity + 5 interface colors
RHETORICAL BEATS: decimal-clause governance · host/guest doctrine as the opening
chapter · guest-color-confers-no-approval rule · open-confirmations block · unnamed-font
refusal + dual stand-ins (Poppins specimens, IBM Plex running text) · closing
restatement-in-one-drawing
AUTHOR PROFILE: not recorded in this reconstruction — backfill from the HTML SEEDS
comment if available
IDIOSYNCRASIES / PROSE FINGERPRINT: backfill from HTML
NOTE: heavy in-body provenance narration (capture counts and dates in body clauses and
figure captions; input materials named on the COVER) — the leakage that motivated the
v1.4 confidence lint. Facts also corrected/extended vs. the v1 LEGO run (Surface Yellow
≈#F8D749 distinguished from Logo Yellow; Utility Dark ≈#102327 recorded; identity black
#000000 from master vs sampled #111111) — adjudicate against original captures and lock
the winners into the canonical LEGO kit before the next run.

### Cross-corpus note — the v3 pair
Unlike the v1 pair, these two books PASS the sibling rules against each other (different
postures, registers, tier vocabularies, table schemas, voice formats, closers) —
evidence the seeds/author machinery works. What they exposed instead: cross-run FACT
drift and provenance leakage, now gated in v1.4. Their coined phrases above are live
corpus entries under diff rule 1; the host/guest CONCEPT graduated to mandatory
conditional content (see the concept table in `anti_fingerprint_checklist.md`) while its
house names retired with this entry.

### Precedent lineages (pending)
When the 23-book professional benchmark corpus is digested into this file (from the
maintained benchmark notes — see `author_synthesis.md`, "Precedent lineages"), those
entries are ANCHORS, not bans: author lineages sample FROM them, and the diff rules
above apply only among this skill's own outputs, never against the professional corpus.

## Appending a new digest

After delivery, write the new book's digest in the schema above, append it here (in the
working copy), and include the updated file in anything shipped back to the person with
a one-line reminder to commit it. A corpus that doesn't grow protects nothing.
