# Install Playwright Skill in Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed
- Node.js installed (v18+ recommended)

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Claude Code can discover the playwright-skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/playwright-skill
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/playwright-skill ~/.claude/skills/playwright-skill
```

### 3. Initialize Skill Environment

Playwright requires browser drivers and dependencies. Please run the setup command in the skill directory:

```bash
cd ~/.claude/skills/playwright-skill
npm run setup
```

### 4. Verify Installation

Restart Claude Code and try the following command to verify the installation:

- "Take a full-page screenshot of http://localhost:3000"
- "do you have playwright-skill?"

If successful, Claude Code will recognize and invoke the Playwright Skill workflow.

## Update

```bash
cd ~/.claude/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
