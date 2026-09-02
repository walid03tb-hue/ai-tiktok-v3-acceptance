# V3 Canonical Domain Model — FROZEN RC1

Responsibilities below are normative. Exact columns may expand, but objects must not be merged in a way that collapses authority or provenance boundaries.

## Workspace / identity

### Workspace
Tenant/security boundary.

### Actor
Authenticated user/service identity used for audit and verification.

### Product
Mutable top-level pointer with immutable server-generated ID and CAS-protected `currentRevisionId`.

### ProductRevision
Immutable revision with `productValuesHash`, `factAuthorityHash`, `claimSetHash`, `revisionSnapshotHash`; `(workspaceId, productId, revisionNumber)` unique.

### ProductFactsSnapshot
Immutable exact facts/provenance/claim snapshot carrying the four Product hash domains.

### VerificationRecord
Immutable server-authoritative record binding exact canonical value/claim identity to actor and time.

## Assets

### Asset
Server-owned Product relationship + lifecycle/status/role history.

### AssetBlob / StorageObject
Physical bytes identity: storage key, SHA-256, byte size, detected MIME, decode/probe metadata.

### RawAssetManifest
Immutable physical-only frozen context. Includes only READY assets and physical/frozen role/availability truth. Does not authenticate AI analysis.

### AssetAnalysis
Immutable multimodal result bound to exact asset SHA + `productValuesHash` + provider/model/prompt/analyzer/schema identity through `assetAnalysisInputHash`.

### AnalysisContext
Immutable exact set of AssetAnalysis IDs/identities used downstream; bound to `rawAssetManifestHash + productValuesHash`.

## Product / marketing intelligence

### ProductIntelligence
Structured AI proposals bound to exact Product semantic context + AnalysisContext. Never authority by itself.

### IntelligenceSuggestion
Field-level proposal with confidence, provenance, evidence references, risk and review status.

## Creative

### CreativeCandidatePool
Non-production candidate set; may contain any count.

### CreativePack
Server-authoritative production aggregate containing **exactly six** distinct eligible creatives; optimistic concurrency protected.

### Creative
Versioned concept output: hook, script, CTA, archetype, exact hash/context/evidence bindings.

### ClaimAssertion
Extracted factual/commercial assertion from actual final production text.

### ClaimGroundingResult
Deterministic authorization result bound to `factAuthorityHash + claimSetHash + creativeTextHash + scriptHash`.

### SemanticConsistencyResult
Product semantic-match result bound to `productValuesHash + creativeTextHash`.

## Voice / timing

### VoiceArtifact
Exact real TTS output with provider/model/settings identity + `audioHash` + probe metadata.

### AlignmentArtifact
Real ASR/alignment bound to `audioHash + scriptHash + provider/model + alignmentNormalizationProfileVersion`.

### MasterTimeline
Deterministic timing model built only from valid VoiceArtifact + AlignmentArtifact.

## Scenes / media generation

### ScenePlan
Visual scene blueprint bound to exact Creative + Timeline + AnalysisContext + assets/segments.

### AIVisualOperation
Durable paid operation with DB-first dedupe claim, provider operation ID, target-specific input hash, restart reconciliation and output validation.

## Render / QA / export

### RenderJob
Durable render operation bound to exact `renderInputHash`.

### RenderArtifact
Physical validated MP4 + `renderOutputHash` + ffprobe metadata.

### QAReview
Exact-output-bound QA state. Canonical states: `NOT_REVIEWED`, `RUNNING`, `APPROVED`, `NEEDS_RERENDER`, `REJECTED`.

### CreativePackExport
Immutable export manifest/ZIP containing only exact approved outputs and hashes.
