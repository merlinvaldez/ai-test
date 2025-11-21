import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_json(filename):
    return json.loads((DATA_DIR / filename).read_text(encoding="utf-8"))


def test_kyc_risk_scores_within_bounds():
    records = load_json("synthetic_kyc.json")
    assert records, "KYC dataset must not be empty"
    for rec in records:
        assert 0 <= rec["risk_score"] <= 1, f"Risk score out of bounds for {rec['customer_id']}"


def test_document_confidence_levels():
    records = load_json("synthetic_kyc.json")
    for rec in records:
        for doc in rec["documents"]:
            assert 0 <= doc["confidence"] <= 1, f"Doc confidence invalid for {rec['customer_id']}"


def test_aml_customer_cross_reference():
    kyc_records = load_json("synthetic_kyc.json")
    aml_cases = load_json("synthetic_aml.json")
    kyc_ids = {rec["customer_id"] for rec in kyc_records}
    for case in aml_cases:
        assert case["customer_id"] in kyc_ids, f"AML case {case['case_id']} missing KYC master"


def test_alert_priority_vocab():
    aml_cases = load_json("synthetic_aml.json")
    allowed = {"Critical", "High", "Medium", "Low"}
    for case in aml_cases:
        assert case["alert_priority"] in allowed, f"Unexpected priority in {case['case_id']}"
