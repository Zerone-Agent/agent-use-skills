# Skill Creator

**Skill Creator** 是 Anthropic 官方提供的技能创建与迭代优化工具，帮助用户高效地创建、测试、评估和改进AI编程技能（Skill），实现从构思到部署的完整工作流。

## 标签

🛠️ 效率工具 | ✅ 已验证

## 核心理念

- **迭代优化 (Iterative Improvement)**：通过测试-评估-改进的循环，持续优化技能质量
- **用户协作 (User Collaboration)**：强调人机协作，让用户参与评估过程以确保技能符合预期
- **量化评估 (Quantitative Evaluation)**：提供基准测试和断言验证，量化技能表现
- **描述优化 (Description Optimization)**：自动优化技能描述，提高触发准确性

## 主要功能与工作流

1. **捕捉意图 (Capture Intent)**：理解用户需求，明确技能的目标、触发条件和预期输出格式
2. **访谈与研究 (Interview and Research)**：主动询问边界情况、输入输出格式、成功标准和依赖项
3. **编写 SKILL.md**：根据用户访谈结果，填写技能名称、描述和详细内容
4. **测试用例设计 (Test Cases)**：创建 2-3 个真实的测试提示，用于验证技能效果
5. **运行与评估 (Run and Evaluate)**：并行运行有技能和无技能的测试，收集定量和定性数据
6. **反馈与改进 (Feedback and Improve)**：基于用户反馈和基准测试结果迭代改进技能
7. **描述优化 (Description Optimization)**：优化 SKILL.md 中的描述字段，提高技能触发准确率
8. **打包与交付 (Package and Present)**：将最终技能打包为 .skill 文件供用户安装

## 技能库概览

该技能包含以下子模块：

- **agents/**：子代理指令
  - `grader.md` — 如何评估断言与输出
  - `comparator.md` — 如何进行盲测 A/B 对比
  - `analyzer.md` — 如何分析版本差异原因
- **scripts/**：自动化脚本
  - `aggregate_benchmark.py` — 聚合基准测试数据
  - `run_loop.py` — 运行描述优化循环
  - `package_skill.py` — 打包技能为 .skill 文件
- **eval-viewer/**：评估查看器
  - `generate_review.py` — 生成交互式 HTML 评估界面
- **references/**：参考文档
  - `schemas.md` — JSON结构定义（evals.json, grading.json 等）
- **assets/**：资源文件
  - `eval_review.html` — 评估审查 HTML 模板

## 安装与支持

Skill Creator 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/skill-creator/INSTALL-zh.md)
- [Cursor](../../cursor/skill-creator/INSTALL-zh.md)
- [Codex](../../codex/skill-creator/INSTALL-zh.md)
- [OpenCode](../../opencode/skill-creator/INSTALL-zh.md)
- [OpenClaw](../../openclaw/skill-creator/INSTALL-zh.md)
- [Zerone](../../zerone/skill-creator/INSTALL-zh.md)
- [Qoder](../../qoder/skill-creator/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)