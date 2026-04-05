#!/usr/bin/env python3
"""
Initialize a .knowledge/ directory structure in a project.

Usage:
    python init_knowledge.py <project-root> [--lang zh|en]

Creates the full nested knowledge base with template files.
"""

import argparse
import os
import sys
from datetime import datetime


def get_today():
    return datetime.now().strftime("%Y-%m-%d")


def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


# === Template Definitions ===

def index_md(project_name):
    return f"""---
project: {project_name}
created: {get_today()}
updated: {get_today()}
---

# {project_name}

> TODO: 一句话描述项目目标

## 技术栈

- **语言**: TODO
- **框架**: TODO
- **运行环境**: TODO
- **关键依赖**: TODO

## 当前状态

- **阶段**: 🟡 初始化
- **当前焦点**: → [current-focus.md](development/current-focus.md)

## 知识库导航

| 目录 | 说明 | 入口 |
|---|---|---|
| `architecture/` | 系统架构 & 设计决策 | [_INDEX.md](architecture/_INDEX.md) |
| `development/` | 开发进度 & 路线图 | [_INDEX.md](development/_INDEX.md) |
| `conventions/` | 编码约定 & 规范 | [_INDEX.md](conventions/_INDEX.md) |
| `context/` | 领域知识 & 注意事项 | [_INDEX.md](context/_INDEX.md) |
| `journal/` | 开发日志 | [_INDEX.md](journal/_INDEX.md) |

## 关键入口

- 🔥 [当前工作焦点](development/current-focus.md)
- 📋 [开发路线图](development/roadmap.md)
- ⚠️ [已知陷阱](context/gotchas.md)
"""


def section_index(section_name, description, files):
    file_rows = "\n".join(
        f"| [{f['name']}]({f['name']}) | {f['desc']} | {get_today()} |"
        for f in files
    )
    return f"""---
section: {section_name}
updated: {get_today()}
---

# {section_name}

> {description}

## 文件列表

| 文件 | 说明 | 最后更新 |
|---|---|---|
{file_rows}
"""


def architecture_overview():
    return f"""---
created: {get_today()}
updated: {get_today()}
tags: [architecture]
---

# 系统架构总览

> TODO: 描述系统的整体架构

## 组件结构

TODO: 主要组件及其关系

## 数据流

TODO: 核心数据流路径

## 关键约束

TODO: 架构层面的约束条件
"""


def current_focus():
    return f"""---
updated: {get_now()}
---

# 🔥 当前工作焦点

## 正在进行

- [ ] 项目初始化 — 搭建基础结构

## 阻塞项

无

## 下一步

- 定义项目架构
- 建立编码规范

## 本轮对话上下文

> 刚完成知识库初始化，项目处于起步阶段。
"""


def roadmap():
    return f"""---
updated: {get_today()}
tags: [planning, roadmap]
---

# 📋 开发路线图

## 里程碑

### M1: 项目初始化 — {get_today()}
<!-- status: 🟡 进行中 -->

- [x] 初始化知识库
- [ ] 定义项目架构
- [ ] 建立编码规范
"""


def changelog():
    return f"""---
updated: {get_today()}
tags: [changelog]
---

# 📝 变更日志

## {get_today()}

- **[init]** 初始化项目知识库
"""


def gotchas():
    return f"""---
updated: {get_today()}
tags: [pitfalls, debugging]
---

# ⚠️ 已知陷阱 & 踩坑记录

> 暂无记录。开发过程中遇到的坑会自动记录在此。
"""


def glossary():
    return f"""---
updated: {get_today()}
tags: [domain, terminology]
---

# 📖 领域术语表

| 术语 | 定义 | 备注 |
|---|---|---|
| | | |
"""


def dependencies():
    return f"""---
updated: {get_today()}
tags: [dependencies]
---

# 📦 外部依赖 & 注意事项

> 暂无记录。添加外部依赖时会自动记录在此。
"""


def coding_style():
    return f"""---
updated: {get_today()}
tags: [conventions, style]
---

# 🎨 编码规范

> TODO: 根据项目实际情况填写编码规范
"""


def journal_index():
    return f"""---
section: 开发日志
updated: {get_today()}
---

# 开发日志

> 按日期记录的开发工作日志

## 文件列表

| 文件 | 说明 | 最后更新 |
|---|---|---|
| [{get_today()}.md]({get_today()}.md) | 项目初始化 | {get_today()} |
"""


def journal_today():
    return f"""---
date: {get_today()}
tags: [journal]
---

# 开发日志 {get_today()}

## 完成的工作

- 初始化项目知识库 (`.knowledge/` 目录)

## 关键发现

- 无

## 遗留问题

- 需要填写项目概述信息 (`INDEX.md`)
- 需要定义系统架构 (`architecture/overview.md`)

## 决策记录

- 采用嵌套式知识库结构管理项目知识
"""


# === Directory & File Creation ===

STRUCTURE = {
    "INDEX.md": index_md,
    "architecture/_INDEX.md": lambda: section_index(
        "系统架构",
        "系统架构设计、组件关系、ADR 架构决策记录",
        [
            {"name": "overview.md", "desc": "系统架构总览"},
        ]
    ),
    "architecture/overview.md": lambda: architecture_overview(),
    "development/_INDEX.md": lambda: section_index(
        "开发进度",
        "开发路线图、当前焦点、变更日志",
        [
            {"name": "current-focus.md", "desc": "🔥 当前工作焦点"},
            {"name": "roadmap.md", "desc": "开发路线图"},
            {"name": "changelog.md", "desc": "变更日志"},
        ]
    ),
    "development/current-focus.md": lambda: current_focus(),
    "development/roadmap.md": lambda: roadmap(),
    "development/changelog.md": lambda: changelog(),
    "conventions/_INDEX.md": lambda: section_index(
        "编码约定",
        "代码风格、命名规范、项目约定",
        [
            {"name": "coding-style.md", "desc": "编码规范"},
        ]
    ),
    "conventions/coding-style.md": lambda: coding_style(),
    "context/_INDEX.md": lambda: section_index(
        "领域知识",
        "领域术语、已知陷阱、外部依赖注意事项",
        [
            {"name": "glossary.md", "desc": "领域术语表"},
            {"name": "gotchas.md", "desc": "已知陷阱 & 踩坑记录"},
            {"name": "dependencies.md", "desc": "外部依赖 & 注意事项"},
        ]
    ),
    "context/glossary.md": lambda: glossary(),
    "context/gotchas.md": lambda: gotchas(),
    "context/dependencies.md": lambda: dependencies(),
    "journal/_INDEX.md": lambda: journal_index(),
}


def init_knowledge(project_root, project_name=None):
    knowledge_dir = os.path.join(project_root, ".knowledge")

    if os.path.exists(knowledge_dir):
        print(f"⚠️  .knowledge/ already exists at {knowledge_dir}")
        print("   Use --force to reinitialize (will not overwrite existing files)")
        return False

    if project_name is None:
        project_name = os.path.basename(os.path.abspath(project_root))

    # Create directories
    dirs_to_create = [
        "",
        "architecture",
        "architecture/decisions",
        "development",
        "conventions",
        "context",
        "journal",
    ]

    for d in dirs_to_create:
        path = os.path.join(knowledge_dir, d)
        os.makedirs(path, exist_ok=True)
        print(f"  📁 Created {os.path.relpath(path, project_root)}")

    # Create files
    for rel_path, content_fn in STRUCTURE.items():
        full_path = os.path.join(knowledge_dir, rel_path)
        if rel_path == "INDEX.md":
            content = content_fn(project_name)
        else:
            content = content_fn()
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  📄 Created {os.path.relpath(full_path, project_root)}")

    # Create today's journal entry
    today_file = os.path.join(knowledge_dir, "journal", f"{get_today()}.md")
    with open(today_file, "w", encoding="utf-8") as f:
        f.write(journal_today())
    print(f"  📄 Created {os.path.relpath(today_file, project_root)}")

    # Create .gitkeep in decisions (empty dir)
    gitkeep = os.path.join(knowledge_dir, "architecture", "decisions", ".gitkeep")
    with open(gitkeep, "w") as f:
        pass

    print(f"\n✅ Knowledge base initialized at {knowledge_dir}")
    print(f"   Next step: Fill in INDEX.md with project overview information")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a .knowledge/ directory in a project"
    )
    parser.add_argument(
        "project_root",
        help="Path to the project root directory"
    )
    parser.add_argument(
        "--name",
        help="Project name (defaults to directory name)",
        default=None
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow initializing even if .knowledge/ exists (won't overwrite files)"
    )
    args = parser.parse_args()

    project_root = os.path.abspath(args.project_root)
    if not os.path.isdir(project_root):
        print(f"❌ Error: {project_root} is not a valid directory")
        sys.exit(1)

    knowledge_dir = os.path.join(project_root, ".knowledge")
    if args.force and os.path.exists(knowledge_dir):
        print(f"⚠️  --force: Reinitializing (existing files will NOT be overwritten)")
        # In force mode, only create missing files
        for rel_path, content_fn in STRUCTURE.items():
            full_path = os.path.join(knowledge_dir, rel_path)
            if not os.path.exists(full_path):
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                if rel_path == "INDEX.md":
                    content = content_fn(args.name or os.path.basename(project_root))
                else:
                    content = content_fn()
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  📄 Created {os.path.relpath(full_path, project_root)}")
            else:
                print(f"  ⏭️  Skipped {os.path.relpath(full_path, project_root)} (exists)")
        print(f"\n✅ Reinitialization complete")
    else:
        init_knowledge(project_root, args.name)


if __name__ == "__main__":
    main()
