# Knowledge File Templates

Standard templates for each file type in the `.knowledge/` directory.

## INDEX.md (Top-Level)

```markdown
---
project: <项目名称>
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <项目名称>

> 一句话描述项目目标

## 技术栈

- **语言**: 
- **框架**: 
- **运行环境**: 
- **关键依赖**: 

## 当前状态

<!-- 用 emoji 标记状态: 🟢 正常 | 🟡 进行中 | 🔴 阻塞 -->

- **阶段**: 🟡 <当前阶段描述>
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
```

## _INDEX.md (Sub-Section Index)

```markdown
---
section: <板块名称>
updated: YYYY-MM-DD
---

# <板块名称>

> 本板块包含的内容概述

## 文件列表

| 文件 | 说明 | 最后更新 |
|---|---|---|
| [filename.md](filename.md) | 简短描述 | YYYY-MM-DD |
```

## Architecture Decision Record (ADR)

```markdown
---
id: NNN
title: <决策标题>
status: proposed | accepted | deprecated | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
---

# ADR-NNN: <决策标题>

## 背景

<为什么要做这个决策>

## 决策

<具体选择了什么方案>

## 考虑的替代方案

- **方案 A**: <描述> — 未选择原因
- **方案 B**: <描述> — 未选择原因

## 影响

- <这个决策带来的影响>

## 相关文件

- [相关链接](../path/to/related.md)
```

## current-focus.md

```markdown
---
updated: YYYY-MM-DD HH:MM
---

# 🔥 当前工作焦点

## 正在进行

- [ ] <任务描述> — <简要上下文>
- [ ] <任务描述> — <简要上下文>

## 阻塞项

- <阻塞描述及原因>

## 下一步

- <紧接着要做的事>

## 本轮对话上下文

> <当前对话的关键背景信息，帮助下一轮对话快速衔接>
```

## gotchas.md

```markdown
---
updated: YYYY-MM-DD
tags: [pitfalls, debugging]
---

# ⚠️ 已知陷阱 & 踩坑记录

## [简短标题]

<!-- added: YYYY-MM-DD -->

**现象**: <出了什么问题>

**根因**: <为什么出问题>

**解决方案**: <怎么解决的>

**相关文件**: `path/to/file.py`

---
```

## glossary.md

```markdown
---
updated: YYYY-MM-DD
tags: [domain, terminology]
---

# 📖 领域术语表

| 术语 | 定义 | 备注 |
|---|---|---|
| <term> | <definition> | <optional context> |
```

## journal/YYYY-MM-DD.md

```markdown
---
date: YYYY-MM-DD
tags: [journal]
---

# 开发日志 YYYY-MM-DD

## 完成的工作

- <具体完成了什么>

## 关键发现

- <开发过程中的重要发现>

## 遗留问题

- <未解决的问题，待下次处理>

## 决策记录

- <当天做出的关键决策及原因>
```

## roadmap.md

```markdown
---
updated: YYYY-MM-DD
tags: [planning, roadmap]
---

# 📋 开发路线图

## 里程碑

### M1: <里程碑名称> — <目标日期>
<!-- status: 🟢 完成 | 🟡 进行中 | ⚪ 未开始 -->

- [x] <已完成任务>
- [ ] <待完成任务>

### M2: <里程碑名称> — <目标日期>

- [ ] <待完成任务>

## 长期规划

- <长期目标>
```

## changelog.md

```markdown
---
updated: YYYY-MM-DD
tags: [changelog]
---

# 📝 变更日志

## YYYY-MM-DD

- **[类型]** <变更描述>
  - 影响范围: <affected scope>
  - 相关 ADR: [ADR-NNN](../architecture/decisions/NNN-title.md)
```

## dependencies.md

```markdown
---
updated: YYYY-MM-DD
tags: [dependencies]
---

# 📦 外部依赖 & 注意事项

## <依赖名称> (版本)

- **用途**: <为什么用这个>
- **注意事项**: <已知的坑或限制>
- **文档**: <官方文档链接>
```

## coding-style.md

```markdown
---
updated: YYYY-MM-DD
tags: [conventions, style]
---

# 🎨 编码规范

## 命名约定

- <规则描述>

## 文件组织

- <规则描述>

## 错误处理

- <规则描述>

## 注释风格

- <规则描述>
```
