# Guizang PPT Skill

**Guizang PPT Skill** is an AI-agent skill for generating single-file HTML horizontal-swipe presentation decks, slide visuals, and social cover pages, featuring two visual systems: editorial magazine and Swiss International Typographic Style.

## Tags

🎨 Design & Creativity | ✅ Verified

## Core Philosophy
- **Agent-Native**: HTML/CSS plain-text format that agents can read, edit, and validate directly — no build tools required.
- **Dual Visual Systems**: Style A (editorial magazine × electronic ink, serif + fluid backgrounds) for narrative storytelling; Style B (Swiss International, sans-serif + grid + high-saturation anchor color) for facts and data.
- **Structured Workflow**: From a 7-question clarification checklist to template copying, content filling, and self-validation, every step is clearly guided.
- **Aesthetic Constraints**: Theme colors are limited to curated presets only (5 for Style A / 4 for Style B) — custom hex values are not allowed, ensuring consistent output quality.

## Key Features & Workflow
1. **Dual-Style Templates**: Style A offers 10 layouts; Style B provides 22 locked layouts covering covers, dividers, big-number pages, image/text combos, timelines, comparisons, KPI towers, and more.
2. **Theme Presets**: Style A ships 5 electronic-ink themes (Ink Classic / Indigo Porcelain / Forest Ink / Kraft Paper / Dune); Style B offers 4 Swiss anchor colors (International Klein Blue / Lemon Yellow / Lemon Green / Safety Orange).
3. **Optional Image Generation**: In Codex, supports generating documentary photos, infographics, flow diagrams, system maps, and UI scenes via GPT-Image 2.0 / GPT-M 2.0.
4. **Multi-Platform Covers**: Generate WeChat 21:9 covers, 1:1 share cards, Xiaohongshu 3:4 covers, and video thumbnails from the same content.
5. **Swiss Layout Validation**: Built-in `validate-swiss-deck.mjs` script checks layout compliance, image slot placement, SVG text traps, and title alignment.
6. **Low-Power Mode**: Press `B` to toggle static mode, disabling WebGL/Canvas animations for low-end devices.

## Skills Library Overview
- **Template Assets**: Style A template (`template.html`), Style B template (`template-swiss.html`), bundled screenshot-background assets.
- **Reference Docs**: Component catalog, 10 layout skeletons, 22 locked Swiss layouts, theme presets, image prompts, screenshot framing guide, quality checklist.
- **Validation Scripts**: Swiss layout validator (`validate-swiss-deck.mjs`).

## Installation & Support
Guizang PPT Skill supports the following AI editors and platforms:
- [Claude Code](../../claudecode/guizang-ppt-skill/INSTALL-en.md)
- [Cursor](../../cursor/guizang-ppt-skill/INSTALL-en.md)
- [Codex](../../codex/guizang-ppt-skill/INSTALL-en.md)
- [OpenCode](../../opencode/guizang-ppt-skill/INSTALL-en.md)
- [OpenClaw](../../openclaw/guizang-ppt-skill/INSTALL-en.md)
- [Zerone](../../zerone/guizang-ppt-skill/INSTALL-en.md)
- [Qoder](../../qoder/guizang-ppt-skill/INSTALL-en.md)

---
For more information, visit: [GitHub - op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)
