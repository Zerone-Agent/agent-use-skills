# Installing Content Research Writer for Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Cursor discovers the content-research-writer skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/content-research-writer
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/content-research-writer ~/.cursor/skills/content-research-writer
```

### 3. Verify Installation

Restart Cursor and ensure you are in **Agent** mode. Then try asking:

- "Help me create an outline for an article about [topic]"
- "do you have content-research-writer?"

If successful, the Cursor Agent will automatically recognize and invoke the Content Research Writer workflow.

## Updating

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
