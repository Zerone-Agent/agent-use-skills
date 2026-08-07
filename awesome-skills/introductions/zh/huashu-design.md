# Huashu Design（花叔 Design）

**Huashu Design** 是一个 HTML 原生的 AI 设计技能，让 AI agent 用一句话产出可交付的高保真设计——交互原型、演讲幻灯片、时间轴动画、信息图，全部基于 HTML 构建，支持导出 MP4/GIF/PPTX/PDF。

## 标签

🎨 设计与创意 | ✅ 已验证

## 核心理念

- **从已有设计上下文出发**：先问用户是否有 design system / UI kit / 品牌素材，不凭空做 hi-fi 设计。涉及具体品牌时强制执行 5 步「核心资产协议」（问 → 搜 → 下载 → 验证 → 固化 spec），确保品牌识别度。
- **Junior Designer 工作流**：开工前先写 assumptions + placeholders + reasoning，尽早展示给用户确认方向，理解错了早改比晚改便宜 100 倍。
- **反 AI slop**：规避紫渐变、emoji 图标、圆角卡片+左 border accent 等 AI 通用视觉最大公约数，用 `text-wrap: pretty`、CSS Grid、oklch 色彩等细节传递品味。
- **设计方向顾问（Fallback）**：需求模糊时从 5 流派 × 20 种设计哲学中推荐 3 个差异化方向，并行生成视觉 Demo 让用户选择。
- **事实验证先于假设**：涉及具体产品/技术时，第一个动作是 WebSearch 验证存在性和状态，禁止凭训练语料做断言。

## 核心功能与工作流

1. **交互原型（App / Web）**：单文件 HTML，iPhone 15 Pro 精确机身，状态驱动多屏切换，Playwright 自动点击测试，典型耗时 10–15 分钟。
2. **演讲幻灯片**：HTML deck（浏览器演讲）+ 可编辑 PPTX（文本框保留，双击可编辑），典型耗时 15–25 分钟。
3. **时间轴动画**：Stage + Sprite 时间片段模型，25fps/60fps MP4 + palette 优化 GIF + 6 首场景化 BGM + 37 个预制 SFX，典型耗时 8–12 分钟。
4. **设计变体探索**：3+ 并排对比，Tweaks 实时调参（配色/字型/信息密度），localStorage 持久化。
5. **信息图 / 可视化**：CSS Grid 精准分栏，杂志级排版，可导 PDF/PNG/SVG。
6. **设计方向顾问**：5 流派 × 20 种设计哲学（信息建筑派/运动诗学派/极简主义派/实验先锋派/东方哲学派），推荐 3 个差异化方向 + 24 个预制 Showcase。
7. **5 维度专家评审**：哲学一致性 / 视觉层级 / 细节执行 / 功能性 / 创新性各 0–10 分，雷达图可视化，输出 Keep / Fix / Quick Wins 清单。

## 技能库概览

- **Starter Components**：幻灯片引擎（deck_stage.js）、动画引擎（animations.jsx）、设备边框（ios_frame.jsx / android_frame.jsx / macos_window.jsx / browser_window.jsx）、变体画布（design_canvas.jsx）
- **设计哲学库**：20 种设计哲学，覆盖 Pentagram 信息建筑、Field.io 运动诗学、Kenya Hara 东方极简、Sagmeister 实验先锋等流派
- **导出工具链**：render-video.js（HTML → MP4）、convert-formats.sh（60fps 插帧 + GIF）、add-music.sh（BGM）、export_deck_pdf.mjs / export_deck_pptx.mjs（PDF/PPTX）
- **品牌资产协议**：5 步硬流程（问 → 搜官方渠道 → 下载资产 → 验证提取 → 固化 brand-spec.md），Logo/产品图/UI 截图为核心资产
- **参考资料**：animation-pitfalls.md、design-styles.md、slide-decks.md、editable-pptx.md、critique-guide.md、video-export.md、audio-design-rules.md 等

## 安装与支持

Huashu Design 支持以下 AI 编辑器和平台：

- [Claude Code](../../claudecode/huashu-design/INSTALL-zh.md)
- [Cursor](../../cursor/huashu-design/INSTALL-zh.md)
- [Codex](../../codex/huashu-design/INSTALL-zh.md)
- [OpenCode](../../opencode/huashu-design/INSTALL-zh.md)
- [OpenClaw](../../openclaw/huashu-design/INSTALL-zh.md)
- [Zerone](../../zerone/huashu-design/INSTALL-zh.md)
- [Qoder](../../qoder/huashu-design/INSTALL-zh.md)

---
更多信息请查看：[GitHub - alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)
