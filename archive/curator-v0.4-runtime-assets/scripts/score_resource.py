#!/usr/bin/env python3
import argparse, json
from pathlib import Path

WEIGHTS = {
    "canonical": {
        "topic_fit": 20,
        "provenance_authority": 25,
        "freshness_compatibility": 20,
        "coverage_completeness": 15,
        "accessibility": 10,
        "maintainability": 5,
        "community_signal": 5,
    },
    "practical": {
        "topic_fit": 20,
        "actionability": 25,
        "reproducibility": 20,
        "freshness_compatibility": 15,
        "credibility": 10,
        "clarity": 5,
        "community_signal": 5,
    },
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slot", choices=WEIGHTS, required=True)
    ap.add_argument("file")
    args = ap.parse_args()
    data = json.loads(Path(args.file).read_text(encoding="utf-8"))
    weights = WEIGHTS[args.slot]
    missing = [k for k in weights if k not in data]
    if missing:
        raise SystemExit("missing fields: " + ", ".join(missing))
    for k in weights:
        v = data[k]
        if not isinstance(v, (int, float)) or not 0 <= v <= 4:
            raise SystemExit(f"{k} must be 0..4")
    # 4 maps to full weight.
    score = sum((data[k] / 4.0) * w for k, w in weights.items())
    print(json.dumps({"slot": args.slot, "score": round(score, 1), "weights": weights}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
