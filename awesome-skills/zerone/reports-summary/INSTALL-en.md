# Installing Reports Summary for Zerone

## Prerequisites

- Zerone installed
- Git installed
- Python and pip installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/reports-summary
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/reports-summary ~/.agents/skills/reports-summary
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart Zerone and try asking:
- "Help me summarize these weekly reports"
- "do you have reports-summary?"

If successful, Zerone will automatically recognize and invoke the Reports Summary skill workflow.

## Updating

```bash
cd ~/.agents/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/reports-summary
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues