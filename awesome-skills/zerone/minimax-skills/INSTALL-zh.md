# 在 Zerone 中安装 MiniMax Skills

## 前置条件

- 已安装 Zerone
- 已安装 Git

## 安装步骤

### 1. 克隆 MiniMax Skills 仓库

```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.agents/minimax-skills
```

### 2. 创建符号链接

创建符号链接，使 Zerone 能够发现 MiniMax 技能：

```bash
mkdir -p ~/.agents/skills
for skill in android-native-dev ios-application-dev flutter-dev react-native-dev frontend-dev fullstack-dev shader-dev gif-sticker-maker vision-analysis minimax-pdf pptx-generator minimax-xlsx minimax-docx minimax-multimodal-toolkit; do
  rm -rf ~/.agents/skills/$skill
  ln -s ~/.agents/minimax-skills/skills/$skill ~/.agents/skills/$skill
done
```

### 3. 验证安装

重启 Zerone，尝试询问：
- "帮我创建一个 PPT 演示文稿"
- "do you have minimax skills?"

如果安装成功，Zerone 会自动识别并调用 MiniMax Skills 工作流。

## 更新

```bash
cd ~/.agents/minimax-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
for skill in android-native-dev ios-application-dev flutter-dev react-native-dev frontend-dev fullstack-dev shader-dev gif-sticker-maker vision-analysis minimax-pdf pptx-generator minimax-xlsx minimax-docx minimax-multimodal-toolkit; do
  rm -rf ~/.agents/skills/$skill
done
```

## 获取帮助

- GitHub：https://github.com/MiniMax-AI/skills