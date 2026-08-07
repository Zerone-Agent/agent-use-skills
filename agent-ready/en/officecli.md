# OfficeCLI - Agent-Ready Certification

**OfficeCLI** has officially passed the **Agent-Ready** certification!

OfficeCLI is the world's first Office suite purpose-built for AI agents — enabling them to create, read, edit, and render Word, Excel, and PowerPoint documents with a single command. Open-source, single binary, no Office installation required.

## Certification Highlights

- **AI-Native from Day One**: Designed specifically for AI Agent consumption — path-based addressing, structured JSON output, progressive complexity (L1 → L2 → L3)
- **Zero Dependencies**: Single self-contained binary with embedded .NET runtime, cross-platform (macOS / Linux / Windows)
- **Built-in Rendering Engine**: Agents can *see* their output — `view html`, `view screenshot`, `watch` (live preview) — no Office required, works in CI / Docker / headless environments
- **150+ Excel Functions Auto-Evaluated**: Write `=SUM(A1:A2)`, get the computed value immediately — no round-trip through Office
- **11 Specialized Sub-skills**: Academic papers, pitch decks, Morph animations, 3D presentations, financial models, data dashboards, and more
- **Built-in MCP Server**: Register with one command — `officecli mcp claude` / `officecli mcp cursor` / `officecli mcp vscode`
- **Template Merge & Round-trip Dump**: `merge` replaces `{{key}}` placeholders; `dump` serializes documents into replayable batch JSON

## Why is it Agent-Ready?

OfficeCLI successfully meets all the core criteria of the Agent-Ready certification:

- **Atomic Action Exposure**: Core features fully exposed via CLI commands — `create`, `view`, `get`, `set`, `add`, `remove`, `move`, `swap`, `query`, `batch`, `merge`, `dump`, `watch`, `validate` — no UI interaction required. Three-layer architecture: L1 semantic views, L2 DOM operations, L3 raw XML fallback.
- **Structured Feedback**: All commands support `--json` with consistent schemas. Structured error codes (`not_found`, `invalid_value`, `unsupported_property`) include suggestions and valid ranges — agents self-correct without human intervention.
- **Security Guardrails**: `validate` checks against OpenXML schema; `view issues` enumerates formatting, content, and structural problems; `watch` provides live preview for human review before final delivery.
- **Verified Integration**: Extensively tested across Claude Code, Cursor, Codex, OpenCode, OpenClaw, Zerone, Qoder, and more. Auto-detects AI tooling during installation and configures itself.

## Core CLI Commands

| Command | Description |
|---------|-------------|
| `officecli create <file>` | Create blank .docx / .xlsx / .pptx |
| `officecli view <file> <mode>` | View content (outline / text / annotated / stats / issues / html / screenshot) |
| `officecli get <file> <path>` | Get element and children (`--json`, `--depth N`) |
| `officecli query <file> <selector>` | CSS-like query (`[attr=value]`, `:contains()`, `:has()`) |
| `officecli set <file> <path> --prop ...` | Modify element properties |
| `officecli add <file> <parent> --type ...` | Add element (or clone with `--from`) |
| `officecli remove <file> <path>` | Remove an element |
| `officecli move <file> <path> --to ...` | Move element |
| `officecli batch <file>` | Multiple operations in one save cycle |
| `officecli merge <template> <output> <data>` | Template merge — replace `{{key}}` placeholders |
| `officecli dump <file>` | Serialize to replayable batch JSON |
| `officecli watch <file>` | Live HTML preview with auto-refresh |
| `officecli validate <file>` | Validate against OpenXML schema |
| `officecli mcp <platform>` | Register MCP server for AI tool integration |

## Comparison

| Feature | OfficeCLI | python-docx / openpyxl | Microsoft Office |
|---------|-----------|----------------------|------------------|
| AI-native CLI + JSON | ✓ | ✗ | ✗ |
| Zero install (single binary) | ✓ | ✗ (Python + pip) | ✗ |
| Word + Excel + PowerPoint | ✓ | Separate libs | ✓ |
| Built-in rendering engine | ✓ | ✗ | ✗ |
| Template merge (`{{key}}`) | ✓ | ✗ | ✗ |
| Live preview | ✓ | ✗ | ✗ |
| Headless / CI | ✓ | ✓ | ✗ |

---

- [OfficeCLI GitHub Repository](https://github.com/iOfficeAI/OfficeCLI)
- [OfficeCLI Official Website](https://officecli.ai)
- [View OfficeCLI Full Documentation](../../awesome-skills/introductions/en/officecli.md)
