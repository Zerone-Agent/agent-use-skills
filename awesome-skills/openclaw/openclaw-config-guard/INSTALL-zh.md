# 在 OpenClaw 中安装 OpenClaw Config Guard

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)，并且命令可在 `PATH` 中使用
- 已安装 Python 3
- 已安装 Git

## 安装步骤

### 1. 克隆技能仓库

如果你还没有在本地保存本仓库，请先执行：

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. 创建技能符号链接

将技能源码目录链接到 OpenClaw 的技能目录，确保 OpenClaw 可以发现并加载该技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/openclaw-config-guard
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/openclaw-config-guard ~/.openclaw/skills/openclaw-config-guard
```

### 3. 确认辅助脚本已就位

该技能包含 Python 辅助脚本和官方参考资料列表。可以用下面的命令确认文件存在：

```bash
ls ~/.openclaw/skills/openclaw-config-guard
ls ~/.openclaw/skills/openclaw-config-guard/scripts
ls ~/.openclaw/skills/openclaw-config-guard/references
```

## 验证安装

重启 OpenClaw 后，可以尝试以下提示词：

- “在不修改任何内容的前提下，先审计我的 OpenClaw 配置。”
- “检查我的 `openclaw.json` 是否存在启动阻断问题，并且只修复有文档依据的问题。”
- “使用 `openclaw-config-guard` 为我的 OpenClaw 配置执行备份、校验并输出总结。”

如果安装成功，OpenClaw 应该能够识别该技能，并按 `SKILL.md` 中定义的工作流执行。

## 更新方法

需要获取最新版本时，更新技能仓库即可：

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## 获取帮助

- 技能问题反馈：https://github.com/Zerone-Agent/agent-use-skills/issues
- OpenClaw 官方文档：https://docs.openclaw.ai/
