# 在 Codex 中安装 Skill Market

## 前置条件

- 已安装 Codex
- 已安装 Git
- 确保你的 Python 环境可以使用 `uv`

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git
```

### 2. 配置技能

将 `skill-market` 目录及其内容放置在您的项目根目录或适用于 Codex 的指定技能目录下，或直接从克隆的仓库中运行。

### 3. 验证安装

运行以下命令以验证环境：

```bash
uv run agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

## 测试连接

您可以尝试搜索一个已知技能来验证连接：
```bash
uv run agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py info agent-browser
```

如果成功返回了技能的详细信息，说明安装成功。

## 更新

```bash
cd agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
