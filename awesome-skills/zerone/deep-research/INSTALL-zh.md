# 在 Zerone 中安装 Deep Research

## 前置条件

- 已安装 Zerone
- 已安装 Git
- 确保已安装 Python 和 pip
- Google AI API Key（用于 Gemini Deep Research）

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Zerone 能够发现 deep-research 技能：

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/deep-research
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/deep-research ~/.agents/skills/deep-research
```

### 3. 配置 API Key

设置 Google AI API Key 环境变量：

```bash
export GOOGLE_AI_API_KEY="your-api-key-here"
```

### 4. 验证安装

重启 Zerone，尝试询问：
- "帮我研究一下 AI 编程助手的市场现状"
- "do you have deep-research?"

如果安装成功，Zerone 会自动识别并调用 Deep Research 技能工作流。

## 更新

```bash
cd ~/.agents/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.agents/skills/deep-research
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues