# Installing Taste Skill for OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone the taste-skill repository

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.openclaw/taste-skill
```

### 2. Symlink the skills

Link all 13 sub-skill folders into OpenClaw's skills directory:

```bash
mkdir -p ~/.openclaw/skills
for skill in ~/.openclaw/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.openclaw/skills/$skill_name
  ln -s "$skill" ~/.openclaw/skills/$skill_name
done
```

### 3. Verify Installation

Restart OpenClaw, then try asking:

- "do you have taste-skill?"
- "use taste-skill to design a brutalist portfolio"

If successful, OpenClaw will automatically pick the right taste-skill sub-skill based on your brief.

## Updating

```bash
cd ~/.openclaw/taste-skill
git pull
```

## Uninstallation

```bash
for skill in ~/.openclaw/taste-skill/skills/*/; do
  rm -rf ~/.openclaw/skills/$(basename "$skill")
done
```

## Getting Help

- Report issues: https://github.com/Leonxlnx/taste-skill/issues
