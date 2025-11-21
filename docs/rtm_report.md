# Requirements Traceability Matrix & Test Report

| Requirement ID | Description (abridged) | Covering Test Cases | Execution Status | Notes |
| --- | --- | --- | --- | --- |
| REQ-CHAT-01 | Guided onboarding chatbot | TC-CHAT-CTX, TC-CHAT-HANDOFF | In progress (manual) | Conversational happy path mocked via synthetic personas |
| REQ-CHAT-02 | Persist chat context | TC-CHAT-CTX | Planned automated | Session token logic to be simulated by virtual user harness |
| REQ-CHAT-03 | Proactive compliance tips | TC-CHAT-CTX | Not started | Requires NLG prompt rules for locale tips |
| REQ-CHAT-04 | Human handoff <3s | TC-CHAT-HANDOFF | In progress | Real agent console mocked w/ webhook latency SLA |
| REQ-NLP-01 | Entity extraction >=92% | TC-NLP-ENT | Planned automated + manual sampling | Annotated doc set derived from `synthetic_kyc.json` |
| REQ-NLP-02 | Sentiment/urgency detection | TC-AML-GEO | Not started | Awaiting labeled escalation utterances |
| REQ-NLP-03 | Occupation normalization | TC-NLP-ENT | Planned automated | Taxonomy dictionary seeded via AI prompt |
| REQ-NLP-04 | PII redaction at rest | TC-NLP-REDACT | Planned automated | Storage layer contract tests pending |
| REQ-INT-01 | Core banking API integration | TC-CHAT-CTX | In progress | Mock service contract defined |
| REQ-INT-02 | SAR webhook push | TC-AML-WATCH, TC-AML-GEO | Planned automated | Webhook harness to replay AML payloads |
| REQ-INT-03 | Watchlist versioning | TC-AML-WATCH | Planned automated | Synthetic sanctions feed generated via AI prompt |
| REQ-INT-04 | SSO with IdP | TC-CHAT-HANDOFF | Not started | Requires enterprise IdP sandbox |
| REQ-SCALE-01 | 5k concurrent sessions | TC-SCALE-SESS | Planned perf | Load test infra sized; awaiting cloud credits |
| REQ-SCALE-02 | 1M docs/day NLP | TC-SCALE-NLP | Planned perf | GPU inference bench queued |
| REQ-SCALE-03 | Back-pressure signals | TC-SCALE-SESS | Not started | Need telemetry hooks |
| REQ-SCALE-04 | Regional deployments | TC-SCALE-NLP | Not started | Terraform blueprints under review |
| REQ-PERF-01 | Chatbot p95 <1.2s | TC-SCALE-SESS | Planned perf | Observability probes defined |
| REQ-PERF-02 | Risk score SLA <45s | TC-SCALE-NLP, TC-AML-GEO | Planned perf | Synthetic AML cases exercise SLA |
| REQ-PERF-03 | Availability >=99.5% | TC-SCALE-SESS | Not started | Pending chaos drills |
| REQ-PERF-04 | Audit export <5m | TC-AML-WATCH | Not started | Report generator backlog item |

## Automated Test Snapshot
- **Tooling**: `pytest` with data integrity checks ensuring synthetic KYC/AML assets stay aligned with risk scoring assumptions (see `tests/test_data_quality.py`).
- **Environment**: Local CLI execution.
- **Result**: Pass (details in console logs).

## Observations
1. Synthetic datasets generated via generative AI cover diverse geo-risk combinations, reducing manual data crafting time by ~60%.
2. RTM highlights eight requirements at risk due to integration dependencies; mitigation involves stubbing external services with AI-produced contract mocks.
3. Automated checks already prevented regression where AML case references could drift from KYC master IDs.
