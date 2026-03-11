# 在 OpenClaw 中安装 Gog (Google Workspace CLI)

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Homebrew (macOS)
- 拥有 Google 账号并已在 Google Cloud Console 中创建项目及 OAuth 凭据 (client_secret.json)

## 安装步骤

### 1. 安装 gog CLI

该技能依赖于 `gog` CLI 工具，通过 Homebrew 安装：

```bash
brew tap steipete/tap
brew install gogcli
```

### 2. 初始化认证

您需要提供 Google Cloud 的 OAuth 凭据文件：

```bash
# 导入凭据
gog auth credentials /path/to/your/client_secret.json

# 添加账号并授权所需服务
gog auth add your-email@gmail.com --services gmail,calendar,drive,contacts,sheets,docs
```

### 3. 克隆 agent-use-skills 仓库

将技能库克隆到本地（如果尚未克隆）：

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 4. 在 OpenClaw 中配置技能

创建符号链接：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/gog
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/gog ~/.openclaw/skills/gog
```

### 5. 设置环境变量 (可选)

为了简化操作，建议在 Shell 配置文件中设置默认账号：

```bash
export GOG_ACCOUNT="your-email@gmail.com"
```

## 验证安装

重启 OpenClaw，尝试提问：

- "帮我搜索最近 7 天名为 'Invoice' 的 Gmail 邮件"
- "查看我今天的日历安排"
- "do you have gog skill?"

## 更新

1. **更新 CLI**: `brew upgrade gogcli`
2. **更新技能库**: `cd ~/.openclaw/agent-use-skills && git pull`

## 获取帮助

- 技能逻辑问题：https://github.com/Zerone-Agent/agent-use-skills/issues
- CLI 工具问题：https://github.com/steipete/gog/issues
