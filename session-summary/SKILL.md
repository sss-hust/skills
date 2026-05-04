---
name: session-summary
description: |
  总结当前会话的学习/开发内容，生成结构化 md 文件。适用于服务器上的 Claude Code、
  Codex CLI、Cursor 等 AI 工具会话结束时，将对话中的知识沉淀为可回顾、可分享的文档。
  触发词：总结、summary、回顾、沉淀、记录下来、wrap up。
---

# session-summary - 会话学习总结器

> 在服务器上对话/开发结束时调用，总结本次会话的核心知识，生成结构化 md 文件，方便日后快速回顾和分享给他人。

## 触发条件

- 用户说"总结一下"/"帮我总结"/"wrap up"/"记录下来"
- 会话即将结束，用户想沉淀本次学习内容

## 输出

在当前目录生成 md 文件：`summary-YYYYMMDD-主题slug.md`

## 总结模板

生成的文件包含两部分：**快速回顾**（30 秒看完要点）+ **详细笔记**（深入理解）

```markdown
---
title: "主题标题"
date: YYYY-MM-DDTHH:MM:SS+08:00
tags: [标签1, 标签2]
type: note
status: draft
source: server
session_tool: claude-code|codex|cursor
description: "一句话描述本次学习了什么"
---

# 主题标题

## 快速回顾

> 30 秒回顾本次学习的核心内容

### 一句话总结
[用一句话概括本次学习的核心收获]

### 关键要点
- ✅ 要点 1
- ✅ 要点 2
- ✅ 要点 3
- ✅ 要点 4（最多 5 个）

### 核心结论
[最重要的一个结论或认知更新]

---

## 详细笔记

### 背景与动机
[为什么要学这个？解决什么问题？]

### 核心概念
[本次学习涉及的关键概念，用自己的话解释]

#### 概念 1: xxx
[解释 + 类比]

#### 概念 2: xxx
[解释 + 类比]

### 关键实现/代码
[如果涉及代码，给出核心片段和解释]

```language
// 关键代码，附带注释
```

### 踩坑记录
[遇到了什么问题？怎么解决的？]

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| xxx  | xxx  | xxx      |

### 待深入
- [ ] 还没搞懂的点
- [ ] 后续想探索的方向

## 参考
- [相关链接或文档]
```

## 处理流程

### Step 1: 回顾会话内容

扫描当前会话中的所有对话，识别：
- 学习了哪些技术概念
- 解决了什么问题
- 写了哪些关键代码
- 踩了哪些坑
- 得出了什么结论

### Step 2: 提炼与组织

按照模板结构组织内容：
- **快速回顾**部分：提炼 3-5 个要点，一句话总结
- **详细笔记**部分：保留关键细节、代码片段、踩坑记录
- 用**自己的话**重新表述，而非直接复制对话内容
- 添加**类比和解释**，让不在现场的人也能看懂

### Step 3: 生成文件

```bash
# 文件名格式
summary-YYYYMMDD-主题slug.md

# 示例
summary-20260504-vllm-dp-learning.md
summary-20260504-debug-kvcache-issue.md
```

文件保存在**当前工作目录**（pwd）下。

### Step 4: 输出提示

```
✅ 会话总结已生成: ./summary-20260504-vllm-dp-learning.md

📋 快速回顾:
- [要点1]
- [要点2]
- [要点3]

💡 后续: 将此文件传到本地后，用 server-digest skill 归档到知识库
```

## 写作原则

1. **对未来的自己友好**: 一周后再看，30 秒内能想起来当时学了什么
2. **对他人友好**: 没有参与对话的人也能看懂，不用额外问你
3. **不丢关键细节**: 核心代码、报错信息、解决方案必须保留
4. **不灌水**: 去除对话中的寒暄、试错过程，只保留有价值的内容
5. **标记未完成**: 没搞懂的明确标 `[ ]`，下次继续

## 与 server-digest 的配合

本 skill 在服务器端生成 md 文件 → 用户通过 scp/手动方式传到本地 → 本地用 server-digest skill 智能归档到 Obsidian 知识库 + 可选同步 iwiki。

```
[服务器] session-summary → summary-xxx.md
                ↓ (scp / 手动传输)
[本地] server-digest → 05-resources/notes/ + iwiki
```

## 示例

**用户**: "总结一下今天学的 vllm DP"

**输出文件** `summary-20260504-vllm-dp.md`:

```markdown
---
title: "vllm 数据并行 (DP) 机制"
date: 2026-05-04T15:30:00+08:00
tags: [vllm, DP, 并行计算, 分布式推理]
type: note
status: draft
source: server
session_tool: claude-code
description: "学习 vllm 中 DP 的配置、调度和与 TP/PP 的组合方式"
---

# vllm 数据并行 (DP) 机制

## 快速回顾

### 一句话总结
DP 通过多个 replica 分流请求来降低单机 KV Cache 压力，replica 间完全独立不通信。

### 关键要点
- ✅ DP 的核心目的是分流请求，降低 KV Cache 压力
- ✅ 每个 replica 有独立的 Scheduler / BlockManager / KV Cache
- ✅ 稠密模型的 DP replica 间不需要通信
- ✅ 请求路由策略：均分 或 prefix 命中优先
- ✅ DP + TP + PP 叠加时，world_size = TP × PP × DP

### 核心结论
DP 是最"廉价"的并行方式——replica 间零通信，只要有足够的卡就能线性扩展吞吐。

---

## 详细笔记
...
```
