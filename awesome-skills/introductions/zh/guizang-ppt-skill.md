# Guizang PPT Skill

**Guizang PPT Skill** 是一款面向 AI Agent 环境的网页 PPT 生成技能，用于产出单文件 HTML 横向翻页演示文稿、PPT 配图及多平台封面，内置电子杂志风与瑞士国际主义两套视觉系统。

## 标签

🎨 设计与创意 | ✅ 已验证

## 核心理念
- **Agent 原生**: HTML/CSS 纯文本格式，Agent 可直接读取、编辑和验证，无需构建工具。
- **双视觉系统**: Style A 电子杂志风（衬线+流体背景）适合叙事表达；Style B 瑞士国际主义（无衬线+网格+高饱和锚点色）适合事实与数据呈现。
- **结构化工作流**: 从需求澄清（7 问清单）到模板拷贝、内容填充、自检校验，每一步都有明确指引。
- **美学约束保护**: 主题色仅允许从预设中选择（杂志风 5 套 / 瑞士风 4 套），不允许自定义 hex 值，确保输出稳定。

## 主要功能与工作流
1. **双风格模板**: Style A（10 种布局）+ Style B（22 种锁定版式），涵盖封面、章节幕封、数据大字报、图文混排、时间线、对比、KPI Tower 等。
2. **主题色预设**: Style A 提供 5 套电子墨水主题（墨水经典/靛蓝瓷/森林墨/牛皮纸/沙丘），Style B 提供 4 套瑞士锚点色（克莱因蓝/柠檬黄/柠檬绿/安全橙）。
3. **可选配图流程**: 在 Codex 环境中支持通过 GPT-Image 2.0 / GPT-M 2.0 生成纪实照片、信息图、流程图、系统关系图和 UI 情景图。
4. **多平台封面生成**: 同一内容可生成公众号 21:9 头图、1:1 分享卡、小红书 3:4 封面、视频号横版封面。
5. **瑞士风版式校验**: 内置 `validate-swiss-deck.mjs` 脚本，可自动检测版式合规性、图片槽位、SVG 文本等问题。
6. **低功耗模式**: 按 `B` 键切换静态模式，关闭 WebGL/Canvas 动画，适配低端设备。

## 技能库概览
- **模板资源**: Style A 模板 (`template.html`)、Style B 模板 (`template-swiss.html`)、截图美化背景素材。
- **参考文档**: 组件手册、10 种布局骨架、22 种瑞士锁定版式、主题色预设、配图提示词、截图适配规范、质量检查清单。
- **校验脚本**: 瑞士风版式校验器 (`validate-swiss-deck.mjs`)。

## 安装与支持
Guizang PPT Skill 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/guizang-ppt-skill/INSTALL-zh.md)
- [Cursor](../../cursor/guizang-ppt-skill/INSTALL-zh.md)
- [Codex](../../codex/guizang-ppt-skill/INSTALL-zh.md)
- [OpenCode](../../opencode/guizang-ppt-skill/INSTALL-zh.md)
- [OpenClaw](../../openclaw/guizang-ppt-skill/INSTALL-zh.md)
- [Zerone](../../zerone/guizang-ppt-skill/INSTALL-zh.md)
- [Qoder](../../qoder/guizang-ppt-skill/INSTALL-zh.md)

---
获取更多信息，请访问：[GitHub - op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)
