# Skills 推荐社区 - 设计文档

**日期**: 2026-03-09  
**状态**: 已批准  
**版本**: 1.0

---

## 1. 项目概述

**Skills 推荐社区** 是一个双向平台：
- **用户端**: 发现和安装适合 AI Agent 框架的技能
- **开发者端**: 贡献技能（前期通过 GitHub 仓库）

### 目标用户
- AI Agent 框架用户（Claude Code/Cursor/OpenCode 等）
- 技能开发者

### 核心功能
1. 技能浏览与搜索（分类、框架筛选）
2. 技能评分与评论
3. 安装指南展示（Markdown 渲染）

---

## 2. 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│                      云服务器 (ECS/EC2)                      │
│  ┌─────────────────┐                         ┌────────────┐ │
│  │    Nginx        │                         │ PostgreSQL │ │
│  │  (反向代理)      │                         │  (数据库)   │ │
│  └────────┬────────┘                         └─────┬──────┘ │
│           │                                        │        │
│  ┌────────▼────────┐                      ┌────────▼──────┐ │
│  │    Next.js      │◄────  HTTP/JSON ────► │   Go + Gin   │ │
│  │   (前端静态)     │                       │   (API 服务)  │ │
│  └─────────────────┘                       └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 技术栈
| 层级 | 技术 | 说明 |
|------|------|------|
| 前端 | Next.js + React | SSR + 静态资源 |
| 后端 | Go + Gin | RESTful API |
| 数据库 | PostgreSQL | 关系型数据库 |
| 部署 | 云服务器 (AWS EC2/阿里云 ECS) | Nginx 反向代理 |
| Markdown 渲染 | react-markdown + remark-gfm | GitHub Flavored Markdown |

### 端口规划
| 服务 | 端口 |
|------|------|
| Nginx | 80/443 |
| Next.js | 3000 |
| Go + Gin | 8080 |
| PostgreSQL | 5432 |

---

## 3. 数据模型

### 3.1 技能表 (skills)
```sql
CREATE TABLE skills (
    id              SERIAL PRIMARY KEY,
    name            VARCHAR(255) NOT NULL,
    description     TEXT NOT NULL,
    category        VARCHAR(100) NOT NULL,
    status          VARCHAR(50) NOT NULL,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP NOT NULL DEFAULT NOW()
);
```

**分类枚举值**: `文档办公`, `设计创意`, `开发测试`, `系统自动化`  
**状态枚举值**: `已验证`, `整理中`

### 3.2 技能框架支持表 (skill_frameworks)
```sql
CREATE TABLE skill_frameworks (
    id              SERIAL PRIMARY KEY,
    skill_id        INTEGER NOT NULL REFERENCES skills(id),
    framework       VARCHAR(50) NOT NULL,
    install_path    VARCHAR(500) NOT NULL,
    UNIQUE(skill_id, framework)
);
```

**框架枚举值**: `Claude Code`, `Cursor`, `OpenCode`, `Codex`, `OpenClaw`, `Qoder`

### 3.3 评分表 (skill_ratings)
```sql
CREATE TABLE skill_ratings (
    id              SERIAL PRIMARY KEY,
    skill_id        INTEGER NOT NULL REFERENCES skills(id),
    user_id         VARCHAR(100) NOT NULL,
    rating          INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE(skill_id, user_id)
);
```

### 3.4 评论表 (skill_comments)
```sql
CREATE TABLE skill_comments (
    id              SERIAL PRIMARY KEY,
    skill_id        INTEGER NOT NULL REFERENCES skills(id),
    user_id         VARCHAR(100) NOT NULL,
    content         TEXT NOT NULL,
    parent_id       INTEGER REFERENCES skill_comments(id),
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP NOT NULL DEFAULT NOW()
);
```

### 3.5 安装统计表 (skill_install_counts)
```sql
CREATE TABLE skill_install_counts (
    id              SERIAL PRIMARY KEY,
    skill_id        INTEGER NOT NULL REFERENCES skills(id) UNIQUE,
    install_count   INTEGER NOT NULL DEFAULT 0,
    last_updated    TIMESTAMP NOT NULL DEFAULT NOW()
);
```

---

## 4. API 设计

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | `/api/skills` | 获取技能列表（支持分类/框架/状态筛选） |
| GET | `/api/skills/:id` | 获取技能详情（含评分、评论、安装指南） |
| GET | `/api/skills/:id/install` | 获取技能安装指南 Markdown |
| POST | `/api/skills/:id/rating` | 提交评分 |
| GET | `/api/skills/:id/comments` | 获取评论列表 |
| POST | `/api/skills/:id/comments` | 提交评论 |
| POST | `/api/skills/:id/install-track` | 记录安装次数 |

### 请求/响应示例

**GET /api/skills**
```json
{
  "data": [
    {
      "id": 1,
      "name": "superpowers",
      "description": "20+ 核心技能，涵盖 TDD、调试和协作模式",
      "category": "开发测试",
      "status": "已验证",
      "frameworks": ["Claude Code", "Cursor", "OpenCode"],
      "avg_rating": 4.8,
      "install_count": 1234,
      "created_at": "2026-03-01T00:00:00Z",
      "updated_at": "2026-03-09T00:00:00Z"
    }
  ],
  "total": 10,
  "page": 1,
  "page_size": 20
}
```

**GET /api/skills/:id**
```json
{
  "id": 1,
  "name": "superpowers",
  "description": "...",
  "category": "开发测试",
  "status": "已验证",
  "frameworks": [...],
  "avg_rating": 4.8,
  "rating_count": 56,
  "install_count": 1234,
  "comments": [...],
  "created_at": "...",
  "updated_at": "..."
}
```

**GET /api/skills/:id/install**
```
Content-Type: text/markdown

# Superpowers Installation Guide

## Claude Code

1. Clone the repository...
```

---

## 5. 前端页面结构

### 5.1 页面路由
```
/pages
├── /index.tsx              # 首页 - 技能列表 + 搜索 + 筛选
├── /skills
│   └── /[id].tsx           # 技能详情页
├── /categories
│   └── /[category].tsx     # 分类页
├── /submit                 # 提交技能 (引导到 GitHub)
└── /about                  # 关于页面
```

### 5.2 核心组件
| 组件 | 说明 |
|------|------|
| `SkillCard` | 技能卡片展示 |
| `SkillList` | 技能列表 + 分页 |
| `SearchFilter` | 搜索和筛选组件 |
| `RatingStars` | 评分展示和提交 |
| `CommentSection` | 评论区 |
| `InstallGuide` | 安装指南 Markdown 渲染 (react-markdown + remark-gfm) |

### 5.3 UI 框架
- **推荐**: shadcn/ui + Tailwind CSS
- **理由**: 现代化设计、组件丰富、易定制

---

## 6. 评论系统设计

### 前期方案（无用户系统）
- 评论者填写昵称（可选）
- 匿名评论 + IP 频率限制（防刷）
- 评论需审核（后台管理或 GitHub Issue）

### 后期方案
- GitHub OAuth 登录（可选）
- 登录用户评论直接显示
- 未登录评论需审核

---

## 7. 技能数据来源

### 同步机制
```
┌─────────────────┐
│  定时任务 (每小时) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ agent-use-skills │
│   仓库读取       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  解析 Markdown   │
│  提取元数据      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  更新 PostgreSQL │
└─────────────────┘
```

### 元数据解析
从 `skills/*.md` 文件中解析：
- 技能名称（H1 标题）
- 描述（首段或 frontmatter）
- 分类（frontmatter 或目录结构）
- 支持框架（目录结构推断）
- 安装指南路径（目录规则）

---

## 8. 项目目录结构

```
agent-use-market/
├── frontend/                    # Next.js 前端
│   ├── src/
│   │   ├── components/          # React 组件
│   │   │   ├── SkillCard.tsx
│   │   │   ├── SkillList.tsx
│   │   │   ├── SearchFilter.tsx
│   │   │   ├── RatingStars.tsx
│   │   │   ├── CommentSection.tsx
│   │   │   └── InstallGuide.tsx
│   │   ├── pages/               # 页面
│   │   │   ├── index.tsx
│   │   │   ├── skills/
│   │   │   ├── categories/
│   │   │   ├── submit.tsx
│   │   │   └── about.tsx
│   │   └── lib/                 # 工具函数
│   │       └── api.ts
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   └── Dockerfile
│
├── backend/                     # Go 后端
│   ├── cmd/
│   │   └── server/
│   │       └── main.go          # 主程序入口
│   ├── internal/
│   │   ├── handlers/            # HTTP handlers
│   │   │   ├── skills.go
│   │   │   ├── ratings.go
│   │   │   └── comments.go
│   │   ├── models/              # 数据模型
│   │   │   ├── skill.go
│   │   │   ├── rating.go
│   │   │   └── comment.go
│   │   ├── repository/          # 数据库访问
│   │   │   └── postgres.go
│   │   └── sync/                # 技能数据同步
│   │       └── sync.go
│   ├── go.mod
│   ├── go.sum
│   └── Dockerfile
│
├── docker-compose.yml           # 本地开发部署
├── deploy/                      # 生产部署配置
│   ├── nginx.conf
│   └── systemd/
│       ├── skills-frontend.service
│       └── skills-backend.service
└── docs/
    └── plans/
        └── 2026-03-09-skills-recommendation-community-design.md
```

---

## 9. 部署方案

### 9.1 开发环境
```bash
# 启动所有服务
docker-compose up -d
```

### 9.2 生产环境
1. 云服务器安装 Docker + Docker Compose
2. 配置 Nginx 反向代理
3. 配置 PostgreSQL 持久化
4. 配置 systemd 服务自启
5. 配置 HTTPS（Let's Encrypt）

### 9.3 环境变量
```bash
# Backend
DATABASE_URL=postgres://user:pass@localhost:5432/skills_db
SKILLS_REPO_PATH=/path/to/agent-use-skills

# Frontend
NEXT_PUBLIC_API_URL=https://api.example.com
```

---

## 10. 开发计划（概要）

### Phase 1: 基础架构
- [ ] 数据库设计与创建
- [ ] Go 后端基础框架
- [ ] Next.js 前端基础框架

### Phase 2: 核心功能
- [ ] 技能列表 API + 页面
- [ ] 技能详情 API + 页面
- [ ] 安装指南渲染

### Phase 3: 社区功能
- [ ] 评分系统
- [ ] 评论系统
- [ ] 安装统计

### Phase 4: 部署与优化
- [ ] 云服务器部署
- [ ] 性能优化
- [ ] SEO 优化

---

## 11. 风险与注意事项

1. **评论审核**: 需要防止垃圾评论，前期可考虑人工审核
2. **数据同步**: 技能数据与 GitHub 仓库的同步策略
3. **安全性**: API 限流、SQL 注入防护、XSS 防护
4. **扩展性**: 未来可能需要用户系统、技能收藏等功能

---

## 12. 下一步

**已批准设计文档，下一步调用 `writing-plans` skill 创建详细实施计划。**
