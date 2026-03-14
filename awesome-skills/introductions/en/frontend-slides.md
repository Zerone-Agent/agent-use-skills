# Frontend Slides

**Frontend Slides** is a Claude Code skill for creating stunning, animation-rich HTML presentations — from scratch or by converting PowerPoint files. It helps non-designers create beautiful web presentations without knowing CSS or JavaScript.

## Tags

Design & Creative | Verified

## Core Philosophy
- **You Don't Need to Be a Designer**: Just react to what you see — the skill handles the design work for you.
- **Zero Dependencies = Freedom**: Generated single HTML files have no framework dependencies and will work in 10 years.
- **Generic Is Forgettable**: Every presentation should feel custom-crafted, not template-generated.
- **Comments Are Kindness**: Code should explain itself to future-you (or anyone else who opens it).

## Key Features & Workflow

1. **Zero Dependencies**: Presentations are single HTML files with inline CSS/JS. No npm, no build tools, no frameworks.
2. **Visual Style Discovery**: Can't articulate design preferences? No problem. The skill generates visual previews and lets you pick what you like.
3. **PPT Conversion**: Convert existing PowerPoint files to web, preserving all images and content.
4. **Anti-AI-Slop**: Curated distinctive styles that avoid generic AI aesthetics (bye-bye, purple gradients on white).
5. **Production Quality**: Accessible, responsive, well-commented code you can customize.

## Creating a New Presentation

1. The skill asks about your content (slides, messages, images)
2. Asks about the feeling you want (impressed? excited? calm?)
3. Generates 3 visual style previews for you to compare
4. Creates the full presentation in your chosen style
5. Opens it in your browser

## Included Styles

### Dark Themes
- **Bold Signal** — Confident, high-impact, vibrant card on dark
- **Electric Studio** — Clean, professional, split-panel
- **Creative Voltage** — Energetic, retro-modern, electric blue + neon
- **Dark Botanical** — Elegant, sophisticated, warm accents

### Light Themes
- **Notebook Tabs** — Editorial, organized, paper with colorful tabs
- **Pastel Geometry** — Friendly, approachable, vertical pills
- **Split Pastel** — Playful, modern, two-color vertical split
- **Vintage Editorial** — Witty, personality-driven, geometric shapes

### Specialty
- **Neon Cyber** — Futuristic, particle backgrounds, neon glow
- **Terminal Green** — Developer-focused, hacker aesthetic
- **Swiss Modern** — Minimal, Bauhaus-inspired, geometric
- **Paper & Ink** — Literary, drop caps, pull quotes

## Architecture

Frontend Slides uses a progressive disclosure architecture — the main SKILL.md is a concise map (~180 lines), with supporting files loaded on-demand only when needed:

- `SKILL.md` — Core navigation file
- `STYLE_PRESETS.md` — Style preset definitions
- `viewport-base.css` — Viewport base styles
- `html-template.md` — HTML template
- `animation-patterns.md` — Animation patterns
- `scripts/extract-pptx.py` — PPT extraction script

## Installation & Support

Frontend Slides supports the following AI editors and platforms:
- [Claude Code](../../claudecode/frontend-slides/INSTALL-en.md)

---
For more information, visit: [GitHub - zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides)
