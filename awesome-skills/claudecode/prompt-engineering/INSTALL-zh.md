# Prompt Engineering - Claude Code 安装指南

## 安装步骤

### 方法一：使用 Marketplace（推荐）

执行以下命令安装：

```bash
/plugin marketplace add Zerone-Agent/agent-use-skills
/plugin install prompt-engineering@agent-use-skills
```

### 方法二：手动安装

1. **克隆仓库**
   ```bash
   git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
   ```

2. **创建符号链接**
   ```bash
   mkdir -p ~/.claude/skills
   ln -s ~/.claude/agent-use-skills/awesome-skills/skills/prompt-engineering ~/.claude/skills/prompt-engineering
   ```

## 验证安装

在 Claude Code 中询问：
- "如何针对复杂逻辑优化我的提示词？"
- "帮我根据 Few-Shot 模式重写这段指令"

## 更新
```bash
cd ~/.claude/agent-use-skills && git pull
```
