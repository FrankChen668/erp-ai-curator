#!/usr/bin/env python3
import argparse, csv, sys
from pathlib import Path

SCHEMAS = {
    "resources.csv": {"resource_id","canonical_url","title","verification_level","verified_at"},
    "topics.csv": {"topic_id","topic_key","topic_type","freshness_class"},
    "recommendations.csv": {"recommendation_id","topic_id","resource_id","slot","status","human_review"},
    "runs.csv": {"run_id","mode","topic_id","started_at","commit_status"},
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    args = ap.parse_args()
    base = Path(args.dir)
    errs=[]
    for fn, required in SCHEMAS.items():
        p=base/fn
        if not p.exists():
            errs.append(f"missing {fn}")
            continue
        with p.open(encoding="utf-8-sig", newline="") as f:
            r=csv.reader(f)
            try: hdr=set(next(r))
            except StopIteration: hdr=set()
        miss=required-hdr
        if miss: errs.append(f"{fn} missing columns: {sorted(miss)}")
    if errs:
        print("INVALID")
        for e in errs: print("-",e)
        sys.exit(1)
    print("VALID")

if __name__ == "__main__":
    main()
