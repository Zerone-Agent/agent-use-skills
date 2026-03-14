# Install Multi Search Engine in Codex

## Prerequisites

- Codex installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Codex can discover the multi-search-engine skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/multi-search-engine
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/multi-search-engine ~/.codex/skills/multi-search-engine
```

### 3. Verify Installation

Restart Codex and try the following command to verify the installation:

- "Search for python tutorials using google"
- "do you have the multi-search-engine skill?"

If successful, Codex will recognize and invoke the Multi Search Engine skill workflow.

## Update

```bash
cd ~/.codex/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
