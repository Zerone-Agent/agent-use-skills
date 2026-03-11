# 在 OpenClaw 中安装 Summarize

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Homebrew (macOS)
- [Gemini API Key](https://aistudio.google.com/app/apikey) (推荐) 或其他支持的模型 Key

## 安装步骤

### 1. 安装 summarize CLI

该技能依赖于 `summarize` CLI 工具，请先通过 Homebrew 安装：

```bash
brew tap steipete/tap
brew install summarize
```

### 2. 克隆 agent-use-skills 仓库

将技能库克隆到本地（如果尚未克隆）：

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 3. 在 OpenClaw 中配置技能

创建符号链接，使 OpenClaw 能够调用该技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/summarize
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/summarize ~/.openclaw/skills/summarize
```

### 4. 设置环境变量

根据您选择的模型设置相应的 API Key：

```bash
export GEMINI_API_KEY="您的密钥"
# 或
export ANTHROPIC_API_KEY="您的密钥"
```

## 验证安装

重启 OpenClaw，尝试提问：

- "帮我总结一下这个网页：https://example.com"
- "总结一下这个本地 PDF 文件：/path/to/document.pdf"

## 更新

1. **更新 CLI**: `brew upgrade summarize`
2. **更新技能库**: `cd ~/.openclaw/agent-use-skills && git pull`

## 获取帮助

- 技能逻辑问题：https://github.com/Zerone-Agent/agent-use-skills/issues
- CLI 工具问题：https://github.com/steipete/summarize/issues
