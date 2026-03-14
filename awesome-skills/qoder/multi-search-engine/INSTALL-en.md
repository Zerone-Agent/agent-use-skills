# Install Multi Search Engine in Qoder

## Prerequisites

- Qoder installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Qoder can discover the multi-search-engine skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/multi-search-engine
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/multi-search-engine ~/.qoder/skills/multi-search-engine
```

### 3. Verify Installation

Restart Qoder and try the following command to verify the installation:

- "Search for python tutorials using google"
- "do you have the multi-search-engine skill?"

If successful, Qoder will recognize and invoke the Multi Search Engine skill workflow.

## Update

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
