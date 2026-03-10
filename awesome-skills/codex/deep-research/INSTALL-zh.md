# 在 Codex 中安装 Deep Research

## 前置条件

- 已安装 [Codex](https://openai.com/index/codex/)
- 已安装 Git
- 已安装 Python 3.8+
- 拥有来自 [Google AI Studio](https://aistudio.google.com/) 的 Gemini API Key

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. 安装 Python 依赖

```bash
pip install -r ~/.codex/agent-use-skills/awesome-skills/skills/deep-research/requirements.txt
```

### 3. 配置 API Key

将 Gemini API key 设置为环境变量：

```bash
export GEMINI_API_KEY=your-api-key-here
```

或者在技能目录下创建 `.env` 文件：

```bash
cp ~/.codex/agent-use-skills/awesome-skills/skills/deep-research/.env.example \
   ~/.codex/agent-use-skills/awesome-skills/skills/deep-research/.env
# 编辑 .env 文件并添加你的 GEMINI_API_KEY
```

### 4. 创建符号链接

创建符号链接，使 Codex 能够发现 deep-research 技能：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/deep-research
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/deep-research ~/.codex/skills/deep-research
```

### 5. 验证安装

重启 Codex，然后尝试询问：

- "研究一下云服务提供商的竞争格局"
- "do you have deep-research?"

如果安装成功，Codex 会自动识别并调用 Deep Research 技能工作流。

## 更新

```bash
cd ~/.codex/agent-use-skills
git pull
pip install -r awesome-skills/skills/deep-research/requirements.txt
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
