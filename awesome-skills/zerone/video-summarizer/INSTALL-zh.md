# 在 Zerone 中安装 Video Summarizer

## 前置条件

- 已安装 Zerone
- 已安装 Git
- 已安装 yt-dlp、ffmpeg 和 OpenAI Whisper

## 安装步骤

### 1. 安装工具依赖

```bash
pip install yt-dlp openai-whisper
brew install ffmpeg  # macOS
# 或 apt install ffmpeg  # Linux
```

### 2. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 3. 创建符号链接

创建符号链接，使 Zerone 能够发现 video-summarizer 技能：

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/video-summarizer
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/video-summarizer ~/.agents/skills/video-summarizer
```

### 4. 验证安装

重启 Zerone，尝试询问：
- "帮我总结这个视频 https://www.youtube.com/watch?v=xxx"
- "do you have video-summarizer?"

如果安装成功，Zerone 会自动识别并调用 Video Summarizer 技能工作流。

## 更新

```bash
cd ~/.agents/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.agents/skills/video-summarizer
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues