# Install Skill Market (Claude Code)

This guide describes how to install and verify the **Skill Market** skill in Claude Code.

## Installation Steps

1. **Environmental Preparation**:
   This skill relies on `uv` for Python environment management. Ensure `uv` is installed on your system.

2. **Add Skill Files**:
   Place the `skill-market` directory and its contents in your project root or designated skills directory.
   Ensure `awesome-skills/skills/skill-market/scripts/market.py` has execution permissions.

3. **Run Initial Check**:
   Run the following command in Claude Code to verify the environment:
   ```bash
   uv run awesome-skills/skills/skill-market/scripts/market.py list
   ```

## Verify Installation

Try searching for a known skill to verify the connection:
```bash
uv run awesome-skills/skills/skill-market/scripts/market.py info imagen
```
If the details for the `imagen` skill are returned successfully, the installation is verified.

## Update Method

Simply pull the latest code from the `agent-use-skills` repository:
```bash
git pull origin main
```

---
Reference: [Zerone Agent SDK](https://github.com/zerone-agent/agent-use-skills)
