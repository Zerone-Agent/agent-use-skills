# Install Humanizer-zh in Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Claude Code can discover the humanizer-zh skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/humanizer-zh
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/humanizer-zh ~/.claude/skills/humanizer-zh
```

### 3. Verify Installation

Restart Claude Code and try the following command to verify the installation:

- "Use humanizer-zh skill to optimize this text"
- "do you have humanizer-zh skill?"

If successful, Claude Code will automatically recognize and invoke the Humanizer-zh skill workflow.

## Update

```bash
cd ~/.claude/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
