# Taste Skill

**Taste Skill** 是一套面向 AI Agent 的"反套路"前端设计技能集，目标是阻止 AI 生成千篇一律、模板化的平庸界面，让 AI 写出更具品味的前端代码与设计参考图。

## 标签

🎨 设计与创意 | ✅ 已验证

## Core Philosophy

- **拒绝"AI 味"**：通过强约束的反重复规则（anti-slop）抑制常见的居中堆叠、默认配色、模板化布局，让界面具有真实的设计意图。
- **设计意图优先**：规则针对设计意图（layout、typography、motion、spacing），而非绑定任何特定框架 API，因此可跨 React / Vue / Svelte 使用。
- **职责单一、按需组合**：每个子技能只做一件事，Agent 根据场景按 install name 精准调用，避免一次塞入过多上下文。
- **可调参的设计语言**：核心技能顶部提供 DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY 三个 1-10 的旋钮，让 AI 输出从"保守干净"到"非对称现代"灵活切换。
- **图像先行**：除输出代码的实现类技能外，还提供图像生成类技能，可与 ChatGPT Images / Codex image mode 配合，先生成参考图再交给编码 Agent 实现。

## Key Features & Workflow

1. **一次安装，全套解锁**：通过 git clone + symlink 把 13 个子技能目录链接到平台 skills 目录；Agent 会根据 brief 自动加载需要的那个。
2. **三种工作模式**：
   - **实现类技能**：直接输出前端代码（taste-skill、gpt-taste、soft-skill 等）。
   - **图像生成类技能**：仅输出参考图（imagegen-frontend-web、imagegen-frontend-mobile、brandkit）。
   - **图像转代码类技能**：先生成参考图、分析后再实现（image-to-code-skill）。
3. **可调旋钮**（仅 taste-skill 主技能）：DESIGN_VARIANCE（布局实验度）、MOTION_INTENSITY（动画强度）、VISUAL_DENSITY（信息密度），数值 1-10。
4. **v1 / v2 双版本**：默认 v2 实验版（含 brief 推断、design-system 映射、硬性禁用 em-dash、规范化的 GSAP 代码骨架、redesign-audit 协议、严格的 pre-flight 检查），同时保留 v1 供依赖原行为的用户。
5. **跨平台兼容**：基于 SKILL.md 这种可移植指令文件，主流编码 Agent（Claude Code、Cursor、Codex、OpenCode、OpenClaw、Zerone、Qoder）均可加载。

## Skills Library Overview

- **主推技能**（覆盖 90% 场景）：
  - `design-taste-frontend`（taste-skill，🆕 v2 实验，**默认首选**）：读 brief → 推断设计语言 → 调三个旋钮 → 出代码。
  - `design-taste-frontend-v1`（taste-skill-v1）：原版，仅在依赖 v1 行为时使用。
  - `gpt-taste`（gpt-tasteskill）：面向 GPT/Codex 的更严格变体，更高的布局方差与更强的 GSAP 指导。
- **场景化扩展**：
  - `image-to-code`（image-to-code-skill）：图像 → 分析 → 代码 一条龙。
  - `redesign-existing-projects`（redesign-skill）：先审计 UI，再修布局/间距/层级。
- **风格化补充**：`high-end-visual-design`（柔和高端）、`minimalist-ui`（Notion/Linear 风）、`industrial-brutalist-ui`（瑞士字体 / 强对比）、`stitch-design-taste`（Google Stitch 兼容）。
- **工程兜底**：`full-output-enforcement`（防止模型输出半截代码）。
- **图像生成类**：`imagegen-frontend-web`（网站 hero/landing/多栏）、`imagegen-frontend-mobile`（iOS/Android 截图与流程）、`brandkit`（logo 方向、配色、字体、品牌应用）。

## Installation & Support

Taste Skill supports the following AI editors and platforms:
- [Claude Code](../../claudecode/taste-skill/INSTALL-zh.md)
- [Cursor](../../cursor/taste-skill/INSTALL-zh.md)
- [Codex](../../codex/taste-skill/INSTALL-zh.md)
- [OpenCode](../../opencode/taste-skill/INSTALL-zh.md)
- [OpenClaw](../../openclaw/taste-skill/INSTALL-zh.md)
- [Zerone](../../zerone/taste-skill/INSTALL-zh.md)
- [Qoder](../../qoder/taste-skill/INSTALL-zh.md)

---
For more information, visit: [GitHub - Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
