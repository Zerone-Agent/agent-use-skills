# Imagen

**Imagen** 是一个利用 Google Gemini 的图像生成能力，在 AI 编码会话期间直接生成图像的技能。

## 核心理念

- **无缝集成**：无需离开终端或编辑器，直接在对话中通过自然语言请求生成图像
- **跨平台兼容**：纯 Python 实现，零依赖（仅使用标准库），支持 Windows、macOS 和 Linux
- **AI 原生工作流**：专为 AI 编码助手设计，能够自动识别图像生成需求并执行

## 核心功能与工作流

1. **多场景生成**：支持生成 UI 模版、图标、插图、架构图、概念图、占位图等
2. **灵活参数**：支持 512px, 1K (默认), 或 2K 分辨率，并可自定义输出路径
3. **极简操作**：输入文本描述 -> 调用 Gemini API -> 自动保存图片 -> 返回文件路径
4. **无需安装依赖**：基于 Python 标准库，只要有 Python 环境和 API Key 即可运行

## 技能库概览

- **图像生成脚本**：`generate_image.py` - 核心驱动脚本，负责与 Google Gemini API 交互
- **配置管理**：支持环境变量和命令行参数，灵活控制模型、尺寸和路径
- **多平台支持**：针对主流 AI 编程平台提供优化指令

## 安装与支持

Imagen 支持以下 AI 编辑器和平台：

- [Claude Code](../../claudecode/imagen/INSTALL-zh.md)
- [Cursor](../../cursor/imagen/INSTALL-zh.md)
- [Codex](../../codex/imagen/INSTALL-zh.md)
- [OpenCode](../../opencode/imagen/INSTALL-zh.md)
- [OpenClaw](../../openclaw/imagen/INSTALL-zh.md)
- [Qoder](../../qoder/imagen/INSTALL-zh.md)

---
更多信息请查看：[GitHub - sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills)
