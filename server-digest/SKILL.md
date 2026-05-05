---
name: server-digest
description: |
  消化服务器上的学习记录。当用户提供来自远程服务器的 md 文件或文本内容（AI 对话记录、
  开发调试日志、学习总结等），智能分类并存入本地 Obsidian 知识库，可选同步到 iwiki。
  触发词：整理、记录、消化、归档、ingest、digest + 服务器/学习/笔记/对话。
---

# server-digest - 服务器学习记录消化器

> 将远程服务器上产生的学习记录（AI 对话、调试日志、学习总结）智能归档到本地知识库，并可选同步到 iwiki。

## 触发条件

当用户的输入包含以下意图时激活此 skill：
- "整理一下这个"/"帮我记录"/"消化这段"/"归档" + 内容或文件
- 用户明确提到来自服务器/远程的学习记录
- 用户提供了包含技术学习内容的 md 文件路径或粘贴内容

## 输入格式

两种输入方式：
1. **文件路径**: 用户提供本地文件路径（如 `/tmp/xxx.md` 或拖入的文件）
2. **粘贴内容**: 用户直接在对话中粘贴 markdown 内容

## 处理流程

### Step 1: 读取内容

如果是文件路径，读取文件内容。如果是粘贴内容，直接使用。

### Step 2: 智能分类

分析内容特征，确定归档类型：

| 内容特征 | 分类 | 目标目录 | 文件名格式 |
|----------|------|----------|------------|
| 技术概念学习、AI对话提炼、框架理解 | note | `05-resources/notes/` | `主题-子主题.md` |
| 结构完整、有深度、适合发布 | blog | `05-resources/blog/` | `YYYYMMDD-slug.md` |
| 调试记录、每日开发进度 | daily | `02-daily/YYYY/MM/` | `YYYY-MM-DD-日记.md`（追加） |
| 项目相关的阶段性记录 | project | `03-projects/项目名/` | 按项目组织 |
| 零散想法、未成形的灵感 | inbox | `01-inbox/` | `YYYYMMDD-HHMMSS-描述.md` |

**分类判断规则：**
- 有清晰的知识结构（概念→原理→示例）→ **note**
- 内容 >1000 字且逻辑完整 → 考虑 **blog**（需用户确认）
- 包含"今天"/"调试"/"修复"/"部署" → **daily/project**
- 很短/很碎/无结构 → **inbox**

### Step 3: 向用户确认分类

向用户展示分析结果：
```
📋 内容分析:
- 主题: [识别出的主题]
- 类型: [note/blog/daily/project/inbox]
- 建议标题: [生成的标题]
- 建议标签: [tag1, tag2, ...]
- 目标位置: [目标路径]

确认归档？还是调整分类？
```

### Step 4: 内容处理

根据类型进行不同程度的处理：

- **note**: 如果原文已经写得好（有段落叙述、有思考过程、有干货），保留原样只补 frontmatter。如果原文过于碎片化或结构混乱，则**用段落式写作重新组织**——像给朋友讲故事一样展开，保留核心代码和关键洞察，去掉对话中的废话和重复。绝不要把好的叙述压缩成干巴巴的要点列表。
- **blog**: 在 note 的基础上进一步润色，补充引言和背景、让外人也能看懂，中文撰写，1500-4000 字。风格参考优质技术博客（有人味、有故事线、有代码解析），而不是教科书或文档。
- **daily**: 追加到当日日记的"随记"部分
- **project**: 追加到对应项目目录
- **inbox**: 最少加工，快速存入

### Step 5: 写入本地知识库

使用 MCP obsidian 工具（`mcp__obsidian__write_note`）写入文件，遵循 CLAUDE.md 中的命名规范和 frontmatter 标准。

### Step 6: 询问 iwiki 同步

```
✅ 已存入本地: [文件路径]

是否同步到 iwiki？
1. 同步到「学习记录」
2. 同步到「工作日志」
3. 不同步
```

### Step 7: 同步到 iwiki（如果选择同步）

```bash
# 学习记录
iwiki-cli create --parent 4020235897 --title "标题" --body-file /tmp/content.md --space "~xxsyang"

# 工作日志
iwiki-cli create --parent 4020235583 --title "标题" --body-file /tmp/content.md --space "~xxsyang"
```

iwiki 智能分配规则：
- 技术学习（note/blog）→ 学习记录 (parentid: 4020235897)
- 工作相关（daily/project）→ 工作日志 (parentid: 4020235583)

## iwiki 配置

```
空间 Key: ~xxsyang
空间 ID: 4020150193
根文档 ID: 4020150195
学习记录目录 ID: 4020235897
工作日志目录 ID: 4020235583
```

## 环境依赖

- `iwiki-cli`: PATH 中可用，TOKEN 通过 `$IWIKI_TOKEN` 或 `$TAI_PAT_TOKEN` 提供
- MCP obsidian: 通过 MCPVault 连接本地 vault `/Users/wobushi/yangfu`

## Frontmatter 模板

```yaml
---
title: "自动生成的标题"
date: YYYY-MM-DDTHH:MM:SS+08:00
updated: YYYY-MM-DDTHH:MM:SS+08:00
tags: [自动提取的标签]
categories: [分类]
type: note|blog|daily|project|inbox
status: draft
description: "一句话描述"
source: server  # 标记来源为服务器
---
```

## 示例用法

**用户**: "帮我整理一下这个" + 粘贴了一段关于 vllm DP 的 AI 对话

**Claude**:
```
📋 内容分析:
- 主题: vllm 数据并行 (DP) 机制
- 类型: note（技术概念学习）
- 建议标题: vllm-数据并行机制
- 建议标签: [vllm, DP, 并行计算, 推理框架]
- 目标位置: 05-resources/notes/vllm-数据并行机制.md

确认归档？
```

**用户**: "确认"

**Claude**:
```
✅ 已存入本地: 05-resources/notes/vllm-数据并行机制.md

是否同步到 iwiki？
1. 同步到「学习记录」
2. 同步到「工作日志」  
3. 不同步
```

**用户**: "1"

**Claude**:
```
✅ 已同步到 iwiki「学习记录」
   URL: https://iwiki.woa.com/p/xxxxxxx
```
