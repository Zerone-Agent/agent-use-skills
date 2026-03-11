# 在 Codex 中安装 Prompt Engineering

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. 创建符号链接
```bash
mkdir -p ~/.codex/skills
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/prompt-engineering ~/.codex/skills/prompt-engineering
```

## 验证安装

重启 Codex，尝试提问：
- "使用思维链 (CoT) 模式分析这段逻辑"

## 更新
```bash
cd ~/.codex/agent-use-skills && git pull
```
