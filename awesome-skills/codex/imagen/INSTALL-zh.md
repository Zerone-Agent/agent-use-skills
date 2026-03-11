# 在 Codex 中安装 Imagen

## 前置条件

- 已安装 Codex
- 已安装 Git
- [Google AI Studio](https://aistudio.google.com/) API Key

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Codex 能够发现 imagen 技能：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/imagen
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/imagen ~/.codex/skills/imagen
```

### 3. 设置环境变量

获取 API Key 并设置：

- **macOS/Linux**: `export GEMINI_API_KEY="您的密钥"`
- **Windows**: `$env:GEMINI_API_KEY="您的密钥"`

### 4. 验证安装

重启 Codex 并确保处于 **Agent** 模式，然后尝试询问：

- "Generate an image of a futuristic city"

如果安装成功，Agent 会自动识别并调用 Imagen 技能。

## 更新

```bash
cd ~/.codex/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
