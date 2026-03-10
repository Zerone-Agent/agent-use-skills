# Installing Content Research Writer for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Claude Code discovers the content-research-writer skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/content-research-writer
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/content-research-writer ~/.claude/skills/content-research-writer
```

### 3. Verify Installation

Restart Claude Code, then try asking the following to verify the installation:

- "Help me create an outline for an article about [topic]"
- "do you have content-research-writer?"

If successful, Claude Code will automatically recognize and invoke the Content Research Writer workflow.

## Updating

```bash
cd ~/.claude/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
