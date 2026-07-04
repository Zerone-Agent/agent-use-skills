# 在 OpenClaw 中安装 Aaron 营销技能库

## 前置条件

- 已安装 [OpenClaw]
- 已安装 Node.js(用于 `npx`)

## 安装

```bash
npx skills add aaron-he-zhu/aaron-marketing-skills
```

安装器会把 69 个技能放入 `.agents/skills/`(项目级;加 `-g` 为全局),并自动链接到 OpenClaw 的技能目录。安装单个技能用 `-s <技能名>`,例如 `-s keyword-research`。

## 验证

向 Agent 提一个营销问题,例如「帮我研究 SaaS 产品的关键词」—— 对应技能会按上下文自动激活。
