# OpenClaw Config Guard

**OpenClaw Config Guard** 是一个以安全为优先的配置维护技能，用于对 OpenClaw 配置进行审计与修复，并提供确定性校验、备份、回滚和变更报告能力。

## 核心理念
- **先审计，后修复**：在做任何修改之前，先校验当前生效的配置并分类问题。
- **以官方证据为准**：将 OpenClaw 官方文档和 CLI 输出作为事实依据，而不是依赖记忆。
- **只修复已被证明的阻断问题**：仅在修复方案有明确文档依据时，自动修复会阻止启动的问题。
- **保留恢复路径**：写入前创建备份，写入后重新校验，若失败则立即回滚。

## 主要功能与工作流

1. **生效配置定位**：优先通过 CLI 检测当前 `openclaw.json` 的实际路径，并提供安全的回退路径。
2. **确定性审计**：将 `openclaw config validate --json` 与可选的 `openclaw doctor --non-interactive` 整合为一致的审计流程。
3. **问题分类**：将会阻止启动的问题与非阻断建议分开处理，确保修复策略保持保守。
4. **安全修复边界**：优先使用 `openclaw config set` 与 `openclaw config unset`，避免无文档依据的修改，且默认不运行 `openclaw doctor --fix`。
5. **备份与回滚**：写入前创建带时间戳的备份，若修改后校验失败则立即恢复。
6. **变更报告**：输出 diff、修改路径摘要和可直接用于汇报的结果，便于审查修复动作。

## 技能组成概览

- **核心技能**：`openclaw-config-guard` 负责定义“先审计后修复”的工作流与最终报告要求。
- **辅助脚本**：`scripts/config_guard.py` 提供路径定位、审计、校验、备份、diff 和报告生成等确定性命令。
- **参考资料**：`references/official-sources.md` 列出了每次判断配置问题前必须查看的 OpenClaw 官方文档。

## 安装与支持

OpenClaw Config Guard 当前支持以下 AI 编辑器和平台：
- [OpenClaw](../../openclaw/openclaw-config-guard/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)
