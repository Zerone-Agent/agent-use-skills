# Installing Taste Skill for Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed

## Installation Steps

### 1. Clone the taste-skill repository

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.cursor/taste-skill
```

### 2. Symlink the skills

Link all 13 sub-skill folders into Cursor's skills directory:

```bash
mkdir -p ~/.cursor/skills
for skill in ~/.cursor/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.cursor/skills/$skill_name
  ln -s "$skill" ~/.cursor/skills/$skill_name
done
```

### 3. Verify Installation

Restart Cursor and switch to **Agent** mode, then try asking:

- "do you have taste-skill?"
- "use taste-skill to design a minimalist landing page"

If successful, Cursor Agent will automatically pick the right taste-skill sub-skill based on your brief.

## Updating

```bash
cd ~/.cursor/taste-skill
git pull
```

## Uninstallation

```bash
for skill in ~/.cursor/taste-skill/skills/*/; do
  rm -rf ~/.cursor/skills/$(basename "$skill")
done
```

## Getting Help

- Report issues: https://github.com/Leonxlnx/taste-skill/issues
