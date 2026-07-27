# Installing Matt Pocock Skills for OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone the mattpocock-skills repository

```bash
git clone https://github.com/mattpocock/skills.git ~/.openclaw/mattpocock-skills
```

### 2. Symlink the skills

Link all skills under `engineering/` and `productivity/` into OpenClaw's skills directory:

```bash
mkdir -p ~/.openclaw/skills
for category in engineering productivity; do
  for skill in ~/.openclaw/mattpocock-skills/skills/$category/*/; do
    skill_name=$(basename "$skill")
    rm -rf ~/.openclaw/skills/$skill_name
    ln -s "$skill" ~/.openclaw/skills/$skill_name
  done
done
```

### 3. Run the one-time setup per repo

Open your project in OpenClaw and run:

```
/setup-matt-pocock-skills
```

It asks about issue tracker, triage labels, and docs location.

### 4. Verify Installation

Type `/ask-matt`, you should see all user-invoked skills.

## Updating

```bash
cd ~/.openclaw/mattpocock-skills
git pull
```

## Uninstallation

```bash
for category in engineering productivity; do
  for skill in ~/.openclaw/mattpocock-skills/skills/$category/*/; do
    rm -rf ~/.openclaw/skills/$(basename "$skill")
  done
done
```

## Getting Help

- Report issues: https://github.com/mattpocock/skills/issues
