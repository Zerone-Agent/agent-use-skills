# 在 OpenClaw 中安装 gstack

## 前置条件

- 已安装 [OpenClaw](https://github.com/openclaw/openclaw)
- 已安装 Claude Code（OpenClaw 通过 ACP 调用 Claude Code 来跑 gstack 全套）
- 已安装 [Git](https://git-scm.com/)、[Bun](https://bun.sh/) v1.0+

## 安装步骤

OpenClaw 提供两种互补方式：

### 方式 A：通过 ACP 调用 Claude Code 跑完整 gstack（推荐）

OpenClaw 通过 ACP spawn Claude Code session，因此只要 Claude Code 装了 gstack，所有 gstack 技能都能用。在你的 OpenClaw agent 中粘贴：

> Install gstack: run `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` to install gstack for Claude Code. Then add a "Coding Tasks" section to AGENTS.md that says: when spawning Claude Code sessions for coding work, tell the session to use gstack skills. Include these examples — security audit: "Load gstack. Run /cso", code review: "Load gstack. Run /review", QA test a URL: "Load gstack. Run /qa https://...", build a feature end-to-end: "Load gstack. Run /autoplan, implement the plan, then run /ship", plan before building: "Load gstack. Run /office-hours then /autoplan. Save the plan, don't implement."

之后与 OpenClaw agent 自然对话即可：

| 你说 | 会发生什么 |
|---|---|
| "Fix the typo in README" | Simple — Claude Code session，不需要 gstack |
| "Run a security audit on this repo" | Spawns Claude Code with `Run /cso` |
| "Build me a notifications feature" | Spawns Claude Code with `/autoplan → implement → /ship` |
| "Help me plan the v2 API redesign" | Spawns Claude Code with `/office-hours → /autoplan`，保存计划不实施 |

### 方式 B：装 4 个 OpenClaw 原生技能（不需要 Claude Code）

适合只想用方法论、不需要全套工具链的场景：

```bash
clawhub install gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

| 技能 | 用途 |
|---|---|
| `gstack-openclaw-office-hours` | 6 个强制提问的产品盘问 |
| `gstack-openclaw-ceo-review` | 4 种 scope 模式的战略挑战 |
| `gstack-openclaw-investigate` | 系统性根因调试方法论 |
| `gstack-openclaw-retro` | 周度工程复盘 |

这是会话型技能，OpenClaw agent 直接在 chat 中跑，无需 spawn Claude Code。

### 验证安装

- 方式 A：在 OpenClaw 中说 "Run a security audit on this repo"，应 spawn 一个 Claude Code session 并运行 `/cso`。
- 方式 B：在 OpenClaw 中直接说 "let's do an office hours session"，应触发 6 个提问。

## 更新

```bash
cd ~/.claude/skills/gstack && ./gstack-upgrade
```

ClawHub 原生技能：

```bash
clawhub update gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

## 卸载

```bash
~/.claude/skills/gstack/bin/gstack-uninstall
clawhub uninstall gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

## 获取帮助

- 文档：https://github.com/garrytan/gstack/tree/main/docs（含 [docs/OPENCLAW.md](https://github.com/garrytan/gstack/blob/main/docs/OPENCLAW.md) 高级派发路由）
- 提交问题：https://github.com/garrytan/gstack/issues
