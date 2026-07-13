# Building the Mark (SVG Techniques)

**If the person already has a logo file (SVG, PNG, or JPG), use it instead of anything below** — embed it directly with a normal `<img src="...">` in place of the `{{MARK_SVG*}}` placeholders. See the "existing logo" note in `SKILL.md` Step 3 for how to handle variation-grid limitations when they only have one color version. Everything in this file is for when no existing mark exists and one needs to be built from scratch.

The brand book should ship with an actual rendered mark, not just a written spec — a real, if simple, geometric identity that a person could screenshot and use as a placeholder icon today. This is achievable in inline SVG using basic shapes (rects, circles, ellipses, simple paths); it is not the same as generating illustrative/photographic artwork, which is out of reach. Two reliable patterns below — pick whichever fits the brand, or invent a similar one from the same primitives (rects, circles, ellipses, simple polygons). Always use literal hex values in the SVG fills, not CSS `var()` — more reliable across renderers.

You need to produce **four sizes/variants** to fill the template placeholders:
- `{{MARK_SVG}}` — large, ~72px tall, used in the mark showcase next to the wordmark
- `{{MARK_SVG_SMALL}}` / `{{MARK_SVG_SMALL_ON_DARK}}` — ~44px, used in the logo variation grid (the `_ON_DARK` version should swap any dark/low-contrast fills for lighter ones so it reads on a dark or saturated background)
- `{{MARK_SVG_ICON_ONLY}}` — same as small, used standalone on white
- `{{MARK_SVG_TINY}}` — ~26px, used repeated in the pattern strip (keep this one simple — it'll repeat 8 times)

## Pattern 1: Monogram badge (safe default, always works)

A rounded-square badge in the primary color, with the brand's first initial in the display typeface, centered. Works for literally any brand — use this when no clearer motif suggests itself, or when the person hasn't given you enough to infer one.

```html
<svg width="72" height="72" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
  <rect width="72" height="72" rx="14" fill="#1B3A2F"/>
  <text x="36" y="48" font-family="Fraunces, Georgia, serif" font-size="34"
        font-weight="700" fill="#FFFFFF" text-anchor="middle">H</text>
</svg>
```

For the tiny pattern-strip version, drop the text (too small to read cleanly) and just use the badge shape, optionally with a small accent dot in the corner:

```html
<svg width="26" height="26" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
  <rect width="72" height="72" rx="14" fill="#1B3A2F"/>
  <circle cx="56" cy="16" r="8" fill="#C9A24B"/>
</svg>
```

## Pattern 2: Motif block-stack (customized, more distinctive)

Build a small, ownable icon from 2-4 simple stacked/overlapping shapes that echo something concrete about the brand — a flame for a candle brand, a wave for a coastal/wellness brand, a mountain for an outdoor brand, a leaf for a botanical one. Keep it to basic shapes; don't attempt detailed illustration or bezier-heavy paths.

Example — a simple candle/flame mark (two ellipses for the flame, a rounded rect for the body):

```html
<svg width="60" height="88" viewBox="0 0 60 88" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="54" width="20" height="30" rx="3" fill="#4B5842"/>
  <ellipse cx="30" cy="40" rx="11" ry="15" fill="#B5502F"/>
  <ellipse cx="30" cy="29" rx="5" ry="8" fill="#F2E9DC"/>
</svg>
```

Example — a simple mountain/peak mark (two overlapping triangles as polygons):

```html
<svg width="72" height="60" viewBox="0 0 72 60" xmlns="http://www.w3.org/2000/svg">
  <polygon points="10,55 34,10 58,55" fill="#31604E"/>
  <polygon points="34,55 50,22 66,55" fill="#79A98E"/>
</svg>
```

When you build a motif mark, always also produce a matching monogram-badge fallback in the spec text (not necessarily rendered) — some applications (favicons at very small sizes, single-color embroidery, etc.) need the simpler fallback, and the brand book's misuse/clear-space notes should mention this.

## Rules that apply to either pattern

- Never use more than 3-4 colors in the mark itself, and pull them straight from the documented palette — don't introduce a new color just for the logo.
- Test the `_ON_DARK` variant actually reads clearly — if a shape's fill is close in value to the dark background, swap it for a lighter palette color or white before finalizing.
- Keep `viewBox` proportions consistent across all four sizes of the same mark (just change the `width`/`height` attributes, not the internal coordinates) so it's recognizably the same mark at every size.
