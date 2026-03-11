# Install Proactive Agent Skill in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills repository

Clone the skills library to your local machine (if not already done):

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Configure Skill in OpenClaw

Create a symbolic link so OpenClaw can find and use the skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/proactive-agent
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/proactive-agent ~/.openclaw/skills/proactive-agent
```

### 3. Initialize Workspace Assets

Proactive Agent requires some core Markdown files to maintain memory and identity. Run the following command:

```bash
# Copy template assets to your OpenClaw workspace
cp -r ~/.openclaw/skills/proactive-agent/assets/*.md ~/.openclaw/workspace/
```

## Verify Installation

Restart OpenClaw. It should detect `ONBOARDING.md` and may start the onboarding process. You can try asking:

- "Start onboarding"
- "do you have proactive-agent skill?"

## Core Recommendations

To get the most out of this skill:
1. **Follow the WAL Protocol**: When you provide corrections, ensure the Agent updates `SESSION-STATE.md`.
2. **Review Buffer Periodicallly**: The Agent manages `working-buffer.md` automatically, but you can check it manually during critical task handovers.

## Update

```bash
cd ~/.openclaw/agent-use-skills && git pull
```

## Get Help

- Skill issues: https://github.com/Zerone-Agent/agent-use-skills/issues
- Reference: [Hal Stack 🦞](https://github.com/halthelobster/hal-stack)
