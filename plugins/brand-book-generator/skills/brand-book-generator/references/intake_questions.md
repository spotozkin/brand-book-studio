# Intake Question Bank

Use these with `ask_user_input_v0` when the brief is thin. Don't dump all of these at once — run 2-4 short rounds (1-3 questions per round), letting earlier answers shape later questions and skipping anything already answered or inferable. Adapt the literal wording to the person's actual business rather than reading these verbatim.

The goal isn't to collect data for its own sake — every question here exists because it changes a concrete decision later (palette, tone, structure, depth). If a question wouldn't change what you build, skip it.

## Round 1 — Business basics (almost always needed first)

- What does the business/practice/project actually do, in one sentence?
- What stage is it at? (options: "Brand new / pre-launch", "Established but never formally branded", "Rebranding something that already exists", "Personal brand for an individual")
- Is there an existing logo or visual identity to build around, or starting fresh? (options: "Existing logo to build around", "Some scattered assets, no real system", "Starting completely from scratch")
- Anything else already made that should be reused rather than reinvented — a tagline, a mission statement, website copy, photography, a name you're set on, social handles? This doesn't fit multiple-choice well, so just ask it as a plain open question in chat rather than through `ask_user_input_v0`. Whatever they hand you here becomes the seed for that section instead of something generated from scratch — don't quietly overwrite a tagline they already like just because you could write a different one.

## Round 2 — Audience and positioning

- Who is this primarily for? (give 3-4 concrete audience options specific to their business, not generic ones — e.g. for a veterinary clinic: "Existing pet owners", "New clients researching online", "Referring clinics", "Media/press")
- What's the main thing that should make someone choose this over the obvious alternative? (options: "Expertise/credibility", "Price/accessibility", "Experience/feel", "Speed/convenience", "Not sure yet — help me figure it out")
- If "not sure yet" is picked, that's a signal to spend more time in the strategy synthesis step rather than rushing to visuals — flag it back to the user rather than guessing.

## Round 3 — Voice and tone

- Pick the 2-3 words that should describe how this brand sounds (offer a curated list relevant to their category, e.g. for a medical practice: "Warm & reassuring", "Expert & precise", "Approachable & plain-spoken", "Premium & polished"; for a startup: "Confident & direct", "Playful & energetic", "Calm & technical", "Bold & contrarian")
- Any brand they admire, in any category, for how it sounds or looks? (free response is fine here, this one doesn't fit multiple choice well — just ask in plain chat if needed)

## Round 4 — Visual preference and scope

- Any color or style instinct already, or fully open? (options: "I have specific colors/style in mind", "I have a rough direction (e.g. 'modern and clean' or 'warm and tactile')", "Fully open to recommendation")
- How much do you want in the final brand book? (options: "Just the essentials — logo system, colors, type, voice", "A solid launch set — essentials plus templates for social/web/print", "A full mature system — everything plus sub-brand and governance rules") — map this to the tiers in `references/asset_inventory.md`

## Notes on style

- Keep each question's options mutually exclusive and genuinely different — not "warm" vs "very warm."
- Where the category is known (medical practice, retail, nonprofit, tech startup), customize the options to that category rather than using generic placeholders — it reads as far more credible and saves a follow-up round.
- If someone answers "not sure" or "help me decide" to a strategic question, don't just pick for them silently — say what you're leaning toward and why, briefly, so they can correct course.
