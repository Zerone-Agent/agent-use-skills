# Install Multi Search Engine in Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Cursor can discover the multi-search-engine skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/multi-search-engine
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/multi-search-engine ~/.cursor/skills/multi-search-engine
```

### 3. Verify Installation

Restart Cursor and ensure you are in **Agent** mode. Then try asking:

- "Search for python tutorials using google"
- "do you have the multi-search-engine skill?"

If successful, Cursor Agent will recognize and invoke the Multi Search Engine skill workflow.

## Update

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
