# 在 OpenClaw 中安装 Tavily Search

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Git
- 已安装 Node.js (用于运行脚本)
- [Tavily API Key](https://tavily.com)

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenClaw 能够发现 tavily-search 技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/tavily-search
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/tavily-search ~/.openclaw/skills/tavily-search
```

### 3. 设置环境变量

获取 API Key 并设置：

- **macOS/Linux**: `export TAVILY_API_KEY="您的密钥"`
- **Windows**: `$env:TAVILY_API_KEY="您的密钥"`

### 4. 验证安装

重启 OpenClaw，尝试提问：

- "帮我搜索关于 [话题] 的最新趋势并给出深度分析"
- "do you have tavily-search skill?"

## 更新

```bash
cd ~/.openclaw/agent-use-skills && git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
