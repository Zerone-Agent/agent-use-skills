# 在 Claude Code 中安装 gstack

## 前置条件

- 已安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- 已安装 [Git](https://git-scm.com/)
- 已安装 [Bun](https://bun.sh/) v1.0+

## 安装步骤

### 1. 一键安装（推荐）

在 Claude Code 中粘贴以下命令（Claude 会自动执行）：

> Install gstack: run **`git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`** then add a "gstack" section to CLAUDE.md that says to use the /browse skill from gstack for all web browsing, never use mcp\_\_claude-in-chrome\_\_\* tools, and lists the available skills. Then ask the user if they also want to add gstack to the current project so teammates get it.

或直接在 shell 中跑：

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup
```

`./setup` 会自动：
- 用 Bun 编译 TypeScript 源码
- 安装定制 Chromium 与 Playwright 依赖
- 创建全局状态目录 `~/.gstack/`
- 注册 MCP server（如 `gbrain`）

### 2. Team Mode（推荐用于共享仓库）

在仓库根目录运行：

```bash
(cd ~/.claude/skills/gstack && ./setup --team) && \
  ~/.claude/skills/gstack/bin/gstack-team-init required && \
  git add .claude/ CLAUDE.md && \
  git commit -m "require gstack for AI-assisted work"
```

团队成员拉到代码后会自动获得 gstack，每小时静默自动更新。如只想"建议"而非"强制"，把 `required` 改成 `optional`。

### 3. 验证安装

在 Claude Code 中输入：

```
/office-hours
```

或更轻量：

```
/hosts
```

应能看到当前 host 信息和已加载技能。

## 更新

```bash
cd ~/.claude/skills/gstack && ./gstack-upgrade
```

或直接：

```bash
cd ~/.claude/skills/gstack && git pull && ./setup
```

Team mode 下每小时自动检查更新（节流、网络失败安全、完全静默）。

## 卸载

```bash
~/.claude/skills/gstack/bin/gstack-uninstall
```

或手动：

```bash
rm -rf ~/.claude/skills/gstack ~/.gstack
```

## 获取帮助

- 文档：https://github.com/garrytan/gstack/tree/main/docs
- 提交问题：https://github.com/garrytan/gstack/issues
