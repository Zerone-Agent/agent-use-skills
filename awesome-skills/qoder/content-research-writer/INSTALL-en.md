# Installing Content Research Writer for Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Qoder discovers the content-research-writer skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/content-research-writer
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/content-research-writer ~/.qoder/skills/content-research-writer
```

### 3. Verify Installation

Restart Qoder, then try asking:

- "Help me create an outline for an article about [topic]"
- "do you have content-research-writer?"

If successful, Qoder will automatically recognize and invoke the Content Research Writer workflow.

## Updating

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
