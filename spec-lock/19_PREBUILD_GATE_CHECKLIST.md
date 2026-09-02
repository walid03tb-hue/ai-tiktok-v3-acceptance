# Pre-Build Gate Checklist — FROZEN RC1

V3 implementation MUST NOT begin until every required item is green.

## Architecture/review
- [x] One primary frozen Constitution exists
- [x] Historical amendments demoted from authority to rationale
- [x] Gemini independent red-team complete
- [x] Claude independent red-team complete
- [x] Red-team P0/P1 architecture decisions reconciled in RC1
- [x] Split hash/staleness model frozen
- [x] RawAssetManifest / AnalysisContext separation frozen
- [x] ProductRevision concurrency contract frozen
- [x] QA canonical status frozen (`APPROVED`, never `PASSED`)
- [x] Arabic script identity vs alignment normalization separated
- [x] Async target-specific pre-start/completion revalidation frozen
- [x] DB-first paid-operation dedupe frozen
- [x] Provider error taxonomy unified
- [x] Production exactly-six CreativePack semantics frozen

## External judge / CI
- [ ] Protected external acceptance repository/package created
- [ ] Builder has no write permission to acceptance source
- [ ] Pinned acceptance revision/checksum configured in CI + BUILD_STATE
- [ ] GitHub implementation repository created
- [ ] Branch protection / required reviews configured
- [ ] CI uses isolated ephemeral PostgreSQL + storage
- [ ] CI baseline green with real migrations

## Risk spikes
- [ ] Spike 1 real multimodal evidence complete
- [ ] Spike 2 Saudi Arabic TTS/alignment complete and thresholds/profile frozen
- [ ] Spike 3 FFmpeg render complete and bounded probe-duration tolerance frozen
- [ ] Spike 4 async restart/dedupe/pre-start revalidation complete
- [ ] Spike 5 Veo viability/product-fidelity complete or consciously deferred with policy

## Cloud/provider/security
- [ ] Provider choices/settings frozen from spike evidence
- [ ] `v3-dev` cloud topology configured as needed
- [ ] Production credentials absent from repo/frontend
- [ ] Secret Manager/provider config plan verified

## Build operating system
- [x] BUILD_STATE protocol present
- [x] Autonomous builder prompt frozen
- [x] Bootstrap script copies frozen docs + CI template
- [ ] Final consistency pass returns no build-blocking contradiction

Only then set `CURRENT_PHASE: PHASE_0`.
