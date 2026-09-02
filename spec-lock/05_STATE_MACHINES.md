# V3 State Machines — FROZEN RC1

## Asset lifecycle
`RECEIVING -> STORED -> HASHED -> PROBED -> VALIDATED -> READY`
Failure: `FAILED`, `QUARANTINED`, `SOURCE_UNAVAILABLE`.
Only server-derived READY. Only READY assets may enter a new RawAssetManifest.

## Asset analysis
`PENDING -> RUNNING -> VALIDATING -> READY`
Failure: `SOURCE_UNAVAILABLE`, `PROVIDER_NOT_CONFIGURED`, `AI_QUOTA_EXHAUSTED`, `AI_RATE_LIMIT`, `AI_TIMEOUT`, `AI_RESPONSE_INVALID`, `FAILED`, `STALE`.

## Product intelligence
`PENDING -> RUNNING -> READY_FOR_REVIEW -> ACCEPTED/PARTIAL/REJECTED`
AI proposals never become USER_VERIFIED automatically.

## Creative
`DRAFT -> VALIDATING -> ELIGIBLE/INELIGIBLE -> REVIEW_REQUIRED -> APPROVED`
Production CreativePack activation requires exactly six APPROVED/eligible creatives under the exact current context.

## Voice job
`PENDING -> QUEUED -> RUNNING -> VALIDATING -> READY`
Failure: provider/config/quota/timeout/invalid media/stale origin.

## Alignment
`PENDING -> QUEUED -> RUNNING -> VALIDATING -> READY`
No interpolated fallback.

## Master timeline
`PENDING -> BUILDING -> VALIDATING -> READY`
Requires exact READY VoiceArtifact + AlignmentArtifact.

## Scene plan
`DRAFT -> VALIDATING -> READY_FOR_REVIEW -> APPROVED`
Manual overrides cannot bypass source/role/evidence rules.

## Veo / AI visual operation
`PENDING -> CLAIMED -> SUBMITTED -> PROVIDER_RUNNING -> DOWNLOADING -> VALIDATING -> READY`
DB uniqueness/dedupe claim occurs before provider dispatch.

## Render job
`PENDING -> QUEUED -> RUNNING -> VALIDATING -> COMPLETED`
COMPLETED only after physical output + ffprobe + hash validation.

## QA review lifecycle
`NOT_REVIEWED -> RUNNING -> APPROVED`
Rework/failure terminal states: `NEEDS_RERENDER`, `REJECTED`.
Default: `NOT_REVIEWED`.
`PASSED`, `FAILED`, and `REVIEW_REQUIRED` are forbidden as canonical QA status values.
Production export requires explicit `APPROVED` bound to exact `renderOutputHash`.
