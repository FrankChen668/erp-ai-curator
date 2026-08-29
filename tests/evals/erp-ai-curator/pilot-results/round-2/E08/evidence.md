# E08 Evidence — Round 2

## 使用的 prompt（原样，未改写）

> Oracle Fusion SCM 我不熟，想找 AI 辅助快速学习模块的高质量方法、教程或 prompt framework。没有好的就明确说没有。

## Artifact 验证（执行 correction D）

| 文件 | 存在 | 非空 | 含最终用户回答 |
|---|---|---|---|
| `round-2/E08/baseline.md` | ✅ | ✅（21,993 B） | ✅ |
| `round-2/E08/with-skill.md` | ✅ | ✅（10,608 B） | ✅ |

两个文件均由独立子代理会话生成后，用 Read 工具逐一复核通过，未出现"调用成功但文件缺失"的情况。

## Session 独立性

- **baseline**：全新启动的独立子代理，只接收原始 prompt，未接触任何 Skill 文件。
- **with-skill**：另一个全新启动的独立子代理，预加载内容仅为 `SKILL.md` 全文；references 按 SKILL.md 加载条件由代理自行打开。两个会话互不共享上下文，未复用 Round-1 输出。

## with-skill 实际 reference 读取顺序（agent 自报 + 产物核对）

1. `references/source-strategy.md` — 开始联网搜索前（多角度关键词、原始来源优先、中英并搜、停止条件）
2. `references/selection-heuristics.md` — 横向比较阶段（核心三问、Task fit、0 推荐判断、Adjacent-option discipline）
3. `references/volatile-fact-check.md` — 风险触发式事实核验阶段（候选涉及免费/价格这一高时效事实）

与 SKILL.md 加载条件一致，未提前批量读取。

## 最终推荐数量

| 组 | 最终推荐数 | 说明 |
|---|---|---|
| baseline | 5（分 A/B/C 三类）+ 1 个自建 prompt 骨架 | A 类含官方 prompt framework、官方博客；B 类含官方模块导览/课程/agent 样例仓库 |
| with-skill | 1（仅"教程"类型） | Oracle 官方 SCM Process Essentials 免费课程；"AI 辅助学习方法 / prompt framework"精确方向明确 0 个够格候选 |

## 实质性事实 / 选择差异（同一 Round 内对比）

1. **Abstain 纪律（本题核心差异）**：用户明确表达"没有好的就明确说没有"，with-skill 应用 **Adjacent-option discipline**——把三组相邻资源（面向资深顾问的 Udemy 课程、Fusion 内置 AI 使用指南、LinkedIn 普通 prompt 列表）逐一判定为"受众/任务错位或不占推荐位"，仅保留 1 个真正落在"教程"类型内的官方免费课程，并明确声明"AI 辅助学习方法/prompt framework 精确方向为 0 推荐"；baseline 将官方 prompt framework、官方博客等也列入推荐位（其自述局限为"不教 SCM 业务、面向 Fusion 内置 AI 配置"），推荐位纪律弱于 with-skill。
2. **MCP Tool 不占推荐位**：with-skill 把 `oracle/skills` 仓库（fusion 域仅为占位 SKILL.md）作为"相邻方向提示"放在推荐表外，未占推荐位——修复了先前版本用 MCP Tool 占推荐位的问题。
3. **事实核验**：两组都对"官方免费课程"做了核验；with-skill 因课程页两次 WebFetch 失败（JS 渲染），按 `volatile-fact-check.md` 升级为强核验，改用官方域搜索摘要 + oracle.com 教育页交叉确认免费性与新手定位，并如实记录"课程正文未能直接抓取"。
4. **0 推荐能力**：两组都敢于保持空缺（baseline 明说"公开域里没有该类资源"；with-skill 对精确方向给 0 推荐），但 with-skill 在"范围内 1 个够格 + 范围外不占位"的边界上更清晰。

## 跨 Round 比较声明

本 evidence 的所有产品结论均只基于 Round 2 内 baseline vs with-skill 配对，未使用 Round-1 数据做任何结论支撑。
