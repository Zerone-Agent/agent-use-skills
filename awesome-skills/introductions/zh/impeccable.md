# Impeccable

**Impeccable** 是由 Paul Bakaus（GDE、前 Google）打造的 AI 设计指导技能，从 Anthropic 官方 frontend-design skill 进化而来，以单一 `/impeccable` 入口提供 23 个子命令、60 条确定性检测规则、live 浏览器迭代与原生 hook 集成。

## 标签

🎨 设计与创意 | 🔍 待验证

## Core Philosophy

- **拒绝 LLM 默认审美**：所有模型都被同一批 SaaS 模板训练过——Inter 字体、紫蓝渐变、卡片套卡片、彩色背景灰字、圆角图标块。Impeccable 通过 60 条确定性检测规则把这些"AI 味"逐条揪出。
- **Brief 高于个人偏好**：明确 pinned 的美学、年代、材质、字体、配色，即使与饱和模式警告冲突也必须尊重——把清晰 brief 引向自己的口味是失败。
- **Brand vs Product 双轨**：`/impeccable init` 区分 brand（营销/落地页/作品集）和 product（应用 UI/仪表盘/工具），后续每个命令都读取这套上下文。
- **四模式语义**：Persuade（说服）、Operate（操作）、Read（阅读）、Experience（沉浸），由访客在该 surface 上的成功定义决定，而不是产品类型。
- **Refinement preserves; redesign replaces**：打磨保留既有身份与文案，重设计则把旧外观当作证据与反例参考。
- **有界验证，不死循环自检**：完整构建→一次性批量检查→批量修复→最多再来一轮确认，避免开放式自我 QA 烧钱做更差的事。

## Key Features & Workflow

1. **一次安装，统一入口**：`npx impeccable install` 自动检测 harness 目录、写入 PRODUCT.md / DESIGN.md 上下文、安装 provider 原生 hook。之后所有操作走 `/impeccable <command>`。
2. **23 个命令**：覆盖构建（init / shape / craft / document / extract）、评估（critique / audit）、精修（polish / bolder / quieter / distill / harden / onboard）、增强（animate / colorize / typeset / layout / delight / overdrive）、修复（clarify / adapt / optimize）、迭代（live）。
3. **60 条确定性检测**：CLI 与浏览器扩展可直接跑 `npx impeccable detect src/`，无需 LLM、无需 API key。覆盖 AI slop（侧栏边线、紫渐变、弹性缓动、暗发光）和通用质量（行宽、内边距、触控目标、跳级标题）。
4. **Live 浏览器迭代**：`/impeccable live` 进入可视化变体模式，在浏览器中选取元素、生成备选方案、应用变更。
5. **Hook 集成**：在 Claude Code / GitHub Copilot / Codex / Cursor / Grok Build 上自动安装原生 hook manifest，对 UI 文件直接编辑时即时拦截或事后报告反模式。
6. **Pin 快捷方式**：常用命令可 `/impeccable pin audit` 创建独立的 `/audit` 等快捷。

## Skills Library Overview

- **构建命令**：`init`（写 PRODUCT.md）、`document`（从代码生成 DESIGN.md）、`extract`（抽 token 与组件）、`shape`（编码前规划 UX/UI）、`craft`（已废弃别名）。
- **评估命令**：`critique`（UX 设计评审 + 启发式打分）、`audit`（a11y / 性能 / 响应式技术检查）。
- **精修命令**：`polish`（最终一公里）、`bolder`（放大保守设计）、`quieter`（压低过激设计）、`distill`（去冗余）、`harden`（错误处理 / i18n / 边界）、`onboard`（首跑 / 空状态 / 激活）。
- **增强命令**：`animate`（动效）、`colorize`（配色）、`typeset`（字体层级）、`layout`（间距与节奏）、`delight`（记忆点）、`overdrive`（突破常规的特效）。
- **修复命令**：`clarify`（UX 文案）、`adapt`（设备适配）、`optimize`（UI 性能）。
- **迭代命令**：`live`（浏览器内可视化变体）。

## Installation & Support

Impeccable supports the following AI editors and platforms (via `npx impeccable install`):
- [Claude Code](../../claudecode/impeccable/INSTALL-zh.md)
- [Cursor](../../cursor/impeccable/INSTALL-zh.md)
- [Codex](../../codex/impeccable/INSTALL-zh.md)
- [OpenCode](../../opencode/impeccable/INSTALL-zh.md)
- [Qoder](../../qoder/impeccable/INSTALL-zh.md)

---
For more information, visit: [impeccable.style](https://impeccable.style) · [GitHub - pbakaus/impeccable](https://github.com/pbakaus/impeccable)
