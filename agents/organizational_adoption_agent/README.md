# Assignment 7 — Organizational Adoption Agent

**Scope:** organizational readiness to plan, govern and sustain Stryker Mako-assisted elective primary total knee replacement. Three fictional NHS hospital profiles contrast organizational readiness with *unchanged* clinical/application evidence.

**Primary:** Teaching Hospital A — PREPARE only; hard patient safety gates unknown.
**Contrast 1:** Community Hospital B — DEFER acquisition due to resources, skills and ownership gaps.
**Contrast 2:** Aggressive Hospital C — BLOCK its 30-day patient launch despite sponsor and capital support.

The folder follows the existing frozen MASY1800 common input/output contracts without modifying core files. The eight dimensions are leadership/sponsorship, skills/training, workflow/process, infrastructure/data, resources/budget, governance/risk, culture/change and operating ownership. Source claims belong to external original guidance/trials; fictional hospital details are case assumptions.

Run from repository root:
```sh
python tools/check_frozen_core.py
for case in primary contrast_1 contrast_2; do
  python tools/build_prompt.py --agent agents/organizational_adoption_agent --case agents/organizational_adoption_agent/cases/$case.json
  python tools/validate_response.py agents/organizational_adoption_agent/responses/${case}_response.json
done
python agents/organizational_adoption_agent/records/check_context_tests.py
```

**Limitations:** These JSON outputs are preserved specialist examples for course assessment, not live clinical approvals or real-hospital evaluations. AI outputs are not direct evidence. An actual hospital would need signed local records and original policy/procurement review.

The detailed complete ZIP and PDF reports were prepared separately for course submission. This repository holds the working text/code/test record.

