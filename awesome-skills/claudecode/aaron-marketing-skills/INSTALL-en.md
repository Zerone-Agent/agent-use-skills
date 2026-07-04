# Installing Aaron Marketing Skills for Claude Code

## Prerequisites

- [Claude Code] installed
- Node.js installed (for `npx` support)

## Installation

```bash
npx skills add aaron-he-zhu/aaron-marketing-skills
```

The installer places all 69 skills in `.agents/skills/` (project) — add `-g` for a global install — and links them into Claude Code's skill directory automatically. Install a single skill with `-s <skill-name>`, e.g. `-s keyword-research`.

## Verify

Ask your agent a marketing question, e.g. *"Research keywords for my SaaS product"* — the matching skill activates by context.

## Alternative: full Claude Code plugin (recommended)

```
/plugin marketplace add aaron-he-zhu/aaron-marketing-skills
/plugin install aaron-marketing@aaron
```

The plugin adds the 5 slash commands (`/aaron-marketing:auto` etc.), session hooks, cross-session memory, and the keyless data connectors on top of the 69 skills.
