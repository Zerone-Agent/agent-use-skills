# 在 OpenCode 中安装 Twitter Algorithm Optimizer

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. 创建符号链接
```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/twitter-algorithm-optimizer ~/.config/opencode/skills/twitter-algorithm-optimizer
```

## 验证安装

重启 OpenCode，尝试提问：
- "分析并优化以下推文的算法表现：[内容]"

## 更新
```bash
cd ~/.config/opencode/agent-use-skills && git pull
```
