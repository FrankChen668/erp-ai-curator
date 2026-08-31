#!/usr/bin/env python3
"""Deterministic repository-contract checks for ERP AI Curator.

This script intentionally checks only machine-verifiable project facts.
It does NOT score recommendation quality or enforce arbitrary prompt-size targets.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRACTICE_SKILL_DIR = ROOT / "skills" / "curating-erp-ai-resources"
ADVISOR_SKILL_DIR = ROOT / "skills" / "advising-erp-ai-capabilities"
RUNTIME_SKILL_DIRS = [PRACTICE_SKILL_DIR, ADVISOR_SKILL_DIR]
RUNTIME_SKILLS = [path / "SKILL.md" for path in RUNTIME_SKILL_DIRS]

CURATION_CASES = [
    ROOT / "docs" / "curation-cases" / "CASE_001_ERP_OPERATING_MANUAL.md",
    ROOT / "docs" / "curation-cases" / "CASE_002_ORACLE_EBS_DEVELOPMENT.md",
    ROOT / "docs" / "curation-cases" / "CASE_003_WEEKLY_REPORT_CONSOLIDATION.md",
    ROOT / "docs" / "curation-cases" / "CASE_004_SAP_BUG_DIAGNOSIS_SYSTEM_ACCESS.md",
]

RUNTIME_REFERENCES = [
    PRACTICE_SKILL_DIR / "references" / "practitioner-discovery.md",
    ADVISOR_SKILL_DIR / "references" / "evidence-and-safety.md",
]

REMOVED_OR_MISPLACED_RUNTIME_FILES = [
    PRACTICE_SKILL_DIR / "README.md",
    ADVISOR_SKILL_DIR / "README.md",
    PRACTICE_SKILL_DIR / "references" / "evidence-and-safety.md",
    ADVISOR_SKILL_DIR / "references" / "practitioner-discovery.md",
    PRACTICE_SKILL_DIR / "references" / "adoption-consistency.md",
    PRACTICE_SKILL_DIR / "references" / "decision-boundaries.md",
]

REQUIRED = [
    ROOT / "docs" / "PROJECT_MAP.md",
    ROOT / "docs" / "PROJECT_NORTH_STAR.md",
    ROOT / "docs" / "OWNER_EXECUTION_RULES.md",
    ROOT / "docs" / "CURRENT_EXECUTION_PLAN_V3.md",
    ROOT / "docs" / "validation" / "EVIDENCE_STATUS.md",
    ROOT / "docs" / "REAL_USER_PILOT_V1.md",
    ROOT / "docs" / "USER_TRIAL_GUIDE_V1.md",
    ROOT / "docs" / "SESSION_HANDOFF_CURRENT.md",
    ROOT / "docs" / "PROJECT_CALIBRATION_20260830.md",
    ROOT / "docs" / "validation" / "CURATION_PACK_01_ADVERSARIAL_REVIEW.md",
    ROOT / "docs" / "validation" / "RELEASE_READINESS_ADVERSARIAL_20260830.md",
    ROOT / "docs" / "validation" / "CURATOR_080_RUNTIME_SIMPLIFICATION.md",
    ROOT / "docs" / "validation" / "CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md",
    *RUNTIME_SKILLS,
    *RUNTIME_REFERENCES,
    *CURATION_CASES,
]

CURRENT_DOCS = [
    ROOT / "README.md",
    ROOT / "docs" / "CURRENT_EXECUTION_PLAN_V3.md",
    ROOT / "docs" / "SESSION_HANDOFF_CURRENT.md",
    ROOT / "docs" / "validation" / "EVIDENCE_STATUS.md",
    ROOT / "docs" / "USER_TRIAL_GUIDE_V1.md",
]

OLD_PILOT_CASES = [
    ROOT / "docs" / "pilot" / "PILOT_CASE_001_ERP_OPERATING_MANUAL.md",
    ROOT / "docs" / "pilot" / "PILOT_CASE_002_ORACLE_EBS_DEVELOPMENT.md",
]

errors: list[str] = []
versions: set[str] = set()


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


for path in REQUIRED:
    check(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")

for skill_dir in RUNTIME_SKILL_DIRS:
    skill = skill_dir / "SKILL.md"
    if not skill.is_file():
        continue

    text = skill.read_text(encoding="utf-8")
    name_match = re.search(r"(?m)^name:\s*([^\n]+)$", text)
    version_match = re.search(r'(?m)^\s*version:\s*"?([^"\n]+)"?\s*$', text)
    check(bool(name_match), f"{skill.relative_to(ROOT)} missing frontmatter name")
    check(bool(version_match), f"{skill.relative_to(ROOT)} missing metadata.version")

    if name_match:
        skill_name = name_match.group(1).strip().strip("\"'")
        check(skill_name == skill_dir.name, f"skill name {skill_name!r} != directory {skill_dir.name!r}")

    if version_match:
        versions.add(version_match.group(1).strip())

    referenced = set(re.findall(r"\(references/([^\)]+\.md)\)", text))
    for ref in referenced:
        check((skill_dir / "references" / ref).is_file(), f"{skill.relative_to(ROOT)} references missing file: references/{ref}")

check(len(versions) == 1, f"runtime Skill versions must match, found: {sorted(versions)}")
version = next(iter(versions), "")
if version:
    for path in CURRENT_DOCS:
        if path.is_file():
            doc = path.read_text(encoding="utf-8")
            check(version in doc, f"current runtime version {version} missing from {path.relative_to(ROOT)}")

for path in REMOVED_OR_MISPLACED_RUNTIME_FILES:
    check(not path.exists(), f"removed/misplaced runtime file exists: {path.relative_to(ROOT)}")

for old in OLD_PILOT_CASES:
    check(not old.exists(), f"legacy Pilot case path still exists: {old.relative_to(ROOT)}")

for case in CURATION_CASES:
    if case.is_file():
        body = case.read_text(encoding="utf-8")
        check("NOT USER-USE EVIDENCE" in body, f"curation case lacks explicit evidence boundary: {case.relative_to(ROOT)}")

map_path = ROOT / "docs" / "PROJECT_MAP.md"
if map_path.is_file():
    map_text = map_path.read_text(encoding="utf-8")
    links = re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", map_text)
    for raw in links:
        if "://" in raw:
            continue
        target = (map_path.parent / raw).resolve()
        check(target.is_file(), f"broken local Markdown link in PROJECT_MAP.md: {raw}")

readme = ROOT / "README.md"
if readme.is_file():
    readme_text = readme.read_text(encoding="utf-8")
    check("CONTROLLED USER TRIAL" in readme_text.upper(), "README missing controlled-user-trial release boundary")
    check("curating-erp-ai-resources" in readme_text, "README missing Practice Curator entry")
    check("advising-erp-ai-capabilities" in readme_text, "README missing Capability Advisor entry")

release_review = ROOT / "docs" / "validation" / "RELEASE_READINESS_ADVERSARIAL_20260830.md"
if release_review.is_file():
    release_text = release_review.read_text(encoding="utf-8").upper()
    check("CONTROLLED USER TRIAL GO / BROAD RELEASE NO" in release_text, "release readiness verdict drifted")

if errors:
    print("PROJECT CONTRACT: FAIL")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print("PROJECT CONTRACT: PASS")
print(f"- runtime version: {version or 'unknown'}")
print(f"- runtime skills: {len(RUNTIME_SKILLS)}")
for skill in RUNTIME_SKILLS:
    print(f"  - {skill.parent.name}: {len(skill.read_text(encoding='utf-8').splitlines())} lines")
print(f"- runtime references: {len(RUNTIME_REFERENCES)}")
print(f"- curation cases: {len(CURATION_CASES)}")
print("- curation/user-use evidence lanes: explicit")
print("- release boundary: controlled trial only")
