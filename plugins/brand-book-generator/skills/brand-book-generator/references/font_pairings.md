# Font Pairings by Vibe

Default less to "editorial serif + clean sans" — that's one vibe among many, and it's been overused as the safe default. Actually look at the tone adjectives from Step 2 and pick a pairing that matches, including bolder/blockier/weirder options when the brand calls for it. Every family below is available via `@fontsource/<slug>` on npm and is genuinely renderable in this environment (unlike Google Fonts referenced by name alone, which silently falls back to a system font — see `SKILL.md` Step 3 for why, and use `scripts/setup_fonts.py <display-slug> <body-slug>` to actually fetch and embed the files).

Pick **one display slug + one body slug** per brand. Mixing a slug from one row's display with another row's body is completely fine and often the more interesting choice — these pairings are starting points, not locked sets.

## Bold / blocky / confident
For brands that want to be loud, direct, unmissable — sports, streetwear, bold consumer products, anything that shouldn't whisper.
- **Display:** `anton` (Anton) — extremely condensed, all-caps energy, poster-like — or `archivo-black` (Archivo Black) — a true black-weight grotesk, no italics or nuance, just weight
- **Body:** `space-grotesk` (Space Grotesk) or `ibm-plex-mono` (IBM Plex Mono, for a technical/stamped feel)

## Geometric / modern-tech
For startups, tools, anything that wants to feel current and precise without being cold.
- **Display:** `unbounded` (Unbounded) — geometric with rounded, slightly maximalist details — or `syne` (Syne) — sharp, variable-width, distinctive at large sizes
- **Body:** `sora` (Sora) or `space-grotesk` (Space Grotesk)

## Editorial / elegant (when warmth or heritage actually fits)
Still worth using — just shouldn't be the automatic default. Right for brands genuinely trading on craft, history, or quiet luxury.
- **Display:** `fraunces` (Fraunces, has real personality at large sizes especially in italic) or `dm-serif-display` (DM Serif Display) or `libre-caslon-display` (Libre Caslon Display, sharper and more contemporary than a classic serif)
- **Body:** `spectral` (Spectral, a readable text serif) or a clean sans like `sora` (Sora) for serif/sans contrast

## Playful / friendly
For brands that want approachability and a little joy — kids' products, casual food/beverage, community-oriented brands.
- **Display:** `righteous` (Righteous) — rounded, casual-confident — or `fjalla-one` (Fjalla One) — condensed but friendlier than Anton
- **Body:** `sora` (Sora) or `space-grotesk` (Space Grotesk)

## Maximalist / loud / directional
For brands actively trying to stand out from a crowded, polite category — fashion-adjacent, culture brands, anything explicitly anti-corporate.
- **Display:** `big-shoulders-display` (Big Shoulders Display, tall/condensed/industrial) or `bricolage-grotesque` (Bricolage Grotesque, an irregular, hand-adjusted grotesk with real character)
- **Body:** `ibm-plex-mono` (IBM Plex Mono) for a technical/directional pairing, or `sora` (Sora) to calm it down slightly

## Choosing

Ask: if this brand were a person raising their voice, would it be a shout, a confident statement, a warm aside, or a wink? Match the display font to that, not to "what brand books usually look like." The body font's job is to stay legible at small sizes — it can be plainer than the display font without the system feeling boring, since the display face is doing the personality work.

If the person gave you a color/style instinct in intake (Round 4), let it inform this too — saturated, high-contrast colors tend to pair with bolder/blockier display type; muted, low-contrast palettes tend to pair with the editorial or geometric options. This isn't a hard rule, just a sanity check against picking a shouty font with a whispering palette or vice versa unless that tension is intentional.
