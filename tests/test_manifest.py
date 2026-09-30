from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]
def test_manifest():
    data = yaml.safe_load((ROOT / "agent.yaml").read_text())
    assert data["spec_version"] == "0.1.0"
    assert data["name"] == "programming-tutor-agent"
    assert data["version"] == "0.1.0"
    for skill in data["skills"]:
        assert (ROOT / "skills" / skill / "SKILL.md").exists()
    for tool in data["tools"]:
        assert (ROOT / "tools" / f"{tool}.yaml").exists()
