# Twitter Algorithm Optimizer - Claude Code 安装指南

## 安装步骤

### 方法一：使用 Marketplace（推荐）

目前该技能正在同步至官方应用市场。同步完成后，您可以执行：

```bash
/plugin marketplace add Zerone-Agent/agent-use-skills
/plugin install twitter-algorithm-optimizer@agent-use-skills
```

### 方法二：手动安装

1. **克隆仓库**
   ```bash
   git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
   ```

2. **创建符号链接**
   ```bash
   mkdir -p ~/.claude/skills
   ln -s ~/.claude/agent-use-skills/awesome-skills/skills/twitter-algorithm-optimizer ~/.claude/skills/twitter-algorithm-optimizer
   ```

## 验证安装

在 Claude Code 中尝试以下对话：
```
帮我分析一下这条推文草稿的算法排名潜力：[推文内容]
```

## 更新方法
```bash
cd ~/.claude/agent-use-skills && git pull
```

## 详细文档
- [GitHub 仓库](https://github.com/Zerone-Agent/agent-use-skills)
