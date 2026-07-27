# Installing Taste Skill for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone the taste-skill repository

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.claude/taste-skill
```

### 2. Symlink the skills

Link all 13 sub-skill folders into Claude Code's skills directory:

```bash
mkdir -p ~/.claude/skills
for skill in ~/.claude/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.claude/skills/$skill_name
  ln -s "$skill" ~/.claude/skills/$skill_name
done
```

### 3. Verify Installation

Restart Claude Code, then try asking:

- "do you have taste-skill?"
- "use taste-skill to design a minimalist landing page"

If successful, Claude Code will automatically pick the right taste-skill sub-skill based on your brief.

## Updating

```bash
cd ~/.claude/taste-skill
git pull
```

## Uninstallation

```bash
for skill in ~/.claude/taste-skill/skills/*/; do
  rm -rf ~/.claude/skills/$(basename "$skill")
done
```

## Getting Help

- Report issues: https://github.com/Leonxlnx/taste-skill/issues
