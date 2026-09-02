# Google Cloud Target Architecture

## Services

### Cloud Run — API
Stateless HTTP API. Resolves canonical context and queues durable operations.

### Cloud Run — Worker
Executes queued TTS/alignment/Veo/render jobs. Separate scaling and timeout behavior from API.

### Cloud SQL — PostgreSQL
Canonical relational state, immutable revisions, jobs, manifests, analyses, creative lineage, render/QA records.

### Cloud Storage
Original uploads, normalized media, TTS audio, AI visuals, render outputs, exports.

### Cloud Tasks
Durable dispatch/retry for async work. Job state remains in PostgreSQL; Cloud Tasks is transport, not source of truth.

### Secret Manager
Provider/API credentials. Never frontend env variables and never committed secrets.

### Vertex AI / Gemini / Veo
Production provider adapters configured via environment/config registry.

### Logging / Monitoring
Structured logs with job/product/workspace IDs, error classification, provider latency, cost-related counters and alerts.

## Environments

- `test`: isolated DB/storage, mocks only.
- `demo`: explicit demo/mock provider metadata.
- `production`: real providers only, fail closed.

Recommended pre-production cloud setup:

- `v3-dev` project for integration testing.
- `v3-prod` created later after acceptance gates are green.

## Do not introduce early

Avoid Kubernetes, Kafka, Redis, or unnecessary microservice decomposition until a measured requirement appears.
