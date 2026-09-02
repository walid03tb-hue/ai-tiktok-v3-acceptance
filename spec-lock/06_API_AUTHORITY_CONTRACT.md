# API Authority Contract — FROZEN RC1

## Principle
Frontend requests actions; server resolves canonical truth.

## Client may send
- user-entered values
- requested Product ID only as an assertion/context target
- desired asset role-change action
- creative edit text
- requested voice profile/settings
- requested navigation/action
- requested render options
- optimistic-concurrency expected revision/currentRevisionId

## Client may never set canonical authority directly
Forbidden public authority fields include:
- USER_VERIFIED
- verifiedFieldKeys
- verifiedAt / verifiedBy / verification actor
- isVerified as trusted state
- READY
- APPROVED
- PASSED
- completedPhases / activePhase
- canonical render eligibility
- canonical semantic PASS
- canonical claim PASS

## Active Product resolution
1. Resolve server/session authoritative active Product for actor/workspace.
2. If none: `ACTIVE_PRODUCT_REQUIRED`.
3. If client Product assertion differs: `PRODUCT_CONTEXT_MISMATCH`.
4. Use server Product only.

## Verification actions
Only explicit server endpoints/services may create verified authority. Bind exact canonical value/claim identity + Product context + expected revision + actor + timestamp.

## ProductRevision concurrency
New revision insert + Product.currentRevisionId update occur in one DB transaction with CAS.
Conflict: HTTP 409 `PRODUCT_REVISION_CONFLICT`.

## CreativePack concurrency
Expected revision required for mutations. Conflict: HTTP 409 `PACK_VERSION_CONFLICT`.

## Missing canonical context
Never synthesize placeholder IDs (`prod_unassigned`, `asm_default`, etc.). Missing required hash/context fails with a deterministic error.
