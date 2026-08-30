# 分槽评分

## 前置条件

**只有 Candidate Gates 全 PASS 的候选才能进入评分。**

评分不是安全网，不能救回：
- 主题错配；
- critical fact conflict；
- 未解析 upstream 的 fork；
- metadata_only 的 practical；
- 明显过期/失效资源。

## 为什么不用一套分数

canonical 与 practical 的使命不同，不能把两者放在同一总榜。

评分只做同槽幸存者排序。

## 评分锚点

每个维度只允许 0–4：

- 0：失败/明显不满足
- 1：弱，存在严重缺陷
- 2：可用，但普通或有明显限制
- 3：强，满足主要要求
- 4：优秀，有清晰证据支撑

不要凭感觉直接填 92、87 之类的数字。脚本会把 0–4 映射为 0–100。

## canonical 权重

| 维度 | 权重 |
|---|---:|
| topic_fit | 20 |
| provenance_authority | 25 |
| freshness_compatibility | 20 |
| coverage_completeness | 15 |
| accessibility | 10 |
| maintainability | 5 |
| community_signal | 5 |

## practical 权重

| 维度 | 权重 |
|---|---:|
| topic_fit | 20 |
| actionability | 25 |
| reproducibility | 20 |
| freshness_compatibility | 15 |
| credibility | 10 |
| clarity | 5 |
| community_signal | 5 |

## 证据纪律

每个 0、1、4 的评分必须有一句短证据；2、3 建议保留证据。

热度只占 5%，且不能跨平台机械比较。

GitHub 的 Star 不能覆盖：fork、停更、无使用说明、版本不兼容等 Gate/事实问题。

## 语言 tie-breaker

语言不计基础分。

同槽候选分差 ≤5 分且质量近似：中文优先；英文明显更权威/完整/更新则保留英文。

## 推荐阈值

建议：
- >=80：强候选
- 72–79：可用但需看竞争情况
- <72：默认不占推荐位

阈值不能救回硬门槛失败项。
