# Imagen - Claude Code Installation Guide

## Installation Steps

### Method 1: Via Plugin Marketplace (Recommended)

Run the following commands in Claude Code:

```bash
/plugin marketplace add sanjay3290/ai-skills
/plugin install imagen@ai-skills
```

### Method 2: Manual Setup

1. **Set Gemini API Key**
   Get an API key from [Google AI Studio](https://aistudio.google.com/) and add it to your environment:
   
   - **macOS/Linux**: `export GEMINI_API_KEY="your-api-key"`
   - **Windows**: `$env:GEMINI_API_KEY="your-api-key"` (PowerShell) or `set GEMINI_API_KEY=your-api-key` (CMD)

2. **Verify Environment**
   ```bash
   echo $GEMINI_API_KEY
   ```

## Verify Installation

In a Claude Code chat, try:
```
Generate an image of a serene mountain lake
```

## Update Method
```bash
/plugin update imagen
```

## Detailed Documentation
- [GitHub Repository](https://github.com/sanjay3290/ai-skills)
