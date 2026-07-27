# Installing Taste Skill for Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
- Git installed

## Installation Steps

### 1. Clone the taste-skill repository

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.qoder/taste-skill
```

### 2. Symlink the skills

Link all 13 sub-skill folders into Qoder's skills directory:

```bash
mkdir -p ~/.qoder/skills
for skill in ~/.qoder/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.qoder/skills/$skill_name
  ln -s "$skill" ~/.qoder/skills/$skill_name
done
```

### 3. Verify Installation

Restart Qoder, then try asking:

- "do you have taste-skill?"
- "use taste-skill to design a Notion-style minimalist product page"

If successful, Qoder will automatically pick the right taste-skill sub-skill based on your brief.

## Updating

```bash
cd ~/.qoder/taste-skill
git pull
```

## Uninstallation

```bash
for skill in ~/.qoder/taste-skill/skills/*/; do
  rm -rf ~/.qoder/skills/$(basename "$skill")
done
```

## Getting Help

- Report issues: https://github.com/Leonxlnx/taste-skill/issues
