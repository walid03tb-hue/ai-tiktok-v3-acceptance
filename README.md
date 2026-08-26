# AI TikTok V3 — Protected External Acceptance Harness

This repository is the independent judge for the V3 implementation. The implementation builder must have read-only access and must never edit acceptance source.

## Integrity rules
- `main` is protected remotely with required human review.
- implementation CI checks out an exact pinned commit SHA.
- `run.sh` verifies frozen-spec hashes before acceptance checks.
- acceptance changes require an operator-approved commit in this repository.

## Current executable scope
Pre-build/Phase 0 integrity is executable now. Phase 1 black-box authority cases are frozen in `cases/phase1_product_authority.json`. Their HTTP adapter is activated only after Phase 0 freezes the exact public response envelope; this avoids inventing an API contract outside the Constitution.

## Run
```bash
V3_APP_ROOT=/path/to/ai-tiktok-creative-factory-v3 ./run.sh
```
