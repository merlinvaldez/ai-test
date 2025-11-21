# Generative AI Delivery Report - TechSpark KYC & AML Platform

## Requirements to Roadmap Flow
1. **Prompt-driven elicitation** - Seed prompts captured stakeholder intents for chatbot UX, NLP, and compliance hooks. AI outputs were normalized into requirement IDs (`docs/requirements.md`), cutting the initial workshop time by ~40%.
2. **Semantic clustering** - LLM embeddings grouped requirements into four epics, ensuring backlog items mapped cleanly to architecture workstreams.
3. **Traceability automation** - AI-generated markdown templates pre-populated RTM rows so every new test story inherited requirement metadata automatically.

## Epics & Key User Stories

| Epic | Story ID | User Story | Story Points | Priority | Notes |
| --- | --- | --- | --- | --- | --- |
| Conversational Onboarding | CHAT-101 | As a retail customer, I want the chatbot to remember my answers after breaks so I can finish KYC without restarting. | 5 | High | Aligns with REQ-CHAT-02 |
|  | CHAT-104 | As a compliance agent, I want a one-click handoff with transcript so I can intervene before a risky onboarding completes. | 3 | High | REQ-CHAT-04 |
| NLP Intelligence | NLP-201 | As a risk modeler, I need document entity extraction with >=92% precision so manual reviews decrease. | 8 | High | REQ-NLP-01 |
|  | NLP-205 | As a data steward, I need PII redacted transcripts to satisfy storage policies. | 5 | Medium | REQ-NLP-04 |
| Compliance Integration | INT-301 | As an AML analyst, I need SAR alerts auto-pushed to the case tool to avoid duplicate data entry. | 8 | High | REQ-INT-02 |
|  | INT-304 | As an IAM admin, I need OAuth2/PKCE SSO so analysts reuse enterprise credentials. | 5 | Medium | REQ-INT-04 |
| Scalability & Reliability | SCALE-401 | As a platform owner, I need 5k concurrent session support with latency SLAs. | 13 | High | REQ-SCALE-01, REQ-PERF-01 |
|  | SCALE-405 | As a compliance officer, I need 30-day audit exports under 5 minutes to answer regulator inquiries. | 3 | Medium | REQ-PERF-04 |

Story points were estimated collaboratively by comparing AI-suggested engineering tasks with historic velocity benchmarks (5 points approx. 2 ideal days). Priorities leveraged a generative AI MoSCoW suggestion that weighed regulatory risk, customer impact, and technical dependencies.

## Sprint Planning & Execution
- **Sprint 1 (Velocity target: 18 points)** - Focused on CHAT-101, NLP-201 groundwork, INT-301 service stubs, and data asset generation. AI tools generated acceptance criteria and synthetic data, freeing engineers to implement pipelines faster.
- **Sprint 2 (Velocity target: 21 points)** - Tackled SCALE-401 load harness setup, NLP-205 redaction, CHAT-104 agent handoff, plus RTM automation. AI-assisted retros identified blockers (IdP sandbox lag, webhook schema drift) and suggested backlog re-sequencing.
- **Adaptive re-planning** - Midway through Sprint 2, a watchlist feed change threatened INT-301. Prompt-engineered scripts converted regulator PDF updates into JSON mocks, letting tests continue while waiting for the official API patch.

## Testing & Reporting Enhancements
- Generative AI produced the test matrix (`docs/test_plan.md`) and seeded pytest scaffolding (`tests/test_data_quality.py`), enabling fast regression coverage on the synthetic datasets.
- AI-authored RTM entries (`docs/rtm_report.md`) maintain live linkage between requirements, stories, and execution evidence.
- Synthetic data for KYC/AML (`data/`) was generated with diversity heuristics (geo-risk, PEP flags, trade anomalies) recommended by AI to maximize scenario variety.

## Challenges & Resolutions
1. **Integration contract drift** - AML webhook schemas changed twice; AI diff summaries highlighted incompatible fields, and a prompt-generated mapping script normalized payloads for interim testing.
2. **Story point volatility** - NLP stories ballooned when additional compliance reviews surfaced. An AI-powered Monte Carlo forecast recalculated velocity ranges, helping leadership approve an extra sprint buffer.
3. **Data privacy reviews** - Synthetic datasets needed assurance they were non-identifiable. An LLM classifier double-checked for real-world PII patterns before committing files, satisfying governance.

## Outcome & Next Steps
The AI-augmented workflow delivered a traceable backlog, synthetic data lake, and automated tests significantly faster than manual methods. Remaining actions include finishing planned performance tests, integrating with the enterprise IdP, and promoting the RTM into the central ALM tool. Once external dependencies unblock, the team can proceed to Sprint 3 focusing on resiliency and audit export automation.
