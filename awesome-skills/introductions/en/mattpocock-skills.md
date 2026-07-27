# Matt Pocock Skills

**Matt Pocock Skills** is a battle-tested skill pack curated from TypeScript educator Matt Pocock's (founder of Total TypeScript) own `.agents/` directory. The skills are intentionally small, easy to adapt, and composable; they work with any model and bring software-engineering fundamentals into AI coding workflows — "skills for real engineers, not vibe coding."

## Tags

💻 Dev & Testing | ✅ Verified

## Core Philosophy

- **Fixes four failure modes**: Built on years of engineering experience, the pack targets the four most common AI agent failures — misalignment, verbosity, broken code, and codebase entropy (ball of mud) — with a reusable workflow for each.
- **Small, hackable, composable**: Each skill has a single responsibility, is independently editable, and works across models. Unlike GSD/BMAD/Spec-Kit, the pack does not take over your process or strip your control.
- **User-invoked vs model-invoked**: A clear two-tier model. User-invoked skills (e.g. `/grill-me`) only fire manually and orchestrate; model-invoked skills (e.g. `tdd`) can be auto-loaded by the agent when the task fits, carrying reusable discipline. User-invoked skills never call each other.
- **Shared language = leverage**: A `CONTEXT.md` plus ADRs capture the domain language so the agent uses one word instead of twenty, saving tokens, improving consistency, and easing code navigation.
- **Feedback loops are the speed limit**: Red-green-refactor, static types, browser access, automated tests — fundamentals beat any flashy tooling.

## Key Features & Workflow

1. **Install once, pick on demand**: 22 active skills span `engineering/` and `productivity/` categories. After install, the agent loads them by context or the user invokes them explicitly.
2. **Router entrypoint `/ask-matt`**: Recommends the right user-invoked skill based on the current situation.
3. **Grilling sessions**: `/grill-me` (non-code) and `/grill-with-docs` (code projects) relentlessly interview you to resolve every branch of the decision tree before any code is written. The latter also updates `CONTEXT.md` and ADRs inline.
4. **Spec → tickets → implementation**: `/to-spec` distills the conversation into a spec → `/to-tickets` breaks it into tracer-bullet tickets (with blocking edges) → `/implement` drives `/tdd` at pre-agreed seams and closes out with `/code-review`.
5. **Architecture governance**: `/improve-codebase-architecture` periodically scans for "deepening opportunities," emits a visual HTML report, and grills through whichever one you pick. `codebase-design` provides shared design vocabulary (deep interfaces, clean seams, testability).
6. **Debugging & recovery**: `diagnosing-bugs` is a disciplined "reproduce → minimise → hypothesise → instrument → fix → regression-test" loop. `resolving-merge-conflicts` resolves conflicts hunk by hunk by tracing each side's intent, never `--abort`.
7. **Auxiliary workflows**: `triage` (state-machine labels on issues), `wayfinder` (split huge uncertain work into "decision tickets" resolved one at a time), `research` (background agent that investigates against primary sources and writes cited markdown), `prototype` (throwaway prototypes for design questions), `handoff` (compact the conversation into a handoff doc), `teach` (multi-session teaching), `writing-great-skills` (meta-reference for writing skills well).

## Skills Library Overview

- **Engineering · user-invoked**: `ask-matt` (router), `grill-with-docs`, `triage`, `improve-codebase-architecture`, `setup-matt-pocock-skills` (one-time per-repo config), `to-spec`, `to-tickets`, `implement`, `wayfinder`.
- **Engineering · model-invoked**: `prototype`, `diagnosing-bugs`, `research`, `tdd`, `domain-modeling`, `codebase-design`, `code-review`, `resolving-merge-conflicts`.
- **Productivity · user-invoked**: `grill-me`, `handoff`, `teach`, `writing-great-skills`.
- **Productivity · model-invoked**: `grilling` (the reusable grilling loop behind `grill-me` and `grill-with-docs`).

## Installation & Support

Matt Pocock Skills supports the following AI editors and platforms:
- [Claude Code](../../claudecode/mattpocock-skills/INSTALL-en.md)
- [Cursor](../../cursor/mattpocock-skills/INSTALL-en.md)
- [Codex](../../codex/mattpocock-skills/INSTALL-en.md)
- [OpenCode](../../opencode/mattpocock-skills/INSTALL-en.md)
- [OpenClaw](../../openclaw/mattpocock-skills/INSTALL-en.md)
- [OpenAgent](../../openagent/mattpocock-skills/INSTALL-en.md)
- [Qoder](../../qoder/mattpocock-skills/INSTALL-en.md)

---
For more information, visit: [GitHub - mattpocock/skills](https://github.com/mattpocock/skills) · [Newsletter](https://www.aihero.dev/s/skills-newsletter)
