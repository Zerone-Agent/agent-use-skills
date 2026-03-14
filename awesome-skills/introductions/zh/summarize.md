# Summarize

**Summarize** 是一个功能强大的全能摘要生成技能，支持对网页 URL、本地文件（如 PDF）、音频、视频以及 YouTube 链接进行快速的内容提炼。

## 标签

文档与办公 | 待验证

## 核心理念

- **全格式支持**：不仅支持文字网页，还能处理 PDF、多媒体文件和 YouTube 视频。
- **多模型驱动**：支持主流大模型（Gemini, Claude, GPT, xAI）作为后端推理引擎。
- **开发者优先**：通过简洁的 CLI 和可选的 JSON 输出，方便 Agent 直接调取和分析结构化摘要。

## 核心功能与工作流

1. **多维摘要**：通过 `summarize` CLI 快速获取 URL 或本地文件的核心内容。
2. **YouTube 智能提取**：支持 YouTube 链接的自动内容转换与总结（可配合 Apify 实现增强支持）。
3. **内容抓取增强**：集成 Firecrawl，可绕过部分网站的反爬虫限制，获取更完整的原始内容。
4. **自定义控制**：支持设置摘要长度（short 到 xxl）及输出格式。

## 技能库概览

- **核心指令**：`summarize` 命令封装。
- **配置系统**：通过 `~/.summarize/config.json` 或环境变量（如 `GEMINI_API_KEY`）进行配置。
- **外部集成**：支持提取模式（--extract-only）以获取未经总结的网页纯净数据。

## 安装与支持

Summarize 目前仅支持以下平台：

- [OpenClaw](../../openclaw/summarize/INSTALL-zh.md)

---
更多信息请查看：[Summarize 官方文档](https://summarize.sh)
