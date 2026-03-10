# Installing Content Research Writer for OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenClaw discovers the content-research-writer skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/content-research-writer
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/content-research-writer ~/.openclaw/skills/content-research-writer
```

### 3. Verify Installation

Restart OpenClaw, then try asking:

- "Help me create an outline for an article about [topic]"
- "do you have content-research-writer?"

If successful, OpenClaw will automatically recognize and invoke the Content Research Writer workflow.

## Updating

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
