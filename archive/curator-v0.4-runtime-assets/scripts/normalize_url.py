#!/usr/bin/env python3
import argparse, hashlib
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

DROP_PREFIXES = ("utm_",)
DROP_KEYS = {"spm", "from", "source", "ref", "ref_src", "share_source", "share_medium"}

def normalize(url: str) -> str:
    p = urlsplit(url.strip())
    scheme = p.scheme.lower()
    host = p.netloc.lower()
    path = p.path.rstrip("/") or "/"
    qs = []
    for k, v in parse_qsl(p.query, keep_blank_values=True):
        lk = k.lower()
        if lk in DROP_KEYS or any(lk.startswith(x) for x in DROP_PREFIXES):
            continue
        qs.append((k, v))
    qs.sort()
    return urlunsplit((scheme, host, path, urlencode(qs), ""))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    args = ap.parse_args()
    u = normalize(args.url)
    rid = "res-" + hashlib.sha256(u.encode()).hexdigest()[:16]
    print(u)
    print(rid)

if __name__ == "__main__":
    main()
