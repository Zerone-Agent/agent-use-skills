# Installation Guide Template (Internal Repository)

For skills from the agent-use-skills repository.

## Template

```markdown
# Installing <Skill Name> for <Platform>

## Prerequisites

- [<Platform>](<platform-url>) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.<platform>/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so <Platform> discovers the skill:

```bash
mkdir -p ~/.<platform>/skills
rm -rf ~/.<platform>/skills/<skill-name>
ln -s ~/.<platform>/agent-use-skills/awesome-skills/skills/<skill-name> ~/.<platform>/skills/<skill-name>
```

### 3. Verify Installation

Restart <Platform>, then try asking:
- "do you have <skill-name>?"

## Updating

```bash
cd ~/.<platform>/agent-use-skills
git pull
```

## Uninstallation

```bash
rm -rf ~/.<platform>/skills/<skill-name>
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
```

## Platform-specific Paths

| Platform    | Skills Directory          | Clone Directory                    |
|-------------|---------------------------|-------------------------------------|
| Claude Code | `~/.claude/skills/`       | `~/.claude/agent-use-skills/`      |
| Cursor      | `~/.cursor/skills/`       | `~/.cursor/agent-use-skills/`      |
| Codex       | `~/.codex/skills/`        | `~/.codex/agent-use-skills/`       |
| OpenCode    | `~/.config/opencode/skills/` | `~/.config/opencode/agent-use-skills/` |
| OpenClaw    | `~/.openclaw/skills/`     | `~/.openclaw/agent-use-skills/`    |
| Zerone   | `~/.agents/skills/`    | `~/.agents/agent-use-skills/`   |
| Qoder       | `~/.qoder/skills/`        | `~/.qoder/agent-use-skills/`       |
```