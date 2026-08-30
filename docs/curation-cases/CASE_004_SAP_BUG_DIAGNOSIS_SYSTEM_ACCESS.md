# Curation Case 004 — SAP 程序 Bug 定位与真实系统访问边界

Date: 2026-08-30
Status: **REAL_USER_ORIGIN CURATION READY — NOT USER-USE EVIDENCE**
Produced with Skill: `curating-erp-ai-resources` `0.7.0`

> 来源：2026-08 训前调研中的真实实施顾问问题。原始诉求之一是：非 ABAP 顾问在单元测试/上线后遇到程序问题，希望 AI 能帮助定位 Bug 原因，最好能定位到具体代码位置，减少等待开发人员人工排查的时间。

## 1. 真实问题

这不是“哪个 AI 最懂 ABAP”。真正任务是：

```text
业务异常 / 报错
→ 找到相关程序与调用链
→ 区分配置/数据/代码问题
→ 定位最可能的错误位置和原因
→ 给开发人员可复核的证据
```

决定 AI 能否完成这件事的关键，不只是模型能力，而是它是否拿到了**真实诊断证据**。

## 2. 当前 baseline

问卷中用户可提供：代码/日志，并希望 AI 帮助定位原因。

如果已有完整或足够的：

- ST22 short dump / error long text；
- source-code snippet；
- active calls / call stack；
- 相关自定义代码；
- 复现步骤与输入数据；

普通成熟 AI / Coding Agent 已经可以做高价值的 read-only evidence analysis：

- 解释 dump / stack；
- 关联异常与代码；
- 提出根因假设；
- 指出需要开发人员重点检查的代码行/对象；
- 区分“已观察事实 / 推断 / 未知”。

此时不需要因为任务叫“SAP Debug”就额外安装 SAP AI Tool。

## 3. 为什么系统证据很关键

SAP 官方资料明确说明：

- ST22 short dump 会保存 runtime error 的详细信息；Long Text 可以看到 error reason/location；source-code snippet 会标出程序终止位置；Active Calls/Events 提供 call stack。
  - https://help.sap.com/docs/SUPPORT_CONTENT/wdabap/3362186674.html
- ABAP Debugger / ADT 能查看 active call stack、进入对应代码层级并检查变量、breakpoints 等 runtime context。
  - https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_752/c238d694b825421f940829321ffa326a/4ec365a66e391014adc9fffe4e204223.html
- 当前 ABAP troubleshooting 文档仍把 short dump、debugger、profiler、trace/log 等作为定位和理解真实问题的重要工具。
  - https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/4ecc7d3a6e391014adc9fffe4e204223.html

这意味着：**真正的瓶颈经常不是“AI 不会推理”，而是 AI 没拿到系统里存在的 runtime evidence。**

## 4. Curator 0.7.0 结论

> **A → 条件化 B。**

### A — 已有足够 dump/log/code evidence

如果用户已经能把必要的 ST22、日志、代码、调用栈等安全导出给现有 AI：

> **先用当前 AI 做 source-grounded、read-only diagnosis，不需要新增专门 Tool / MCP。**

输出应该是：

- Observed facts；
- likely root cause；
- suspected code/object location；
- missing evidence；
- developer verification steps。

AI 不应把“可能原因”写成已经确认的系统事实。

### Conditional B — 根因依赖 AI 当前拿不到的系统事实

只有当实际阻塞变成：

- dump / runtime context 无法完整导出；
- 必须查询真实 development object / where-used / metadata；
- 必须看实时变量、调用链、trace、ATC 或系统对象；
- 诊断反复发生，人工从 SAP 系统搬运 evidence 成为主要成本；

才值得考虑**受控 SAP-native / MCP / IDE integrated read access**。

此时升级原因是“真实系统 evidence access”，不是“SAP 标签”。

## 5. 当前 SAP AI / Agentic 能力边界

SAP 2026 当前官方资料显示，Joule for Developers / ABAP AI 已有 code explanation、code completion、unit-test/generation 等能力，并正在通过 MCP/agentic tools 扩展 ABAP 开发任务；官方材料中还出现 ATC check/fix、object creation、activation、unit-test 等工具方向。

- https://help.sap.com/docs/abap-cloud/abap-development-tools-for-visual-studio-code/capabilities
- https://www.sap.com/documents/2025/02/b4f714de-f57e-0010-bca6-c68f7e60039b.html

但这些事实**不能直接证明**：

- 非 ABAP 实施顾问可以无门槛获得；
- 它已经是日常生产 Bug 根因定位的默认最佳选择；
- 它适用于所有 ECC / S/4HANA / on-prem / cloud 版本；
- 它应该获得写权限。

近期 SAP 社区实践讨论仍显示明显的 availability/licensing/实际效果分歧，因此当前不把 Joule 或 ABAP MCP 作为默认用户推荐。

## 6. 当前最值得采用的实践

```text
业务异常
→ 先拿 ST22 / log / source snippet / call stack / relevant code
→ 现有 AI 做 read-only evidence analysis
→ 明确 Observed / Inference / Unknown
→ AI 给出最可能根因 + 证据缺口 + 建议检查对象
→ 开发人员/系统工具复核
→ 只有 evidence 获取本身成为瓶颈时，再升级受控 SAP-native access
```

这个模式比“让 AI 直接猜哪行代码错了”更稳，也比一开始给 AI 高权限系统连接更安全。

## 7. 权限边界

理解/诊断任务默认 read-only。

“某 MCP / Agent 能修改代码、运行修复、创建对象”不等于当前诊断任务应该授权写入。

只有用户明确进入修复/开发任务，并且变更范围、权限、测试和回滚机制清楚时，才讨论写操作。

## 8. 给用户的最小 Curator 输出

> **如果你已经能拿到完整的 ST22、日志、调用栈和相关代码，先不用找新的 SAP AI 工具，现有 AI 已经可以帮你做只读根因分析和代码位置假设。真正值得升级专门能力的情况，是问题事实只能留在 SAP 系统里，人工反复查 ST22、对象、where-used、变量/调用链已经成为主要瓶颈；这时才考虑受控的 SAP-native/Joule/MCP 访问。诊断阶段默认只读，不因为工具“能改代码”就授予写权限。**

## 9. Evidence boundary

本 Case 支持的是**采用边界判断**：何时 current AI + exported evidence 足够，何时系统 evidence access 才构成真实 capability gap。

它没有证明 Joule、任何 ABAP MCP 或某个 Coding Agent在真实用户项目里已经减少诊断时间，也没有形成 REAL_USER_USE 产品价值证据。
