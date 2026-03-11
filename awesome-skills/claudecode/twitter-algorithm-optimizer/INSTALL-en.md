# Twitter Algorithm Optimizer - Claude Code Installation Guide

## Installation Steps

### Method 1: Via Plugin Marketplace (Recommended)

Once the skill is synced to the marketplace, run:

```bash
/plugin marketplace add Zerone-Agent/agent-use-skills
/plugin install twitter-algorithm-optimizer@agent-use-skills
```

### Method 2: Manual Setup

1. **Clone repository**
   ```bash
   git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
   ```

2. **Create symbolic link**
   ```bash
   mkdir -p ~/.claude/skills
   ln -s ~/.claude/agent-use-skills/awesome-skills/skills/twitter-algorithm-optimizer ~/.claude/skills/twitter-algorithm-optimizer
   ```

## Verify Installation

In a Claude Code chat, try:
```
Analyze the algorithmic ranking potential of this tweet draft: [Your tweet]
```

## Update Method
```bash
cd ~/.claude/agent-use-skills && git pull
```

## Detailed Documentation
- [GitHub Repository](https://github.com/Zerone-Agent/agent-use-skills)
