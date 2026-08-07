# Video Summarizer

**Video Summarizer** 是一个视频内容提取与结构化总结技能，能够下载视频、转录语音、生成结构化摘要，并将结果保存为 Obsidian 笔记。

## 标签

🗂️ 文档与办公 | ✅ 已验证

## 核心理念

- **全链路自动化**：从视频下载到语音转录再到摘要生成，实现端到端的自动化处理，无需人工介入中间环节
- **结构化知识沉淀**：将非结构化的视频内容转化为可检索、可关联的 Obsidian 笔记，构建个人知识库
- **双语适配**：支持中文（B站、抖音等）和英文（YouTube 等）视频内容的智能识别与转录
- **总结与逐字稿分离**：生成独立的摘要笔记和完整逐字稿笔记，通过 Obsidian 双向链接互相关联

## 主要功能与工作流

1. **视频下载**：支持 YouTube、B站及所有 yt-dlp 兼容平台的视频下载，自动提取标题、作者和日期等元数据
2. **音频提取**：使用 ffmpeg 从视频中提取高质量 MP3 音频
3. **语音转录**：基于 OpenAI Whisper（turbo 模型）将语音转为文字，支持自动语言检测，中文内容可手动指定语言以提升准确率
4. **结构化摘要生成**：根据转录文本生成包含"一句话核心"、"主要论据"和"关键信息"表格的标准化摘要
5. **Obsidian 笔记保存**：自动创建摘要笔记和逐字稿笔记，添加 YAML frontmatter（标题、来源、作者、日期、标签），通过 wikilinks 建立双向链接
6. **临时文件自动清理**：处理完成后自动删除下载的视频和音频文件

## 工具依赖

| 工具 | 用途 |
|------|------|
| `yt-dlp` | 视频下载与元数据提取 |
| `ffmpeg` | 音频提取（MP3） |
| `whisper`（OpenAI） | 语音转录为文字 |
| `obsidian` CLI | 创建和管理 Obsidian 笔记 |

## 触发场景

- 用户分享视频链接并要求总结、提取要点或分析内容
- 用户要求转录视频内容或生成视频笔记
- 用户要求将视频内容保存到 Obsidian

## 安装与支持

Video Summarizer 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/video-summarizer/INSTALL-zh.md)
- [Cursor](../../cursor/video-summarizer/INSTALL-zh.md)
- [Codex](../../codex/video-summarizer/INSTALL-zh.md)
- [OpenCode](../../opencode/video-summarizer/INSTALL-zh.md)
- [OpenClaw](../../openclaw/video-summarizer/INSTALL-zh.md)
- [Zerone](../../zerone/video-summarizer/INSTALL-zh.md)
- [Qoder](../../qoder/video-summarizer/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)
