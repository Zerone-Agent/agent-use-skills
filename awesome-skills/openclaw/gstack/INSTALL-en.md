# Installing gstack for OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/openclaw/openclaw) installed
- Claude Code installed (OpenClaw spawns Claude Code via ACP to run the full gstack suite)
- [Git](https://git-scm.com/) and [Bun](https://bun.sh/) v1.0+ installed

## Installation Steps

OpenClaw offers two complementary paths:

### Option A: ACP into Claude Code for the full gstack suite (recommended)

OpenClaw spawns Claude Code sessions via ACP, so every gstack skill just works once Claude Code has gstack installed. Paste this to your OpenClaw agent:

> Install gstack: run `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` to install gstack for Claude Code. Then add a "Coding Tasks" section to AGENTS.md that says: when spawning Claude Code sessions for coding work, tell the session to use gstack skills. Include these examples — security audit: "Load gstack. Run /cso", code review: "Load gstack. Run /review", QA test a URL: "Load gstack. Run /qa https://...", build a feature end-to-end: "Load gstack. Run /autoplan, implement the plan, then run /ship", plan before building: "Load gstack. Run /office-hours then /autoplan. Save the plan, don't implement."

Then just talk to your OpenClaw agent naturally:

| You say | What happens |
|---|---|
| "Fix the typo in README" | Simple — Claude Code session, no gstack needed |
| "Run a security audit on this repo" | Spawns Claude Code with `Run /cso` |
| "Build me a notifications feature" | Spawns Claude Code with `/autoplan → implement → /ship` |
| "Help me plan the v2 API redesign" | Spawns Claude Code with `/office-hours → /autoplan`, saves plan without implementing |

### Option B: Install 4 native OpenClaw skills (no Claude Code required)

For when you only want the methodologies without the full toolchain:

```bash
clawhub install gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

| Skill | What it does |
|---|---|
| `gstack-openclaw-office-hours` | Product interrogation with 6 forcing questions |
| `gstack-openclaw-ceo-review` | Strategic challenge with 4 scope modes |
| `gstack-openclaw-investigate` | Root cause debugging methodology |
| `gstack-openclaw-retro` | Weekly engineering retrospective |

These are conversational skills — your OpenClaw agent runs them directly in chat, no Claude Code spawn needed.

### Verify Installation

- Option A: Say "Run a security audit on this repo" in OpenClaw; it should spawn a Claude Code session running `/cso`.
- Option B: Say "let's do an office hours session" in OpenClaw; it should trigger the 6 forcing questions.

## Updating

```bash
cd ~/.claude/skills/gstack && ./gstack-upgrade
```

For ClawHub native skills:

```bash
clawhub update gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

## Uninstallation

```bash
~/.claude/skills/gstack/bin/gstack-uninstall
clawhub uninstall gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

## Getting Help

- Docs: https://github.com/garrytan/gstack/tree/main/docs (including [docs/OPENCLAW.md](https://github.com/garrytan/gstack/blob/main/docs/OPENCLAW.md) for advanced dispatch routing)
- Report issues: https://github.com/garrytan/gstack/issues
