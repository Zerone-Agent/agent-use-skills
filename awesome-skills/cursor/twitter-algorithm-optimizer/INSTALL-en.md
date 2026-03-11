# Install Twitter Algorithm Optimizer in Cursor

## Installation Steps

### 1. Clone repository
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create symbolic link
```bash
mkdir -p ~/.cursor/skills
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/twitter-algorithm-optimizer ~/.cursor/skills/twitter-algorithm-optimizer
```

## Verify Installation

Restart Cursor, ensure you are in **Agent** mode, and try:
- "Optimize my tweet based on Twitter algorithm: [Content]"

## Update
```bash
cd ~/.cursor/agent-use-skills && git pull
```
