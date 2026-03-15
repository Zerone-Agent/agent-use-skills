# 在 OpenClaw 中安装 Skill Market

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Git
- 确保你的 Python 环境可以使用 `uv`

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenClaw 能够发现 skill-market 技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/skill-market
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/skill-market ~/.openclaw/skills/skill-market
```

### 3. 验证安装

执行以下命令或重启 OpenClaw 后询问以验证是否安装成功：

```bash
uv run ~/.openclaw/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

或者在 OpenClaw 中尝试询问：
- "列出 skill market 上的所有可用技能"
- "do you have skill-market?"

如果安装成功，OpenClaw 会自动识别并调用 Skill Market 技能工作流。

## 更新

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
