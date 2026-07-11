# Brand Book Studio

Turn any business, practice, or personal brand into a **complete, print-ready PDF brand book** — plus a machine-readable **AI Brand Kit** file that keeps every future AI-generated asset (social posts, ads, emails) unmistakably on-brand.

Built and battle-tested on real client engagements. Two modes, diagnosed automatically:

- **Create** — no identity exists yet: strategy → voice → a real rendered geometric mark → full color/type system → applications → PDF.
- **Codify** — the brand already exists (a live website, real logo files) but is undocumented: the skill *extracts* the system into staff-and-vendor-ready guidelines without inventing anything.

Every engagement also ships a `[brand]-BRAND.md` guardrails file: hand it to Claude (or any AI) and ask for "an Instagram ad for our 10% off sale" — it comes back in the right hex codes, the right voice, with the required compliance language, every time.

## Install

**Claude Code (plugin):**
```
/plugin marketplace add spotozkin/brand-book-studio
/plugin install brand-book-generator@brand-book-studio
```

**Claude.ai / Claude Desktop (skill upload):**
1. Download `brand-book-generator.zip` from this repo's [Releases](../../releases).
2. In Claude: Settings → Capabilities → Skills → Upload skill (requires Pro/Max/Team/Enterprise with code execution enabled).
3. Start a chat: *"Build me a brand book for my pottery studio."*

## What's inside

```
plugins/brand-book-generator/skills/brand-book-generator/
├── SKILL.md                        # the full workflow, both modes
├── assets/
│   ├── brand_book_template.html    # CSS-variable-driven PDF template
│   └── brand_kit_template.md       # the AI Brand Kit guardrails template
├── references/
│   ├── worked_examples.md          # two illustrative case studies (create vs codify)
│   ├── preset_systems.md           # two contrast-checked example systems
│   ├── intake_questions.md · asset_inventory.md · mark_techniques.md
│   ├── font_pairings.md · pdf_brand_book_structure.md
│   └── accessibility_and_legal.md
└── scripts/
    ├── setup_fonts.py              # embeds real Google Fonts via @fontsource
    └── check_contrast.py           # WCAG contrast checker
```

## Example prompts

- "Build a brand book for my new coffee cart, we're called Ember & Oak"
- "Here are screenshots of our firm's website — document our brand for the staff"
- "Make me the AI brand kit file too so my social manager's ChatGPT stays on-brand"

## License

MIT — see [LICENSE](LICENSE).
