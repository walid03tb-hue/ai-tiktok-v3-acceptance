#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
phase1=json.loads((R/'cases/phase1_product_authority.json').read_text())
ids=[c['id'] for c in phase1['cases']]
assert len(ids)==len(set(ids))
assert len(ids)>=10
allids=json.loads((R/'cases/all_phase_acceptance_ids.json').read_text())
flat=[x for xs in allids['groups'].values() for x in xs]
assert len(flat)==len(set(flat))
assert len(flat)>=50
print('ACCEPTANCE_CASE_CATALOG_PASS')
