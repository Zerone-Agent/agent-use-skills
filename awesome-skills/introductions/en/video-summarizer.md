# Video Summarizer

**Video Summarizer** is a video content extraction and structured summarization skill that downloads videos, transcribes speech to text, generates structured summaries, and saves results as linked Obsidian notes.

## Tags

🗂️ Documents & Office | ✅ Verified

## Core Philosophy

- **End-to-End Automation**: From video download to speech transcription to summary generation, the entire pipeline runs automatically without manual intervention
- **Structured Knowledge Capture**: Transforms unstructured video content into searchable, interlinked Obsidian notes for building a personal knowledge base
- **Bilingual Adaptation**: Supports both Chinese (Bilibili, Douyin, etc.) and English (YouTube, etc.) video content with intelligent language detection
- **Summary & Transcript Separation**: Generates independent summary notes and full transcript notes, linked bidirectionally via Obsidian wikilinks

## Key Features & Workflow

1. **Video Download**: Downloads videos from YouTube, Bilibili, and all yt-dlp compatible platforms, automatically extracting metadata such as title, author, and upload date
2. **Audio Extraction**: Uses ffmpeg to extract high-quality MP3 audio from video files
3. **Speech Transcription**: Converts speech to text using OpenAI Whisper (turbo model), with automatic language detection and optional manual language specification for improved accuracy on Chinese content
4. **Structured Summary Generation**: Produces a standardized summary from the transcript, including a one-line core point, key arguments, and a structured information table
5. **Obsidian Note Saving**: Automatically creates summary and transcript notes with YAML frontmatter (title, source, author, date, tags), interconnected via wikilinks
6. **Automatic Cleanup**: Removes downloaded video and audio temporary files after processing is complete

## Tool Dependencies

| Tool | Purpose |
|------|---------|
| `yt-dlp` | Video download and metadata extraction |
| `ffmpeg` | Audio extraction (MP3) |
| `whisper` (OpenAI) | Speech-to-text transcription |
| `obsidian` CLI | Create and manage Obsidian notes |

## Trigger Scenarios

- User shares a video URL and asks for a summary, key points extraction, or content analysis
- User wants to transcribe video content or generate video notes
- User wants to save video content to Obsidian

## Installation & Support

Video Summarizer supports the following AI editors and platforms:
- [Claude Code](../../claudecode/video-summarizer/INSTALL-en.md)
- [Cursor](../../cursor/video-summarizer/INSTALL-en.md)
- [Codex](../../codex/video-summarizer/INSTALL-en.md)
- [OpenCode](../../opencode/video-summarizer/INSTALL-en.md)
- [OpenClaw](../../openclaw/video-summarizer/INSTALL-en.md)
- [Zerone](../../zerone/video-summarizer/INSTALL-en.md)
- [Qoder](../../qoder/video-summarizer/INSTALL-en.md)

---
For more information, visit: [GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)
