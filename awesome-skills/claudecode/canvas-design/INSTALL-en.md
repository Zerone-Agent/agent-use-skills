# Install Canvas Design in Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Claude Code can discover the canvas-design skill (including its font library):

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/canvas-design
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/canvas-design ~/.claude/skills/canvas-design
```

### 3. Verify Installation

Restart Claude Code and try the following command:

- "Create a poster based on [a theme]"
- "do you have canvas-design skill?"

If successful, Claude Code will recognize and invoke the Canvas Design workflow, starting with the creation of a design philosophy.

## Update

```bash
cd ~/.claude/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
