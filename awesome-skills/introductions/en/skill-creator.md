# Skill Creator

**Skill Creator** is Anthropic's official skill creation and iterative optimization tool, helping users efficiently create, test, evaluate, and improve AI programming skills (Skills), implementing a complete workflow from conception to deployment.

## Tags

🛠️ Productivity Tools | ✅ Verified

## Core Philosophy

- **Iterative Improvement**: Continuously optimize skill quality through the test-evaluate-improve cycle
- **User Collaboration**: Emphasize human-AI collaboration, involving users in the evaluation process to ensure skills meet expectations
- **Quantitative Evaluation**: Provide benchmark testing and assertion verification to quantify skill performance
- **Description Optimization**: Automatically optimize skill descriptions to improve triggering accuracy

## Key Features & Workflow

1. **Capture Intent**: Understand user requirements, clarify skill goals, trigger conditions, and expected output formats
2. **Interview and Research**: Proactively ask about edge cases, input/output formats, success criteria, and dependencies
3. **Write SKILL.md**: Based on user interview results, fill in skill name, description, and detailed content
4. **Test Cases Design**: Create 2-3 realistic test prompts to verify skill effectiveness
5. **Run and Evaluate**: Run tests with and without skill in parallel, collect quantitative and qualitative data
6. **Feedback and Improve**: Iteratively improve skills based on user feedback and benchmark results
7. **Description Optimization**: Optimize the description field in SKILL.md to improve skill triggering accuracy
8. **Package and Present**: Package the final skill as a .skill file for user installation

## Skills Library Overview

This skill includes the following submodules:

- **agents/**: Subagent instructions
  - `grader.md` — How to evaluate assertions against outputs
  - `comparator.md` — How to conduct blind A/B comparison
  - `analyzer.md` — How to analyze why one version beat another
- **scripts/**: Automation scripts
  - `aggregate_benchmark.py` — Aggregate benchmark test data
  - `run_loop.py` — Run description optimization loop
  - `package_skill.py` — Package skill as .skill file
- **eval-viewer/**: Evaluation viewer
  - `generate_review.py` — Generate interactive HTML evaluation interface
- **references/**: Reference documentation
  - `schemas.md` — JSON structure definitions (evals.json, grading.json, etc.)
- **assets/**: Resource files
  - `eval_review.html` — Evaluation review HTML template

## Installation & Support

Skill Creator supports the following AI editors and platforms:
- [Claude Code](../../claudecode/skill-creator/INSTALL-en.md)
- [Cursor](../../cursor/skill-creator/INSTALL-en.md)
- [Codex](../../codex/skill-creator/INSTALL-en.md)
- [OpenCode](../../opencode/skill-creator/INSTALL-en.md)
- [OpenClaw](../../openclaw/skill-creator/INSTALL-en.md)
- [Zerone](../../zerone/skill-creator/INSTALL-en.md)
- [Qoder](../../qoder/skill-creator/INSTALL-en.md)

---
For more information, visit: [GitHub - agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)