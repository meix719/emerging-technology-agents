# Emerging Technology Adoption Agent
Version 1.1 | Mei Qiong Xue | Assignment 6

Run from scaffold root:
```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json
python tools/validate_response.py agents/adoption_agent/responses/primary_response.json
```
Paste the generated packet into ChatGPT, save its JSON and validate. Repeat contrast_1 and contrast_2. No API key needed. Files under core/, tools/ and agents/_template/ are unchanged.

The saved responses are interactive ChatGPT analyses, not clinical experiments or a separately deployed autonomous agent. Tests establish schema and reasoning behaviour only. All hospitals are hypothetical. Evidence may need refreshing.
