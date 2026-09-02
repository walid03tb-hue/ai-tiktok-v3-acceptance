# Provider Contracts — FROZEN RC1

## Global production rule
Production never silently falls back to mock/demo/deterministic success.
Provider calls use one shared timeout/retry/quota/circuit/error-classification module.

## Canonical error taxonomy
- `PROVIDER_NOT_CONFIGURED`
- `PROVIDER_AUTH_FAILED`
- `SOURCE_UNAVAILABLE`
- `AI_QUOTA_EXHAUSTED`
- `AI_RATE_LIMIT`
- `AI_SERVICE_UNAVAILABLE`
- `AI_CLIENT_ERROR`
- `AI_TIMEOUT`
- `AI_RESPONSE_INVALID`
- `STALE_ASYNC_RESULT`

## Shared execution policy
- Hard daily/project quota fails fast; do not fan out across models/attempts after classification.
- Bounded retries only for explicitly transient failures.
- Pre-start dependency revalidation occurs before paid dispatch.
- Completion revalidation occurs before result becomes current.

## Asset Intelligence provider
Input: real validated media bytes/authenticated exact media ref + authoritative Product semantic context. Exact cache identity includes `productValuesHash` and provider/model/prompt/analyzer/schema. Output: strict asset/product/SHA identity, structured observations/evidence/segments. Visual provenance = `VISUAL_OBSERVATION`.

## Product / Ad Intelligence provider
Consumes canonical Product values + exact AnalysisContext. May propose insights; may not invent missing facts or authorize claims.

## Creative provider
Consumes exact Product/authority/claim/AnalysisContext. Produces candidates only; deterministic validators decide eligibility.

## Semantic consistency provider
Bound to `productValuesHash + creativeTextHash`. Cannot bypass claim, asset, or workspace truth.

## TTS provider
Production real configured provider only. Physical audio must exist, hash, and probe before READY. Missing provider is failure, not synthetic fallback.

## Alignment provider
Real ASR/alignment only. Timestamps derive from audio. Arabic tolerance uses a separate versioned alignment normalization profile; no proportional interpolation.

## Veo provider
DB-first unique claim before paid dispatch. Persist providerOperationId, exact dedupe identity/input hash, restart reconciliation and downloaded-output validation before READY.
