# Installing Matt Pocock Skills for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone the mattpocock-skills repository

```bash
git clone https://github.com/mattpocock/skills.git ~/.config/opencode/mattpocock-skills
```

### 2. Symlink the skills

Link all skills under `engineering/` and `productivity/` into OpenCode's skills directory:

```bash
mkdir -p ~/.config/opencode/skills
for category in engineering productivity; do
  for skill in ~/.config/opencode/mattpocock-skills/skills/$category/*/; do
    skill_name=$(basename "$skill")
    rm -rf ~/.config/opencode/skills/$skill_name
    ln -s "$skill" ~/.config/opencode/skills/$skill_name
  done
done
```

### 3. Run the one-time setup per repo

Open your project in OpenCode and run:

```
/setup-matt-pocock-skills
```

It asks about issue tracker, triage labels, and docs location.

### 4. Verify Installation

Type `/ask-matt`, you should see all user-invoked skills.

## Updating

```bash
cd ~/.config/opencode/mattpocock-skills
git pull
```

## Uninstallation

```bash
for category in engineering productivity; do
  for skill in ~/.config/opencode/mattpocock-skills/skills/$category/*/; do
    rm -rf ~/.config/opencode/skills/$(basename "$skill")
  done
done
```

## Getting Help

- Report issues: https://github.com/mattpocock/skills/issues
