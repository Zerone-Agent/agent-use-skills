# Proactive Agent (主动型智能体)

**Proactive Agent** 是一个旨在将 AI 智能体从“被动执行者”转变为“主动合作伙伴”的架构与技能集。它包含了一套完整的持久化内存管理、自我改进准则及安全加固模式，确保智能体能够预判用户需求、在上下文丢失后快速恢复，并持续优化自身性能。

## 标签

开发与测试 | 待验证

## 核心理念

- **主动预判**：不仅仅是询问“我该做什么？”，而是主动思考“我能做些什么让用户感到惊喜？”。
- **状态持久化**：通过 **WAL (Write-Ahead Logging)** 协议和**工作缓冲区 (Working Buffer)**，确保在长对话导致的上下文截断后，智能体仍能“记得”关键决策和当前任务进度。
- **不懈的韧性 (Relentless Resourcefulness)**：在报告“无法完成”之前，尝试至少 5-10 种不同的方法或工具组合。
- **安全进化**：通过 ADL（抗漂移限制）和 VFM（价值优先修改）协议，确保智能体在自我优化过程中保持稳定且不偏离业务目标。

## 核心功能与工作流

1. **三层存储架构**：
    - `SESSION-STATE.md`：记录当前任务的活跃“内存”。
    - `memory/`（每日记录）：原始会话日志。
    - `MEMORY.md`：沉淀长期的智慧与经验。
2. **WAL 协议**：在回复用户之前，优先将更正、偏好、决定和关键数值写入 `SESSION-STATE.md`。
3. **工作缓冲区 (Working Buffer)**：当上下文占用超过 60% 后启动，实时记录交互，为上下文压缩后的恢复提供“救命稻草”。
4. **自主 Cron 任务**：区分“提示型任务”与“执行型任务”，利用隔离会话（isolated agentTurn）在后台自动完成维护和检查工作。
5. **反向提示词 (Reverse Prompting)**：主动询问用户偏好和辅助信息，消除未知的盲点。

## 技能库概览

- **核心资产**：包含 `ONBOARDING.md`、`SOUL.md`、`AGENTS.md` 等核心定义文件模板。
- **脚本工具**：如安全审计脚本 (`security-audit.sh`) 和心跳检查模板。
- **协议集**：包含 WAL、ADL、VFM 等多套标准化的智能体行为协议。

## 安装与支持

Proactive Agent 目前仅支持以下平台：

- [OpenClaw](../../openclaw/proactive-agent/INSTALL-zh.md)

---
更多信息请查看：[Hal Stack 🦞](https://github.com/halthelobster/hal-stack)
