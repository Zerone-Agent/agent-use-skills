# Imagen - Claude Code 安装指南

## 安装步骤

### 方法一：使用 Marketplace（推荐）

在 Claude Code 中执行以下命令：

```bash
/plugin marketplace add sanjay3290/ai-skills
/plugin install imagen@ai-skills
```

### 方法二：手动安装

1. **设置 Gemini API Key**
   在 [Google AI Studio](https://aistudio.google.com/) 获取 API Key，并将其添加到您的环境变量：
   
   - **macOS/Linux**: `export GEMINI_API_KEY="您的密钥"`
   - **Windows**: `$env:GEMINI_API_KEY="您的密钥"` (PowerShell) 或 `set GEMINI_API_KEY=您的密钥` (CMD)

2. **验证环境变量**
   ```bash
   echo $GEMINI_API_KEY
   ```

## 验证安装

安装完成后，在 Claude Code 中尝试以下对话：
```
生成一张宁静的山间湖泊图像
```

## 更新方法
```bash
/plugin update imagen
```

## 详细文档
- [GitHub 仓库](https://github.com/sanjay3290/ai-skills)
