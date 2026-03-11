# 在 OpenCode 中安装 Prompt Engineering

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. 创建符号链接
```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/prompt-engineering ~/.config/opencode/skills/prompt-engineering
```

## 验证安装

重启 OpenCode，尝试提问：
- "如何在这个技能中使用说服原则？"

## 更新
```bash
cd ~/.config/opencode/agent-use-skills && git pull
```
