# 在 OpenCode 中安装 Deep Research

## 前置条件

- 已安装 [OpenCode.ai](https://opencode.ai)
- 已安装 Git
- 已安装 Python 3.8+
- 拥有来自 [Google AI Studio](https://aistudio.google.com/) 的 Gemini API Key

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. 安装 Python 依赖

```bash
pip install -r ~/.config/opencode/agent-use-skills/awesome-skills/skills/deep-research/requirements.txt
```

### 3. 配置 API Key

将 Gemini API key 设置为环境变量：

```bash
export GEMINI_API_KEY=your-api-key-here
```

或者在技能目录下创建 `.env` 文件：

```bash
cp ~/.config/opencode/agent-use-skills/awesome-skills/skills/deep-research/.env.example \
   ~/.config/opencode/agent-use-skills/awesome-skills/skills/deep-research/.env
# 编辑 .env 文件并添加你的 GEMINI_API_KEY
```

### 4. 创建符号链接

创建符号链接，使 OpenCode 能够发现 deep-research 技能：

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/deep-research
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/deep-research ~/.config/opencode/skills/deep-research
```

### 5. 重启 OpenCode

重启 OpenCode，插件将自动注入 Deep Research 上下文。

通过询问以下问题验证安装："do you have deep-research?"

## 更新

```bash
cd ~/.config/opencode/agent-use-skills
git pull
pip install -r awesome-skills/skills/deep-research/requirements.txt
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
