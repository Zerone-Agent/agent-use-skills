# WeWrite

**WeWrite** 是一款专为微信公众号打造的全流程 AI 写作助手，从热点抓取到草稿箱推送，一句话即可完成。

## 标签

🗂️ 文档与办公 | 🔍 待验证

## 核心哲学

- **全流程自动化**：一句话触发 8 个步骤完整流程，从选题到发布零人工干预
- **真实信息锚定**：WebSearch 采集真实数据/引述/案例，禁止编造，素材来源可追溯
- **人机协作增强**：AI 初稿 + 2-3 个编辑锚点，3-5 分钟加入个人观点，让文章从"AI 生成"变成"你的作品"
- **风格飞轮学习**：导入范文建立风格库，每次修改后自动学习，越用越像你的写作风格
- **降级容错设计**：每一步都有降级方案，配置缺失也不阻断流程

## 核心能力与工作流

### 1. 热点抓取与选题评分
- **多平台热点**：微博 + 头条 + 百度实时热搜，Python 脚本抓取
- **SEO 量化评分**：百度 + 360 搜索关键词热度分析
- **智能选题**：生成 10 个选题 × 3 维度评分，历史去重避免重复

### 2. 框架生成与素材采集
- **7 套写作骨架**：痛点型、故事型、清单型、对比型、热点解读型、纯观点型、复盘型
- **真实素材采集**：WebSearch 自动采集 5-8 条真实素材（具名来源 + 具体数据/引述/案例）
- **内容增强策略**：按框架类型自动匹配——角度发现/密度强化/细节锚定/真实体感

### 3. 智能写作与风格注入
- **维度随机化**：2-3 个表达维度随机激活（叙事视角/时间线/类比域/情绪基调/节奏）
- **5 套写作人格**：midnight-friend（极度口语化）、warm-editor（温暖叙事）、industry-observer（中性分析）、sharp-journalist（犀利简洁）、cold-analyst（冷静克制）
- **范文风格库**：导入已发布文章，自动注入你的风格指纹（句长节奏、情绪表达、转折方式）
- **编辑锚点**：在关键位置标记"在这里加一句你自己的话"

### 4. SEO 优化与质量验证
- **SEO 策略**：3 个备选标题 + 摘要（≤40 字）+ 5 标签 + 关键词密度优化
- **质量检查**：11 项检测（句长方差、词汇温度、段落节奏、情绪极性、真实锚定等）
- **定向修复**：不达标项自动定位具体段落/句子，1-2 轮修复

### 5. 视觉 AI 配图
- **封面生成**：3 组创意提示词，提取 3-5 个具体实体，保证画面可识别性
- **内文配图**：3-6 张配图（infographic/scene/flowchart/comparison/framework/timeline）
- **风格一致性**：封面确认后提取视觉锚点，全文配图保持色板和调性一致

### 6. 排版引擎与发布
- **16+ 排版主题**：professional-clean、tech-modern、warm-editorial、sspai、github 等
- **微信兼容修复**：CJK-Latin 自动加空格、加粗标点外移、外链转脚注、暗黑模式适配
- **容器语法**：`:::dialogue`、`:::timeline`、`:::callout`、`:::quote` 支持复杂排版
- **草稿箱推送**：直接推送至微信公众号草稿箱，或本地 HTML 预览

### 7. 效果复盘与风格学习
- **数据回填**：微信数据分析 API 回填阅读数据，统计哪种框架/策略表现最好
- **学习飞轮**：每次编辑后说"学习我的修改"，自动提取修改模式加入 playbook
- **排版学习**：从任意公众号文章 URL 提取排版主题
- **文章采集**：从公众号 URL 提取正文为 Markdown，导入范文库

## 技能库概览

### 核心脚本
- **数据采集**：`fetch_hotspots.py`（多平台热点）、`seo_keywords.py`（SEO 分析）、`fetch_stats.py`（微信数据回填）
- **风格学习**：`extract_exemplar.py`（范文风格提取）、`learn_edits.py`（学习修改）、`learn_theme.py`（学习排版）
- **质量检查**：`humanness_score.py`（11 项质量检测）
- **工具链**：`build_playbook.py`（生成 Playbook）、`diagnose.py`（配置检查）

### 排版工具
- **CLI 工具**：`toolkit/cli.py`（preview/publish/gallery/themes/image-post）
- **主题引擎**：16+ YAML 主题，支持暗黑模式
- **微信 API**：`publisher.py`、`wechat_api.py`（草稿箱推送、图片上传）
- **图片生成**：`image_gen.py`（9 个 provider，自动 fallback）

### 参考文档
- **写作规范**：`writing-guide.md`、`frameworks.md`、`content-enhance.md`
- **SEO 规则**：`seo-rules.md`、`topic-selection.md`
- **视觉规范**：`visual-prompts.md`
- **微信限制**：`wechat-constraints.md`
- **流程文档**：`onboard.md`、`learn-edits.md`、`effect-review.md`

## 安装与支持

WeWrite 支持以下 AI 编辑器和平台：

- [Claude Code](../../claudecode/wewrite/INSTALL-zh.md)
- [OpenClaw](../../openclaw/wewrite/INSTALL-zh.md)
- [Cursor](../../cursor/wewrite/INSTALL-zh.md)
- [Codex](../../codex/wewrite/INSTALL-zh.md)
- [OpenCode](../../opencode/wewrite/INSTALL-zh.md)
- [Zerone](../../zerone/wewrite/INSTALL-zh.md)
- [Qoder](../../qoder/wewrite/INSTALL-zh.md)

---
更多信息，请访问：[GitHub - oaker-io/wewrite](https://github.com/oaker-io/wewrite)
