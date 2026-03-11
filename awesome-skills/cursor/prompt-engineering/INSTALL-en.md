# Install Prompt Engineering in Cursor

## Installation Steps

### 1. Clone repository
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create symbolic link
```bash
mkdir -p ~/.cursor/skills
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/prompt-engineering ~/.cursor/skills/prompt-engineering
```

## Verify Installation

Restart Cursor, ensure you are in **Agent** mode, and try:
- "Optimize this instruction based on prompt engineering best practices."

## Update
```bash
cd ~/.cursor/agent-use-skills && git pull
```
