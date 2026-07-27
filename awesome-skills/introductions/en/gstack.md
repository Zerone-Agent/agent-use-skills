# gstack

**gstack** is Y Combinator President Garry Tan's personal Claude Code setup, made public. It turns a single agent into a virtual engineering team of 23 specialist roles covering the full sprint flow — Think → Plan → Build → Review → Test → Ship → Reflect — so a part-time builder can ship like a 20-person team.

## Tags

💻 Dev & Testing | 🔍 Pending Verification

## Core Philosophy

- **One person is a team**: With AI, the marginal cost of completeness approaches zero. In the first 60 days of 2026, Garry Tan used gstack part-time to ship 3 production services + 40+ features; logical code-change pace is ~810× his 2013 rate.
- **Boil the Ocean**: "Don't boil the ocean" was right when engineering time was the bottleneck. AI makes the 90% solution and the 100% solution differ by seconds — so always do the complete thing. Lake by lake, eventually the whole ocean boils.
- **Search Before Building**: Three layers of knowledge — Layer 1 (battle-tested patterns, verify before assuming), Layer 2 (current ecosystem trends, beware Mr. Market), Layer 3 (first-principles observations, the most valuable of all).
- **The process is the product**: Every skill reads the previous one's output — `/office-hours` writes the design doc that `/plan-ceo-review` reads; `/plan-eng-review` writes the test plan that `/qa` picks up; `/review` finds the bugs that `/ship` verifies are fixed. Nothing falls through the cracks.
- **Real browser, real tests, real PRs**: QA is not simulation — a custom Chromium actually clicks through flows. Ship is not commentary — sync main, run tests, audit coverage, push, open PR, all in one command.

## Key Features & Workflow

1. **30-second install**: `git clone ~/.claude/skills/gstack && ./setup`. The setup script auto-distributes skills to `~/.<platform>/skills/gstack-*/` for the chosen host, installs the custom Chromium + Playwright, and registers the MCP server.
2. **Team mode**: Inside your repo, run `./setup --team && bin/gstack-team-init required`, then commit `.claude/` and `CLAUDE.md`. Teammates get gstack automatically with a silent hourly auto-update check.
3. **Sprint end-to-end**: Product interrogation (`/office-hours`) → strategy review (`/plan-ceo-review`) → architecture lock-in (`/plan-eng-review`) → design scoring (`/plan-design-review`) → DX review (`/plan-devex-review`) → auto-planning (`/autoplan`) → code review (`/review`) → real-browser QA (`/qa`) → shipping (`/ship` / `/land-and-deploy` / `/canary`) → retrospective (`/retro`).
4. **Design specialists**: `/design-consultation` (build a design system from scratch), `/design-shotgun` (4–6 mockup variants side by side with taste memory), `/design-html` (production HTML via Pretext computed layout), `/design-review` (audit + atomic-commit fixes).
5. **Security & performance**: `/cso` (OWASP Top 10 + STRIDE, 17 false-positive exclusions, 8/10 confidence gate, independent verification), `/benchmark` (Core Web Vitals + before/after), `/canary` (post-deploy console / perf / page-failure monitoring loop).
6. **Multi-agent pairing**: `/pair-agent` lets any AI agent (OpenClaw, Hermes, Codex, Cursor) share the same browser — auto-ngrok tunnel, tab isolation, rate limiting, activity attribution.
7. **Power tools**: `/codex` (OpenAI Codex second opinion), `/careful`, `/freeze` / `/unfreeze` (pause/resume selected skills), `/guard`, `/learn` (feed knowledge to gstack), `/document-release`, `/document-generate`, `/make-pdf`, `/diagram`.
8. **gbrain integration (optional)**: `/setup-gbrain` indexes your code into a semantic-searchable knowledge base so gstack can cite the whole monorepo as context; `/sync-gbrain` rebuilds incrementally.

## Skills Library Overview

- **Think**: `/office-hours` (YC-style 6 forcing questions that rewrite your product framing).
- **Plan**: `/plan-ceo-review` (4 scope modes), `/plan-eng-review` (ASCII data flow / state machines / test matrix), `/plan-design-review` (0-10 scoring + AskUserQuestion), `/plan-devex-review` (DX EXPANSION / POLISH / TRIAGE), `/plan-tune`, `/autoplan` (run the full plan chain).
- **Build**: `/spec`, `/design-consultation`, `/design-shotgun`, `/design-html`, `/ios-clean`, `/ios-sync`.
- **Review**: `/review` (production-grade bug detection + auto-fix), `/investigate` (Iron Law: no fixes without investigation, stop after 3 failed fixes), `/devex-review`, `/design-review`, `/cso` (OWASP + STRIDE).
- **Test**: `/qa` (real browser + auto regression tests), `/qa-only` (report only), `/ios-qa`, `/ios-fix`, `/benchmark`.
- **Ship**: `/ship` (sync main + tests + coverage audit + push + open PR), `/land-and-deploy` (merge + wait CI/deploy + verify), `/canary` (deploy monitoring).
- **Reflect**: `/retro`, `/document-release`, `/document-generate`.
- **Browse & Pair**: `/browse`, `/connect-chrome`, `/open-gstack-browser`, `/setup-browser-cookies`, `/pair-agent`, `/scrape`.
- **Utility**: `/make-pdf`, `/diagram`, `/learn`, `/gstack-upgrade`, `/freeze` / `/unfreeze` / `/guard` / `/careful`, `/hosts`, `/health`, `/codex` (Codex second opinion).

## Installation & Support

gstack supports the following AI editors and platforms (via `./setup` or `--host <name>`):
- [Claude Code](../../claudecode/gstack/INSTALL-en.md)
- [Cursor](../../cursor/gstack/INSTALL-en.md)
- [Codex](../../codex/gstack/INSTALL-en.md)
- [OpenCode](../../opencode/gstack/INSTALL-en.md)
- [OpenClaw](../../openclaw/gstack/INSTALL-en.md)

---
For more information, visit: [GitHub - garrytan/gstack](https://github.com/garrytan/gstack)
