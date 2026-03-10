# Install Canvas Design in Codex

## Prerequisites

- [Codex](https://openai.com/index/codex/) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. Create a symbolic link

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/canvas-design
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/canvas-design ~/.codex/skills/canvas-design
```

### 3. Verify Installation

Restart Codex and try asking:

- "Design a minimalist poster"
- "do you have canvas-design skill?"

## Update

```bash
cd ~/.codex/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
