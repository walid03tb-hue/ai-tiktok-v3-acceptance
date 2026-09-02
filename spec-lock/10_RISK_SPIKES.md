# V3 Pre-Build Risk Spikes — FROZEN RC1

These are throwaway proofs. They do not become production architecture by accident. Capture results in a dated report before provider contracts are finalized.

## Spike 1 — Real multimodal evidence
Input: real Product image + real Product video bytes.
Prove: validated media -> provider -> strict structured AssetAnalysis -> exact observations/evidence/segments -> schema validation -> persisted exact identities.
Pass only if wrong/missing identity and malformed timing fail closed.

## Spike 2 — Saudi Arabic TTS + real alignment
Input: representative 70–90 word Saudi Arabic scripts, including:
- tashkeel/no tashkeel
- Alef variants
- Arabic + English terms
- Western/Arabic-Indic digits
- prices/percentages
- punctuation and short CTA phrases

Prove: real TTS -> physical audio hash/probe -> real ASR/alignment timestamps -> versioned tolerant matcher.
Measure transcript coverage, ordered correspondence, false-positive/false-negative cases, first/last timing, and number equivalence.

Critical design rule: **do not change canonical `scriptHash` to make ASR matching easier.** Tune a separate `alignmentNormalizationProfileVersion` and freeze thresholds only after measured results.

## Spike 3 — MasterTimeline -> FFmpeg
Input: real audio/alignment + 3–4 real clips + captions.
Prove: one canonical timeline drives preview/render -> 1080x1920, 30fps, H.264/yuv420p + AAC -> ffprobe/hash validation.
Measure realistic container/stream duration jitter and freeze a bounded validation tolerance.

## Spike 4 — Async crash/restart/dedupe
Prove both:
1. queued job becomes stale before start -> pre-start revalidation prevents paid provider call;
2. provider operation starts -> worker dies -> restart reuses exact operation, no duplicate call;
3. sibling Creative changes -> unrelated target job remains valid;
4. target dependency changes -> old completion becomes STALE and cannot overwrite current.

## Spike 5 — Veo viability/product fidelity
Test 9:16 hook/lifestyle/reaction/context shots and any product-referenced generation. Record fidelity failures (logo/color/shape/function). Freeze policy for which scene classes may use AI visuals versus mandatory real Product footage.

## Exit rule
No spike is "PASS" because a demo looked good once. Record inputs, provider/model/settings, reproducible output evidence, observed failure modes, and the architecture decision derived from the experiment.
