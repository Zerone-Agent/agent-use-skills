# Skills 推荐社区实施计划

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 构建一个 Skills 推荐社区平台，让用户可以浏览、搜索、评分和评论 AI Agent 技能。

**Architecture:** 前后端分离架构，Next.js 前端负责展示，Go + Gin 后端提供 RESTful API，PostgreSQL 存储数据。所有服务部署在同一台云服务器，Nginx 反向代理。

**Tech Stack:** Next.js 14 + React 18, Go 1.21 + Gin, PostgreSQL 15, Tailwind CSS + shadcn/ui, react-markdown + remark-gfm

---

## Phase 1: 基础架构 (预计 2 小时)

### Task 1: 创建项目目录结构

**Files:**
- Create: `frontend/package.json`
- Create: `frontend/tsconfig.json`
- Create: `frontend/tailwind.config.js`
- Create: `frontend/next.config.js`
- Create: `backend/go.mod`
- Create: `docker-compose.yml`

**Step 1: 创建 frontend/package.json**

```json
{
  "name": "skills-community-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "14.1.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-markdown": "^9.0.1",
    "remark-gfm": "^4.0.0",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.2.1"
  },
  "devDependencies": {
    "@types/node": "^20.11.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "autoprefixer": "^10.4.17",
    "eslint": "^8.56.0",
    "eslint-config-next": "14.1.0",
    "postcss": "^8.4.35",
    "tailwindcss": "^3.4.1",
    "typescript": "^5.3.3"
  }
}
```

**Step 2: 创建 frontend/tsconfig.json**

```json
{
  "compilerOptions": {
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./src/*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

**Step 3: 创建 frontend/tailwind.config.js**

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'anthropic-dark': '#141413',
        'anthropic-light': '#faf9f5',
        'anthropic-gray': '#b0aea5',
        'anthropic-border': '#e8e6dc',
        'anthropic-orange': '#d97757',
        'anthropic-blue': '#6a9bcc',
        'anthropic-green': '#788c5d',
      },
      fontFamily: {
        heading: ['Poppins', 'Arial', 'sans-serif'],
        body: ['Lora', 'Georgia', 'serif'],
      },
    },
  },
  plugins: [],
}
```

**Step 4: 创建 frontend/next.config.js**

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
}

module.exports = nextConfig
```

**Step 5: 创建 backend/go.mod**

```go
module github.com/agent-use/skills-community/backend

go 1.21

require (
	github.com/gin-gonic/gin v1.9.1
	github.com/lib/pq v1.10.9
	github.com/joho/godotenv v1.5.1
)
```

**Step 6: 创建 docker-compose.yml**

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: skills_user
      POSTGRES_PASSWORD: skills_pass
      POSTGRES_DB: skills_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./backend/schema.sql:/docker-entrypoint-initdb.d/schema.sql

  backend:
    build: ./backend
    ports:
      - "8080:8080"
    environment:
      DATABASE_URL: postgres://skills_user:skills_pass@postgres:5432/skills_db
    depends_on:
      - postgres

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:8080/api
    depends_on:
      - backend

volumes:
  postgres_data:
```

**Step 7: Commit**

```bash
git add frontend/package.json frontend/tsconfig.json frontend/tailwind.config.js frontend/next.config.js backend/go.mod docker-compose.yml
git commit -m "feat: create project base structure"
```

---

### Task 2: 创建数据库 Schema

**Files:**
- Create: `backend/schema.sql`

**Step 1: 创建完整的数据库 schema**

```sql
-- 技能表
CREATE TABLE skills (
    id              SERIAL PRIMARY KEY,
    name            VARCHAR(255) NOT NULL,
    description     TEXT NOT NULL,
    category        VARCHAR(100) NOT NULL,
    status          VARCHAR(50) NOT NULL,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP NOT NULL DEFAULT NOW()
);

-- 技能框架支持表
CREATE TABLE skill_frameworks (
    id              SERIAL PRIMARY KEY,
    skill_id        INTEGER NOT NULL REFERENCES skills(id) ON DELETE CASCADE,
    framework       VARCHAR(50) NOT NULL,
    install_path    VARCHAR(500) NOT NULL,
    UNIQUE(skill_id, framework)
);

-- 评分表
CREATE TABLE skill_ratings (
    id              SERIAL PRIMARY KEY,
    skill_id        INTEGER NOT NULL REFERENCES skills(id) ON DELETE CASCADE,
    user_id         VARCHAR(100) NOT NULL,
    rating          INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE(skill_id, user_id)
);

-- 评论表
CREATE TABLE skill_comments (
    id              SERIAL PRIMARY KEY,
    skill_id        INTEGER NOT NULL REFERENCES skills(id) ON DELETE CASCADE,
    user_id         VARCHAR(100) NOT NULL,
    content         TEXT NOT NULL,
    parent_id       INTEGER REFERENCES skill_comments(id) ON DELETE CASCADE,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP NOT NULL DEFAULT NOW()
);

-- 安装统计表
CREATE TABLE skill_install_counts (
    id              SERIAL PRIMARY KEY,
    skill_id        INTEGER NOT NULL REFERENCES skills(id) ON DELETE CASCADE UNIQUE,
    install_count   INTEGER NOT NULL DEFAULT 0,
    last_updated    TIMESTAMP NOT NULL DEFAULT NOW()
);

-- 索引
CREATE INDEX idx_skills_category ON skills(category);
CREATE INDEX idx_skills_status ON skills(status);
CREATE INDEX idx_skill_frameworks_skill_id ON skill_frameworks(skill_id);
CREATE INDEX idx_skill_ratings_skill_id ON skill_ratings(skill_id);
CREATE INDEX idx_skill_comments_skill_id ON skill_comments(skill_id);
```

**Step 2: Commit**

```bash
git add backend/schema.sql
git commit -m "feat: add database schema"
```

---

### Task 3: 创建后端主程序入口

**Files:**
- Create: `backend/cmd/server/main.go`
- Create: `backend/internal/handlers/health.go`

**Step 1: 创建 main.go**

```go
package main

import (
	"log"
	"os"

	"github.com/agent-use/skills-community/backend/internal/handlers"
	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {
	godotenv.Load()

	r := gin.Default()

	api := r.Group("/api")
	{
		api.GET("/health", handlers.HealthCheck)
	}

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	log.Printf("Server starting on port %s", port)
	if err := r.Run(":" + port); err != nil {
		log.Fatal(err)
	}
}
```

**Step 2: 创建 health handler**

```go
package handlers

import "github.com/gin-gonic/gin"

func HealthCheck(c *gin.Context) {
	c.JSON(200, gin.H{
		"status": "ok",
	})
}
```

**Step 3: 创建 backend/Dockerfile**

```dockerfile
FROM golang:1.21-alpine

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN go build -o main ./cmd/server

EXPOSE 8080

CMD ["./main"]
```

**Step 4: 测试后端启动**

```bash
cd backend
go run cmd/server/main.go
# Expected: Server starting on port 8080
```

**Step 5: Commit**

```bash
git add backend/cmd/server/main.go backend/internal/handlers/health.go backend/Dockerfile
git commit -m "feat: create backend server entry point"
```

---

### Task 4: 创建前端基础页面

**Files:**
- Create: `frontend/src/app/layout.tsx`
- Create: `frontend/src/app/page.tsx`
- Create: `frontend/src/app/globals.css`
- Create: `frontend/src/components/Header.tsx`

**Step 1: 创建 layout.tsx**

```tsx
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import Header from '@/components/Header'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'AgentUse Skills - AI 技能推荐社区',
  description: '发现和安装适合 AI Agent 框架的技能',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="zh-CN">
      <body className={inter.className}>
        <Header />
        <main className="min-h-screen">{children}</main>
      </body>
    </html>
  )
}
```

**Step 2: 创建 Header 组件**

```tsx
export default function Header() {
  return (
    <header className="border-b border-anthropic-border bg-anthropic-light">
      <div className="container mx-auto px-4 py-4">
        <nav className="flex items-center justify-between">
          <a href="/" className="text-xl font-bold font-heading text-anthropic-dark hover:text-anthropic-orange transition">
            AgentUse Skills
          </a>
          <div className="space-x-6">
            <a href="/" className="font-body text-anthropic-dark hover:text-anthropic-orange transition">
              技能列表
            </a>
            <a href="/about" className="font-body text-anthropic-dark hover:text-anthropic-orange transition">
              关于
            </a>
          </div>
        </nav>
      </div>
    </header>
  )
}
```

**Step 3: 创建首页 page.tsx**

```tsx
export default function Home() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-8">技能推荐社区</h1>
      <p className="text-gray-600 mb-8">
        发现和安装适合 AI Agent 框架的技能
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* 技能卡片将在这里渲染 */}
      </div>
    </div>
  )
}
```

**Step 4: 创建 globals.css**

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=Poppins:wght@400;500;600;700&display=swap');

:root {
  --anthropic-dark: #141413;
  --anthropic-light: #faf9f5;
  --anthropic-gray: #b0aea5;
  --anthropic-border: #e8e6dc;
  --anthropic-orange: #d97757;
  --anthropic-blue: #6a9bcc;
  --anthropic-green: #788c5d;
}

body {
  background-color: var(--anthropic-light);
  color: var(--anthropic-dark);
  font-family: var(--font-lora), Georgia, serif;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-poppins), Arial, sans-serif;
}
```

**Step 5: 测试前端启动**

```bash
cd frontend
npm install
npm run dev
# Expected: Ready in 123ms
```

**Step 6: Commit**

```bash
git add frontend/src/app/layout.tsx frontend/src/app/page.tsx frontend/src/app/globals.css frontend/src/components/Header.tsx
git commit -m "feat: create frontend base layout"
```

---

## Phase 2: 后端 API 开发 (预计 3 小时)

### Task 5: 创建数据模型

**Files:**
- Create: `backend/internal/models/skill.go`
- Create: `backend/internal/models/rating.go`
- Create: `backend/internal/models/comment.go`

**Step 1: 创建 skill 模型**

```go
package models

import "time"

type Skill struct {
	ID          int       `json:"id"`
	Name        string    `json:"name"`
	Description string    `json:"description"`
	Category    string    `json:"category"`
	Status      string    `json:"status"`
	CreatedAt   time.Time `json:"created_at"`
	UpdatedAt   time.Time `json:"updated_at"`
}

type SkillWithFrameworks struct {
	Skill
	Frameworks   []string `json:"frameworks"`
	AvgRating    float64  `json:"avg_rating"`
	InstallCount int      `json:"install_count"`
}
```

**Step 2: 创建 rating 模型**

```go
package models

import "time"

type Rating struct {
	ID        int       `json:"id"`
	SkillID   int       `json:"skill_id"`
	UserID    string    `json:"user_id"`
	Rating    int       `json:"rating"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
}
```

**Step 3: 创建 comment 模型**

```go
package models

import "time"

type Comment struct {
	ID        int       `json:"id"`
	SkillID   int       `json:"skill_id"`
	UserID    string    `json:"user_id"`
	Content   string    `json:"content"`
	ParentID  *int      `json:"parent_id,omitempty"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
}
```

**Step 4: Commit**

```bash
git add backend/internal/models/*.go
git commit -m "feat: create data models"
```

---

### Task 6: 创建数据库连接层

**Files:**
- Create: `backend/internal/repository/postgres.go`

**Step 1: 创建数据库连接**

```go
package repository

import (
	"database/sql"
	"fmt"
	"os"

	_ "github.com/lib/pq"
)

type Database struct {
	DB *sql.DB
}

func NewDatabase() (*Database, error) {
	dbURL := os.Getenv("DATABASE_URL")
	if dbURL == "" {
		return nil, fmt.Errorf("DATABASE_URL not set")
	}

	db, err := sql.Open("postgres", dbURL)
	if err != nil {
		return nil, err
	}

	if err := db.Ping(); err != nil {
		return nil, err
	}

	return &Database{DB: db}, nil
}

func (d *Database) Close() {
	d.DB.Close()
}
```

**Step 2: Commit**

```bash
git add backend/internal/repository/postgres.go
git commit -m "feat: add database connection layer"
```

---

### Task 7: 创建技能列表 API

**Files:**
- Create: `backend/internal/handlers/skills.go`
- Create: `backend/internal/repository/skill_repository.go`

**Step 1: 创建技能仓库接口**

```go
package repository

import "github.com/agent-use/skills-community/backend/internal/models"

type SkillRepository struct {
	db *Database
}

func NewSkillRepository(db *Database) *SkillRepository {
	return &SkillRepository{db: db}
}

func (r *SkillRepository) GetAll(filters map[string]string) ([]models.SkillWithFrameworks, error) {
	query := `
		SELECT s.id, s.name, s.description, s.category, s.status, s.created_at, s.updated_at
		FROM skills s
		WHERE 1=1
	`
	
	if category, ok := filters["category"]; ok {
		query += fmt.Sprintf(" AND s.category = '%s'", category)
	}
	
	if status, ok := filters["status"]; ok {
		query += fmt.Sprintf(" AND s.status = '%s'", status)
	}

	rows, err := r.db.DB.Query(query)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var skills []models.SkillWithFrameworks
	for rows.Next() {
		var s models.Skill
		err := rows.Scan(&s.ID, &s.Name, &s.Description, &s.Category, &s.Status, &s.CreatedAt, &s.UpdatedAt)
		if err != nil {
			return nil, err
		}
		skills = append(skills, models.SkillWithFrameworks{Skill: s})
	}
	return skills, nil
}
```

**Step 2: 创建技能 handler**

```go
package handlers

import (
	"github.com/agent-use/skills-community/backend/internal/repository"
	"github.com/gin-gonic/gin"
)

type SkillsHandler struct {
	repo *repository.SkillRepository
}

func NewSkillsHandler(repo *repository.SkillRepository) *SkillsHandler {
	return &SkillsHandler{repo: repo}
}

func (h *SkillsHandler) List(c *gin.Context) {
	filters := map[string]string{
		"category": c.Query("category"),
		"status":   c.Query("status"),
	}

	skills, err := h.repo.GetAll(filters)
	if err != nil {
		c.JSON(500, gin.H{"error": err.Error()})
		return
	}

	c.JSON(200, gin.H{"data": skills, "total": len(skills)})
}
```

**Step 3: 更新 main.go 注册路由**

```go
// 在 Task 3 的 main.go 基础上添加
skillsHandler := handlers.NewSkillsHandler(repository.NewSkillRepository(db))
api.GET("/skills", skillsHandler.List)
```

**Step 4: Commit**

```bash
git add backend/internal/handlers/skills.go backend/internal/repository/skill_repository.go
git commit -m "feat: implement skills list API"
```

---

## Phase 3: 前端页面开发 (预计 3 小时)

### Task 8: 创建技能列表组件

**Files:**
- Create: `frontend/src/components/SkillCard.tsx`
- Create: `frontend/src/components/SkillList.tsx`

**Step 1: 创建 SkillCard 组件**

```tsx
interface SkillCardProps {
  id: number
  name: string
  description: string
  category: string
  status: string
  frameworks: string[]
  avg_rating?: number
  install_count?: number
}

export default function SkillCard({ name, description, category, status, frameworks, avg_rating, install_count }: SkillCardProps) {
  return (
    <div className="border border-anthropic-border rounded-lg p-6 hover:shadow-lg transition bg-anthropic-light">
      <div className="flex justify-between items-start mb-2">
        <h3 className="text-xl font-semibold font-heading text-anthropic-dark">{name}</h3>
        <span className={`px-2 py-1 text-sm rounded ${status === '已验证' ? 'bg-anthropic-green/20 text-anthropic-green' : 'bg-anthropic-orange/20 text-anthropic-orange'}`}>
          {status}
        </span>
      </div>
      <p className="font-body text-anthropic-gray mb-4">{description}</p>
      <div className="flex items-center gap-2 text-sm font-body text-anthropic-gray">
        <span>{category}</span>
        {avg_rating && (
          <span>⭐ {avg_rating.toFixed(1)}</span>
        )}
        {install_count !== undefined && (
          <span>📥 {install_count}</span>
        )}
      </div>
      <div className="mt-4 flex flex-wrap gap-2">
        {frameworks.map((fw) => (
          <span key={fw} className="px-2 py-1 bg-anthropic-border/30 text-anthropic-dark text-xs rounded font-body">
            {fw}
          </span>
        ))}
      </div>
    </div>
  )
}
```

**Step 2: Commit**

```bash
git add frontend/src/components/SkillCard.tsx
git commit -m "feat: create SkillCard component"
```

---

## Phase 4: 评分评论功能 (预计 2 小时)

### Task 9: 创建评分 API

**Files:**
- Create: `backend/internal/handlers/ratings.go`
- Create: `backend/internal/repository/rating_repository.go`

*(参考 Task 7 的模式实现)*

---

### Task 10: 创建评论 API

**Files:**
- Create: `backend/internal/handlers/comments.go`
- Create: `backend/internal/repository/comment_repository.go`

*(参考 Task 7 的模式实现)*

---

## Phase 5: 部署配置 (预计 1 小时)

### Task 11: 创建 Nginx 配置

**Files:**
- Create: `deploy/nginx.conf`

**Step 1: 创建 Nginx 配置文件**

```nginx
upstream backend {
    server localhost:8080;
}

upstream frontend {
    server localhost:3000;
}

server {
    listen 80;
    server_name your-domain.com;

    location /api {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        proxy_pass http://frontend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

**Step 2: Commit**

```bash
git add deploy/nginx.conf
git commit -m "feat: add nginx configuration"
```

---

## 下一步

**计划完成并保存到** `docs/plans/2026-03-09-skills-recommendation-community-plan.md`

**两种执行方式可选：**

1. **子代理驱动 (当前会话)** - 我为每个任务分配新的子代理，任务间进行代码审查，快速迭代
2. **并行会话 (独立会话)** - 在新会话中使用 executing-plans 执行

**选择哪种方式？**
