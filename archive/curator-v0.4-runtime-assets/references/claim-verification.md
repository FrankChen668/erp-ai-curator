# 关键事实核验

## 为什么需要

第三方教程最危险的问题不是“写得差”，而是**步骤很完整但关键事实已经错了**。这种内容看起来最像高质量资源，也最容易误导用户。

因此 practical 资源中的重要声明必须和官方/原始事实锚点交叉核验。

## 哪些属于 material claim

至少包括：

- 安装命令、配置文件位置、环境变量；
- API base URL、endpoint、认证方式；
- 模型名、版本名、provider 名；
- 产品是否支持某能力；
- 是否支持某平台/Agent/Skill/MCP；
- 价格、订阅、额度；
- deprecated / migration / breaking change；
- 明确效率/成本/性能数字；
- “自动完成某操作”之类会改变用户行为的能力声明。

普通观点、作者偏好、经验建议不必逐句核验。

## Capability Claim 的边界必须同构

产品能力声明最容易发生“偷换层级”。对每个 capability claim，必须额外记录：

| 字段 | 含义 |
|---|---|
| claim_capability_mode | standard_product / custom_extension / third_party_wrapper / unknown |
| anchor_capability_mode | 官方锚点实际证明的能力模式 |
| claim_platform_scope | 文章声称适用的平台/edition/部署范围 |
| anchor_platform_scope | 官方锚点实际适用范围 |
| scope_match | true / false / unclear |

硬规则：

- `custom_extension` 的官方文档不能作为 `standard_product` 原生能力的证明；
- 第三方 wrapper 能做到，不等于原产品能做到；
- S/4HANA Cloud Public 的能力不能自动外推到 Private / On-Premise；
- 旧版、预览版、限定租户能力不能外推为当前 GA 通用能力；
- `scope_match=false` 且影响核心价值 → critical conflict；
- `scope_match=unclear` → human_review，不得自动推荐。

示例：

> 第三方教程声称“Joule 可直接完成完整 SPRO 配置链”。
> 官方锚点只是“如何开发自定义 Joule Skill 并连接后端”。
> 两者 capability_mode 不同，不能互证；若没有标准 Joule 当前能力锚点支持该声明，应 conflict/unclear，而不是“加一句平台限制后继续推荐”。

## 锚点优先级

1. 官方当前文档 / 官方 Release / 官方产品页；
2. 原始仓库 README / Release / source metadata；
3. 官方 issue / maintainer 明确说明；
4. 多个可靠独立来源交叉确认。

搜索摘要、转载、AI总结不能作为事实锚点。

## 核验表

每条 material claim 内部记录：

| 字段 | 含义 |
|---|---|
| claim | 第三方资源实际声称什么 |
| criticality | critical / non_critical |
| anchor_url | 官方/原始锚点 |
| anchor_fact | 锚点实际说明 |
| verdict | supported / conflict / unclear |
| checked_at | 核验日期 |
| claim_capability_mode | 若为能力声明，声明属于哪种能力模式 |
| anchor_capability_mode | 官方锚点证明的能力模式 |
| claim_platform_scope | 声称的平台/edition/部署范围 |
| anchor_platform_scope | 官方锚点的平台/edition/部署范围 |
| scope_match | true / false / unclear |

## Critical 的判断

如果该声明错误会导致以下任一后果，就标记 critical：

- 用户照做无法运行；
- 用户配置错 API / 凭证 / 模型；
- 用户误以为产品具备不存在的能力；
- 用户做出明显错误的购买/部署/迁移决定；
- 资源的核心卖点因此不成立。

## 处理规则

- critical + supported：继续；
- critical + conflict：直接 `REJECT_FACT_CONFLICT`；
- critical + unclear：`human_review=true`，不得自动推荐；
- non_critical + conflict：可降分，但必须在推荐理由或限制里说明；
- capability_mode 不一致或 platform scope 不一致，且影响核心能力：按 critical conflict 处理；
- 没有 material claim：`claims=not_applicable`。

## 禁止行为

- 不得把“作者说能做”当成产品事实；
- 不得用另一篇社区文章证明第一篇社区文章；
- 不得看到步骤截图就默认配置仍然有效；
- 不得把发布日期新等同于事实正确；
- 不得自行执行教程命令来替代官方核验。


## 厂商自报数字不是独立事实

厂商/产品自己的案例中出现“3–6 周降到 2 小时”“85% fit”等数字，可以记录为 `vendor_claim`，但不得在推荐理由里改写成已经独立验证的客观事实。

推荐这类资源时，优先说明可核验的流程、管线、输入输出；若保留数字，必须写“厂商称/该页面声称”，且不能把数字作为主要推荐依据。
