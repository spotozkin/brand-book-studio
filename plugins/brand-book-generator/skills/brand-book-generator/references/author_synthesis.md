# Author Synthesis — Simulating Independent Authorship

Run as **Step 2.7**, after the central question, before any outline. This is the positive
divergence engine: the gates (`anti_fingerprint_checklist.md`, `structural_digests.md`)
catch convergence after the fact; this step prevents it at the source.

## Why an author, not more axes

The professional corpus doesn't vary randomly — it varies because it had independent
authors: different firms, lineages, convictions, blind spots, solving different problems
in different decades. Dice-rolling on axes produces incoherent variety, and incoherent
variety is itself a tell. What reads as human is a book that is internally coherent
around a point of view that differs from every other book's point of view. So: before
outlining, synthesize the author of THIS book, and make every downstream judgment call
as that author.

## The profile schema

Write one short paragraph plus a spec block, recorded verbatim in the book's digest:

```
HANDLE: <two-word shorthand, e.g. "the Basel systematist", "the editorial romantic">
LINEAGE: <design tradition — Swiss modernist grid / print-era corporate ID /
  editorial-magazine / digital design-systems / vernacular-craft / brutalist-web /
  government-standards / fashion-house atelier / ...>
ERA OF FORMATION: <the decade whose defaults they absorbed>
CONVICTIONS (2): <e.g. "governance documents should be beautiful" /
  "a rule without a stated consequence is a suggestion">
BLIND SPOT (1): <something they under-attend to — recorded so the imperfection
  budget below has a coherent source>
PET MOVE (1): <a signature habit — a margin-note voice, a recurring diagram style,
  an insistence on one-idea-per-page>
CADENCE TARGETS: <bands for scripts/prose_fingerprint.py — sentence mean/variance,
  em-dash per 1000 words, aphorism ratio, heading length>
PLAUSIBILITY: <one line: why this author would credibly be hired by this brand>
```

## Derivation guardrails

- **Plausible for the brand.** The author must be someone this category and client would
  actually hire — a heritage watchmaker does not hire the brutalist-web author. The
  PLAUSIBILITY line is checked at the gate; an implausible author fails.
- **Evidence-compatible.** The author's convictions must not conflict with the Step 1.5
  evidence or the central question; the author serves the engagement, not vice versa.
- **The profile drives, it doesn't decorate.** Seeds (`structural_seeds.md`), register,
  page rhythm, what gets emphasized, and the cadence targets all flow from the profile.
  If a downstream choice can't be traced to the profile, the question, or a seed, it's
  habit — re-derive.

## Non-resemblance rules (hard gate)

Profiles across the portfolio must not resemble one another, within reason. Diff the
candidate profile against every AUTHOR PROFILE in `structural_digests.md`:

1. **Lineage never matches the immediately previous book's.** Deeper in the corpus, a
   lineage may recur only when the brand category genuinely demands it — and then every
   other field must diverge.
2. **At most ONE conviction may overlap** with any single corpus profile, and never the
   same pair.
3. **Pet move is never reused. Blind spot is never reused.**
4. **Cadence-target band must differ from the immediately previous book** on at least
   two of the four metrics.
5. **Composite rule:** matching any corpus entry on two or more of {lineage, either
   conviction, pet move, cadence band} = fail; re-synthesize.

"Within reason": two brands in the same category two years apart may share a lineage —
real markets have schools. What they may never share is the full disposition. When in
doubt, diverge.

## The imperfection budget

Real professional books are not uniformly rigorous — a chapter runs long because someone
cared too much, a convention appears once and is never systematized, an opinionated
aside survives editing. Even excellence, held perfectly level across every section, is a
machine tell. Each book therefore carries **one or two authored idiosyncrasies**, drawn
from the profile:

- Must be TRACEABLE to the pet move, a conviction, or the blind spot — coherent
  personality, never random noise or error.
- Legitimate forms: a disproportionately deep pet chapter; a signature margin-note habit
  used a handful of times; a stated, reasoned refusal to cover something out of scope; a
  numbering or captioning quirk applied consistently; one editorial aside in the
  author's voice.
- **Never touches floor content.** The completeness floors (`document_postures.md`)
  remain the hard deck: an idiosyncrasy may add or flavor, never omit, blur, or make a
  required capability harder to use. Contrast is still measured; claims are still
  sourced; the mark rules are still complete.
- Recorded in the digest (IDIOSYNCRASIES field) so it is never reused.

## Hash-committed choice — entropy where entropy belongs

After the question, seeds, and profile have spoken, some choices remain genuinely free
(which of three valid cover archetypes; quote closer vs. spec closer; two equally
justified section orders). Do not let the model pick — it will pick its comfort default
every time, and that default is the next fingerprint. Commit the pick to a hash:

```bash
python3 scripts/committed_choice.py "<brand>" "<YYYY-MM-DD>" "<choice-label>" "optA|optB|optC"
```

Deterministic, auditable, un-rerollable. Use it ONLY for choices that are truly free
after all derivation — never to skip deriving. Log every committed choice in the SEEDS
comment (`label=option (committed)`), so the gate can verify free choices were committed
rather than defaulted.

## Precedent lineages (hook — pending benchmark corpus)

When the 23-book benchmark digests are added to `structural_digests.md` (from the
maintained benchmark notes), LINEAGE stops being free-text: each engagement samples one
or two precedent traditions as ancestry — inheriting a disposition, never imitating a
book — with no lineage repeated in consecutive engagements. Until those digests land,
derive lineage from the taxonomy list in the schema above.
