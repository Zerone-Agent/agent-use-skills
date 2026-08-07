# Installing Content Research Writer for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/content-research-writer
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/content-research-writer ~/.agents/skills/content-research-writer
```

### 3. Verify Installation

Restart Zerone and try asking:
- "Help me write a blog post about AI development"
- "do you have content-research-writer?"

If successful, Zerone will automatically recognize and invoke the Content Research Writer skill workflow.

## Updating

```bash
cd ~/.agents/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/content-research-writer
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues