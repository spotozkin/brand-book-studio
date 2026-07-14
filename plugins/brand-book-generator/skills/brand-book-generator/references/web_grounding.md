# Web Grounding — Zero-Hallucination Sourcing and the Guided Site Capture (Mode B)

Purpose: every fact in a Mode B book must be true, every value must be reproducible, and
the finished book must resemble the live site on the FIRST pass. This file governs (1)
what counts as evidence, (2) date accuracy, and (3) what to ask the person for — up to
and including a two-minute DevTools walkthrough — so the excavation starts from
canonical values instead of guesses.

## 1. The evidence hierarchy — what may ground a claim

Every color value, font claim, factual statement, quote, and measurement in the book
must trace to one of these classes, ranked. When classes conflict, the higher class
wins. Log the class of every palette entry and proof point in working notes as you go.

1. **Supplied master files** — vector fills, embedded fonts, SVG geometry read directly
   from files the person uploaded. Canonical.
2. **DevTools extractions the person provides** — CSS custom properties / design tokens,
   computed `font-family` values, rendered-font names, asset files saved from the
   Network panel. Canonical for digital values (still confirm font LICENSING, per the
   existing unnamed-font rule — the name being known does not clear the license).
3. **Verbatim page text** — copy the person pasted, or text fetched live this session
   with the web tools. Quote-anchor it: keep the exact source sentence next to the claim
   in working notes.
4. **Pixel samples from supplied screenshots** — provisional, tolerance-flagged, subject
   to the palette-determinism gate.
5. **The person's direct statements** — usable for their own business facts; still ask
   for a source for anything that will print as a proof point.

**Class 0 — BANNED: model memory.** What the model "knows" about a brand from training
is not evidence. No palette value, founding date, tagline, product name, slogan history,
or design fact may enter the book because the model remembers it — even for famous
brands, even when memory is probably right. If it isn't in classes 1–5 from THIS
session, it doesn't ship. This is the zero-hallucination rule, and it has no exceptions:
a Mode B book about a brand the model knows well must be buildable, unchanged, about a
brand the model has never heard of.

Corollaries:
- **Live-fetch verification.** If web tools are available and a claim came from a page,
  fetch the page this session and confirm the wording before printing it. If web tools
  are NOT available, only user-supplied captures and pastes count — say so and ask for
  what's missing rather than filling from memory.
- **No compositing.** Never merge a fetched fact with a remembered detail ("the site
  says founded 1932" + remembered "in Billund" = one sourced clause and one
  hallucination). The whole printed sentence must be covered by the evidence.
- **Absence is reportable.** If a fact can't be grounded, the book says nothing about it
  or routes it as an open confirmation — it never approximates. (Existing rule,
  restated here because web sourcing is where it breaks most.)

## 2. Date discipline — no wrong years, ever

Models write wrong years from stale habit; a brand book with last year's date on the
cover is instantly amateur. Rules:

- **The current date comes from the machine, not from memory.** Before writing any
  cover, document-control block, or "next review" line, run `date +"%d %B %Y"` in the
  session and use that output verbatim. Never type a year from recall.
- **Capture dates are the person's dates.** Label screenshots/extractions with the date
  the person says they captured them (ask if unstated); a fetch performed this session
  is dated with the machine date. Never backfill or estimate a capture date.
- **Historical dates are class 1–3 facts.** Founding years, milestones, and "since"
  claims follow the evidence hierarchy like any other fact.
- **Review dates are computed.** "Next review: [current + 6 months]" is arithmetic on
  the machine date, stated explicitly.
- **Pre-export year grep.** Before render, grep the HTML for all four-digit years
  (`grep -oE "\b(19|20)[0-9]{2}\b" brand_book.html | sort | uniq -c`) and account for
  every one: each is either a sourced historical fact or derived from the machine date.
  An unaccountable year is a gate failure.

## 3. The capture ladder — Claude works first, the user works last

Goal: the person does as little as possible. Climb this ladder rung by rung; never ask
for a higher rung until the lower ones are exhausted, and when you do ask, name the
SPECIFIC missing items ("I have your palette and fonts; I only need two screenshots"),
never the whole list again.

### Rung 0 — the URL. Claude fetches; the user does nothing.

If web tools are available in the session, this rung is mandatory before any ask:

1. Fetch the homepage HTML. From it, harvest: inline `<svg>` marks in header/nav (real
   vector artwork — class 2 evidence), `<img>` sources matching logo/brand/mark, all
   `<link rel="stylesheet">` URLs, `<link rel="icon">` URLs, `<meta name="theme-color">`,
   the `<title>`, and nav/footer text including the legal line.
2. Fetch each linked CSS file. Extract `:root` / `html` custom properties (the design
   tokens — canonical hexes), `@font-face` family names and font URLs, and the
   `font-family` stacks on body/heading rules. Tokens found here END the palette-sampling
   problem for digital values.
3. Fetch the about/history/press pages for proof-point copy, and any press-kit page for
   official logo downloads.
4. Log everything harvested with its URL as the anchor (class 2–3 evidence).

Limits to expect and note: JS-rendered sites can return thin HTML; login-walled pages
don't fetch; fetching returns text, not rendered pixels — so layout, photography style,
and visual rhythm still need screenshots (rung 1). If fetch is unavailable or blocked,
say so plainly and move up the ladder — never fill the gap from memory (class 0).

### Rung 1 — everyday screenshots + pasted words. No tools, no DevTools.

Always asked (cheap, high-value, and the only source of visual-layout truth). Send as a
short friendly message with the exact keystrokes for their OS:

- Screenshots — Mac: **Cmd+Shift+4** then drag; Windows: **Win+Shift+S** then drag —
  of: the homepage from the top, the main menu (with a dropdown open if there is one),
  one product/service page, the about page, and the very bottom of any page (the
  footer). Phone screenshots of the mobile site are a welcome bonus.
- Copy-paste the words (highlight → Ctrl/Cmd+C, straight into the chat): the big
  headline on the homepage, the tagline, the tiny legal line at the very bottom of the
  site, and 2-3 sentences of typical page text.
- Confirm: "were these taken today?" (capture-date discipline, §2), and attach any logo
  files they already have.

### Rung 2 — the bookmarklet. One drag, one click, one copy. Still no DevTools.

Use only when rung 0 couldn't run or came back thin (JS-rendered site, blocked fetch,
ambiguous values). Send the person these steps verbatim, with the code block:

> 1. Show your bookmarks bar (Ctrl/Cmd+Shift+B if it's hidden).
> 2. Right-click the bookmarks bar → "Add page/bookmark". Name it **Brand Capture** and
>    paste the entire code below into the URL/address field. Save.
> 3. Go to your website, click **Brand Capture** in the bookmarks bar.
> 4. A white box appears with text already selected — press **Ctrl/Cmd+C**, come back
>    here, and paste. Click anywhere on the page to close the box. That's it.

The bookmarklet source lives at `assets/brand_capture_bookmarklet.txt` (single line,
paste-ready). What it gathers: the site's `:root` design tokens (same-origin
stylesheets), the ACTUAL computed color/background/font/weight/size of body, h1, h2, p,
links, and buttons (works even when tokens don't), logo image URLs, header inline SVG,
favicon URLs, theme color, page title/URL, and a timestamp — as one JSON blob. It only
reads the page and shows a text box; it sends nothing anywhere. If their browser blocks
bookmarklets, fall through to rung 3's console variant with the "allow pasting" warning.

### Rung 3 — DevTools. Power users and stubborn gaps only.

Never the opening ask. Offer when the person is comfortable ("if you happen to know your
way around DevTools…") or when one specific value resists rungs 0–2:

- **Rendered font name:** right-click any headline → Inspect → **Computed** tab →
  scroll to **Rendered Fonts** at the bottom — that names the font file actually drawn.
  (This is the one fact only DevTools gives; rungs 0–2 yield the font-family stack,
  which is usually sufficient.)
- **Console variant of the bookmarklet:** F12 → Console → paste the same code without
  the `javascript:` prefix → Enter. Warn Chrome users in advance: the first paste is
  blocked until you type `allow pasting` and press Enter — this is normal.
- **Logo via Network:** F12 → Network tab → filter "svg" → reload → right-click the
  logo asset → Save.
- **Full-size page screenshot:** F12 → Ctrl/Cmd+Shift+P → type "screenshot" → "Capture
  full size screenshot."

### What to ask in words, at any rung

- Exact business name as it should print; marks carrying ® / ™.
- Any hexes or font names they already know (class 5 — verify against captures).
- Who built the site (the builder often holds the master assets requests will route to).
- "Is anything on the current site WRONG that you don't want codified?" — codifying a
  known mistake is the one way Mode B fidelity backfires; log exclusions explicitly.

### One-pass fidelity checklist (before building, confirm you hold)

□ Real logo artwork (vector from rung 0/2/3, or best available raster) — never a
  screenshot crop
□ Palette source of class ≤4 — tokens/computed values (class 2) preferred over samples
□ Font names from tokens/computed/rendered (class 2) OR the unnamed-font rule engaged
□ Visual captures covering: nav, hero, product surface, editorial surface, footer
□ Verbatim key copy: hero, tagline, footer legal line
□ Capture date confirmed; machine date pulled for the book's own dates
□ Known-wrong elements excluded and logged

Missing items are asked for ONCE more by name, then the book proceeds with gaps
documented and routed — never filled from memory (class 0).

## 4. Interaction with existing gates

The palette-determinism gate consumes class 1–2 values as canonical and class 4 as
provisional. The confidence lint still applies: none of this machinery is narrated on
body pages — tokens, DevTools, and capture methods live at the seeded provenance
placement like all other evidence. The grounding & date gate in
`anti_fingerprint_checklist.md` enforces this file at export time.
