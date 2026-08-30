# ERP AI Curator — Real User Use Validation V1

Date: 2026-08-30
Status: **OPEN FOR NATURAL REAL-USER FEEDBACK**

> 本文件只定义真实用户使用后的产品验证证据。真实问卷问题本身、Cloud 对真实问题做出的 Curator 推荐，不等于用户已经使用了产品。

## 1. 两条 Lane 必须分开

### Lane A — REAL_USER_ORIGIN CURATION

输入来自真实同事/问卷/Owner 的真实工作问题，但研究和推荐由 Curator/Cloud 完成。

价值：

- 验证产品确实从真实问题出发；
- 暴露搜索、判断、证据和产品边界问题；
- 形成可以真正发给用户的推荐。

不能声称：

- 用户采用了；
- 节省时间；
- 降低返工；
- 比普通 AI / 自己搜索更好。

这类产物放在 `docs/curation-cases/`。

### Lane B — REAL_USER_USE VALIDATION

真实同事实际收到 Curator 推荐后，自然地学习、采用、修改、忽略或拒绝。

只有这条 Lane 才能形成产品价值证据。

## 2. Validation question

> **真实 ERP / 企业信息化同事收到 Curator 的小而可信的实践/资源推荐后，是否觉得它比普通 AI 或自己漫无目的搜索更值得使用？**

观察的是 curation value，不是用户是否能完成我们设计的测试协议。

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

使用当前 `skills/curating-erp-ai-resources/SKILL.md` 输出：

- A/B/C 结论；
- 当前任务下优先推荐的实践；
- 真正改变选择的证据；
- 默认 0–1 个最值得看的资源；
- 适用/不适用边界；
- 从哪里开始学习/采用。

**不要默认附带“请按以下步骤测试并回报结果”。**

## 5. 自然反馈即可

用户后续如果有反馈，只记录会改变产品判断的事实：

- 哪条建议/哪个资源有用、没用或错误；
- 是否采用、修改、拒绝或忽略，为什么；
- 是否减少了搜索/选择/配置成本；
- 是否漏掉重要能力、环境、权限、隐私或版本约束；
- 如果真的用于工作，是否出现可观察的返工增减；
- 是否愿意再带另一个真实问题回来。

不要求打分，不要求长问卷。

## 6. 证据强弱

### 强证据

- 用户实际采用/修改推荐，并有具体工作结果或返工事实；
- 用户能明确说明 Curator 替他省掉了什么搜索/选型判断；
- 用户指出了一个具体错误/遗漏，能直接驱动方法修正。

### 有用的负证据

- 用户明确拒绝推荐，并给出具体原因：错误环境、过时、权限/数据不允许、安装成本高、资源质量低、已有更好做法等。

### 不是产品价值证据

- 问卷里出现了真实问题；
- Cloud 为真实问题写出了一份漂亮 curation；
- Owner/Agent 说“看起来不错”；
- synthetic benchmark 通过；
- 为了证明项目，要求用户专门跑工具测试。

## 7. 失败信号

出现以下任一情况就值得窄修正：

- Curator 比用户自己搜还重；
- 推荐仍像工具目录；
- practitioner 证据缺失却强写“最佳”；
- 现有 AI 明显够用仍强推工具；
- 明确 capability gap 却一律退回普通 AI；
- 推荐资源与真实 artifact/environment 不匹配；
- 漏掉企业数据/权限/版本边界；
- 用户看完仍不知道什么值得关注；
- Curator 变成执行教练/测试协调器。

修最窄、可复现的问题，不为单一奇例建立新框架。

## 8. 当前关系

`REAL_USER_ORIGIN CURATION` 可以由 Cloud 持续推进，不需要等 Lane B 反馈才能研究下一个真实问题。

`REAL_USER_USE VALIDATION` 是外部证据 Lane，只在真实反馈自然出现时记录。

产品不能用 Lane A 冒充 Lane B，也不能为了制造 Lane B 把用户变成测试员。
