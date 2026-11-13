"""Assignment 7: lightweight cross-context invariant checks (not clinical validation)."""
import json
from pathlib import Path
base = Path(__file__).resolve().parents[1]
names = ["primary", "contrast_1", "contrast_2"]
d = [json.loads((base / "responses" / (n + "_response.json")).read_text()) for n in names]
assert len({x["general_et_finding"] for x in d}) == 1, "General ET evidence unexpectedly changed"
assert len({x["application_finding"] for x in d}) == 1, "Application evidence unexpectedly changed"
assert len({x["organization_specific_finding"] for x in d}) == 3, "No organizational differentiation"
assert "PLANNING ONLY" in d[0]["organization_specific_finding"]
assert "DEFER" in d[1]["organization_specific_finding"]
assert "BLOCK" in d[2]["organization_specific_finding"]
for x in d:
    assert len(x["abstention_or_more_information_needed"]) >= 1
    for term in ["leadership/sponsorship", "skills/training", "workflow/process", "infrastructure/data", "resources/budget", "governance/risk", "culture/change", "operating ownership"]:
        assert term in x["organization_specific_finding"], term
print("PASS: application/general evidence stable, organization conclusions differentiated, missing evidence and 8 dimensions.")
