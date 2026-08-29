# Oracle Fusion SCM：AI 辅助快速学习模块的教程 / prompt framework 资源推荐

## 先说结论

**你要的那个东西——「专门教人用 AI 快速上手 Oracle Fusion SCM 各模块」的 prompt framework 或学习方法论——我没有找到，明确说：没有。**

我做了 9 组关键词搜索、实际打开了 11 个页面，检索到的资源呈现出一个很清晰的错位：

- **Oracle 官方的 prompt 资源**，全部面向「如何构建 / 配置 Fusion AI Agent」，不是「如何学 SCM 模块」；
- **第三方的 Oracle SCM prompt 资源**，全部面向「用 AI 做供应链决策与分析」，也不是「学模块」；
- 真正落在「用 AI 学 SCM 模块」这个交叉点上的，**一篇都没有**。

所以下面我给的是 4 个**够格但都需要你自己迁移**的资源，外加一个我自己搭的可落地做法。我会把每个资源的"够格在哪 / 不够格在哪"说清楚，你可以自己判断要不要花时间。

---

## 推荐 1：Oracle 官方《Basics of Prompt Engineering》——目前能找到的最扎实的 prompt 框架

- **链接**：https://blogs.oracle.com/fusioncoe/basics-of-prompt-engineering
- **发布方 / 时间**：Oracle 官方博客（fusioncoe），2026-02-18，6 分钟阅读
- **我已打开原文确认，不是只看摘要**

**它给的是什么**：这是 Oracle 官方对 AI Agent Studio 提示词体系的完整拆解，结构很硬：

- 三种 agent 模式（Single / Multi-Agent 层级式 / Workflow），各自对应不同 prompt 写法
- **四类 prompt**：System Prompt（身份与能力边界）、Topic（可复用指令块）、Summarization Prompt（**输出格式在这里配，不在 system prompt 里**）、Workflow Prompt / LLM Node（单次结构化任务）
- System Prompt 的**五层解剖**：Persona / Scope / Tools / Constraints / Topic References
- Topic 表达式 `$topic.<topic_code>`、Topic 的撰写原则对照表（具体 vs 空泛、中立语言、单一主题）
- 多步 Topic 的**顺序闸门**写法：`"Authenticate user. If step 1 fails, do not proceed to steps 2 or 3."`
- Supervisor 与 Worker 两类 agent 的 prompt 侧重点差异

**为什么值得你花这 6 分钟**：这是唯一一个把 prompt 当"可复用工程结构"来讲的官方材料，不是"写好提示词的 10 个技巧"那种水货。里面的 **Context（上下文）+ Task（任务）+ Output spec（输出规格）** 三段式，以及"把关键约束和边界写进 prompt"的思路，可以原封不动迁移到"让 AI 给我讲清楚 SCM 某个模块"。

**不够格在哪**：它从头到尾讲的是"怎么给 AI Agent 写提示词"，例子全是 HCM  payroll / pay slip。跟 SCM 模块学习没有直接关系，需要你自己做迁移。

---

## 推荐 2：Oracle 官方《Best Practices for Prompts in AI Agent Studio》——可直接抄的战术与一个现成模板

- **链接**：https://blogs.oracle.com/fusioncoe/best-practices-for-prompts-in-ai-agent-studio
- **发布方 / 时间**：Oracle 官方博客（fusioncoe），作者 Aarti Satyamurthy（AI Solutions Director），2026-02-18
- **我已打开原文确认**

**它给的是什么**，比第 1 篇更实操：

- **8 条 prompt 战术**：从简到繁迭代 / 试验指令顺序（约束放开头还是结尾效果不同）/ 用明确动作动词（Write、Classify、Summarize、Validate…，别用 handle、process）/ 具体但别啰嗦（10 行精确 > 50 行冗余）/ 模块化复用 / 显式声明依赖（"必须先调 A，A 失败就停"）/ 写明前提假设 / **绝不在 prompt 里放 PII**
- **7 个常见错误对照表**（含症状与解法）：角色含糊、无边界、prompt 过载、无错误处理、依赖顺序未定义、指令自相矛盾、**默认模型知道你没说的东西**
- **一个可直接复制的 LLM 故障排查模板**：把「当前 prompt + 出问题的提问 + 期望输出」三段喂给任意 LLM，让它找出冲突、歧义、缺失的错误处理和未声明的假设
- 工具描述撰写准则、测试与部署检查清单

**为什么值得看**：那个故障排查模板可以直接拿来当"我这个 prompt 为什么不好使"的诊断器。第 6 条"Anticipate Dependencies"和第 8 条"绝不用 PII"是很多人的盲区。

**不够格在哪**：同样是面向 agent 构建，且示例仍然是 HR 域。

---

## 推荐 3：Terillium《AI Prompts for Oracle SCM》——唯一找到的 SCM 专属 prompt 集合（但请批判使用）

- **链接**：https://terillium.com?p=58018/
- **发布方 / 时间**：Terillium（Oracle 实施合作伙伴），作者 Margo Burichin，2026-04-22 发布，**2026-08-25 更新**（很新）
- **我已打开原文确认**

**它给的是什么**：按 5 个供应链业务域分类的自然语言 prompt 示例，每类 3 条，共 15 条：

| 业务域 | 示例 prompt |
|---|---|
| 需求计划与预测 | "Which forecasts have the highest risk of inaccuracy?" / "How would a 10% increase in demand impact inventory levels?" |
| 库存优化 | "Which items are currently overstocked across all warehouses?" / "Where do we have slow-moving inventory?" |
| 采购与供应商 | "Which suppliers have the highest risk of delay?" / "Where can we consolidate vendors to reduce costs?" |
| 物流与运输 | "What shipments are at risk of delay this week?" / "Which lanes have the highest cost variability?" |
| 情景规划 | "What happens if a key supplier goes offline for two weeks?" |

**够格在哪**：这是全网唯一一个**按 Oracle SCM 业务域组织**的 prompt 清单，而且发布于 2026 年 8 月，时效性好。这 15 条本身就是一个不错的"SCM 该问什么问题"的骨架——对不熟 SCM 的人，光把这 5 个域的名字和它们的典型问法过一遍，就已经建立了模块地图。

**不够格在哪（重要，请务必注意）**：

1. **不是 framework，也没有任何方法论**——它就是一份问句清单，没有教你怎么写 prompt。
2. **作者是 Terillium 的内容与社交媒体负责人**，不是 SCM 顾问，原文介绍写的是"leads content and social media"。内容可信度需要打折。
3. **这是"用 AI 做供应链决策"的 prompt，不是"学 SCM 模块"的 prompt**——正好跟你想要的差一层。
4. **文末是营销转化**：整篇最后导向 Terillium 的 "Oracle AI Strategy Workshop" 收费咨询。文章里的准确定性是内容营销资产。

**我的建议**：把这 15 条当**模块地图和提问灵感**用，别当教材用。

---

## 推荐 4：Oracle Cloud Success Navigator 的 AI Adoption Center（免费）

- **入口**：https://www.oracle.com/au/customer-success/navigator/
- **相关课程**：《Oracle AI Success Navigator Essentials》，1h49m，13 个模块
  - https://learn.oracle.com/ols/course/oracle-ai-success-navigator-essentials/146587/164295
- **我已打开 Oracle 官方博客确认**：https://blogs.oracle.com/oracleuniversity?p=492 （2025-09-22，作者 Chris Supangat，Oracle Customer Success Services）

**它是什么**：Oracle 官方博客明确写道——Cloud Success Navigator 内的 **AI Adoption Center 可免费使用**，里面可以学到"Oracle 有哪些 AI 能力"、"Fusion AI Agent Studio 概览"、"实施最佳实践与治理"、"在你的 Fusion 实例里启用 AI 的前置条件"。

**为什么对你有用**：这是唯一一个**免费、官方、且明确以"帮你把 AI 用起来"为目的**的入口。如果你连"SCM 里哪些地方有 AI、分别叫什么"都还没概念，从这里起步最省事，比在外面乱搜强。

**不够格在哪**：它服务的是"实施/采纳 Oracle AI 功能"这条线（路线图、配置、治理、启用前置条件），**不是教你学 SCM 业务模块**。博客里那句 "Race to Certification 免费到 2025-10-31" 也早已过期，别信那个时间点。

---

## 补充参考（不是推荐，但值得先扫一眼）

**Oracle 官网《Oracle AI for SCM》功能清单页**
- https://www.oracle.com/ua/scm/ai/
- 我已打开确认。它按业务域（成本管理 / 制造与维护 / 订单管理与物流 / 采购 / PLM / 质量管理 / 可持续 / 供应链计划 / 供应商管理）罗列了 SCM 的全部 AI 功能，并用 `*` 标注生成式 AI、`**` 标注 AI Agent。

**为什么先扫它**：这是"Oracle SCM 的 AI 到底覆盖到哪"的一手地基。看完你就知道哪些模块有 AI 加持、哪些没有，避免对着一个根本没 AI 功能的模块死磕 prompt。它**不是教程也没 prompt**，纯产品清单，所以不放进正式推荐。

---

## 既然没有现成的，我给你一个可落地的做法

**说明：下面这个不是我搜到的现成资源，是我基于上面已验证的 Oracle 官方框架（三段式 Context/Task/Output spec、五层 System Prompt 解剖、8 条战术）推导出来的。请把它当作起点自行迭代，别当标准答案。**

### 第一步：先给 AI 一个稳定的"Oracle SCM 顾问"人设（对应官方五层解剖）

```
你是 Oracle Fusion Cloud SCM 的功能顾问，面向的是第一次接触该模块的业务人员。

【Scope】只覆盖 Oracle Fusion Cloud SCM 的以下模块：
Procurement / Inventory Management / Order Management /
Manufacturing / Supply Chain Planning / Cost Management / Logistics。

【Constraints】
- 涉及具体的菜单路径、配置任务名、Profile Option 名称、表名/字段名时，
  必须明确标注「该项需对照 docs.oracle.com 与你所在版本的 Release Notes 核实」。
- 不确定就直接说不确定。禁止生成看起来合理但你无法确认的配置路径或字段名。
- 回答中给出你在 docs.oracle.com 上对应的文档线索（功能域或文档标题级别即可）。

【Output】
- 先用 3-5 条 bullet 给出结论，再展开。
- 涉及操作流程时，用「设置 / 执行 / 验证」三段组织。
```

**关键在第 2 条约束。** 这不是形式主义——Oracle 的表名、字段名、菜单路径、Profile Option 是 LLM 幻觉的重灾区（我在检索中看到 HCM 领域的实践总结提到：AI 会编造不存在的列名、会用已废弃的 `_F` 表而不是 `_M` 表、会用标准 SQL 语法去写 OTBI 的 Logical SQL——SCM 侧同样的风险只会更高）。Oracle 官方自己在 agent system prompt 示例里写的也是同一条原则：**"Never generate facts. All answers should rely on tool call response."**

### 第二步：学某个模块时，用「业务流 → 配置 → 异常」三层递进，别直接问"XX 模块是什么"

直接问"介绍一下 Inventory Management"只会得到一篇百科摘要，没用。换成三层：

1. **业务流**：`从供应商收货到可用量更新，Inventory Management 里完整经过哪些环节？每个环节的系统动作是什么？`
2. **配置**：`要让上面第 3 个环节跑通，需要完成哪些功能设置？请按 Functional Setup Manager 的任务组织方式列出。`
3. **异常**（这层最能暴露你自己的理解盲区）：`如果收货后可用量没有增加，请列出 5 个最可能的排查方向，并说明每一条该去哪里验证。`

第 3 层是真正拉开水平的问法——它逼 AI 输出"怎么验证"，而不是"是什么"。

### 第三步：把第一步的人设 prompt 本身也拿去诊断

用推荐 2 里那个现成的排查模板，把你自己写好的 prompt + 一次不满意的回答 + 期望回答，三段喂给任意 LLM，让它指出冲突、歧义、缺失的错误处理。官方博客称这一步能抓到人工审阅经常漏掉的问题。

---

## 明确没找到、我不推荐的

以下几类我检索到了，**评估后认为不够格，明确说没有**：

- **专门针对「用 AI 学 Oracle Fusion SCM 模块」的 prompt framework**：无。Oracle 官方的所有 prompt 资源都是 agent 构建导向，第三方的是供应链决策导向。
- **Oracle 官方出品的「SCM 模块学习 prompt 模板库」**：无。官方最接近的是那份《Oracle AI for Fusion Applications》Q&A PDF（https://docs.oracle.com/en/cloud/saas/fusion-ai/aiaqa/questions-and-answers.pdf），里面有 prompt 四要素（Instruction / Context / Input data / Output format）、四种技巧（zero-shot / few-shot / CoT / prompt chaining）和最佳实践表，**但它是泛 Fusion 层面、面向配置 AI 功能的，不是 SCM 学习**。（补充：我尝试抓取这个 PDF 的正文失败了，返回的是二进制流，上面的内容是从搜索引擎索引到的正文确认的，不是我直接读的原文。）
- **LinkedIn 上那篇 18 条 Oracle Cloud prompt（含 SCM 4 条）**：https://www.linkedin.com/pulse/stay-ahead-prompts-oracle-cloud-applications-hrishabh-dubey
  我打开了原文。发表于 **2023-06-09**，SCM 只有 4 条（新建物料 / 需求预测补货 / 采购申请转订单 / 仓储收货履约），全部是 "Scenario + Describe how you would..." 的句式，**没有任何框架、没有防幻觉约束、没有版本意识**。三年过去，Oracle 已经迭代了 24D/25A/26A/26B 多个版本。**不推荐。**
- **各类「Oracle SCM 面试题」「Oracle SCM 培训」内容站**（unogeeks / softonlinetraining / ccodez 等）：SEO 内容农场，非 AI 辅助学习，不推荐。
- **Creative Flakes《Ask Oracle — The State of AI Across Fusion SCM》**：https://www.creativeflakes.com/insights/fusion-scm-ai-magazine
  我打开确认了。它是第三方合作伙伴的**产品发布盘点**（截至 2026 年 4 月 SCM 各模块已 ship 的 AI Agent 清单，带 readiness note 编号），**明确不是教程也没有 prompt framework**。如果你只想知道"SCM 有哪些 AI Agent 已经上线"，它有价值；对你的需求，**不推荐**。

---

## 运行记录

### 实际使用的搜索关键词（共 9 组，均真实执行）

1. `Oracle Fusion SCM AI prompt framework learning`
2. `Oracle Fusion Cloud SCM training tutorial learning path`
3. `using generative AI to learn Oracle Fusion applications prompt library`
4. `Oracle Fusion AI Agent Studio prompt engineering guide best practices`
5. `mylearn.oracle.com "Oracle AI in Fusion Cloud Supply Chain Management" course`
6. `"Oracle AI Agent Studio for Fusion Applications Foundations Associate" learning path mylearn`
7. `ChatGPT Claude prompt to learn Oracle Fusion SCM module quickly consultant`
8. `Oracle AI Success Navigator learn.oracle.com course roadmap best practices`
9. `Oracle Fusion SCM prompts ChatGPT templates supply chain functional consultant practical`

### 实际打开过的原始链接（共 11 个）

**成功打开并确认正文（9 个）**

| # | 链接 | 结果 |
|---|---|---|
| 1 | https://blogs.oracle.com/fusioncoe/basics-of-prompt-engineering | 成功。确认为 Oracle 官方，2026-02-18，四类 prompt + 五层解剖 |
| 2 | https://blogs.oracle.com/fusioncoe/best-practices-for-prompts-in-ai-agent-studio | 成功。确认作者 Aarti Satyamurthy，2026-02-18，8 条战术 + 7 错误对照 + 排查模板 |
| 3 | https://terillium.com?p=58018/ | 成功。确认 2026-04-22 发布 / 2026-08-25 更新，15 条 SCM prompt，作者为内容营销岗，文末导向收费 Workshop |
| 4 | https://www.oracle.com/ua/scm/ai/ | 成功。确认为官方产品功能清单页（`*` 生成式 AI / `**` AI Agent），非教程 |
| 5 | https://blogs.oracle.com/oracleuniversity?p=492 | 成功。确认 2025-09-22，AI Adoption Center 免费；同时确认其"免费到 2025-10-31"已过期 |
| 6 | https://www.creativeflakes.com/insights/fusion-scm-ai-magazine | 成功。确认为第三方产品发布盘点，无 prompt framework |
| 7 | https://www.linkedin.com/pulse/stay-ahead-prompts-oracle-cloud-applications-hrishabh-dubey | 成功（正文可读，互动需登录）。确认 2023-06-09，SCM 仅 4 条，无框架 |
| 8 | https://learn.oracle.com/ols/course/oracle-ai-success-navigator-essentials/146587/164295 | 部分成功。返回标题与课程名，模块大纲未渲染 |
| 9 | https://docs.oracle.com/en/cloud/saas/fusion-ai/aiaqa/questions-and-answers.pdf | **抓取失败**（见下） |

**打开失败（2 个）**

| # | 链接 | 失败情况 |
|---|---|---|
| 10 | https://mylearn.oracle.com/ou/learning-path/oracle-ai-in-fusion-cloud-supply-chain-manufacturing-scm-new/155950 | 返回内容仅 44 字符（"Oracle MyLearn"），页面为 SPA，内容由 JS 渲染 |
| 11 | https://mylearn.oracle.com/ou/course/oracle-ai-agent-studio-for-fusion-applications/160251/ | 同上，仅返回 "Oracle MyLearn" |

### 遇到的异常与失败（如实记录）

1. **Oracle MyLearn / learn.oracle.com 全站为 SPA，WebFetch 抓不到正文。**
   三次尝试（两个 mylearn 页面、一个 learn.oracle.com/ols 页面）均只返回标题或空壳。**这直接导致我放弃推荐 Oracle University 的两条付费/认证学习路径**——即"Oracle AI in Fusion Cloud Supply Chain & Manufacturing (SCM)"（约 5-6.7h，含 Assessment）和"Oracle AI Agent Studio for Fusion Applications Foundations Associate"（4h07m，含 1Z0-1145-1 认证）。
   我只在搜索引擎索引到的正文里看到了它们的课程大纲，但**未能打开原始页面亲自确认**，因此按纪律不将其列为正式推荐。如果你有 Oracle 账号能直接登录 MyLearn，这两条路径其实值得自己去看一眼——尤其是前者，它是官方唯一一条 SCM 专属的 AI 学习路径。

2. **Oracle 官方文档 PDF 抓取失败。**
   https://docs.oracle.com/en/cloud/saas/fusion-ai/aiaqa/questions-and-answers.pdf 返回的是 `%PDF-1.4` 二进制流（约 10 万字符的压缩数据），无法解析正文。该文档中关于 prompt 四要素、四种技巧、最佳实践表的内容，我是从搜索引擎索引到的正文以及另一份镜像 https://docs.oracle.com/cd/E56931_01/trans/G22516-14/questions-and-answers.pdf 的索引内容交叉确认的，**不是我直接读取的原文**。故将其降级为"补充参考"，不列为正式推荐。

3. **未发现伪造或不存在的资源。** 本次推荐的所有链接均真实存在于搜索结果中，且除上述 3 个失败项外，均已打开原文核对过内容与发布时间。

4. **联网能力全程可用**，WebSearch 与 WebFetch 均正常返回结果，未出现需要中断或声明"无法完成推荐"的情况。
