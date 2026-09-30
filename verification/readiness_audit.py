from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
required = ["agent.yaml","SOUL.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md","README.md",".env.example","requirements.txt","pytest.ini"]
for name in required:
    assert (ROOT / name).exists(), name
text = (ROOT / "EXPLAINABILITY.md").read_text()
for heading in ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]:
    assert heading in text, heading
for bad in ["## Inputs\n","## Decision\n","## Limits\n"]:
    assert bad not in text, bad
manifest = (ROOT / "agent.yaml").read_text()
assert 'spec_version: "0.1.0"' in manifest
assert re.search(r"name: programming-tutor-agent", manifest)
print("Local structural audit: PASS")
