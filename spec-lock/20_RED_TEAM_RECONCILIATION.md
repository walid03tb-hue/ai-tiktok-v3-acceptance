# V3 Red-Team Reconciliation — Gemini + Claude — RC1

This file records the accepted architecture decisions after two independent pre-build reviews. It is explanatory; the normative implementation contract is the frozen Constitution and supporting files.

## Accepted P0 decisions

### 1. Split canonical hash model
Accepted. Single `factsHash` / `assetManifestHash` model removed. Frozen Product domains: `productValuesHash`, `factAuthorityHash`, `claimSetHash`, `revisionSnapshotHash`. Frozen asset domains: `rawAssetManifestHash`, `assetAnalysisInputHash`, `analysisContextHash`.

### 2. RawAssetManifest != AnalysisContext
Accepted. Raw manifest proves physical/frozen media truth only. AI analysis identity lives in immutable AnalysisContext.

### 3. AssetAnalysis cache includes Product semantic context
Accepted. Exact `assetAnalysisInputHash` includes `productValuesHash`; no OR/legacy cache fallback.

### 4. Claim vs semantic invalidation are different
Accepted. Semantic consistency binds `productValuesHash + creativeTextHash`. Claim grounding binds `factAuthorityHash + claimSetHash + creativeTextHash + scriptHash`.

### 5. ProductRevision concurrency
Accepted. Unique revision number + one-transaction insert/CAS pointer update; conflict = 409 `PRODUCT_REVISION_CONFLICT`.

### 6. Async staleness is target-specific
Accepted. `packRevision` / Product revision may be audit metadata but not universal invalidation. Revalidate exact operation dependency before start/paid dispatch and before applying completion.

### 7. Canonical QA enum
Accepted. `NOT_REVIEWED`, `RUNNING`, `APPROVED`, `NEEDS_RERENDER`, `REJECTED`. `PASSED` forbidden as canonical QA status.

### 8. Arabic alignment normalization
Problem accepted; Gemini's proposed solution was narrowed. Canonical `scriptHash` preserves actual production spoken-copy identity. Tolerant Arabic/number matching is a separate versioned alignment normalization profile. Do not globally fold `ة -> ه`; thresholds/rules must be proven by Spike 2.

### 9. Veo/paid-operation concurrent duplicate spend
Accepted and treated as P0. DB uniqueness claim occurs before provider dispatch; only one winner may call provider.

### 10. Acceptance-suite technical protection
Accepted. Preferred design: separate private read-only acceptance repo/package pinned by revision/checksum. Same-repo prose protection is insufficient.

## Accepted P1 hardening
- Pre-start async revalidation to avoid paying for already-stale work.
- RawAssetManifest includes READY assets only.
- Production CreativePack is exactly six; under-six candidate set is not a production pack.
- CI runs real migrations against ephemeral PostgreSQL/PGlite and isolated storage.
- Provider error taxonomy is one canonical shared enum.
- Local storage adapter must enforce resolved-root containment; client never chooses arbitrary physical path.
- FFprobe/container duration validation uses a bounded tolerance frozen after Spike 3, not exact-millisecond equality.

## Explicitly rejected/modified review advice

### Arabic scriptHash normalization
Rejected as originally phrased. Removing diacritics/folding letters/expanding digits before `scriptHash` can merge distinct canonical copy identities and create cache/audit ambiguity. Those transformations are allowed only in alignment matching profile.

### Global `ة -> ه`
Not frozen. Too aggressive without measured evidence. Spike 2 may justify a narrower equivalence rule.

## Current build verdict
Architecture reconciliation: complete for RC1.
Implementation start: **NOT YET**. External acceptance harness, risk spikes, GitHub/CI setup, and one final consistency pass remain pre-build gates.
