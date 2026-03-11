# Prompt Engineering - Claude Code Installation Guide

## Installation Steps

### Method 1: Via Marketplace (Recommended)

Run the following commands:

```bash
/plugin marketplace add Zerone-Agent/agent-use-skills
/plugin install prompt-engineering@agent-use-skills
```

### Method 2: Manual Setup

1. **Clone repository**
   ```bash
   git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
   ```

2. **Create symbolic link**
   ```bash
   mkdir -p ~/.claude/skills
   ln -s ~/.claude/agent-use-skills/awesome-skills/skills/prompt-engineering ~/.claude/skills/prompt-engineering
   ```

## Verify Installation

Ask Claude Code:
- "How can I optimize my prompt for complex logic?"
- "Rewrite this instruction using the Few-Shot pattern."

## Update
```bash
cd ~/.claude/agent-use-skills && git pull
```
