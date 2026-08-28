# 数据模型

V0.1 的“一张主表”会让资源事实和推荐关系混在一起。V0.2 拆成四张表。

## 1. resources.csv — 资源事实

一条 URL 只存在一次。

核心字段：
- resource_id
- canonical_url
- title
- resource_type：资源客观类型，建议 tool/skill/tutorial/official_doc/case/collection/prompt_framework/other
- platform
- language
- author
- published_at
- updated_at
- version_scope
- provenance_class
- access_status
- verification_level
- verified_at
- content_fingerprint（可选）

## 2. topics.csv — 用户入口主题

核心字段：
- topic_id
- topic_key
- topic_type: task/tool/skill
- lifecycle_stage
- workstream
- task
- tool
- skill_name
- role_tags
- freshness_class
- created_at

## 3. recommendations.csv — 资源 × 主题关系

同一资源可推荐给多个任务，不复制资源本身。

核心字段：
- recommendation_id
- topic_id
- resource_id
- slot: canonical/practical
- status: candidate/recommended/superseded/rejected
- score
- why_recommended
- duplicate_group
- replacement_of
- replaced_by
- human_review
- decision_confidence
- decided_at

## 4. runs.csv — 采编运行记录

核心字段：
- run_id
- mode
- topic_id
- started_at
- finished_at
- query_count
- fetch_count
- source_coverage
- blocked_sources
- candidates_found
- proposed_changes
- commit_status
- notes

## ID 规则

- resource_id：由 canonical_url 稳定哈希生成。
- topic_id：由规范化 topic_key 稳定哈希生成。
- recommendation_id：由 topic_id + resource_id + slot 稳定哈希生成。

不得使用随机 ID 导致重复。

## V0.4 staging 审计记录（不增加正式第五张表）

为了避免把逐候选 Gate/claim 细节塞进正式资源表，V0.4 建议每次运行在 staging 保存临时 `candidate-review.jsonl` 或等价结构。

每条候选至少包含：
- candidate_url
- topic_id
- slot
- resource_type
- requested_resource_types
- fit_sentence
- reroute_topic（可选）
- gate_topic_fit / gate_output_fit / gate_resource_type_fit / gate_provenance / gate_claims / gate_practicality / gate_freshness
- gate_result
- rejection_code
- verification_level
- material_claims（若有；capability claim 还需 capability_mode / platform_scope / scope_match）
- repo.is_fork / upstream_url / upstream_checked（GitHub 若适用）
- evidence（短事实列表）
- human_review

该文件用于人工抽查和回归测试，不要求进入最终用户视图，也不改变四表正式数据模型。
