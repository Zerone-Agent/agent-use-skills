# Installing multi-search-engine for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenCode's native skill tool discovers multi-search-engine skills:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/multi-search-engine
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/multi-search-engine ~/.config/opencode/skills/multi-search-engine
```

### 3. Restart OpenCode

Restart OpenCode. The plugin will automatically inject multi-search-engine context.

Verify by asking: "do you have multi-search-engine?"

## Updating

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
