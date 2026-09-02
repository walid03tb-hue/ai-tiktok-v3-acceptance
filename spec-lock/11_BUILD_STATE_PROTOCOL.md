# V3 Build State and Recovery Protocol — FROZEN RC1

Create `V3_BUILD_STATE.md` from the first coding session.

## Required fields
- CURRENT_PHASE
- LAST_COMPLETED_PHASE
- CURRENT_TASK
- NEXT_EXACT_TASK
- COMPLETED_MIGRATIONS
- CURRENT_SCHEMA_VERSION
- TEST_COUNTS_UNIT
- TEST_COUNTS_INTEGRATION
- TEST_COUNTS_HTTP_E2E
- TEST_COUNTS_ACCEPTANCE
- ACCEPTANCE_SUITE_REVISION_OR_CHECKSUM
- LAST_GREEN_COMMIT
- FILES_CHANGED_THIS_PHASE
- OPEN_BLOCKERS
- FROZEN_DECISIONS
- PROVIDER_CONFIG_STATUS
- REQUIRED_MANUAL_ACTIONS

## Update rule
After every meaningful milestone:
1. run required tests
2. fix implementation failures
3. verify external acceptance suite revision/checksum did not change unexpectedly
4. update build state
5. commit
6. continue automatically

## Stop conditions
Stop only for:
- quota/tool exhaustion
- missing credentials when no safe offline work remains
- contradiction in frozen normative spec
- external acceptance test that appears wrong (report; never edit it)
- real blocker not safely resolvable from frozen contracts

Do not stop just to report phase completion.

## Recovery prompt
```
Continue V3 from repository state and V3_BUILD_STATE.md.
Read 01_V3_MASTER_CONSTITUTION_FROZEN.txt and frozen supporting contracts first.
Resume exactly from NEXT_EXACT_TASK.
Do not redo green phases.
Do not redesign frozen architecture.
Do not edit the protected external acceptance suite.
Verify acceptance-suite revision/checksum, run required tests, update build state, commit, and continue until completion, a true blocker, or quota exhaustion.
```
