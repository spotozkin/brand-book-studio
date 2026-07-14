# The Asset Call — Collect What Exists Before Designing Anything

Purpose: the single best predictor of whether the finished book matches what the person
is picturing is whether their REAL materials were in hand before anything was designed.
People carry a mental image of their brand built from assets they already own — a logo
on their storefront, the pattern on their packaging, the photo style on their Instagram.
If the skill designs first and asks later, it competes with that mental image and loses.
If it collects first, it builds ON the image.

## When and how to run it

Run the asset call ONCE, after Round 1 intake (or immediately, if the brief already
shows an identity exists), and BEFORE strategy synthesis. It is a plain chat message,
not an `ask_user_input_v0` prompt — the tappable tool cannot receive files, and this
step is about attachments. Keep it to one short message: what to attach, in priority
order, tailored to what they've said. Then WAIT for the reply before building.

Skip it only when the person has clearly said they're starting completely from scratch
with nothing — and even then, still invite reference material (see "starting fresh"
below).

## What to ask for, in priority order

Tailor the list to their business — don't paste all of this verbatim. Ask for whatever
plausibly exists:

1. **Logo files** — every version they have. SVG/AI/EPS ideal; PNG/JPG fine; a photo of
   the sign or a business card counts if that's all there is. Explicitly invite variants:
   icon-only, horizontal, reversed/white, old versions.
2. **Symbols, motifs, devices, patterns** — anything recurring: a monogram, a graphic
   device, a border, a texture on packaging or bags, an icon set.
3. **Screenshots of what exists in the wild** — their website homepage, an Instagram
   grid, a storefront photo, packaging, signage, a menu, a brochure. Screenshots are
   underrated: they carry palette, type behavior, photography style, and layout habits
   all at once.
   **Mode B, site-based identities:** upgrade this item with the capture ladder in
   `references/web_grounding.md`. Rung 0 is Claude's job, not theirs — fetch the site
   from the URL alone (HTML, CSS tokens, @font-face names, logo SVGs, page copy) before
   asking for anything. Then ask only for what fetch couldn't see: rung 1 everyday
   screenshots with exact OS keystrokes plus pasted key copy, rung 2 the one-click
   bookmarklet (`assets/brand_capture_bookmarklet.txt`) if fetch was blocked or thin,
   rung 3 DevTools only for the comfortable or for one stubborn value. Canonical values
   collected here are what let the book match the live site in one pass.
4. **Photography or media they consider "them"** — 3-5 photos they'd be happy to see in
   the book, or a link to where their imagery lives.
5. **Fonts they own or already use** — names are enough; files only if they have a
   license that permits sharing.
6. **Prior documentation** — any old style guide, one-pager, pitch deck, or "brand
   colors" note, however informal.
7. **Reference/aspiration material** — anything from OTHER brands they're drawn to
   (label it as reference, never to copy). This is the closest available proxy for the
   picture in their head when they own little themselves.

Close the message with a pressure-release line: "Whatever you have is useful — even one
photo. And if you have nothing yet, just say 'starting fresh' and we'll build from
zero."

## What each asset changes downstream (handling table)

| Asset received | What it becomes |
|---|---|
| Logo file(s) | Canon. Embed the real file everywhere the mark appears — never redraw. Variation grid shows ONLY variants that exist; missing variants are noted as gaps to request from the original designer, not fabricated. Seed the palette from its colors. |
| Symbol/motif/pattern | A first-class section (pattern system / device chapter) built around the REAL element; often decides the cover archetype (pattern-field or contained cover per `layout_grammar.md`). |
| Site/social screenshots | Palette sampling source, typography-behavior evidence, voice evidence (real copy), imagery-direction evidence. In Mode B these are the primary excavation site. |
| Their photography | Imagery direction is written to describe what they SHOWED, not a generic style; if quality varies, say which of their photos exemplify the direction. |
| Fonts named/owned | Build the type system on those (verify license posture); open-license stand-ins only when the real face is unavailable, always disclosed. |
| Old guide/deck | Mine it for decided-once answers (tagline, values, colors) — never silently overwrite something they already committed to. |
| Reference material from other brands | Direction-setting only. Extract the qualities they respond to (contrast, warmth, density) and name those qualities back to them; never transplant another brand's system. |

Every received file goes into the asset index/manifest with filename, source ("client
supplied"), and date — supplied assets are provenance-tracked the same as generated ones.

## The confirmation echo

After receiving assets, reflect a one-paragraph read back BEFORE building: "Here's what
I'm taking from these: your green is the anchor, the bee mark is untouchable, your
photography is warm and candid, and the site's all-caps buttons are a habit worth
keeping (or breaking — your call)." This costs one message and catches mismatches at the
cheapest possible moment. It also surfaces the create-vs-codify mode question naturally:
rich assets usually mean Mode B or hybrid.

## Starting fresh

If they truly have nothing: proceed Mode A, but still offer the reference-material
invitation (item 7) — "any brand whose look or voice you admire, screenshots welcome."
People who own zero assets still carry a mental picture; reference material is how it
gets out of their head and into the brief. Never make someone with no assets feel
behind — one line, move on.
