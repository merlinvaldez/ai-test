# Test Strategy, Scenarios, and Cases

## Scope
Generative AI prompts were used to expand stakeholder notes into concrete, testable scenarios across chatbot orchestration, NLP pipelines, and downstream compliance integrations. The resulting plan aligns with the requirement IDs in `docs/requirements.md`.

## Test Matrix

| Test ID | Scenario | Requirement(s) | Key Steps | Synthetic Data | Expected Outcome |
| --- | --- | --- | --- | --- | --- |
| TC-CHAT-CTX | Persist 30 min chat context | REQ-CHAT-02, REQ-INT-01 | Simulate multi-turn onboarding, pause 25 min, resume | `synthetic_kyc.json` record CUST-001 | Chat resumes without data loss; session token reused |
| TC-CHAT-HANDOFF | Human handoff speed | REQ-CHAT-04, REQ-INT-04 | Trigger risk alert >0.7, request agent | CUST-004 high risk | Agent console receives transcript in <3s |
| TC-NLP-ENT | Document entity extraction accuracy | REQ-NLP-01, REQ-NLP-03 | Upload documents and compare parsed entities to ground truth | CUST-002 license, CUST-005 trade license | >=92% precision, taxonomy label + confidence exposed |
| TC-NLP-REDACT | PII redaction prior to storage | REQ-NLP-04 | Persist chat transcript and inspect stored version | All chat channels | Tokens matching regex for SSN/National IDs replaced with hash |
| TC-AML-WATCH | Watchlist ingestion to SAR webhook | REQ-INT-02, REQ-INT-03 | Inject new sanction entry and execute AML case sync | AML-1002 | SAR webhook gets enriched payload with versioned list |
| TC-SCALE-SESS | Concurrent sessions throughput | REQ-SCALE-01, REQ-PERF-01 | Run 5k virtual users via load generator | Mixed customer cohort | Error rate <2%, p95 latency <1.2s |
| TC-SCALE-NLP | NLP doc throughput | REQ-SCALE-02, REQ-PERF-02 | Send 1M docs/day load profile | Document set of 10MB | Processing completes <45s p90 per doc |
| TC-AML-GEO | High-risk geo routing | REQ-PERF-02, REQ-INT-02 | Submit transfer to embargoed jurisdiction | AML-1004 | Case auto-escalates to SAR drafting queue |

## Execution Notes
- Each case is tagged with a requirement ID to streamline traceability and automated reporting.
- Synthetic datasets (`data/synthetic_kyc.json`, `data/synthetic_aml.json`) drive deterministic assertions in automated tests and can be extended for load profiles.
- pytest is configured (see `tests/`) for lightweight data integrity checks; performance scenarios rely on external load tooling but share the same IDs for unified reporting.
