# Install Humanizer-zh in Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Qoder can discover the humanizer-zh skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/humanizer-zh
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/humanizer-zh ~/.qoder/skills/humanizer-zh
```

### 3. Verify Installation

Restart Qoder and try asking:

- "Use humanizer-zh skill to optimize this text"
- "do you have humanizer-zh skill?"

If successful, Qoder will automatically recognize and invoke the Humanizer-zh skill workflow.

## Update

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
