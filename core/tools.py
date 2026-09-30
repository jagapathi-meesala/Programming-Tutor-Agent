import re
from contracts.tool_contract import ToolContract
from core.validation import validate_object


def explain_code(data: dict) -> dict:
    errors = validate_object(data, {"code": str, "language": str})
    if errors: raise ValueError("; ".join(errors))
    code, language = data["code"], data["language"].lower()
    if not code.strip(): raise ValueError("field 'code' must not be empty")
    lines = code.splitlines()
    definitions = [l.strip() for l in lines if re.match(r"^(def|class|function)\b", l.strip())]
    control_flow = [l.strip() for l in lines if re.match(r"^(if|elif|else|for|while|switch|case|try|except|catch)\b", l.strip())]
    imports = [l.strip() for l in lines if re.match(r"^(import|from)\b", l.strip())]
    return {"language": language, "line_count": len(lines), "imports": imports, "definitions": definitions, "control_flow": control_flow, "summary": "Static structural explanation only; execution was not performed."}


def debug_code(data: dict) -> dict:
    errors = validate_object(data, {"code": str, "language": str})
    if errors: raise ValueError("; ".join(errors))
    code, language = data["code"], data["language"].lower()
    if not code.strip(): raise ValueError("field 'code' must not be empty")
    findings = []
    rules = []
    if language == "python":
        rules = [(r"^\s*if\s+[^:]+$", "PY001", "A Python if statement appears to be missing a colon.", "Add ':' to the end of the conditional statement."),
                 (r"^\s*(for|while)\s+[^:]+$", "PY002", "A Python loop statement appears to be missing a colon.", "Add ':' to the end of the loop header.")]
    for lineno, line in enumerate(code.splitlines(), 1):
        for pattern, rule_id, message, suggestion in rules:
            if re.search(pattern, line):
                findings.append({"rule": rule_id, "line": lineno, "evidence": line.strip(), "message": message, "suggestion": suggestion})
    return {"language": language, "findings": findings, "summary": "Static pattern analysis only; findings are not proof of runtime failure."}


def generate_practice(data: dict) -> dict:
    errors = validate_object(data, {"topic": str, "language": str, "difficulty": str})
    if errors: raise ValueError("; ".join(errors))
    topic, language, difficulty = data["topic"].strip(), data["language"].strip(), data["difficulty"].strip().lower()
    if not topic or not language: raise ValueError("topic and language must not be empty")
    if difficulty not in {"beginner", "intermediate", "advanced"}: raise ValueError("difficulty must be beginner, intermediate, or advanced")
    prompts = {
        "beginner": f"Write a {language} program that demonstrates {topic} using a small input and clear output.",
        "intermediate": f"Implement a {language} solution involving {topic}, then explain its time and space complexity.",
        "advanced": f"Design and implement a {language} solution using {topic}, including edge-case analysis and a justification of the chosen approach."
    }
    return {"topic": topic, "language": language, "difficulty": difficulty, "exercises": [prompts[difficulty], f"Create three test cases for the {topic} solution and explain why each case matters."]}

TOOLS = [
    ToolContract("explain-code", "Explain the static structure of supplied source code.", {"code": "string", "language": "string"}, explain_code),
    ToolContract("debug-code", "Detect a small set of deterministic source-code patterns.", {"code": "string", "language": "string"}, debug_code),
    ToolContract("generate-practice", "Generate deterministic programming practice tasks.", {"topic": "string", "language": "string", "difficulty": "string"}, generate_practice),
]
