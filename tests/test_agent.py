from core.agent import build_registry, run_tool

def test_registry_discovery():
    assert build_registry().discover() == ["debug-code", "explain-code", "generate-practice"]

def test_explain():
    result = run_tool("explain-code", {"language":"python", "code":"import math\ndef f(x):\n    return x + 1"})
    assert result["ok"] is True
    assert result["result"]["line_count"] == 3

def test_debug():
    result = run_tool("debug-code", {"language":"python", "code":"if x > 2\n    print(x)"})
    assert result["ok"] is True
    assert result["result"]["findings"][0]["rule"] == "PY001"

def test_practice():
    result = run_tool("generate-practice", {"topic":"loops", "language":"python", "difficulty":"beginner"})
    assert result["ok"] is True
    assert len(result["result"]["exercises"]) == 2

def test_invalid_input():
    result = run_tool("generate-practice", {"topic":"loops", "language":"python", "difficulty":"expert"})
    assert result["ok"] is False

def test_unknown_tool():
    result = run_tool("missing", {})
    assert result["ok"] is False
    assert result["error"]["code"] == "UNKNOWN_TOOL"
