# Huashu Design - Zerone Installation Guide

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.agents/huashu-design
```

### 2. Create Symlink

```bash
mkdir -p ~/.agents/skills
ln -sf ~/.agents/huashu-design ~/.agents/skills/huashu-design
```

### 3. Verify Installation

Restart Zerone, then try:

```
Do a 5-dimension expert review on this design
```

If the skill is loaded correctly, the AI will automatically recognize and invoke the Huashu Design workflow.

## Updating

```bash
cd ~/.agents/huashu-design && git pull
```

## Uninstallation

```bash
rm ~/.agents/skills/huashu-design
```

## Getting Help

- GitHub Repository: https://github.com/alchaincyf/huashu-design
- Report Issues: https://github.com/alchaincyf/huashu-design/issues
