# 安装 Skill Market (OpenCode)

本指南介绍如何在 OpenCode 中使用 **Skill Market** 技能。

## 安装步骤

1. **环境准备**：
   OpenCode 与 `uv` 环境高度兼容。确保系统中已安装 `uv`。

2. **验证工具**：
   在 OpenCode 终端中运行以下命令：
   ```bash
   uv run awesome-skills/skills/skill-market/scripts/market.py list
   ```

## 验证安装

查询技能兼容性：
```bash
uv run awesome-skills/skills/skill-market/scripts/market.py info content-research-writer
```

---
参考：[Zerone Agent GitHub](https://github.com/zerone-agent/agent-use-skills)
