# Installing Matt Pocock Skills for Codex

## Prerequisites

- [Codex](https://openai.com/codex) installed
- Git installed

## Installation Steps

### 1. Clone the mattpocock-skills repository

```bash
git clone https://github.com/mattpocock/skills.git ~/.codex/mattpocock-skills
```

### 2. Symlink the skills

Link all skills under `engineering/` and `productivity/` into Codex's skills directory:

```bash
mkdir -p ~/.codex/skills
for category in engineering productivity; do
  for skill in ~/.codex/mattpocock-skills/skills/$category/*/; do
    skill_name=$(basename "$skill")
    rm -rf ~/.codex/skills/$skill_name
    ln -s "$skill" ~/.codex/skills/$skill_name
  done
done
```

### 3. Run the one-time setup per repo

Open your project in a Codex session and run:

```
/setup-matt-pocock-skills
```

It asks about issue tracker, triage labels, and docs location.

### 4. Verify Installation

Open `/skills` or type `$ask-matt`, you should see all user-invoked skills.

## Updating

```bash
cd ~/.codex/mattpocock-skills
git pull
```

## Uninstallation

```bash
for category in engineering productivity; do
  for skill in ~/.codex/mattpocock-skills/skills/$category/*/; do
    rm -rf ~/.codex/skills/$(basename "$skill")
  done
done
```

## Getting Help

- Report issues: https://github.com/mattpocock/skills/issues
