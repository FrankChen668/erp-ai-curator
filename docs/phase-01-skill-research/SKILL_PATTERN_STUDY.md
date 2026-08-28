# 21 个开源 Agent Skill 设计模式研究

> 研究日期：2026-08-28  
> 目的：研究设计逻辑，不复制第三方受版权/许可约束的具体内容。  
> 注：Anthropic 仓库中部分 Skill 带有专有许可；本项目只提炼抽象设计模式。

## 1. 横向摘要

| # | Skill | 类型 | 最值得学习的设计 | 对 ERP AI Curator 的启示 |
|---|---|---|---|---|
| 1 | Anthropic `skill-creator` | Skill 创建 / Eval | 先捕获意图，再写草案；真实 Prompt 做 with-skill / baseline；主观任务重人评 | **先定义真实任务和成功标准，再写 Skill** |
| 2 | `doc-coauthoring` | 高判断协作 | Context Gathering → Refinement → Reader Testing；允许用户拒绝结构化流程 | 高判断任务应是**协作启发式**，不是硬流水线 |
| 3 | `frontend-design` | 高判断创作 | 给设计原则、反默认模式、自我批评，而不是给固定模板 | 对“什么是好资源”更适合给判断原则，不适合 JSON 穷举 |
| 4 | `mcp-builder` | 工程工作流 | Research → Implementation → Test → Evaluation；各阶段有 Done 条件 | 实现阶段需要明确阶段合同，但这是**工程 Skill**，不能直接照搬到采编 |
| 5 | `claude-api` | 动态事实 / 路由 | 不从记忆猜 API；按语言/场景按需读 reference；先选最简单 surface | 时效内容应动态查事实源，主 Skill 不内嵌易过期知识 |
| 6 | `pdf` | 确定性文件处理 | 大量成熟操作模式，复杂分支移入 reference | 确定性工具领域适合具体配方；采编不是同类任务 |
| 7 | `pptx` | 确定性 + 视觉 | Create/Edit/Read 先路由；脚本做结构验证；Gotchas 高密度 | 脚本用于**可确定验证**，而不是判断“推荐得好不好” |
| 8 | `docx` | 确定性文件处理 | 任务→工具路线；输出后 render/validate | “运行成功”和“结果正确”分开验证 |
| 9 | `xlsx` | 强确定性 | 公式重算、错误检查、精确约束；明确“绿灯不等于逻辑正确” | validator 只能证明结构，不可替代产品质量——与 V0.4 教训高度一致 |
| 10 | `web-artifacts-builder` | 工程产出 | 5 步最短主流程；测试是必要时/之后做，避免阻塞用户价值 | 不应把验证仪式放在所有任务前面 |
| 11 | `canvas-design` | 极高判断创作 | 用视觉哲学提高方向一致性，保留巨大创作自由 | 高判断 Skill 需要“方向 + 品质基准”，不是微观规则 |
| 12 | `internal-comms` | 路由型 | 主 SKILL 极短，只识别类型并加载对应 examples | **主 Skill 可做 router，细节按需读取** |
| 13 | `brand-guidelines` | 静态参考 | 边界清楚、信息稳定、直接提供域知识 | 静态稳定知识才适合直接内嵌 |
| 14 | `theme-factory` | 选项 + 人决策 | 展示有限选项→用户选择→执行；无合适主题再生成 | 对主观选择保留明确的人类裁决点 |
| 15 | `slack-gif-creator` | 约束 + 工具 | 平台约束 + 可复用 utilities + validator | 尺寸/格式等机器可判约束适合脚本化 |
| 16 | `algorithmic-art` | 高判断 + 可重复 | 先哲学再实现；seed 保证可重复；模板做 asset | 创造性判断与确定性复现可以分层，而不是互相替代 |
| 17 | `academy-guide` | **推荐/导航型** | 强匹配才推荐；最多 1–2；动态 catalog；过期即不信；弱匹配时保持沉默 | **与 ERP AI Curator 最接近的官方参考样本** |
| 18 | `discernment-nudge` | 条件触发 | 极精细的“何时用/何时不用”；一次/对话；避免重复和噪声 | 好 Skill 的边界很多时候来自 **skip conditions**，不是更多执行步骤 |
| 19 | Agents365 `drawio-skill` | 工具型复杂 Skill | 明确 Use / Do NOT use；错场景主动路由其他工具；大量 scripts 按需读取 | 工具生态要敢于说“不要用我”；references 做能力地图 |
| 20 | `deep-research` | **高判断研究型** | 反确认偏差；多角度搜索；权衡来源不数数量；解决冲突；结论优先 | 资源采编应该吸收“搜索多个立场 + 真正做选择” |
| 21 | `skill-creator-plus` | Skill 创建 / 工程化 | 明确 Script vs Instruct；先 Success Criteria；Trigger/Functional/Baseline 三类测试 | 对我们最重要的是**不要过早脚本化判断** |

## 2. 最相关的五个样本

### 2.1 `academy-guide`：推荐型 Skill 的直接参照

这是本轮与 ERP AI Curator 最接近的样本。

关键设计：

- 先回答用户当前问题，资源推荐只是补充；
- **只在 strong match 时推荐**；
- 最多 2 个资源，通常 1 个更好；
- 如果必须写“虽然它不完全覆盖，但……”这种 caveat，就意味着匹配失败；
- 推荐目录不写死在 Skill 中，而是运行时读取动态 catalog；
- catalog 有 stale 时间，过期后不再信任；
- 不能验证具体条目时，宁可只指向可信入口，不猜具体内容；
- “silence is better than noise”。

对我们的直接启示：

> 资源推荐系统的第一目标不是覆盖率，而是信任密度。

来源：  
https://github.com/anthropics/skills/blob/main/skills/academy-guide/SKILL.md

### 2.2 `deep-research`：搜索不是积累，而是管理不确定性

关键设计：

- 先把问题从“主题”改成“决策 + 约束 + 答案形式”；
- 搜索时主动改变词汇、立场和时间窗口；
- 必须寻找至少一个可能反对领先答案的可信来源；
- 十篇复制同一原始 Benchmark 的文章，只算一份证据；
- 冲突不能用“各有观点”糊过去，要解释边界；
- 结论先于链接堆积；
- 没有打开的来源不能引用；
- 明确 inference 与 documented fact 的区别。

对我们的直接启示：

> ERP AI Curator 不应该是“搜到资源”，而应该是“替用户完成横向比较后的决策压缩”。

来源：  
https://github.com/arjunprabhulal/agent-skills/blob/main/skills/research/deep-research/SKILL.md

### 2.3 Anthropic `skill-creator`：先 Eval，再固化

关键设计：

- 先捕获 intent / trigger / expected output；
- Skill 初稿后用真实 Prompt 测试；
- 新 Skill 应与“没有 Skill”的 baseline 对比；
- 既看定量，也让用户直接看输出做定性判断；
- 主观 Skill 不强行发明 assertions；
- 失败后根据真实输出修 Skill，而不是靠先验把规则一次写满；
- progressive disclosure：metadata → SKILL.md → bundled resources。

对我们的直接启示：

> 我们之前应该更早拿 10 个真实顾问任务做“有 Skill vs 无 Skill”对比，而不是先设计四表和 Gate。

来源：  
https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md

### 2.4 `skill-creator-plus`：Script vs Instruct

其归纳非常适合解释我们此前的偏航。

适合脚本：

- deterministic / repeatable；
- 固定 schema / regex / exit code 能验证；
- boilerplate；
- 反复重写会浪费 Agent。

适合 instruction：

- judgment；
- context-dependent decisions；
- flexible error recovery；
- workflow orchestration。

对我们的直接启示：

> “这个资源是否真的值得 ERP 顾问点击”属于 judgment，不应该被 `validate_candidate.py` 逐步替代。

来源：  
https://github.com/yaniv-golan/skill-creator-plus/blob/main/skill-creator-plus/skills/skill-creator-plus/SKILL.md

### 2.5 `xlsx`：机器验证的边界

`xlsx` 的一个高价值原则是：

> 公式能成功 recalculation，不代表公式逻辑正确。

这和我们 V0.4 的 `TOTAL_ERRORS=0` 几乎是同一个问题：

- JSON 自洽；
- validator 没报错；
- 不代表这个候选真的值得推荐。

对我们的直接启示：

> 确定性检查只能做质量底线，不能成为高判断任务的成功指标。

来源：  
https://github.com/anthropics/skills/blob/main/skills/xlsx/SKILL.md

## 3. 跨样本收敛出来的设计规律

### Pattern A — Progressive Disclosure 是默认架构

成熟 Skill 很少要求模型一开始把全部细节读完。

典型形式：

```text
description
  ↓
SKILL.md：主路线 / 选择逻辑
  ↓
references：只有命中场景才读
  ↓
scripts：直接执行，不必占用上下文
```

这意味着主 Skill 的任务不是“囊括所有规则”，而是：

> 让 Agent 知道当前应该走哪条路，以及何时读取什么。

### Pattern B — 自由度必须与任务性质匹配

高判断任务：

- research
- writing
- design
- recommendation

普遍使用：

- 原则；
- 反例；
- 选择启发式；
- self-critique；
- human feedback。

高确定性任务：

- PDF manipulation
- XLSX formula validation
- PPTX OOXML validation
- GIF size check

普遍使用：

- scripts；
- fixed commands；
- schema；
- validators。

**两类任务不能用同一种治理方式。**

### Pattern C — 好 Skill 会明确“什么时候不要用”

`drawio-skill` 会把白板图路由给 Excalidraw、diagrams-as-code 路由给 Mermaid。

`discernment-nudge` 用大量篇幅定义 skip condition。

`academy-guide` 明确弱匹配不推荐。

边界不是附属信息，而是 Skill 可靠性的核心。

### Pattern D — Search / Recommendation 要防 Confirmation 与 Accumulation

`deep-research` 把两大失败直接命名：

- Confirmation：找到支持第一印象的证据就停；
- Accumulation：搜很多，但把决策工作留给用户。

ERP AI Curator 两种风险都很高。

### Pattern E — Dynamic Facts 不要静态写死

`claude-api` 遇到 API drift 要查 live source。

`academy-guide` 推荐 catalog 运行时获取，并做 stale check。

对 AI 工具、模型配置、Skill 生态等高变化主题：

> Skill 应保存“去哪查、怎么比较”的知识，而不是把“当前答案”永久写死。

### Pattern F — Eval 应该衡量“有没有增益”

Anthropic `skill-creator` 不是只验证 Skill 文件合法，而是：

- with-skill；
- baseline；
- qualitative review；
- quantitative assertions（仅在适合时）。

对我们的核心 Eval 应更接近：

> “使用 Skill 后，这组推荐是否更值得 ERP 顾问点击/分享？”

而不是：

> “candidate JSON 是否 0 ERROR？”

### Pattern G — Done Condition 很重要，但必须属于正确层级

`mcp-builder` 的每阶段 Done 条件非常清楚。

这对**本地 Agent 开发**很重要。

但不意味着资源采编本身也要被写成六个 Gate。

区别：

- 开发 SPEC：应高度明确；
- 采编判断：应保留模型判断空间。

## 4. 研究中观察到的反模式

以下不是说这些模式永远错误，而是对 ERP AI Curator 当前阶段风险很高。

### Anti-pattern 1 — Database-first

在产品价值未验证前先围绕表结构设计采编流程。

风险：

- 数据模型开始反向控制产品；
- Agent 优化“填字段”，而不是“找到好东西”。

### Anti-pattern 2 — Universal validator

把所有任务都压成同一组 Gate / JSON validator。

风险：

- 高判断结论被标签游戏替代；
- Agent 学会调整字段以 PASS；
- 0 ERROR 被误解成产品正确。

### Anti-pattern 3 — Static truth repository for volatile AI ecosystem

AI 模型、Agent 工具、API、教程快速变化。

静态维护大量“事实”会产生高 refresh 成本和过时风险。

### Anti-pattern 4 — Scoring as a substitute for comparison

高分不等于“这个主题下最值得推荐”。

最终推荐仍然需要横向比较与取舍。

### Anti-pattern 5 — Eval overfitting to previous failures

只把 V0.2/V0.3 出错案例写成越来越多规则，会让 Skill 越来越像历史补丁集合。

正确做法应是：

> 从失败抽象出少量高层原则，然后拿新任务验证泛化。

## 5. 参考来源

### Anthropic 官方

- Agent Skills 工程文章  
  https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Effective context engineering  
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Skills repository  
  https://github.com/anthropics/skills

### 社区

- Draw.io Skill  
  https://github.com/Agents365-ai/drawio-skill
- Deep Research Skill  
  https://github.com/arjunprabhulal/agent-skills/blob/main/skills/research/deep-research/SKILL.md
- Skill Creator Plus  
  https://github.com/yaniv-golan/skill-creator-plus
