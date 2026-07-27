# Installing Matt Pocock Skills for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone the mattpocock-skills repository

```bash
git clone https://github.com/mattpocock/skills.git ~/.openagent/mattpocock-skills
```

### 2. Symlink the skills

Link all skills under `engineering/` and `productivity/` into OpenAgent's skills directory:

```bash
mkdir -p ~/.openagent/skills
for category in engineering productivity; do
  for skill in ~/.openagent/mattpocock-skills/skills/$category/*/; do
    skill_name=$(basename "$skill")
    rm -rf ~/.openagent/skills/$skill_name
    ln -s "$skill" ~/.openagent/skills/$skill_name
  done
done
```

### 3. Run the one-time setup per repo

Open your project in OpenAgent and run:

```
/setup-matt-pocock-skills
```

It asks about issue tracker, triage labels, and docs location.

### 4. Verify Installation

Type `/ask-matt`, you should see all user-invoked skills.

## Updating

```bash
cd ~/.openagent/mattpocock-skills
git pull
```

## Uninstallation

```bash
for category in engineering productivity; do
  for skill in ~/.openagent/mattpocock-skills/skills/$category/*/; do
    rm -rf ~/.openagent/skills/$(basename "$skill")
  done
done
```

## Getting Help

- Report issues: https://github.com/mattpocock/skills/issues
