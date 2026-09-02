# V3 Definition of Done — FROZEN RC1

## Foundation done
- server authority + workspace tests green
- immutable CAS-protected Product revisions/snapshots
- split hash domains implemented once
- precise staleness tests green
- physical media truth green
- READY-only RawAssetManifest freeze
- exact AnalysisContext binding green
- AssetAnalysis cache bound to productValuesHash
- no production mock fallback
- migrations run successfully on ephemeral PostgreSQL/PGlite in CI

## Creative done
- production pack = exactly six or fail closed
- semantic Product consistency gate
- all final factual/commercial assertions extracted
- deterministic claim grounding bound to authority/claim hashes
- evidence-gated BEFORE_AFTER/social proof/urgency
- atomic pack replacement
- optimistic concurrency
- one canonical scriptHash = hook+script+CTA

## Voice/timeline done
- real production TTS
- real ASR alignment
- versioned Saudi-Arabic alignment matcher validated by Spike 2
- no scriptHash corruption for ASR tolerance
- no unrelated audio fallback
- canonical MasterTimeline
- pre-start + completion stale async guards

## Visual/render done
- exact scene/asset/segment binding
- selective AI visuals with DB-first paid-op dedupe
- restart-safe provider operations
- canonical render gate
- real FFmpeg output
- exact output hash/probe validation
- QA default NOT_REVIEWED, canonical approval = APPROVED, exact-output bound

## Production done
- workspace/auth boundaries
- Cloud SQL / Cloud Storage / Cloud Tasks / Secret Manager
- migrations tested
- worker restart reconciliation
- rate/upload/path controls
- structured logs/monitoring
- protected read-only external acceptance suite with pinned revision/checksum
- no runtime artifacts in repo/release
- no unresolved P0/P1 blocker from final external audit

## Meaning of ready
A phase is complete only when real HTTP/worker/storage/provider paths satisfy frozen invariants and the protected acceptance suite is green. A UI, mocked happy path, or self-authored PASS is not completion.
