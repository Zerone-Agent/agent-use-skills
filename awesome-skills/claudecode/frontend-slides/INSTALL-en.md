# Installing Frontend Slides for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed
- (For PPT conversion) Python 3 with `python-pptx` library

## Installation Steps

### Option 1: Direct Clone (Recommended)

Clone the Frontend Slides repository directly into your Claude Code skills directory:

```bash
git clone https://github.com/zarazhangrui/frontend-slides.git ~/.claude/skills/frontend-slides
```

### Option 2: Manual Copy

```bash
# Create the skill directory
mkdir -p ~/.claude/skills/frontend-slides/scripts

# Clone to a temporary directory
git clone https://github.com/zarazhangrui/frontend-slides.git /tmp/frontend-slides

# Copy core files
cp /tmp/frontend-slides/SKILL.md ~/.claude/skills/frontend-slides/
cp /tmp/frontend-slides/STYLE_PRESETS.md ~/.claude/skills/frontend-slides/
cp /tmp/frontend-slides/viewport-base.css ~/.claude/skills/frontend-slides/
cp /tmp/frontend-slides/html-template.md ~/.claude/skills/frontend-slides/
cp /tmp/frontend-slides/animation-patterns.md ~/.claude/skills/frontend-slides/
cp /tmp/frontend-slides/scripts/extract-pptx.py ~/.claude/skills/frontend-slides/scripts/

# Clean up
rm -rf /tmp/frontend-slides
```

### Install PPT Conversion Dependency (Optional)

If you need to convert PowerPoint files to web presentations, install `python-pptx`:

```bash
pip install python-pptx
```

## Verify Installation

Restart Claude Code, then verify the installation by typing:

```
/frontend-slides
```

Or try asking directly:

- "I want to create a pitch deck for my AI startup"
- "Convert my presentation.pptx to a web slideshow"

If successful, Claude Code will automatically recognize and invoke the Frontend Slides workflow, guiding you through style selection and presentation creation.

## Updating

```bash
cd ~/.claude/skills/frontend-slides
git pull
```

## Getting Help

- Report issues: https://github.com/zarazhangrui/frontend-slides/issues
