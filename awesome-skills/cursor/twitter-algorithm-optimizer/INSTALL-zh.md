# 在 Cursor 中安装 Twitter Algorithm Optimizer

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. 创建符号链接
```bash
mkdir -p ~/.cursor/skills
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/twitter-algorithm-optimizer ~/.cursor/skills/twitter-algorithm-optimizer
```

## 验证安装

重启 Cursor 并确保处于 **Agent** 模式，尝试提问：
- "基于 Twitter 算法优化我的推文：[内容]"

## 更新
```bash
cd ~/.cursor/agent-use-skills && git pull
```
