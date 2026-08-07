# Installing WeWrite for Zerone

## Prerequisites

- Zerone installed
- Git installed
- Node.js and npm installed

## Installation Steps

### 1. Clone wewrite

```bash
git clone https://github.com/oaker-io/wewrite.git ~/.agents/wewrite
```

### 2. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/wewrite
ln -s ~/.agents/wewrite/skills/wewrite ~/.agents/skills/wewrite
```

### 3. Install Dependencies (Optional)

For full functionality, install dependencies:

```bash
cd ~/.agents/wewrite
npm install
pip install -r requirements.txt  # Python script dependencies
```

### 4. Verify Installation

Restart Zerone and try asking:
- "Help me write a WeChat article"
- "do you have wewrite?"

If successful, Zerone will automatically recognize and invoke the WeWrite skill workflow.

## Updating

```bash
cd ~/.agents/wewrite
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/wewrite
```

## Getting Help

- GitHub: https://github.com/oaker-io/wewrite