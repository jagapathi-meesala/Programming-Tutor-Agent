from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def test_explainability_headings():
    text = (ROOT / "EXPLAINABILITY.md").read_text()
    assert text.count("## Inputs and Data Sources") == 1
    assert text.count("## Decision and Reasoning") == 1
    assert text.count("## Limits and Constraints") == 1
    assert "## Inputs\n" not in text
    assert "## Decision\n" not in text
    assert "## Limits\n" not in text

def test_tools_and_skills_exist():
    for name in ["explain-code", "debug-code", "generate-practice"]:
        assert (ROOT / "tools" / f"{name}.yaml").exists()
    for name in ["code-explanation", "debugging", "practice-generation"]:
        assert (ROOT / "skills" / name / "SKILL.md").exists()
