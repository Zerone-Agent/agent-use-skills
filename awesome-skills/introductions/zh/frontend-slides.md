# Frontend Slides

**Frontend Slides** 是一个 Claude Code 技能，用于创建精美、动画丰富的 HTML 演示文稿——可以从零开始创建，也可以从 PowerPoint 文件转换。它帮助非设计师无需了解 CSS 或 JavaScript 即可制作漂亮的网页演示。

## 标签

🎨 设计与创意 | ✅ 已验证

## 核心理念
- **你不需要成为设计师**：你只需对所看到的内容做出反应，技能会帮你完成设计工作。
- **零依赖即为自由**：生成的单个 HTML 文件没有任何框架依赖，10 年后仍然能正常运行。
- **拒绝泛化模板**：每个演示文稿都应该感觉像量身定做的，而不是模板生成的。
- **注释即善意**：代码应该向未来的你（或任何打开它的人）解释自己。

## 主要功能与工作流

1. **零依赖 (Zero Dependencies)**：生成的演示文稿是单个 HTML 文件，内联 CSS/JS，无需 npm、构建工具或框架。
2. **视觉风格探索 (Visual Style Discovery)**：不知道如何描述你的设计偏好？没关系——技能会生成多个视觉预览供你挑选。
3. **PPT 转换 (PPT Conversion)**：支持将现有 PowerPoint 文件转换为网页版演示文稿，保留所有图片和内容。
4. **反 AI 套路 (Anti-AI-Slop)**：精心策划的独特风格，避免千篇一律的 AI 审美（告别白底紫渐变）。
5. **生产级质量 (Production Quality)**：生成的代码具有无障碍性、响应式布局和详细注释，方便自定义。

## 创建新演示的流程

1. 技能会询问你的内容（幻灯片、信息、图片）
2. 询问你想要营造的感觉（震撼？兴奋？平静？）
3. 生成 3 个视觉风格预览供你对比选择
4. 使用你选定的风格创建完整的演示文稿
5. 在浏览器中打开查看

## 内置风格库

### 暗色主题
- **Bold Signal** — 自信、高冲击力、暗底上的鲜艳卡片
- **Electric Studio** — 干净、专业、分栏布局
- **Creative Voltage** — 活力十足、复古现代、电蓝色 + 霓虹
- **Dark Botanical** — 优雅、精致、暖色点缀

### 亮色主题
- **Notebook Tabs** — 编辑风、有组织感、带彩色标签的纸张
- **Pastel Geometry** — 友好、亲切、垂直胶囊式布局
- **Split Pastel** — 活泼、现代、双色垂直分割
- **Vintage Editorial** — 风趣、个性十足、几何图形

### 专业主题
- **Neon Cyber** — 未来感、粒子背景、霓虹光效
- **Terminal Green** — 面向开发者、黑客审美
- **Swiss Modern** — 极简、包豪斯风格、几何元素
- **Paper & Ink** — 文学感、首字母大写、拉引引用

## 架构设计

Frontend Slides 采用渐进式披露 (Progressive Disclosure) 架构——主 SKILL.md 是一个简洁的导航图（约 180 行），支持文件仅在需要时按需加载：

- `SKILL.md` — 核心导航文件
- `STYLE_PRESETS.md` — 风格预设定义
- `viewport-base.css` — 视口基础样式
- `html-template.md` — HTML 模板
- `animation-patterns.md` — 动画模式
- `scripts/extract-pptx.py` — PPT 提取脚本

## 安装与支持

Frontend Slides 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/frontend-slides/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides)
