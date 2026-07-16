# Rendering Pitfalls — WeasyPrint Failure Modes That Look Like Design Bugs

Purpose: WeasyPrint (Pango/Cairo underneath) diverges from a browser in a few specific,
recurring ways that don't throw errors — the render succeeds, the PDF opens fine, and the
bug only shows up as a visual defect a person has to spot on the page. Every pitfall below
was caught in production books (LEGO Mode B test, Jul 2026) after export, meaning it
survived a code-runs-without-error check — and in one case (the flex-shrink family) it
recurred in three different forms in the same book even after the first form had already
been documented here, which is the reason `scripts/detect_page_overflow.py` exists: a
prose rule you have to remember to apply is not sufficient on its own, so Step 5 now runs
an automated script that catches the visible symptom (content outside its margin)
regardless of which CSS default caused it, rather than depending on a rule being recalled
correctly on every new flex row written weeks later. Treat every rule here as an
authoring constraint applied WHILE writing the HTML, AND treat the detector script as the
backstop that catches what the authoring constraint missed — not either/or.

## Pitfall 1 — Pictographic/emoji characters collapse instead of rendering

**What happens:** WeasyPrint's font stack has no bundled color-emoji font. A glyph outside
the loaded fonts' coverage doesn't reliably fall back to a visible placeholder — it can
render at zero or near-zero advance width. The text immediately after it then shifts left
to fill the phantom space, and on a tightly laid-out page (a component mockup, a legend
row, a button label) that shift is enough to make unrelated text overlap.

**Why it's dangerous:** it's invisible in the HTML source (the character looks fine as
text) and invisible in a "did it render" check (the PDF has the right page count, the
right structure, no exceptions). It only shows up as garbled-looking text in a visual
QA pass, and it's easy to misdiagnose as a layout/CSS problem instead of a missing-glyph
problem.

**The rule:** never use an emoji or pictographic Unicode character for iconography in a
generated book — not as a literal character, not as an HTML numeric entity (`&#128717;`
and similar). This includes seemingly-safe basics (🎂, 🧱, 🛍, 📍) as well as obviously
risky ones. A small set of very old, plain symbol-block characters (★ U+2605, ♡ U+2661)
usually renders because they've been in general-purpose fonts for decades, but "usually"
is not a determinism guarantee this skill accepts elsewhere (see the palette-determinism
gate) — so **draw every icon as inline SVG instead, always**:

```html
<svg viewBox="0 0 16 16" style="width:0.82em;height:0.82em;vertical-align:-0.08em;"
     xmlns="http://www.w3.org/2000/svg">
  <circle cx="6.2" cy="6.2" r="4.4" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <line x1="9.6" y1="9.6" x2="13.2" y2="13.2" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
</svg>
```

`currentColor` inherits the surrounding text color for free (dark on light, light on
dark). Size it in `em` so it scales with the surrounding type. A handful of generic UI
glyphs (search, pin, heart, bag, star, tag, price-tag, pieces/count, chevron, check) cover
nearly every mockup this skill builds — keep a small personal library of these paths once
built rather than re-deriving them per book, but never fall back to an emoji character
because deriving the SVG feels like more work in the moment.

**Mechanical check before export:**

```bash
grep -noE "&#[0-9]{4,6};" brand_book.html | awk -F: -v c=9000 '{split($0,a,";"); n=a[1]; gsub(/[^0-9]/,"",n); if (n+0>c) print}'
```

Simpler in practice: grep for any numeric character entity at all and eyeball the list —
a finished book should have none, because every icon is SVG and all real copy is plain
text. Also check the raw bytes for emoji ranges directly, in case literal UTF-8 emoji
characters were pasted in instead of entities. `grep -P` with astral-plane codepoints
(`\x{1F300}` and above) is unreliable across environments — some builds error out on the
codepoint rather than matching it — so use Python instead, which handles it consistently:

```bash
python3 -c "
import re
text = open('brand_book.html', encoding='utf-8').read()
hits = re.findall(r'[\U0001F300-\U0001FAFF\u2600-\u27BF]', text)
print('emoji-range hits:', len(hits), hits[:20])
"
```

Zero matches required on both checks. A hit on either is an export blocker, not a style
note.

## Pitfall 2 — Flex rows silently distort or overflow instead of wrapping

**What happens:** this is one underlying cause with three different visible symptoms,
all caught in the same book:

- A fixed-size circular badge (a numbered callout flag) compresses into an oval, and
  different badges on the same page compress by different amounts depending on how
  much text sits next to them.
- A button/pill sized to hug its content instead balloons in height and wraps its
  label onto two lines, even though there's visibly enough room for one.
- A column of text in a multi-column row refuses to shrink, and instead pushes itself
  (and everything after it) past the edge of its container — off the visible page
  in the worst case.

All three come from the same handful of CSS flexbox defaults doing the "wrong" thing
for a print-style fixed-page layout (they're often fine or invisible in a scrolling
browser page, which is why this is easy to get wrong): a flex item's `flex-shrink`
defaults to `1` (it CAN compress), a flex item's `min-width` defaults to `auto` (it
WON'T compress below its own content's natural minimum, e.g. its longest unbreakable
word), and a flex row's `flex-wrap` defaults to `nowrap` (a row that doesn't fit just
overflows instead of breaking to a second line). Depending on which of those three
defaults bites, you get compression (badges), refusal-to-shrink-so-something-else-gives
(buttons wrapping oddly), or overflow (footer columns running off the page). None of
these throw an error. All three passed a "did it render" check and only showed up on
close visual inspection of one specific page each.

**The rule — author every flex row with explicit intent on every child, not defaults:**

1. **Anything that must hold an exact size or shape** (a numbered badge, an icon chip,
   a button/pill whose label must stay on one line) gets:
   ```css
   flex: 0 0 auto;      /* or a specific size: flex: 0 0 15pt; for a fixed badge */
   white-space: nowrap;  /* the label can't wrap internally */
   ```
   For true fixed-dimension shapes (circles especially), also add `min-width`/
   `min-height` matching the intended size and `box-sizing: border-box`, per the
   original circle case below.

2. **Anything that's allowed — expected — to shrink or wrap** (a text column, a
   paragraph inside a flex item) gets:
   ```css
   min-width: 0;   /* overrides the default `auto` floor that blocks shrinking */
   ```
   Without this, a column with a long word or a tracked-caps heading will refuse to
   compress and will push the row past its container instead.

3. **Any row where the total content might not fit at some width** gets:
   ```css
   flex-wrap: wrap;
   ```
   as a safety net, so if items can't all fit on one line they drop to a second line
   instead of running off the page. Pair this with rule 1 on the items inside it (each
   item should wrap as a whole unit, not break awkwardly mid-content).

**A worked example (the footer bug):** four columns in a row, one of them containing
"SUBSCRIBE TO DIGITAL MARKETING EMAILS" as a tracked-caps heading plus an email-input
pill and a Subscribe pill. The fix applied all three rules together: `min-width:0` on
every column so they could shrink, `flex-wrap:wrap` on both the column row and the
inner pill row so content drops to new lines instead of pushing past the container,
and `white-space:nowrap` + `flex:0 0 auto` on the two pills so they stay intact as
units when they do wrap.

**The original circle case, preserved as the canonical fixed-shape pattern:**

```css
.flag {
  flex: 0 0 15pt;        /* refuses to grow OR shrink, ever, regardless of siblings */
  width: 15pt;
  height: 15pt;
  min-width: 15pt;       /* belt-and-suspenders against any flex-basis edge case */
  min-height: 15pt;
  box-sizing: border-box;
  border-radius: 50%;
}
```

Test any reusable badge/chip/button class against a worst case before trusting it: put
it beside a sibling with a very long line of text (not just the short placeholder you
first typed) and confirm the element's rendered pixel dimensions don't change between a
short-sibling row and a long-sibling row.

**The real fix is automated, not a memorized rule — see `scripts/detect_page_overflow.py`.**
Three instances of this exact bug family shipped in the same book despite the circle
version already being documented here after an earlier round, which means "remember to
apply the CSS rule" is not sufficient on its own — it's easy to write a new flex row
days later and forget the guard. Run the detector script on every export (Step 5 gate,
below); it rasterizes every page and flags any page whose declared margin band contains
content that shouldn't be there, catching overflow mechanically instead of depending on
a person or model happening to look closely at exactly the right page.

**Mechanical check before export:**

```bash
python3 scripts/detect_page_overflow.py brand_book.pdf brand_book.html --skip-pages <cover>,<closer>
```

A clean run reports zero flagged pages. Any flagged page needs the three-rule pattern
above applied to whichever flex row is on it, then a re-render and re-check — don't
hand-wave a flagged page as "probably fine," since every flagged page in this book's
history turned out to be a real bug once actually looked at.

## Why these live in a dedicated file

Both bugs share a signature worth naming: the HTML is syntactically fine, the render
completes without error, the page count and structure are correct, and the defect is
only visible on the finished page — which means a code-level review misses both, and only
a genuine visual QA pass (rendering to PNG and looking, per SKILL.md Step 5) catches them.
That makes prevention-at-authoring-time the only reliable defense; catching them after the
fact depends on remembering to look at exactly the right page. Build every icon as SVG and
every fixed-size shape with a flex guard from the first draft, every time, rather than
treating these as a post-render cleanup pass.
