# Huashu Design

**Huashu Design** is an HTML-native AI design skill that lets AI agents produce deliverable high-fidelity designs from a single prompt — interactive prototypes, presentation slides, timeline animations, and infographics, all built with HTML and exportable to MP4/GIF/PPTX/PDF.

## Tags

🎨 Design & Creativity | ✅ Verified

## Core Philosophy

- **Start from existing design context**: Ask for design systems, UI kits, and brand assets before creating. When a specific brand is involved, enforce a 5-step "Core Asset Protocol" (Ask → Search → Download → Verify → Solidify spec) to ensure brand recognizability.
- **Junior Designer workflow**: Write assumptions + placeholders + reasoning upfront, show early to the user for confirmation. Fixing misunderstandings early costs 100x less than fixing them late.
- **Anti AI slop**: Avoid the visual "lowest common denominator" of AI output — purple gradients, emoji icons, rounded cards with left border accent. Use `text-wrap: pretty`, CSS Grid, oklch colors, and carefully chosen serif display fonts instead.
- **Design Direction Advisor (Fallback)**: When requirements are vague, recommend 3 differentiated directions from 5 genres × 20 design philosophies, generate parallel visual demos for the user to choose from.
- **Fact verification before assumptions**: When specific products or technologies are mentioned, the first action is WebSearch to verify existence and status — never assert facts from training data alone.

## Key Features & Workflow

1. **Interactive Prototypes (App / Web)**: Single-file HTML, pixel-accurate iPhone 15 Pro bezel, state-driven multi-screen navigation, Playwright automated click testing. Typical time: 10–15 min.
2. **Presentation Slides**: HTML deck (browser-based presenting) + editable PPTX (preserved text boxes, double-click to edit). Typical time: 15–25 min.
3. **Timeline Animations**: Stage + Sprite time-slice model, 25fps/60fps MP4 + palette-optimized GIF + 6 scene-based BGM tracks + 37 pre-built SFX. Typical time: 8–12 min.
4. **Design Variants**: 3+ side-by-side comparisons, real-time Tweaks (color/typography/density), localStorage persistence.
5. **Infographics / Visualizations**: CSS Grid precise columns, magazine-grade typography, exportable to PDF/PNG/SVG.
6. **Design Direction Advisor**: 5 genres × 20 design philosophies (Information Architecture / Kinetic Poetry / Minimalism / Experimental Avant-garde / Eastern Philosophy), 3 differentiated directions + 24 pre-built showcases.
7. **5-Dimension Expert Review**: Philosophical consistency / Visual hierarchy / Detail execution / Functionality / Innovation, each scored 0–10, radar chart visualization, outputs Keep / Fix / Quick Wins checklist.

## Skills Library Overview

- **Starter Components**: Slide engine (deck_stage.js), animation engine (animations.jsx), device frames (ios_frame.jsx / android_frame.jsx / macos_window.jsx / browser_window.jsx), variant canvas (design_canvas.jsx)
- **Design Philosophy Library**: 20 design philosophies spanning Pentagram information architecture, Field.io kinetic poetry, Kenya Hara Eastern minimalism, Sagmeister experimental avant-garde, and more
- **Export Toolchain**: render-video.js (HTML → MP4), convert-formats.sh (60fps interpolation + GIF), add-music.sh (BGM), export_deck_pdf.mjs / export_deck_pptx.mjs (PDF/PPTX)
- **Brand Asset Protocol**: 5-step hard flow (Ask → Search official channels → Download assets → Verify & extract → Solidify into brand-spec.md), with Logo/Product images/UI screenshots as first-class assets
- **Reference Materials**: animation-pitfalls.md, design-styles.md, slide-decks.md, editable-pptx.md, critique-guide.md, video-export.md, audio-design-rules.md, and more

## Installation & Support

Huashu Design supports the following AI editors and platforms:

- [Claude Code](../../claudecode/huashu-design/INSTALL-en.md)
- [Cursor](../../cursor/huashu-design/INSTALL-en.md)
- [Codex](../../codex/huashu-design/INSTALL-en.md)
- [OpenCode](../../opencode/huashu-design/INSTALL-en.md)
- [OpenClaw](../../openclaw/huashu-design/INSTALL-en.md)
- [Zerone](../../zerone/huashu-design/INSTALL-en.md)
- [Qoder](../../qoder/huashu-design/INSTALL-en.md)

---
For more information, visit: [GitHub - alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)
