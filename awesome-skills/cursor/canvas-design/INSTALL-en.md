# Install Canvas Design in Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Cursor can discover the canvas-design skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/canvas-design
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/canvas-design ~/.cursor/skills/canvas-design
```

### 3. Verify Installation

Restart Cursor and ensure you are in **Agent** mode, then try asking:

- "Create an artwork based on [theme]"
- "do you have canvas-design skill?"

If successful, Cursor Agent will recognize and invoke the Canvas Design skill.

## Update

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
