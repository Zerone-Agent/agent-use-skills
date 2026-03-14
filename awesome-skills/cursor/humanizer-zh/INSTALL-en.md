# Install Humanizer-zh in Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Cursor can discover the humanizer-zh skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/humanizer-zh
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/humanizer-zh ~/.cursor/skills/humanizer-zh
```

### 3. Verify Installation

Restart Cursor and ensure you are in **Agent** mode, then try asking:

- "Use humanizer-zh skill to optimize this text"
- "do you have humanizer-zh skill?"

If successful, Cursor Agent will automatically recognize and invoke the Humanizer-zh skill workflow.

## Update

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
