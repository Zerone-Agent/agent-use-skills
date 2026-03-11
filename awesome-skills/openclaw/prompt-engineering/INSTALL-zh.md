# 在 OpenClaw 中安装 Prompt Engineering

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. 创建符号链接
```bash
mkdir -p ~/.openclaw/skills
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/prompt-engineering ~/.openclaw/skills/prompt-engineering
```

## 验证安装

重启 OpenClaw，尝试提问：
- "帮我设计一个高可靠性的提示词模版"

## 更新
```bash
cd ~/.openclaw/agent-use-skills && git pull
```
