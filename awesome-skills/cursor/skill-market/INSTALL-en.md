# Install Skill Market (Cursor)

This guide describes how to configure and use the **Skill Market** skill in Cursor.

## Installation Steps

1. **Environmental Dependencies**:
   Ensure `uv` (recommended) or `python 3.10+` is installed on your system.

2. **Configure Skill**:
   You can run the market scripts directly in the Cursor terminal. To use it in Agent mode, ensure the path to `scripts/market.py` is correct.

3. **Test Connection**:
   Open Cursor terminal and run:
   ```bash
   uv run awesome-skills/skills/skill-market/scripts/market.py list
   ```

## Verify Installation

Query skill details:
```bash
uv run awesome-skills/skills/skill-market/scripts/market.py info agent-browser
```

---
Reference: [Zerone Agent SDK](https://github.com/zerone-agent/agent-use-skills)
