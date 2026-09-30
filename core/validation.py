from typing import Any

def validate_object(data: Any, required: dict[str, type]) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["input must be an object"]
    for key, expected in required.items():
        if key not in data:
            errors.append(f"missing required field: {key}")
        elif not isinstance(data[key], expected):
            errors.append(f"field '{key}' must be {expected.__name__}")
    return errors
