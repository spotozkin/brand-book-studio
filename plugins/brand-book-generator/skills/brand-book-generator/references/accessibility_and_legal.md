# Accessibility and Legal Notes

This skill should make brands more usable and more defensible, not less. None of this is legal advice — the goal is to flag the right things and track provenance, not to assert certainty the skill doesn't have.

## Color contrast (WCAG 2.2)

Always check the brand's primary text/background color pairings before finalizing the palette:

- Normal text against its background: minimum **4.5:1** contrast ratio
- Large text (roughly 18pt+/14pt bold+) against its background: minimum **3:1**
- Required non-text UI elements and graphics (icons, form borders, chart elements) against adjacent colors: minimum **3:1**

Use `scripts/check_contrast.py` on every primary text/background pairing rather than eyeballing it — saturated brand colors frequently fail contrast against white or against each other even when they look fine on screen. If a brand color fails contrast for text use, don't silently substitute a different color — note it explicitly: "your primary accent works great for backgrounds/graphics but doesn't meet text contrast minimums on white; here's a darker variant for text use, with the original reserved for accents and large elements."

Also avoid recommending "images of text" (text baked into a graphic) where real, selectable text would work — it's worse for both accessibility and on-brand consistency across updates.

## Typography licensing

Default to open-license families (Google Fonts and similar) unless the person says they already have commercial font licenses. State this choice explicitly rather than silently picking a font — something like "I'm recommending [font], which is free for commercial use including logos; if you already have a licensed font family you'd rather use, let me know and I'll build around that instead."

Don't package or redistribute font binary files unless you've confirmed the specific license permits it. Recording the font name and source is enough for the brand book; actual font files are a separate concern from document generation.

## AI-generated and AI-assisted imagery

If any imagery in the brand book (moodboard references, concept visuals) was AI-generated or AI-assisted rather than licensed/owned photography, note that in the asset index. Don't imply that AI-generated visual concepts carry the same ownership certainty as commissioned or licensed photography — copyrightability of AI-assisted work varies by jurisdiction and by how much human creative editing went into the final piece. The practical move is just to track provenance (what's AI-assisted, what's licensed stock, what's owned/original) so the person can make an informed call later, not to resolve the legal question yourself.

## Trademark and naming

This skill doesn't perform trademark clearance searches. If a brand name, tagline, or wordmark seems like it could collide with an existing mark in the same category, it's worth a one-line mention ("you may want to have this name checked for trademark conflicts before committing to it widely") rather than silence — but don't claim to have cleared it. If web search is available in the session, a quick search for `"[name]" trademark` or the desired domain/handle can surface an obvious conflict worth flagging — but frame it explicitly as a spot-check, not a clearance search, since a real one needs an attorney or a proper search service and this is just a sanity check.

## What goes in the asset index

For every non-trivial asset in the final package (fonts, any AI-assisted imagery, any stock photography), record: what it is, where it came from, what license applies, and when it was added. A few lines of a table is enough — the point is traceability, not bureaucracy.
