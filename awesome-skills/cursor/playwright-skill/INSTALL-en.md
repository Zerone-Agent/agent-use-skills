# Install Playwright Skill in Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed
- Node.js installed (v18+ recommended)

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Cursor can discover the playwright-skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/playwright-skill
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/playwright-skill ~/.cursor/skills/playwright-skill
```

### 3. Initialize Skill Environment

Playwright requires browser drivers and dependencies. Please run the setup command in the skill directory:

```bash
cd ~/.cursor/skills/playwright-skill
npm run setup
```

### 4. Verify Installation

Restart Cursor and ensure you are in **Agent** mode, then try asking:

- "Take a full-page screenshot of http://localhost:3000"
- "do you have playwright-skill?"

If successful, Cursor Agent will recognize and invoke the Playwright Skill workflow.

## Update

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
