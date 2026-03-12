# 安装 Skill Market (Cursor)

本指南介绍如何在 Cursor 中配置并使用 **Skill Market** 技能。

## 安装步骤

1. **环境依赖**：
   确保你的系统中安装了 `uv` (推荐) 或 `python 3.10+`。

2. **配置技能**：
   你可以直接在 Cursor 的终端中运行市场脚本。如果要在 Agent 模式下使用，请确保 `scripts/market.py` 路径正确。

3. **测试连接**：
   打开 Cursor 终端并运行：
   ```bash
   uv run awesome-skills/skills/skill-market/scripts/market.py list
   ```

## 验证安装

查询一个技能详情：
```bash
uv run awesome-skills/skills/skill-market/scripts/market.py info agent-browser
```

---
参考：[Zerone Agent 技术文档](https://github.com/zerone-agent/agent-use-skills)
