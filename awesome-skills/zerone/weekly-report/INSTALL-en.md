# Installing Weekly Report for Zerone

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
rm -rf ~/.agents/skills/weekly-report
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/weekly-report ~/.agents/skills/weekly-report
```

### 3. Install Python Dependencies

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. Verify Installation

Restart Zerone and try asking:
- "Help me generate this week's weekly report"
- "do you have weekly-report?"

If successful, Zerone will automatically recognize and invoke the Weekly Report skill workflow.

## Updating

```bash
cd ~/.agents/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/weekly-report
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues