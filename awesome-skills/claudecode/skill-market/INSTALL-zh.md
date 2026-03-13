# 安装 Skill Market (Claude Code)

本指南介绍如何在 Claude Code 中安装并验证 **Skill Market** 技能。

## 安装步骤

1. **确保环境准备就绪**：
   本技能依赖 `uv` 进行 Python 环境管理。请确保您的系统中已安装 `uv`。

2. **添加技能文件**：
   将 `skill-market` 目录及其内容放置在您的项目根目录或指定技能目录下。
   确保 `awesome-skills/skills/skill-market/scripts/market.py` 具有执行权限。

3. **运行初始化检查**：
   在 Claude Code 中运行以下命令以验证环境：
   ```bash
   uv run awesome-skills/skills/skill-market/scripts/market.py list
   ```

## 验证安装

您可以尝试搜索一个已知技能来验证连接：
```bash
uv run awesome-skills/skills/skill-market/scripts/market.py info imagen
```
如果成功返回了 `imagen` 技能的详细信息，说明安装成功。

## 更新方法

只需拉取 `agent-use-skills` 仓库的最新代码即可：
```bash
git pull origin main
```

---
参考官方文档: [Zerone Agent SDK](https://github.com/zerone-agent/agent-use-skills)
