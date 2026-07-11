# Preset systems — contrast-checked starting points

Two complete, original example systems (all ratios below measured with `scripts/check_contrast.py` logic; verify again after any mutation). Use a preset ONLY as a seed when the person asks for a fast start or their brief maps cleanly onto the archetype — then mutate it (hues, mark, copy) so no two clients ship the same book. Never present a preset as a bespoke design without saying it started from a template system.

---

## Preset 1: "Warm Expert" — personal expert / coach / wellness-forward brand

```css
:root {
  /* Surfaces */
  --bg-page:      #FBF3EC;  /* cream — page background */
  --surface-1:    #F2DCC8;  /* sand — hero / primary surface */
  --surface-card: #FFFFFF;

  /* Brand hierarchy */
  --primary:      #C4562E;  /* terracotta — carries the brand: buttons, nav, stats, featured cards.
                               4.1:1 on cream — large text & UI only; use --interactive for body-size text */
  --interactive:  #96401F;  /* darker sibling — hover, CTAs, eyebrow labels, small text (6.3:1 on cream) */

  /* Text */
  --ink:          #2E1F1A;  /* all body text — 14.4:1 on cream, 11.9:1 on sand, 15.8:1 on white */
  --text-muted:   #7D6459;  /* secondary text — 5.0:1 on cream */

  /* Constrained accent family (appears in exactly 3 named places) */
  --accent-deep:  #1F4E4A;  /* deep teal — cream text on it hits 8.5:1, white 9.3:1 */
  --accent-soft:  #6FA29A;  /* soft teal — only on dark accent surfaces */
  --accent-earth: #C89B6D;  /* ochre — mark/motif detail only */
}
```
**Type pairing idea:** a display serif with a featured italic accent style + a humanist sans for body/UI (see `font_pairings.md` for renderable options by vibe).
**Mark recipe:** stacked-block or badge motif (3–4 basic shapes), each shape a named palette color; mark doubles as a repeating strip pattern (state a minimum repeat count and a banned background).
**Voice frame skeleton:** warm/direct · evidence-based · plainspoken · specific · inclusive — fill say/not-this pairs from the client's actual domain.
**Structure to preserve when mutating:** one loud primary + one darker interactive sibling that handles small text + one accent limited to named locations + a warm near-black ink. The hues are fully swappable (coral, ochre, plum, moss all work); the *hierarchy* is the preset.

---

## Preset 2: "Quiet Authority" — established clinical / professional-services practice

```css
:root {
  /* Closed 5-color system — the book should state: "if a color isn't here, it isn't a brand color" */
  --ink-navy: #26303B;  /* THE brand color: logo, all text, buttons, dark heroes */
  --stone:    #DDD6C9;  /* text & motifs on navy, icon fills, section panels */
  --paper:    #F2EFE9;  /* page background, nav, cards, light fills */
  --slate:    #7C8289;  /* DECORATIVE ONLY — fails AA for normal text (3.4:1 on paper) */
  --white:    #FFFFFF;  /* headlines over photography, clean cards */
}
/* Approved text pairings (measured): navy/white 13.4:1 · navy/paper 11.7:1 ·
   navy/stone 9.3:1 · stone/navy 9.3:1. These four ONLY. */
```
**Type system idea:** a single neutral grotesque family for every role, with wide uppercase letterspacing as the typographic signature (display ~+14–16% tracking, eyebrows +20%+), echoing a letterspaced wordmark.
**Motif recipe:** one geometric mark drawn from the brand's name or logo, used as scattered low-opacity (12–25%) watermark clusters — asymmetric, varied sizes, some cropping off-edge, never over faces or body text, never a uniform grid.
**Voice frame skeleton:** expert · warm · confident · natural, each with sounds-like/not pairs. Calm CTAs; hard ban on urgency spam.
**Structure to preserve when mutating:** one dark authority color doing all text + two paper neutrals + one decorative-only mid-tone + white, with the closed-set rule stated in prose. The dark can move toward espresso, charcoal, or deep green; the neutrals shift warm or cool with it.

---

## When to reach for which

| Signal in brief | Preset |
|---|---|
| Individual expert, mission-driven, wants warmth/personality, anti-corporate | Warm Expert |
| Established practice/firm, premium positioning, "sophisticated not intimidating," photography-led | Quiet Authority |
| Neither fits | Build from scratch per Step 3 — presets are accelerants, not defaults |
