# Canonical Hash Domains and Staleness Matrix — FROZEN RC1

## Hash rules

All hashes come from one canonical module using stable deterministic serialization + SHA-256.

- `productValuesHash`: semantic Product values only; excludes provenance/actors/timestamps/verification metadata.
- `factAuthorityHash`: exact fact values + provenance/evidence/verification authority.
- `claimSetHash`: exact claims/risk/evidence/authorization state.
- `revisionSnapshotHash`: full immutable ProductRevision audit identity; never universal invalidation key.
- `rawAssetManifestHash`: exact physical frozen assets/SHAs/roles/availability/render-safe metadata only.
- `assetAnalysisInputHash`: workspaceId + productId + assetSha256 + productValuesHash + provider + model + promptVersion + analyzer/schemaVersion.
- `analysisContextHash`: exact validated AssetAnalysis identities + rawAssetManifestHash + productValuesHash.
- `creativeTextHash`: exact production creative semantic/copy identity including final production spoken/subtitle text required by claim gates.
- `scriptHash`: exact spoken hook + script + CTA using semantic-preserving canonicalization only.
- `audioHash`: SHA-256 over real audio bytes.
- `alignmentHash`: exact validated alignment + audioHash + scriptHash + provider/model/version + alignment normalization profile version.
- `timelineHash`: exact MasterTimeline content.
- `scenePlanHash`: exact scene plan + bound assets/segments/AI-media refs.
- `renderInputHash`: every physical render dependency.
- `renderOutputHash`: SHA-256 over final rendered bytes.

## Arabic alignment identity rule

`scriptHash` is NOT computed from tolerant ASR-normalized Arabic. Alignment matching uses a separate versioned normalization profile and preserves mapping back to raw canonical text.

## Missing binding rule

Missing required hash/context = incompatible. `!hash || compatible` is forbidden.

## Staleness matrix

| Change | Raw assets | Asset analysis | Product intelligence | Semantic | Claim grounding | TTS | Alignment | Timeline | Scenes | Render | QA |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Same value becomes USER_VERIFIED | keep | keep | keep unless authority-sensitive UI needs refresh | keep | re-ground affected | keep if script unchanged | keep | keep | keep unless eligibility changes | keep if input unchanged | keep exact-output QA |
| Claim verification only | keep | keep | keep | keep | re-ground affected | keep if text unchanged | keep | keep | keep unless eligibility changes | keep if input unchanged | keep |
| Claim removal | keep | keep | usually keep | keep | stale affected | stale only if creative text/validity changes | downstream as needed | downstream | downstream | downstream | downstream |
| Product semantic value change | keep raw bytes | stale exact Product-dependent analyses | stale | stale | stale | stale only where resulting creative text changes/invalidates | downstream | downstream | downstream | downstream | downstream |
| Asset bytes change | new physical context | stale exact asset | stale dependent | stale dependent | stale if evidence dependency changes | keep if text remains valid | keep | keep | stale dependent | stale dependent | stale |
| Asset role/availability change | old manifest historical; create new current context | analysis may remain reusable by exact input hash | context-dependent stale | candidate eligibility stale | evidence-dependent stale | keep if creative unchanged | keep | keep | stale dependent | stale | stale |
| Creative hook/script/CTA edit | keep | keep | keep | stale | stale | stale | stale | stale | stale | stale | stale |
| Voice settings change | keep | keep | keep | keep | keep | stale | stale | stale | stale | stale | stale |
| Alignment provider/profile change | keep | keep | keep | keep | keep | keep | stale | stale | stale | stale | stale |
| Scene override | keep | keep | keep | keep | keep | keep | keep | keep | stale | stale | stale |
| Render settings change | keep | keep | keep | keep | keep | keep | keep | keep | keep | stale | stale |
| QA decision only | keep | keep | keep | keep | keep | keep | keep | keep | keep | keep | QA state only |

## Async rule

Async staleness revalidation uses the target operation's exact input/dependency hash, not aggregate `packRevision` alone. Revalidate immediately before paid dispatch/start and again before applying completion.
