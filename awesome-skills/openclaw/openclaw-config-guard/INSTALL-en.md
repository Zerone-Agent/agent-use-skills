# Install OpenClaw Config Guard in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed and available in `PATH`
- Python 3 installed
- Git installed

## Installation Steps

### 1. Clone the skill library

Clone the repository to your local machine if you have not already done so:

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create the skill symlink

Link the skill source directory so OpenClaw can discover and load it:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/openclaw-config-guard
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/openclaw-config-guard ~/.openclaw/skills/openclaw-config-guard
```

### 3. Confirm the helper script is available

This skill ships with a Python helper script and official reference list. Verify the files are present:

```bash
ls ~/.openclaw/skills/openclaw-config-guard
ls ~/.openclaw/skills/openclaw-config-guard/scripts
ls ~/.openclaw/skills/openclaw-config-guard/references
```

## Verify Installation

Restart OpenClaw and try prompts such as:

- "Audit my OpenClaw config before making any changes."
- "Check whether my `openclaw.json` has startup blockers and only fix documented issues."
- "Use `openclaw-config-guard` to back up, validate, and summarize my OpenClaw config."

If installation is successful, OpenClaw should discover the skill and use the workflow defined in `SKILL.md`.

## Update

Update the skill library when you want the latest version:

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Get Help

- Skill issues: https://github.com/Zerone-Agent/agent-use-skills/issues
- OpenClaw documentation: https://docs.openclaw.ai/
