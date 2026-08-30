#!/usr/bin/env python3
"""Deterministic repository-contract checks for ERP AI Curator.

This script intentionally checks only machine-verifiable project facts.
It does NOT score recommendation quality or validate product value.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "curating-erp-ai-resources"
SKILL = SKILL_DIR / "SKILL.md"

REQUIRED = [
    ROOT / "docs" / "PROJECT_MAP.md",
    ROOT / "docs" / "PROJECT_NORTH_STAR.md",
    ROOT / "docs" / "OWNER_EXECUTION_RULES.md",
    ROOT / "docs" / "CURRENT_EXECUTION_PLAN_V3.md",
    ROOT / "docs" / "validation" / "EVIDENCE_STATUS.md",
    ROOT / "docs" / "REAL_USER_PILOT_V1.md",
    ROOT / "docs" / "SESSION_HANDOFF_CURRENT.md",
    ROOT / "docs" / "PROJECT_CALIBRATION_20260830.md",
    SKILL,
    SKILL_DIR / "references" / "adoption-consistency.md",
    SKILL_DIR / "references" / "decision-boundaries.md",
    SKILL_DIR / "references" / "evidence-and-safety.md",
    ROOT / "docs" / "curation-cases" / "CASE_001_ERP_OPERATING_MANUAL.md",
    ROOT / "docs" / "curation-cases" / "CASE_002_ORACLE_EBS_DEVELOPMENT.md",
]

CURRENT_DOCS = [
    ROOT / "README.md",
    ROOT / "docs" / "CURRENT_EXECUTION_PLAN_V3.md",
    ROOT / "docs" / "SESSION_HANDOFF_CURRENT.md",
    ROOT / "docs" / "validation" / "EVIDENCE_STATUS.md",
]

OLD_PILOT_CASES = [
    ROOT / "docs" / "pilot" / "PILOT_CASE_001_ERP_OPERATING_MANUAL.md",
    ROOT / "docs" / "pilot" / "PILOT_CASE_002_ORACLE_EBS_DEVELOPMENT.md",
]

errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


for path in REQUIRED:
    check(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")

if SKILL.is_file():
    text = SKILL.read_text(encoding="utf-8")
    name_match = re.search(r"(?m)^name:\s*([^\n]+)$", text)
    version_match = re.search(r'(?m)^\s*version:\s*"?([^"\n]+)"?\s*$', text)
    check(bool(name_match), "SKILL.md missing frontmatter name")
    check(bool(version_match), "SKILL.md missing metadata.version")

    if name_match:
        skill_name = name_match.group(1).strip().strip('"\'')
        check(skill_name == SKILL_DIR.name, f"skill name {skill_name!r} != directory {SKILL_DIR.name!r}")
    else:
        skill_name = ""

    version = version_match.group(1).strip() if version_match else ""
    if version:
        for path in CURRENT_DOCS:
            if path.is_file():
                doc = path.read_text(encoding="utf-8")
                check(version in doc, f"current Skill version {version} missing from {path.relative_to(ROOT)}")

    referenced = set(re.findall(r"\(references/([^\)]+\.md)\)", text))
    for ref in referenced:
        check((SKILL_DIR / "references" / ref).is_file(), f"SKILL.md references missing file: references/{ref}")

check(not (SKILL_DIR / "README.md").exists(), "runtime Skill package must not contain README.md")

for old in OLD_PILOT_CASES:
    check(not old.exists(), f"legacy Pilot case path still exists: {old.relative_to(ROOT)}")

for case in REQUIRED[-2:]:
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
    check("version: `0.6.0`" not in readme_text, "README contains known stale Skill version 0.6.0")

if errors:
    print("PROJECT CONTRACT: FAIL")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print("PROJECT CONTRACT: PASS")
print(f"- skill: {skill_name or 'unknown'}")
print(f"- version: {version or 'unknown'}")
print(f"- required files: {len(REQUIRED)}")
print("- curation/user-use evidence lanes: explicit")
print("- runtime Skill README: absent")
