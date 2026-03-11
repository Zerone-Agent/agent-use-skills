# 在 OpenClaw 中安装 Twitter Algorithm Optimizer

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. 创建符号链接
```bash
mkdir -p ~/.openclaw/skills
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/twitter-algorithm-optimizer ~/.openclaw/skills/twitter-algorithm-optimizer
```

## 验证安装

重启 OpenClaw，尝试提问：
- "如何根据 Twitter 算法提升我的推文曝光？"

## 更新
```bash
cd ~/.openclaw/agent-use-skills && git pull
```
