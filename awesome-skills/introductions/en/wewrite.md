# WeWrite

**WeWrite** is an all-in-one AI writing assistant for WeChat Official Accounts, from hot topic discovery to draft box publishing, completed with a single sentence.

## Tags

🗂️ Documents & Office | 🔍 Pending Verification

## Core Philosophy

- **Full-Process Automation**: Trigger an 8-step complete workflow with one sentence, zero manual intervention from topic selection to publishing
- **Real Information Anchoring**: WebSearch collects real data/quotes/cases, prohibits fabrication, traceable source materials
- **Human-AI Collaboration Enhancement**: AI draft + 2-3 editing anchor points, add personal insights in 3-5 minutes, transforming articles from "AI-generated" to "your work"
- **Style Flywheel Learning**: Import exemplars to build a style library, automatically learn after each edit, increasingly mimicking your writing style
- **Degradation Tolerance Design**: Each step has a fallback plan, process continues even with missing configurations

## Core Capabilities & Workflow

### 1. Hot Topic Discovery & Topic Scoring
- **Multi-Platform Hotspots**: Weibo + Toutiao + Baidu real-time trending topics, Python script scraping
- **SEO Quantitative Scoring**: Baidu + 360 search keyword popularity analysis
- **Intelligent Topic Selection**: Generate 10 topics × 3-dimensional scoring, historical deduplication to avoid repetition

### 2. Framework Generation & Material Collection
- **7 Writing Frameworks**: Pain point, Story, List, Comparison, Hot take, Pure opinion, Retrospective
- **Real Material Collection**: WebSearch automatically collects 5-8 real materials (named sources + specific data/quotes/cases)
- **Content Enhancement Strategy**: Auto-match by framework type—angle discovery/density boost/detail anchoring/real feel

### 3. Intelligent Writing & Style Injection
- **Dimension Randomization**: 2-3 expression dimensions randomly activated (narrative perspective/timeline/analogy domain/emotional tone/rhythm)
- **5 Writing Personas**: midnight-friend (extremely conversational), warm-editor (warm narrative), industry-observer (neutral analysis), sharp-journalist (sharp concise), cold-analyst (calm restrained)
- **Exemplar Style Library**: Import published articles, automatically inject your style fingerprints (sentence length rhythm, emotional expression, transition patterns)
- **Editing Anchor Points**: Mark key locations with "add your own words here"

### 4. SEO Optimization & Quality Validation
- **SEO Strategy**: 3 alternate titles + summary (≤40 chars) + 5 tags + keyword density optimization
- **Writing Quality Check**: Sentence length variance, vocabulary temperature, paragraph rhythm, emotional polarity, forbidden words, real anchoring, specificity
- **Content Quality Check**: Enhancement penetration, opening hook, golden sentence density, operational density, angle sharpness, scene immersion, authentic voices

### 5. Visual AI & Layout Engine
- **AI Image Generation**: Cover 3 creative prompts + 3-6 in-article images, 9 providers with automatic fallback
- **16+ Layout Themes**: professional-clean, tech-modern, warm-editorial, sspai, github, etc.
- **WeChat Compatibility Fix**: CJK-Latin auto-spacing, bold punctuation repositioning, external link footnotes, dark mode adaptation
- **Container Syntax**: `:::dialogue`, `:::timeline`, `:::callout`, `:::quote` for complex layouts
- **Draft Box Publishing**: Direct push to WeChat Official Account draft box, or local HTML preview

### 6. Effect Review & Style Learning
- **Data Backfill**: WeChat data analysis API backfills reading data, statistics on which framework/strategy performs best
- **Learning Flywheel**: After each edit, say "learn my changes", automatically extract modification patterns into playbook
- **Layout Learning**: Extract layout themes from any WeChat article URL
- **Article Collection**: Extract article body from WeChat URL to Markdown, import into exemplar library

## Skills Library Overview

### Core Scripts
- **Data Collection**: `fetch_hotspots.py` (multi-platform hotspots), `seo_keywords.py` (SEO analysis), `fetch_stats.py` (WeChat data backfill)
- **Style Learning**: `extract_exemplar.py` (exemplar style extraction), `learn_edits.py` (learn modifications), `learn_theme.py` (learn layout)
- **Quality Check**: `humanness_score.py` (11-item quality detection)
- **Toolkit**: `build_playbook.py` (generate Playbook), `diagnose.py` (configuration check)

### Layout Tools
- **CLI Tool**: `toolkit/cli.py` (preview/publish/gallery/themes/image-post)
- **Theme Engine**: 16+ YAML themes, dark mode supported
- **WeChat API**: `publisher.py`, `wechat_api.py` (draft box publishing, image upload)
- **Image Generation**: `image_gen.py` (9 providers, automatic fallback)

### Reference Documentation
- **Writing Guidelines**: `writing-guide.md`, `frameworks.md`, `content-enhance.md`
- **SEO Rules**: `seo-rules.md`, `topic-selection.md`
- **Visual Guidelines**: `visual-prompts.md`
- **WeChat Constraints**: `wechat-constraints.md`
- **Process Docs**: `onboard.md`, `learn-edits.md`, `effect-review.md`

## Installation & Support

WeWrite supports the following AI editors and platforms:

- [Claude Code](../../claudecode/wewrite/INSTALL-en.md)
- [Cursor](../../cursor/wewrite/INSTALL-en.md)
- [Codex](../../codex/wewrite/INSTALL-en.md)
- [OpenCode](../../opencode/wewrite/INSTALL-en.md)
- [OpenClaw](../../openclaw/wewrite/INSTALL-en.md)
- [Zerone](../../zerone/wewrite/INSTALL-en.md)
- [Qoder](../../qoder/wewrite/INSTALL-en.md)

---
For more information, visit: [GitHub - oaker-io/wewrite](https://github.com/oaker-io/wewrite)
