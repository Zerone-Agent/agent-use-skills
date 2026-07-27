# Installing Taste Skill for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone the taste-skill repository

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.config/opencode/taste-skill
```

### 2. Symlink the skills

Link all 13 sub-skill folders into OpenCode's skills directory:

```bash
mkdir -p ~/.config/opencode/skills
for skill in ~/.config/opencode/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.config/opencode/skills/$skill_name
  ln -s "$skill" ~/.config/opencode/skills/$skill_name
done
```

### 3. Verify Installation

Restart OpenCode, then try asking:

- "do you have taste-skill?"
- "use taste-skill to redesign an existing project"

If successful, OpenCode will automatically pick the right taste-skill sub-skill based on your brief.

## Updating

```bash
cd ~/.config/opencode/taste-skill
git pull
```

## Uninstallation

```bash
for skill in ~/.config/opencode/taste-skill/skills/*/; do
  rm -rf ~/.config/opencode/skills/$(basename "$skill")
done
```

## Getting Help

- Report issues: https://github.com/Leonxlnx/taste-skill/issues
