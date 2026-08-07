# Installing Self-Improving Agent for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone self-improving-agent

```bash
git clone https://github.com/peterskoett/self-improving-agent.git ~/.agents/self-improving-agent
```

### 2. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/self-improving-agent
ln -s ~/.agents/self-improving-agent/skills/self-improving-agent ~/.agents/skills/self-improving-agent
```

### 3. Verify Installation

Restart Zerone and try asking:
- "Help me record this learning experience"
- "do you have self-improving-agent?"

If successful, Zerone will automatically recognize and invoke the Self-Improving Agent skill workflow.

## Updating

```bash
cd ~/.agents/self-improving-agent
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/self-improving-agent
```

## Getting Help

- GitHub: https://github.com/peterskoett/self-improving-agent