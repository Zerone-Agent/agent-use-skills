# Installing Deep Research for Zerone

## Prerequisites

- Zerone installed
- Git installed
- Python and pip installed
- Google AI API Key (for Gemini Deep Research)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/deep-research
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/deep-research ~/.agents/skills/deep-research
```

### 3. Configure API Key

Set the Google AI API Key environment variable:

```bash
export GOOGLE_AI_API_KEY="your-api-key-here"
```

### 4. Verify Installation

Restart Zerone and try asking:
- "Research the current state of AI programming assistants market"
- "do you have deep-research?"

If successful, Zerone will automatically recognize and invoke the Deep Research skill workflow.

## Updating

```bash
cd ~/.agents/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/deep-research
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues