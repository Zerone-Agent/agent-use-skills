# Install Playwright Skill in Codex

## Prerequisites

- [Codex](https://openai.com/index/codex/) installed
- Git installed
- Node.js installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. Create a symbolic link

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/playwright-skill
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/playwright-skill ~/.codex/skills/playwright-skill
```

### 3. Initialize Environment

```bash
cd ~/.codex/skills/playwright-skill
npm run setup
```

### 4. Verify Installation

Restart Codex and try asking:

- "Take a full-page screenshot of http://localhost:3000"
- "do you have playwright-skill?"

## Update

```bash
cd ~/.codex/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
