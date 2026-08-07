# Installation Guide Template (External Repository)

For skills from external GitHub repositories.

## Template

```markdown
# Installing <Skill Name> for <Platform>

## Prerequisites

- [<Platform>](<platform-url>) installed
- Git installed

## Installation Steps

### 1. Clone <skill-repo>

```bash
git clone https://github.com/<org>/<skill-repo>.git ~/.<platform>/<skill-repo>
```

### 2. Symlink Skills

Create symlinks so <Platform> discovers the skills:

```bash
mkdir -p ~/.<platform>/skills
for skill in $(ls ~/.<platform>/<skill-repo>/skills); do
  rm -rf ~/.<platform>/skills/$skill
  ln -s ~/.<platform>/<skill-repo>/skills/$skill ~/.<platform>/skills/$skill
done
```

### 3. Verify Installation

Restart <Platform>, then try asking:
- "do you have <skill-name>?"

If successful, <Platform> will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.<platform>/<skill-repo>
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.<platform>/<skill-repo>/skills); do
  rm -rf ~/.<platform>/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/<org>/<skill-repo>
- Report issues: https://github.com/<org>/<skill-repo>/issues
```

## Platform-specific Paths

| Platform    | Skills Directory          | Clone Directory                    |
|-------------|---------------------------|-------------------------------------|
| Claude Code | `~/.claude/skills/`       | `~/.claude/`                        |
| Cursor      | `~/.cursor/skills/`       | `~/.cursor/`                        |
| Codex       | `~/.codex/skills/`        | `~/.codex/`                         |
| OpenCode    | `~/.config/opencode/skills/` | `~/.config/opencode/`           |
| OpenClaw    | `~/.openclaw/skills/`     | `~/.openclaw/`                      |
| Zerone   | `~/.agents/skills/`    | `~/.agents/`                     |
| Qoder       | `~/.qoder/skills/`        | `~/.qoder/`                         |
```