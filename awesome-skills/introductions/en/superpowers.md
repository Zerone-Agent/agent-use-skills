# Superpowers

**Superpowers** is an agentic skills framework and software development methodology designed for AI coding agents. Built on a system of composable "skills," it aims to elevate AI assistants from simple code generators to mature software engineers through standardized workflows.

## Core Philosophy
The design of Superpowers emphasizes:
- **Test-Driven Development (TDD)**: Write tests first; always verify the correctness of the code.
- **Systematic over Ad-hoc**: Use standardized processes instead of guessing.
- **Complexity Reduction**: Keep simplicity as the primary goal.
- **Evidence over Claims**: Verification is required before declaring success.

## Key Features & Workflow
Superpowers manages the complete development lifecycle:

1. **Brainstorming**: Activates before writing code. Refines ideas through questions, explores alternatives, and creates a validated design document.
2. **Git Worktrees**: Creates an isolated workspace after design approval to ensure a clean environment and a solid test baseline.
3. **Writing Plans**: Breaks work into bite-sized tasks (2-5 minutes each), each with exact file paths, complete code, and verification steps.
4. **Subagent-Driven Development**: Dispatches subagents to execute tasks with a two-stage review process (spec compliance and code quality).
5. **Enforced TDD**: Implements a strict "RED-GREEN-REFACTOR" cycle. Any code written before tests is automatically deleted to ensure pure TDD.
6. **Code Review**: Automated reviews occur between tasks; critical issues block further progress.
7. **Finishing a Development Branch**: Verifies all tests and provides options to merge, create a PR, or clean up the environment.

## Skills Library Overview
- **Testing/Debugging**: Systematic debugging, RED-GREEN-REFACTOR cycles, and verification-before-completion.
- **Collaboration/Planning**: Socratic design refinement, detailed plan writing, and parallel subagent dispatching.
- **Meta Skills**: Guidelines for creating new skills (`writing-skills`) and the system manual.

## Installation & Support
Superpowers supports major AI-powered editors and platforms:
- [Claude Code](../../claudecode/superpowers/INSTALL-en.md)
- [Cursor](../../cursor/superpowers/INSTALL-en.md)
- [Codex](../../codex/superpowers/INSTALL-en.md)
- [OpenCode](../../opencode/superpowers/INSTALL-en.md)


---
For more information, visit: [GitHub - obra/superpowers](https://github.com/obra/superpowers)
