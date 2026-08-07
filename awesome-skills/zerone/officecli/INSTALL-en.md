# Installing OfficeCLI for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Install OfficeCLI Binary

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```

### 2. Clone OfficeCLI Repository

```bash
git clone https://github.com/iOfficeAI/OfficeCLI.git ~/.agents/officecli
```

### 3. Symlink Skills

Create symlinks so Zerone discovers all OfficeCLI skills:

```bash
mkdir -p ~/.agents/skills
for skill in $(ls ~/.agents/officecli/skills); do
  rm -rf ~/.agents/skills/$skill
  ln -s ~/.agents/officecli/skills/$skill ~/.agents/skills/$skill
done
```

This installs all 11 skills: `officecli`, `officecli-docx`, `officecli-pptx`, `officecli-xlsx`, `officecli-academic-paper`, `officecli-pitch-deck`, `officecli-data-dashboard`, `officecli-financial-model`, `officecli-word-form`, `morph-ppt`, `morph-ppt-3d`.

### 4. Verify Installation

Restart Zerone, then try asking:
- "do you have officecli?"
- "create a PowerPoint presentation"

If successful, Zerone will automatically recognize and invoke the OfficeCLI skill.

## Updating

```bash
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
cd ~/.agents/officecli
git pull
```

OfficeCLI checks for binary updates automatically. Disable with `officecli config autoUpdate false`.

## Uninstallation

```bash
for skill in $(ls ~/.agents/officecli/skills); do
  rm -rf ~/.agents/skills/$skill
done
rm -rf ~/.agents/officecli
```

## Getting Help

- GitHub: https://github.com/iOfficeAI/OfficeCLI
- Report issues: https://github.com/iOfficeAI/OfficeCLI/issues
