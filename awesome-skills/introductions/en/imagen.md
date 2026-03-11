# Imagen

**Imagen** is a skill that leverages Google Gemini's image generation capabilities to generate images directly during AI coding sessions.

## Core Philosophy

- **Seamless Integration**: Generate images using natural language requests directly in your conversation without leaving the terminal or editor.
- **Cross-Platform Compatibility**: Pure Python implementation with zero dependencies (uses standard library only), supporting Windows, macOS, and Linux.
- **AI-Native Workflow**: Specifically designed for AI coding assistants, automatically recognizing and fulfilling image generation needs.

## Key Features & Workflow

1. **Multi-Scenario Generation**: Supports creating UI mockups, icons, illustrations, architecture diagrams, concept art, placeholder images, and more.
2. **Flexible Parameters**: Supports 512px, 1K (default), or 2K resolutions with customizable output paths.
3. **Minimalist Operation**: Input text description -> Call Gemini API -> Auto-save image -> Return file path.
4. **No Dependency Installation**: Based on the Python standard library; runs anywhere with a Python environment and an API Key.

## Skills Library Overview

- **Image Generation Script**: `generate_image.py` - The core driver script for interacting with the Google Gemini API.
- **Configuration Management**: Supports environment variables and command-line arguments for flexible control over models, sizes, and paths.
- **Multi-Platform Support**: Optimized instructions provided for mainstream AI coding platforms.

## Installation & Support

Imagen supports the following AI editors and platforms:

- [Claude Code](../../claudecode/imagen/INSTALL-en.md)
- [Cursor](../../cursor/imagen/INSTALL-en.md)
- [Codex](../../codex/imagen/INSTALL-en.md)
- [OpenCode](../../opencode/imagen/INSTALL-en.md)
- [OpenClaw](../../openclaw/imagen/INSTALL-en.md)
- [Qoder](../../qoder/imagen/INSTALL-en.md)

---
For more information, visit: [GitHub - sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills)
