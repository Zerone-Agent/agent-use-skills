# Taste Skill

**Taste Skill** is an anti-slop frontend design skill pack for AI agents. It stops AI from shipping boring, generic, templated interfaces and pushes it toward frontend code and reference imagery with real design intent.

## Tags

🎨 Design & Creativity | ✅ Verified

## Core Philosophy

- **Anti "AI slop"**: Strong anti-repetition rules suppress the usual centered stacks, default purple gradients, and template layouts, giving the UI genuine design intent.
- **Design intent first**: Rules target intent (layout, typography, motion, spacing) rather than any framework API, so they work across React / Vue / Svelte.
- **Single responsibility, compose on demand**: Each sub-skill does one job; the Agent loads only the one matching the brief by install name, keeping context lean.
- **Tunable design language**: The headline skill exposes three 1-10 dials — DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY — to slide output from "conservative and clean" to "asymmetric and modern".
- **Image-first**: Beyond code-producing skills, the pack includes image-generation skills that pair with ChatGPT Images or Codex image mode to produce reference frames before the coding agent implements them.

## Key Features & Workflow

1. **Install once, unlock everything**: `git clone + symlink` links all 13 sub-skill folders into the platform's skills directory; the Agent loads the right one based on the brief.
2. **Three operating modes**:
   - **Implementation skills**: output frontend code directly (taste-skill, gpt-taste, soft-skill, etc.).
   - **Image-generation skills**: output reference imagery only (imagegen-frontend-web, imagegen-frontend-mobile, brandkit).
   - **Image-to-code skills**: generate references, analyze them, then implement (image-to-code-skill).
3. **Tunable dials** (taste-skill only): DESIGN_VARIANCE (layout experimentation), MOTION_INTENSITY (animation depth), VISUAL_DENSITY (info per viewport), 1-10.
4. **v1 / v2 dual tracks**: v2 (experimental) is the default, adding brief inference, design-system mapping, hard em-dash ban, canonical GSAP skeletons, redesign-audit protocol, and a strict pre-flight check. v1 is preserved for users who depend on the original behavior.
5. **Cross-platform**: Built on the portable SKILL.md instruction file, all major coding agents (Claude Code, Cursor, Codex, OpenCode, OpenClaw, Zerone, Qoder) can load it.

## Skills Library Overview

- **Headline skills** (cover ~90% of use cases):
  - `design-taste-frontend` (taste-skill, 🆕 v2 experimental, **default pick**): read brief → infer design language → tune dials → ship code.
  - `design-taste-frontend-v1` (taste-skill-v1): the original v1, use only when you depend on its exact behavior.
  - `gpt-taste` (gpt-tasteskill): stricter GPT/Codex-oriented variant with higher layout variance and stronger GSAP guidance.
- **Scenario extensions**:
  - `image-to-code` (image-to-code-skill): full image → analyze → code pipeline.
  - `redesign-existing-projects` (redesign-skill): audit UI first, then fix layout, spacing, hierarchy.
- **Stylistic add-ons**: `high-end-visual-design` (soft, premium), `minimalist-ui` (Notion/Linear vibe), `industrial-brutalist-ui` (Swiss type, hard contrast), `stitch-design-taste` (Google Stitch compatible).
- **Engineering guardrail**: `full-output-enforcement` (stops the model from shipping half-finished code).
- **Image-generation skills**: `imagegen-frontend-web` (hero/landing/multi-section), `imagegen-frontend-mobile` (iOS/Android screens and flows), `brandkit` (logo directions, palettes, type, brand applications).

## Installation & Support

Taste Skill supports the following AI editors and platforms:
- [Claude Code](../../claudecode/taste-skill/INSTALL-en.md)
- [Cursor](../../cursor/taste-skill/INSTALL-en.md)
- [Codex](../../codex/taste-skill/INSTALL-en.md)
- [OpenCode](../../opencode/taste-skill/INSTALL-en.md)
- [OpenClaw](../../openclaw/taste-skill/INSTALL-en.md)
- [Zerone](../../zerone/taste-skill/INSTALL-en.md)
- [Qoder](../../qoder/taste-skill/INSTALL-en.md)

---
For more information, visit: [GitHub - Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
