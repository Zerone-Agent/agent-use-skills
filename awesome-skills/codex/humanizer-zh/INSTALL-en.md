# Install Humanizer-zh in Codex

## Prerequisites

- [Codex](https://openai.com/index/codex/) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Codex can discover the humanizer-zh skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/humanizer-zh
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/humanizer-zh ~/.codex/skills/humanizer-zh
```

### 3. Verify Installation

Restart Codex and try asking:

- "Use humanizer-zh skill to optimize this text"
- "do you have humanizer-zh skill?"

If successful, Codex will automatically recognize and invoke the Humanizer-zh skill workflow.

## Update

```bash
cd ~/.codex/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
