# Impeccable

**Impeccable** is an AI design direction skill built by Paul Bakaus (GDE, ex-Google). It evolved from Anthropic's official frontend-design skill into a single `/impeccable` entrypoint with 23 sub-commands, 60 deterministic detector rules, live browser iteration, and native hook integration.

## Tags

🎨 Design & Creativity | 🔍 Pending Verification

## Core Philosophy

- **Reject the LLM default aesthetic**: Every model was trained on the same SaaS templates — Inter everywhere, purple-to-blue gradients, cards nested in cards, gray text on colored backgrounds, the rounded-square icon tile. Impeccable's 60 deterministic detector rules surface every one of these "AI tells".
- **The brief wins**: Honor pinned aesthetics, eras, materials, fonts, and palettes even when they conflict with a saturated-pattern warning. Redirecting a clear brief toward your taste is failure.
- **Brand vs Product dual track**: `/impeccable init` distinguishes brand (marketing/landing/portfolio) from product (app UI/dashboard/tool); every later command reads this context.
- **Four visitor modes**: Persuade, Operate, Read, Experience — chosen by what visitor success looks like on that surface, not by product category.
- **Refinement preserves; redesign replaces**: Polish keeps identity and copy; redesign treats the old look as evidence and anti-reference.
- **Bounded verification, not open-ended self-QA**: Build fully → inspect once with a batched round → fix everything in one batch → confirm with at most one more round. Open-ended self-QA burns money doing worse.

## Key Features & Workflow

1. **One install, one entrypoint**: `npx impeccable install` auto-detects harness folders, writes PRODUCT.md / DESIGN.md context, and installs a provider-native hook. After that everything goes through `/impeccable <command>`.
2. **23 commands**: Build (init / shape / craft / document / extract), Evaluate (critique / audit), Refine (polish / bolder / quieter / distill / harden / onboard), Enhance (animate / colorize / typeset / layout / delight / overdrive), Fix (clarify / adapt / optimize), Iterate (live).
3. **60 deterministic detectors**: Run `npx impeccable detect src/` from the CLI or browser extension with no LLM and no API key. Covers AI slop (side-tab borders, purple gradients, bounce easing, dark glows) and general quality (line length, padding, touch targets, skipped headings).
4. **Live browser iteration**: `/impeccable live` enters visual variant mode — pick elements in the browser, generate alternatives, apply changes.
5. **Hook integration**: Installs a provider-native hook on Claude Code, GitHub Copilot, Codex, Cursor, and Grok Build that surfaces design anti-patterns on direct UI edits (Cursor blocks pre-write, others report post-edit and on Stop).
6. **Pin shortcuts**: `/impeccable pin audit` creates a standalone `/audit` shortcut.

## Skills Library Overview

- **Build**: `init` (write PRODUCT.md), `document` (generate DESIGN.md from code), `extract` (pull tokens & components), `shape` (plan UX/UI before code), `craft` (deprecated alias).
- **Evaluate**: `critique` (UX review with heuristic scoring), `audit` (a11y / perf / responsive checks).
- **Refine**: `polish` (final pass), `bolder` (amplify safe designs), `quieter` (tone down loud designs), `distill` (strip to essence), `harden` (errors / i18n / edge cases), `onboard` (first-run / empty states / activation).
- **Enhance**: `animate` (motion), `colorize` (strategic color), `typeset` (typography hierarchy), `layout` (spacing & rhythm), `delight` (memorable touches), `overdrive` (technically extraordinary effects).
- **Fix**: `clarify` (UX copy), `adapt` (device adaptation), `optimize` (UI performance).
- **Iterate**: `live` (browser-embedded visual variants).

## Installation & Support

Impeccable supports the following AI editors and platforms (via `npx impeccable install`):
- [Claude Code](../../claudecode/impeccable/INSTALL-en.md)
- [Cursor](../../cursor/impeccable/INSTALL-en.md)
- [Codex](../../codex/impeccable/INSTALL-en.md)
- [OpenCode](../../opencode/impeccable/INSTALL-en.md)
- [Qoder](../../qoder/impeccable/INSTALL-en.md)

---
For more information, visit: [impeccable.style](https://impeccable.style) · [GitHub - pbakaus/impeccable](https://github.com/pbakaus/impeccable)
