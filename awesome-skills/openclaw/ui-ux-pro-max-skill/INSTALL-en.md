# UI UX Pro Max - OpenClaw Installation Guide

## Installation Steps

### Using CLI Tool

1. **Install CLI globally**

```bash
npm install -g uipro-cli
```

2. **Initialize your project**

```bash
cd /path/to/your/project
uipro init --ai openclaw
```

## Verify Installation

After installation, try the following conversation in OpenClaw:

```
Build a landing page for my SaaS product
```

If the skill is loaded correctly, the AI will automatically generate a design system and begin implementing the UI.

## Usage

### Skill Mode (Auto-activate)

Simply describe your UI/UX task in conversation, and the skill will activate automatically:

```
Build a landing page for my SaaS product
Create a dark mode dashboard
Design a mobile app UI for e-commerce
```

### Advanced: Persist Design System

Generate and save design system to files:

```bash
python3 .openclaw/skills/ui-ux-pro-max/scripts/search.py "SaaS dashboard" --design-system --persist -p "MyApp"
```

This creates a `design-system/` folder structure:
- `MASTER.md` - Global design system (colors, typography, spacing, components)
- `pages/` - Page-specific override rules

## Update Method

```bash
npm update -g uipro-cli
uipro init --ai openclaw
```

## Detailed Documentation

- [GitHub Repository](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [Official Website](https://uupm.cc)
