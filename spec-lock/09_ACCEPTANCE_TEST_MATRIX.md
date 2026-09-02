# External Acceptance Test Matrix — FROZEN RC1

The acceptance suite is an **independent judge**. The autonomous builder must not have write permission to it.

Preferred mechanism: separate private repository/package consumed read-only by implementation CI. Acceptable fallback: same repo only with CODEOWNERS + required human review + branch protection. Prose-only protection is insufficient.

## Product authority / concurrency
- Same-name Products remain isolated.
- Client cannot create USER_VERIFIED.
- Client actor spoof ignored/rejected.
- Pricing/review/fulfillment `isVerified=true` cannot create authority.
- Removed verified claim does not resurrect.
- Two concurrent Product mutations from the same base revision: exactly one wins; no duplicate revisionNumber; loser gets `PRODUCT_REVISION_CONFLICT`.
- VerifyFact and fact edit racing from same base cannot silently lose either write.

## Hash / staleness
- Verification-only change preserves `productValuesHash`.
- Verification changes `factAuthorityHash` as expected.
- Claim verification can re-trigger grounding without reprocessing physical assets/AssetAnalysis.
- Product semantic change invalidates Product-dependent AssetAnalysis even when asset bytes are unchanged.
- Missing hash/context fails closed.
- Sibling Creative edit does not stale an unrelated in-flight operation whose target-specific input hash is unchanged.

## Assets / RawAssetManifest
- Storage write failure cannot create READY.
- Zero-byte/truncated/fake media blocked.
- MIME spoof blocked.
- Corrupt MP4 blocked by probe.
- SHA comes from real bytes.
- Manifest freeze rejects non-READY asset with `ASSET_NOT_READY`.
- `REFERENCE_ONLY` / `DO_NOT_USE` cannot become production footage.
- RawAssetManifest hash does not change merely because analysis/provider output changes.

## Multimodal intelligence / AnalysisContext
- Provider receives real media/ref.
- Wrong/missing required asset/product/SHA identity rejected according to provider schema.
- Invalid score/enum/timestamp rejected.
- AssetAnalysis cache requires exact `assetAnalysisInputHash`.
- Product value change breaks cache identity.
- Frozen AnalysisContext cannot drift to arbitrary/latest analysis.
- Downstream Phase 3/4 requires exact AnalysisContext ID/hash and exact analysis IDs.
- Missing Product facts remain UNKNOWN.
- Structured visual evidence is actually persisted and available downstream.
- BEFORE_AFTER evidence references exact analysis/segment.

## Creative
- Fewer than six eligible distinct creatives => `INSUFFICIENT_ELIGIBLE_CONCEPTS`; no production pack activated.
- BEFORE_AFTER requires exact grounded claim + exact visual evidence.
- SOCIAL_PROOF requires verified review evidence.
- URGENCY requires verified offer/pricing/scarcity evidence.
- Every factual assertion in hook/script/CTA/spoken lines/subtitles is extracted and grounded.
- AI classification cannot self-authorize.
- Semantic wrong-Product text blocks approval.
- Six replacement is atomic.
- `scriptHash` is exactly canonical hook+script+CTA everywhere.

## TTS / Arabic alignment
- Missing provider cannot fall back to synthetic production audio.
- Missing intended audio returns `SOURCE_UNAVAILABLE`, never default WAV.
- `audioHash` is direct byte SHA-256.
- 50-word script + 2 aligned words => `ALIGNMENT_INCOMPLETE`.
- Alignment timestamps derive from real ASR, not proportional spacing.
- Arabic script with tashkeel / Alef variants / numeric forms can match provider transcript through the versioned alignment-normalization profile without changing `scriptHash`.
- Actual mismatched words still fail; tolerant normalization must not create false completion.
- Stale completion cannot overwrite edited target script.

## Async / paid provider
- Revalidate target-specific input immediately before provider dispatch; stale queued job spends zero paid call.
- Concurrent identical Veo requests execute exactly one paid provider call via DB uniqueness claim.
- Worker restart reconciles in-flight provider operation without duplicate spend.
- Stale provider completion is retained historically but not applied as current.

## Render / QA
- Render row cannot complete without physical MP4.
- FFmpeg failure => RenderJob failed.
- Wrong dimensions/streams/duration block completion.
- Container/stream duration tolerance is explicitly bounded by render contract, not exact-millisecond equality.
- QA default `NOT_REVIEWED`.
- Canonical QA never uses `PASSED`.
- QA `APPROVED` is bound to exact `renderOutputHash`.
- Download/export only exact approved output.

## Security / workspace
- Cross-workspace reads/writes blocked.
- Client cannot choose unsafe physical storage path.
- Local storage adapter rejects traversal and verifies resolved path remains inside configured root.
- Upload size/type/byte validation enforced.
- Secrets never returned to client.

## CI / harness integrity
- Acceptance suite itself runs against isolated ephemeral DB/storage.
- Implementation builder cannot modify acceptance source.
- CI records/validates acceptance-suite revision or checksum.
- A changed acceptance-suite revision without approved operator action blocks the build.
