# ERP AI Curator — V3 系统测试方案

> 目的：验证 V3 的判断机制是否真的能帮助泛 ERP / 企业信息化从业者选择更合适的 AI 工作方式，而不是验证某个 Skill 文件是否能 PASS。
>
> 上位依据：`PROJECT_NORTH_STAR.md`、`AI_LEVERAGE_MODEL_V3.md`、`SKILL_BLUEPRINT_V3.md`、`PROTOCOL_V3.md`。

## 1. 第一性测试目标

V3 必须回答的不是：

> 能不能找到 Tool / Skill？

而是：

> **面对真实工作任务，能否正确判断“现有 AI + 现有工具链是否已足够”，并且只在存在真实能力缺口时引入专门方案？**

因此测试拆成四层，顺序不能倒置：

1. **L0 — Trigger / Task Understanding**：是否理解用户真正要做什么，是否该进入 V3；
2. **L1 — AI Leverage Diagnosis**：A/B/C 判断是否有证据，是否识别当前 baseline；
3. **L2 — Real Execution / Incremental Value**：真正执行后，新方案是否带来可观察增量；
4. **L3 — Skill Uplift**：最后才比较“普通 AI”与“正式 Skill 封装”。

目前只进入 L0–L2。L3 暂不启动。

---

## 2. 测试的三个对象必须分开

### A. 测 V3 判断机制

测试问题：

- 有没有误触发？
- 有没有一看到 Skill/Tool 就 Mode B？
- 有没有识别用户已有 Codex、内部工具、现有 workflow？
- 有没有正确识别特殊输出、系统访问、runtime observation、高频重复等真实能力缺口？
- Mode C 是否真的给了最小试验和 upgrade signal？

### B. 测某个外部 Tool / Skill 的增量价值

只有 V3 已经形成 Mode B 假设后才测试。

测试问题：

- 现有工具链做不到什么？
- 新方案是否真正补上这个缺口？
- 是“能力增加”，还是只是流程变复杂？
- 产物质量、步骤数、返工次数、可编辑性、可追溯性等是否有实质改善？

Graph Engineering 之类属于这一层，不属于第一层。

### C. 测未来 ERP AI Curator Skill 封装

这是最后一层。

只有前两层证明 V3 方法反复有价值后，才比较：

- ordinary AI conversation
- with ERP AI Curator Skill

这层只回答“是否值得封装成 Skill”，不能反过来证明产品方向。

---

## 3. Pilot-01：先跑 5 个真实任务

第一轮只跑 5 个真实问题，不追求数量覆盖。

任务来源优先级：

1. 当前正在做的真实项目问题；
2. 过去已经真实发生、但尚未按 V3 执行的问题；
3. 问卷 / 同事真实问题；
4. 不用 synthetic case 补矩阵。

5 个任务应尽量自然覆盖以下不同压力，但**不要提前告诉 Codex 预期 Mode**：

- 一个明显的直接执行任务，测试是否 `NO_TRIGGER`；
- 一个现有 Codex/工具链很可能已经能完成的任务，测试过度 Tooling；
- 一个有明确特殊能力缺口的任务，例如可编辑原生格式 / runtime tracing /真实系统访问；
- 一个是否值得引入专门方案并不确定的任务，测试 Mode C；
- 一个高波动或高成本的配置/兼容问题，测试事实核验和复杂度判断。

注意：这些是选题压力，不是正确答案标签。

---

## 4. 每个任务采用“两阶段执行”，防止先装工具再找理由

### Stage 1 — Diagnosis Only

Codex 只能：

- 理解原始问题；
- 读取必要的本地材料；
- 盘点当前已有 AI / Agent / Tool；
- 做不改变项目状态的轻量检查；
- 输出 `NO_TRIGGER / A / B / C` 假设；
- 明确依据和不确定项。

此阶段禁止：

- 安装新 Skill / MCP / Tool；
- 大规模子 Agent 扫描；
- 为证明某方案有效而运行整套测试；
- 修改项目代码；
- 修改 V3 文档。

Stage 1 的核心产物只有一句：

> **当前 baseline 的能力缺口到底是什么？**

如果说不清，不得进入 Mode B 安装实验。

### Stage 2 — Execution / Counterfactual Test

根据 Stage 1：

#### NO_TRIGGER

直接退出 Curator 测试。记录“正确没有介入”即可。

#### Mode A

用用户当前已有 AI + Toolchain 真正完成一个最小真实样本。

验证：

- 是否已经能交付；
- 主要问题是否真与工具能力有关；
- 是否存在反证说明其实需要专门方案。

#### Mode B

必须先保留 **Baseline Artifact**，再引入候选方案。

顺序：

1. 当前工具链做一次最小真实样本；
2. 记录产物/失败点；
3. 再安装或启用专门方案；
4. 用同一输入、同一目标再做一次；
5. 比较增量价值。

不允许只有“安装后扫描结果”，没有 baseline 对照。

#### Mode C

只做最小试验，不安装复杂方案。

必须记录：

- 试验是什么；
- 结果怎样；
- 哪个具体现象会触发升级到 Mode B。

---

## 5. 比较什么：不用总分，只保留可观察证据

每个 Stage 2 最多比较下面这些与任务相关的项目，不要求全部填写：

### 能力

- baseline 能否完成目标；
- 新方案是否增加 baseline 原本没有的能力；
- 是否只是包装同一种能力。

### 产物

- 最终产物是否真实存在；
- 是否满足关键格式/协议/可编辑性要求；
- 是否更完整、更可复核、更可执行。

### 成本

- 安装 / 配置 / 学习成本；
- 执行步骤；
- 返工次数；
- 是否需要额外服务、账号、模型或依赖。

### 企业可用性

- 数据 / 源码是否离开当前环境；
- 权限与账号要求；
- 是否与现有开发/项目流程冲突；
- 是否容易形成新的维护依赖。

### 稳定性

- 同一真实输入是否能重复得到可接受结果；
- 是否高度依赖偶然 Prompt / 某个模型；
- 版本/配置是否容易过时。

不使用 100 分评分。

---

## 6. 每题的最小证据文件

建议 Pilot 只允许新增：

```text
docs/validation/local-pilot-01/
├── T01.md
├── T02.md
├── T03.md
├── T04.md
└── T05.md
```

每题固定格式：

```text
# Txx

Original task:
原始问题，不润色。

Source / Role:
知道才填。

Current baseline:
当前已有 AI / Agent / Toolchain。

Stage 1 diagnosis:
NO_TRIGGER / A / B / C

Reason:
3–6 条关键证据。

Capability gap:
如果是 B，必须一句话写清；否则写 none / uncertain。

Stage 2 action:
实际做了什么。

Baseline artifact / evidence:
路径、截图、命令结果或明确说明没有。

Specialized artifact / evidence:
仅 Mode B 填。

Observed delta:
真正增加了什么 / 没增加什么。

Critical limitation:
有则写。

Final judgement:
KEEP CURRENT / ADOPT SPECIALIZED / CONDITIONAL / NO_TRIGGER

Open question:
只留真正影响结论的问题。
```

禁止写长篇执行日志代替证据。

---

## 7. Codex 执行纪律

这部分必须严格，因为本地 Agent 当前最大的风险不是“不会查”，而是**容易把流程做得很完整，却没有证明价值**。

执行顺序固定：

> **Action → Artifact Check → Evidence Check → Next Action**

每一个关键动作后必须先确认：

1. 产物是否真的存在；
2. 产物是否来自当前这次运行；
3. 它是否证明了刚才要验证的假设；
4. 如果没有，不能继续拿后续动作掩盖。

子 Agent、测试数量、healthcheck 通过、节点失败=0，都不是产品结论。

---

## 8. 对抗性审查问题

云端在每题完成后主要攻击以下问题：

1. **过度 Tooling**：是不是现有 Codex 已经能做，它却先装新东西？
2. **Baseline 造弱**：是不是故意用很弱的 Prompt/方式让新工具看起来更强？
3. **能力偷换**：新方案是不是只是更方便，而不是解决真实缺口？
4. **输出偷换**：用户要 editable / runtime / system action，结果只给静态说明？
5. **过程冒充结果**：扫描、测试很多，但最终产物并没有更好？
6. **成本忽略**：新增依赖的安装/学习/维护成本有没有算进去？
7. **语义逃避**：遇到难判断就全部 Mode C？
8. **搜索偏航**：简单问题是否又开始大量翻官网？
9. **环境忽略**：客户数据、源码、权限、本地/云端边界有没有被漏掉？
10. **V3 迎合**：是不是为了看起来符合 V3 而机械选择 A/B/C？

---

## 9. Pilot-01 结束后怎么判断

不设“5 题必须 4 题 PASS”之类机械阈值。

只看四个问题：

### Q1. V3 是否改变了错误决策？

例如：

- 避免安装一个没必要的 Tool；
- 识别出普通 AI 无法提供的 runtime / editable / integration 能力；
- 通过 Mode C 避免过早复杂化。

### Q2. 判断是否经得住真实执行？

Stage 1 认为 A，实际 baseline 却做不到，说明诊断偏乐观。

Stage 1 认为 B，但 baseline 已经能完成，说明过度 Tooling。

### Q3. 新方案是否存在可观察的增量？

不是“Agent 说更好”，而是实际 artifact / capability / steps / repeatability 有变化。

### Q4. 这套判断是否值得固化？

如果普通 Codex 在不给 V3 的情况下也稳定会做这些判断，就没必要急着做 Skill。

---

## 10. 第二阶段：Fresh Paired Test

只有 Pilot-01 表明 V3 判断有价值后才启动。

使用新的真实任务做 paired test：

### Baseline session

- 新会话；
- 只给原始任务和正常上下文；
- 不加载 ERP AI Curator V3 文档。

### V3 session

- 另一个新会话；
- 同一原始任务；
- 相同项目状态 / 工具权限；
- 加载 V3 当前权威文档。

比较：

- 是否误触发；
- 是否识别 current baseline；
- 是否过度 Tooling；
- 是否识别真实能力缺口；
- 是否给出更经济的执行路径；
- 最终实际结果是否更有用。

不要用“推荐数量”作为胜负指标。

---

## 11. 何时才开发正式 Skill

只有同时出现这些信号才进入 Skill 实现：

- 多个真实任务中 V3 判断反复改变了有价值的决策；
- 本地真实执行支持这些判断，而不是只靠文字推理；
- paired test 表明普通 Codex 容易遗漏这些判断；
- V3 的改进来自少量通用原则，不依赖场景硬编码；
- 没有重新滑向资源库、评分、Gate 或多 Agent 流水线。

否则继续把 V3 当作人工/云端工作方法，不为了形式开发 Skill。

---

## 12. 当前建议的实际下一步

1. 不开发 Skill；
2. 建 `validation/local-v3-pilot-01` 分支；
3. 选第一个真实任务；
4. Codex 只做 Stage 1 Diagnosis；
5. 把 Stage 1 结果交给云端对抗性审查；
6. 通过后再进入 Stage 2 真执行；
7. 一题完整闭环后再开始第二题。

第一题不要再用 Graph Engineering 继续扫同一个项目，避免已有上下文污染结论。优先选一个新的真实工作任务。