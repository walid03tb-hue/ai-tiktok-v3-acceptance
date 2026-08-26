#!/usr/bin/env python3
from __future__ import annotations
import hashlib, os, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
APP=Path(os.environ['V3_APP_ROOT']).resolve() if os.environ.get('V3_APP_ROOT') else None

def sha256(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()
def fail(msg): print('ACCEPTANCE_INTEGRITY_FAIL: '+msg, file=sys.stderr); raise SystemExit(1)
entries=[]
for line in (ROOT/'frozen-spec.sha256').read_text().splitlines():
    if line.strip():
        digest,name=line.split(maxsplit=1); entries.append((digest,name.strip()))
for digest,name in entries:
    p=ROOT/'spec-lock'/name
    if not p.exists() or sha256(p)!=digest: fail('acceptance spec-lock drift: '+name)
if APP:
    if not APP.exists(): fail('V3_APP_ROOT missing: '+str(APP))
    for digest,name in entries:
        p=APP/'docs'/'v3'/name
        if not p.exists(): fail('implementation missing frozen doc: docs/v3/'+name)
        if sha256(p)!=digest: fail('implementation modified frozen doc: docs/v3/'+name)
print(f'ACCEPTANCE_INTEGRITY_PASS: {len(entries)} frozen documents verified')
