# Installing Content Research Writer for Codex

## Prerequisites

- [Codex](https://openai.com/index/codex/) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Codex discovers the content-research-writer skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/content-research-writer
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/content-research-writer ~/.codex/skills/content-research-writer
```

### 3. Verify Installation

Restart Codex, then try asking:

- "Help me create an outline for an article about [topic]"
- "do you have content-research-writer?"

If successful, Codex will automatically recognize and invoke the Content Research Writer workflow.

## Updating

```bash
cd ~/.codex/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
