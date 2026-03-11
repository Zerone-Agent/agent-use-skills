# 在 OpenCode 中安装 Imagen

## 前置条件

- 已安装 OpenCode
- 已安装 Git
- [Google AI Studio](https://aistudio.google.com/) API Key

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenCode 能够发现 imagen 技能：

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/imagen
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/imagen ~/.config/opencode/skills/imagen
```

### 3. 设置环境变量

获取 API Key 并设置：

- **macOS/Linux**: `export GEMINI_API_KEY="您的密钥"`
- **Windows**: `$env:GEMINI_API_KEY="您的密钥"`

### 4. 验证安装

重启 OpenCode 并确保处于 **Agent** 模式，然后尝试询问：

- "Generate an image of a futuristic city"

如果安装成功，Agent 会自动识别并调用 Imagen 技能。

## 更新

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
