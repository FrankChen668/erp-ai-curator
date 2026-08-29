# E01 Evidence — Round 2

## 使用的 prompt（原样，未改写）

> 我想给 SAP/Oracle 实施顾问找能用 Claude Code 或类似 Agent 生成可编辑 draw.io 业务流程图的 AI Skill/实操资源。少而精，中文有高质量的可以优先。

## Artifact 验证（执行 correction D）

| 文件 | 存在 | 非空 | 含最终用户回答 |
|---|---|---|---|
| `round-2/E01/baseline.md` | ✅ | ✅（11,124 B） | ✅ |
| `round-2/E01/with-skill.md` | ✅ | ✅（9,495 B） | ✅ |

两个文件均由独立子代理会话生成后，用 Read 工具逐一复核通过，未出现"调用成功但文件缺失"的情况。

## Session 独立性

- **baseline**：全新启动的独立子代理，只接收原始 prompt，未接触任何 Skill 文件；产物中无 `erp-ai-curator` / references 痕迹。
- **with-skill**：另一个全新启动的独立子代理，预加载内容仅为 `SKILL.md` 全文；references 文件按 SKILL.md 的加载条件由代理自行用 Read 打开。两个会话互不共享上下文，未复用 Round-1 输出。

## with-skill 实际 reference 读取顺序（agent 自报 + 产物核对）

1. `references/source-strategy.md` — 开始联网搜索前（设计关键词与来源优先级）
2. `references/selection-heuristics.md` — 第一轮搜索后、出现多候选需横向取舍时
3. `references/volatile-fact-check.md` — 推荐含"安装与配置 / draw.io Desktop 依赖 / 版本要求"时

与 SKILL.md 加载条件一致，未提前批量读取。

## 最终推荐数量

| 组 | 最终推荐数 | 说明 |
|---|---|---|
| baseline | 5 | 官方插件 + 中文增强 fork + 官方提示词 + BPMN 规范 + 实操避坑（另附说明） |
| with-skill | 2 | jgraph/drawio-mcp（官方插件）+ Agents365-ai/drawio-skill（社区增强） |

## 实质性事实 / 选择差异（同一 Round 内对比）

1. **推荐收敛**：baseline 给 5 个资源（含 2 个官方文档类 + 3 个 Skill/教程类），with-skill 收敛为 2 个（官方插件 + 1 个社区增强 Skill），符合 0–2 契约。
2. **对官方能力的判断路径不同**：baseline 直接判定"官方插件只覆盖通用 draw.io 知识、没有 BPMN/泳道专门规范"，并据此把第三方 BPMN/泳道类资源列为补充；with-skill 对官方插件与候选均执行 Whole-resource check（打开官方 README 与插件目录确认能力边界），再决定社区增强 Skill 是否构成独立增量价值（BPMN/泳道预设 + 中文文档），未基于"官方缺 X"这一未经验证的缺口推荐重叠资源。
3. **中文侧处理一致**：两组均判定中文高质量内容为转载/无原始出处，未占推荐位；with-skill 额外把推荐 2 的 README_CN.md 作为同等质量下的中文 tie-breaker 计入理由。
4. **事实核验**：with-skill 显式触发 `volatile-fact-check.md` 核验安装命令与依赖（draw.io Desktop、版本 ≥30），结论来自 jgraph 与 Agents365-ai 官方仓库 README 原文，未发现与第三方冲突；baseline 也回官方仓库核验了安装方式改版，但未形成独立的核验环节记录。

## 跨 Round 比较声明

本 evidence 的所有产品结论均只基于 Round 2 内 baseline vs with-skill 配对，未使用 Round-1 数据做任何结论支撑。
