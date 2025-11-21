# TechSpark KYC & AML Platform - Functional Requirements

The IDs below feed into the RTM and test assets. They are grouped around the primary capability pillars requested in the brief.

## Chatbot Functionality
- **REQ-CHAT-01** - Provide a guided onboarding chatbot that can capture full KYC data and route to manual review when risk > configured threshold.
- **REQ-CHAT-02** - Persist multi-turn conversation context for 30 minutes of inactivity to avoid re-entering KYC data.
- **REQ-CHAT-03** - Offer proactive compliance tips (e.g., document formats) based on customer locale and product type.
- **REQ-CHAT-04** - Support human handoff via secure agent console with full transcript sharing in <3 seconds.

## NLP Capabilities
- **REQ-NLP-01** - Extract named entities (names, addresses, IDs, employers) from uploaded documents with >=92% precision.
- **REQ-NLP-02** - Detect sentiment and urgency cues to prioritize potential AML escalations automatically.
- **REQ-NLP-03** - Normalize unstructured occupation descriptions to a regulated taxonomy with confidence scores.
- **REQ-NLP-04** - Redact PCI/PII tokens when storing chat history while retaining compliance audit trails.

## Integration with Existing Systems
- **REQ-INT-01** - Integrate with core banking KYC API for customer master lookup/read/write.
- **REQ-INT-02** - Push suspicious activity alerts (SAR) to the AML case management tool via REST webhook.
- **REQ-INT-03** - Consume sanctions/PEP watchlist updates every 4 hours and version them for traceability.
- **REQ-INT-04** - Support single sign-on with the enterprise IdP using OAuth2 + PKCE for analyst tools.

## Scalability Needs
- **REQ-SCALE-01** - Handle 5k concurrent chatbot sessions with <2% error rate during onboarding surges.
- **REQ-SCALE-02** - Scale NLP inference layer horizontally to process 1M documents/day.
- **REQ-SCALE-03** - Provide automatic back-pressure signals to upstream channels when latency >700 ms.
- **REQ-SCALE-04** - Offer regional data residency deployment options (US-EAST, EU-WEST, AP-SG).

## Performance Expectations
- **REQ-PERF-01** - Chatbot first response time <1.2 s at p95, measured end-to-end.
- **REQ-PERF-02** - Document ingestion to risk score SLA of <45 seconds at p90.
- **REQ-PERF-03** - System availability >=99.5% monthly with zero data loss RPO.
- **REQ-PERF-04** - Generate compliance audit exports in <5 minutes for a 30-day window.
