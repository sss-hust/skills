---
name: project-knowledge
description: >
  This skill manages a nested, hierarchical knowledge base within the project repository
  (`.knowledge/` directory) to enable efficient knowledge sharing across multiple AI agents
  and conversation turns. This skill should be used when: (1) starting a new conversation
  on an existing project — to quickly onboard by reading the knowledge base; (2) during
  development — to automatically persist valuable discoveries, decisions, and context;
  (3) when the user explicitly asks to initialize, read, or update project knowledge.
  Trigger words include: knowledge, 知识库, onboard, context, 上下文, project-knowledge,
  /knowledge, /init-knowledge.
---

# Project Knowledge

A nested, hierarchical knowledge management system that lives inside the project repository,
enabling multi-agent and multi-turn conversation knowledge sharing.

## Core Principles

1. **嵌套式结构** — 信息分层组织，每层有 `_INDEX.md` 作为入口，避免单文件信息过载
2. **渐进式加载** — 先读 `INDEX.md` 获取全局概览，再按需深入子目录
3. **自动写入** — 工作过程中发现关键信息时主动写入对应文件
4. **手动触发读取** — 新对话开始时用户触发冷启动读取

## Directory Structure

```
.knowledge/
├── INDEX.md                     # 项目总入口：概述 + 技术栈 + 当前状态 + 子目录指引
├── architecture/                # 系统架构 & 设计决策
│   ├── _INDEX.md                # 架构板块索引
│   ├── overview.md              # 系统架构总览
│   └── decisions/               # ADR (Architecture Decision Records)
│       └── NNN-title.md         # 单条决策记录
├── development/                 # 开发进度 & 路线图
│   ├── _INDEX.md                # 开发板块索引
│   ├── roadmap.md               # 整体开发路线
│   ├── current-focus.md         # 🔥 当前工作焦点（最高频更新文件）
│   └── changelog.md             # 关键变更日志
├── conventions/                 # 编码约定 & 规范
│   ├── _INDEX.md                # 约定板块索引
│   └── coding-style.md          # 代码风格约定
├── context/                     # 领域知识 & 注意事项
│   ├── _INDEX.md                # 上下文板块索引
│   ├── glossary.md              # 领域术语表
│   ├── gotchas.md               # 已知陷阱 & 踩坑记录
│   └── dependencies.md          # 外部依赖 & 注意事项
└── journal/                     # 开发日志（按日期）
    ├── _INDEX.md                # 日志板块索引
    └── YYYY-MM-DD.md            # 按日期的开发日志
```

## Workflow: Reading Knowledge (Cold Start)

When a user triggers knowledge reading (e.g., `/knowledge`, "读一下项目知识库", "帮我了解这个项目"),
follow this progressive loading protocol:

### Phase 1: Global Overview

1. Read `.knowledge/INDEX.md` — obtain project name, tech stack, current status, and directory map
2. Read `.knowledge/development/current-focus.md` — understand what is actively being worked on
3. Summarize findings to the user in a concise briefing

### Phase 2: On-Demand Deep Dive

Based on the current task, selectively read deeper files:

| Task Type | Files to Read |
|---|---|
| Implementing a feature | `architecture/overview.md` + `conventions/coding-style.md` |
| Debugging | `context/gotchas.md` + `architecture/overview.md` |
| Architecture design | `architecture/decisions/` directory listing, then relevant ADRs |
| Understanding progress | `development/roadmap.md` + `development/changelog.md` |
| Onboarding (full) | All `_INDEX.md` files across all subdirectories |

### Phase 3: Journal Check (Optional)

If recent context is important, read the latest 1-2 journal entries from `journal/`.

## Workflow: Writing Knowledge (Auto-Persist)

During any conversation, when any of the following events occur, proactively write to the
corresponding knowledge file. **Always append, never overwrite existing content** unless
explicitly correcting an error.

### Auto-Write Triggers

| Event | Target File | Action |
|---|---|---|
| Architecture decision made | `architecture/decisions/NNN-title.md` | Create new ADR file |
| System design discussed/changed | `architecture/overview.md` | Update relevant section |
| Bug discovered with root cause | `context/gotchas.md` | Append new entry |
| New domain term encountered | `context/glossary.md` | Append definition |
| Coding convention established | `conventions/coding-style.md` | Append rule |
| Milestone completed | `development/changelog.md` | Append entry |
| Current focus shifted | `development/current-focus.md` | Update (overwrite is OK here) |
| Significant work session done | `journal/YYYY-MM-DD.md` | Create or append daily entry |
| New dependency added/quirk found | `context/dependencies.md` | Append entry |
| Development plan changed | `development/roadmap.md` | Update relevant section |

### Write Format Guidelines

- **Frontmatter**: Every knowledge file should have YAML frontmatter with `created`, `updated`, and `tags`
- **Append marker**: When appending, add a timestamp comment `<!-- updated: YYYY-MM-DD HH:MM -->`
- **Keep atomic**: Each entry should be self-contained and understandable without reading other files
- **Cross-reference**: Use relative links `[overview](../architecture/overview.md)` to connect related knowledge
- **Language**: Match the project's primary language (follow user preference)

### Write Notification

After writing knowledge, briefly notify the user:
> 📝 已更新知识库：`.knowledge/context/gotchas.md` — 记录了 [简短描述]

## Workflow: Initializing Knowledge Base

When a user asks to initialize project knowledge (e.g., `/init-knowledge`, "帮我初始化知识库"),
run the initialization script:

```bash
python <skill-path>/scripts/init_knowledge.py <project-root>
```

The script creates the full `.knowledge/` directory tree with template files.
After initialization, guide the user to fill in `INDEX.md` with project overview information.

If the script is unavailable, manually create the directory structure following the templates
in `references/file-templates.md`.

## Workflow: Updating INDEX Files

After creating or modifying any knowledge file, check if the parent `_INDEX.md` needs updating.
Each `_INDEX.md` should list all files in its directory with one-line descriptions.
The top-level `INDEX.md` should reflect the overall project state.

## File Templates

Refer to `references/file-templates.md` for the standard templates for each file type.
These templates define the expected structure and frontmatter format.

## Workflow: Knowledge Audit

When the user asks to audit or review the knowledge base ("审查知识库", "knowledge audit"):

1. List all files in `.knowledge/` recursively
2. Check each file's `updated` frontmatter date
3. Flag files not updated in the last 30 days as potentially stale
4. Report a summary with recommendations for what to update or archive
