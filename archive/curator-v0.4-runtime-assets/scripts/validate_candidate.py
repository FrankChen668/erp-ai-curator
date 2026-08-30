#!/usr/bin/env python3
"""Deterministic pre-score guard for V0.4 candidate records.

This does not decide whether evidence is true. It prevents obvious workflow
violations: gate failures, resource-type mismatch, unresolved forks, critical
claim conflicts, capability-scope substitution, metadata-only practical
resources, and unsupported superlatives.
"""
import argparse
import json
import sys
from pathlib import Path

BANNED = ["最好", "最强", "唯一", "最完整", "维护最认真", "行业标杆", "必看", "闭眼入"]
VALID_GATE = {"pass", "review", "fail", "not_applicable"}
GATE_FIELDS = [
    "gate_topic_fit",
    "gate_output_fit",
    "gate_resource_type_fit",
    "gate_provenance",
    "gate_claims",
    "gate_practicality",
    "gate_freshness",
]
VALID_RESOURCE_TYPES = {
    "tool", "skill", "tutorial", "official_doc", "case",
    "collection", "prompt_framework", "other"
}
VALID_CAPABILITY_MODES = {
    "standard_product", "custom_extension", "third_party_wrapper", "unknown"
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    args = ap.parse_args()

    data = json.loads(Path(args.file).read_text(encoding="utf-8"))
    errors = []

    slot = data.get("slot")
    if slot not in {"canonical", "practical"}:
        errors.append("slot must be canonical or practical")

    resource_type = data.get("resource_type")
    if resource_type not in VALID_RESOURCE_TYPES:
        errors.append(f"resource_type must be one of {sorted(VALID_RESOURCE_TYPES)}")

    requested = data.get("requested_resource_types")
    if not isinstance(requested, list) or not requested:
        errors.append("requested_resource_types must be a non-empty list")
    else:
        unknown = [x for x in requested if x not in VALID_RESOURCE_TYPES]
        if unknown:
            errors.append(f"unknown requested_resource_types: {unknown}")
        if resource_type in VALID_RESOURCE_TYPES and resource_type not in requested:
            errors.append("resource_type is outside requested_resource_types")

    for field in GATE_FIELDS:
        value = data.get(field)
        if value not in VALID_GATE:
            errors.append(f"{field} must be one of {sorted(VALID_GATE)}")

    if data.get("gate_result") != "pass":
        errors.append("gate_result must be pass before scoring/recommending")

    if data.get("human_review") is True:
        errors.append("human_review=true candidate cannot auto-pass")

    if data.get("critical_claim_conflicts", 0) not in (0, None):
        errors.append("critical claim conflict blocks recommendation")

    for field in ["gate_topic_fit", "gate_output_fit", "gate_resource_type_fit", "gate_provenance", "gate_freshness"]:
        if data.get(field) != "pass":
            errors.append(f"{field} must pass")

    if data.get("gate_claims") not in {"pass", "not_applicable"}:
        errors.append("gate_claims must be pass or not_applicable")

    if slot == "practical":
        if data.get("verification_level") not in {"content_checked", "cross_checked"}:
            errors.append("practical requires content_checked or cross_checked")
        if data.get("gate_practicality") != "pass":
            errors.append("practical slot requires gate_practicality=pass")

    repo = data.get("repo") or {}
    if repo.get("is_fork") is True:
        if repo.get("upstream_checked") is not True:
            errors.append("fork requires upstream_checked=true")
        if not repo.get("upstream_url"):
            errors.append("fork requires upstream_url")
        if data.get("selected_over_upstream") is True and not data.get("fork_advantage_evidence"):
            errors.append("fork selected over upstream requires fork_advantage_evidence")

    for i, claim in enumerate(data.get("material_claims") or []):
        critical = claim.get("criticality") == "critical"
        verdict = claim.get("verdict")
        if critical and verdict == "conflict":
            errors.append(f"material_claims[{i}] critical conflict")
        if critical and verdict == "unclear":
            errors.append(f"material_claims[{i}] critical unclear requires human review")

        if claim.get("claim_type") == "product_capability":
            cm = claim.get("claim_capability_mode")
            am = claim.get("anchor_capability_mode")
            if cm not in VALID_CAPABILITY_MODES:
                errors.append(f"material_claims[{i}] invalid claim_capability_mode")
            if am not in VALID_CAPABILITY_MODES:
                errors.append(f"material_claims[{i}] invalid anchor_capability_mode")
            scope_match = claim.get("scope_match")
            if scope_match not in {True, False, "unclear"}:
                errors.append(f"material_claims[{i}] scope_match must be true/false/unclear")
            if critical and (cm != am or scope_match is False):
                errors.append(f"material_claims[{i}] critical capability mode/scope mismatch")
            if critical and scope_match == "unclear":
                errors.append(f"material_claims[{i}] critical capability scope unclear")

    why = data.get("why_recommended", "") or ""
    for term in BANNED:
        if term in why and not data.get("superlative_evidence"):
            errors.append(f"unsupported superlative in why_recommended: {term}")

    if errors:
        print(json.dumps({"valid": False, "errors": errors}, ensure_ascii=False, indent=2))
        sys.exit(1)

    print(json.dumps({"valid": True, "message": "candidate passed V0.4 deterministic pre-score guards"}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
