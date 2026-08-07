# Installing Obsidian CLI for Zerone

## Prerequisites

- Zerone installed
- Git installed
- Obsidian Desktop v1.12.0+ installed with CLI enabled (Settings → Command line interface → Toggle ON)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/pablo-mano/Obsidian-CLI-skill.git ~/.agents/Obsidian-CLI-skill
```

### 2. Symlink the Skill

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/obsidian-cli
ln -s ~/.agents/Obsidian-CLI-skill/skills/obsidian-cli ~/.agents/skills/obsidian-cli
```

### 3. Verify Installation

Restart Zerone, then try asking:

- "Read my daily note"
- "Search my vault for meeting notes"
- "do you have obsidian-cli?"

If successful, Zerone will automatically recognize and invoke the Obsidian CLI skill.

## Updating

```bash
cd ~/.agents/Obsidian-CLI-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.agents/skills/obsidian-cli
```

## Getting Help

- GitHub: https://github.com/pablo-mano/Obsidian-CLI-skill
- Report issues: https://github.com/pablo-mano/Obsidian-CLI-skill/issues
