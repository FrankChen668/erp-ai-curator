# ERP AI Curator — Real User Use Validation V1

Date: 2026-08-31
Status: **OPEN FOR NATURAL REAL-USER FEEDBACK**
Runtime: `0.9.1`

> 本文件只定义真实用户使用后的产品价值证据。真实问卷问题本身、Cloud 对真实问题做出的 Curator 推荐，不等于用户已经使用了产品。

## 1. 两条 Lane 必须分开

### Lane A — REAL_USER_ORIGIN CURATION

输入来自真实同事/问卷/Owner 的真实工作问题，但研究和推荐由 Curator/Cloud 完成。

它可以验证：

- 产品确实从真实问题出发；
- 搜索、判断、证据和产品边界是否合理；
- 推荐是否足以真正发给用户。

它不能证明：

- 用户采用了；
- 节省了时间；
- 降低了返工；
- 比普通 AI / 用户自搜索更好。

这类产物放在 `docs/curation-cases/`。

### Lane B — REAL_USER_USE VALIDATION

真实同事实际收到 Runtime 结果后，自然地学习、采用、修改、忽略或拒绝。

只有这条 Lane 才能形成产品价值证据。

## 2. Validation question

> **真实 ERP / 企业信息化同事使用 ERP AI Curator 后，是否觉得它比普通 AI 或自己漫无目的搜索/选型更值得再次使用？**

观察的是搜索、筛选和选型判断价值，不是用户是否完成我们设计的测试协议。

## 3. 最小输入

真实用户问题保持原始语境：

```text
role / project context
+ actual materials available
+ concrete action/problem
+ expected deliverable
+ material constraints
```

不要求用户先选择 Problem Card，也不要求为了验证项目提供敏感材料。

## 4. 用户先收到什么

根据用户真实意图使用当前 Runtime：

### 找实践 — Practice Curator

`skills/curating-erp-ai-resources/`

正常结果应让用户知道：

- 当前最值得先看的 **1–3 个** practitioner 实践/教程/案例；
- 为什么匹配其角色、任务和交付物；
- 为什么优先于其它 serious candidates；
- 哪一个先看；
- 重要的 freshness、作者自实践/营销、语言/生态、权限或 coverage 边界。

正常 external curation 必须基于本次 fresh discovery 与本次实际检查的外部资源成立；历史项目 evidence 只能作为 lead。

### 做能力选择 — Capability Advisor

`skills/advising-erp-ai-capabilities/`

正常结果应是：

- **现有工具已够**；或
- **值得补能力**：明确 concrete gap 与最小必要升级；或
- **条件式升级**：明确决定是否升级的真实条件。

不要为了显得有价值而制造新 Tool/Skill/MCP 推荐。

**不要默认附带“请按以下步骤测试并回报结果”。**

## 5. 自然反馈即可

用户后续如果有反馈，只记录会改变产品判断的事实：

- 哪条建议/哪个资源有用、没用或错误；
- 是否采用、修改、拒绝或忽略，为什么；
- 是否减少了搜索/筛选/选型成本；
- 是否漏掉重要能力、环境、权限、隐私、版本或交付物约束；
- 如果真的用于工作，是否出现可观察的返工增减；
- 是否愿意再带另一个真实问题回来。

不要求打分，不要求长问卷。

## 6. 证据强弱

### 强证据

- 用户实际采用/修改推荐，并有具体工作结果或返工事实；
- 用户能明确说明 Curator 替他省掉了什么搜索/筛选/选型判断；
- 用户指出一个具体错误/遗漏，能直接驱动方法修正；
- 用户主动带第二个真实问题回来。

### 有用的负证据

- 用户明确拒绝推荐并给出具体原因：错误环境、过时、权限/数据不允许、安装成本高、资源质量低、已有更好做法等。

### 不是产品价值证据

- 问卷里出现了真实问题；
- Cloud 为真实问题写出一份漂亮 curation；
- Owner/Agent 说“看起来不错”；
- synthetic benchmark / contract checker 通过；
- 为了证明项目，要求用户专门跑工具测试；
- source-adapter / mature-Skill qualification 成功。

## 7. 失败信号

出现以下任一情况就值得窄修正：

- Curator 比用户自己搜还重；
- 推荐仍像工具目录；
- practitioner 证据缺失却强写“最佳”；
- 历史项目推荐污染当前候选；
- 现有 AI 明显够用仍强推工具；
- 明确 capability gap 却一律退回普通 AI；
- 推荐资源与真实 artifact/environment 不匹配；
- 漏掉企业数据/权限/版本边界；
- source acquisition 只增加链接，没有增加可判断的原始证据；
- 用户看完仍不知道什么值得先做；
- Curator 变成执行教练/测试协调器。

修最窄、可复现的问题，不为单一奇例建立新框架。

## 8. 当前关系

`REAL_USER_ORIGIN CURATION` 可由 Cloud 按真实任务继续，不需要为填证据矩阵批量制造 case。

`REAL_USER_USE VALIDATION` 是当前产品价值里程碑，只在真实反馈自然出现时记录。

Source acquisition / source composition 只是 enabling infrastructure；除非它在真实任务里改变推荐判断，否则不能替代 Lane B，也不应单独扩张成工程主线。
