# Install Multi Search Engine in Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Claude Code can discover the multi-search-engine skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/multi-search-engine
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/multi-search-engine ~/.claude/skills/multi-search-engine
```

### 3. Verify Installation

Restart Claude Code and try the following command to verify the installation:

- "Search for python tutorials using google"
- "do you have the multi-search-engine skill?"

If successful, Claude Code will recognize and invoke the Multi Search Engine skill workflow.

## Update

```bash
cd ~/.claude/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
