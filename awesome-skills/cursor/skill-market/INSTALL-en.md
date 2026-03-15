# Installing Skill Market for Cursor

## Prerequisites

- Cursor installed
- Git installed
- Ensure your Python environment can use `uv`

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git
```

### 2. Configure Skill

Place the `skill-market` directory and its contents in your project root or designated skills directory for Cursor, or simply run it from the cloned repository.

### 3. Verify Installation

Run the following command to verify the environment:

```bash
uv run agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

## Verify Connection

Try searching for a known skill to verify the connection:
```bash
uv run agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py info agent-browser
```

If the details for the skill are returned successfully, the installation is verified.

## Updating

```bash
cd agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
