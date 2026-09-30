from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class ToolContract:
    name: str
    purpose: str
    input_schema: dict[str, Any]
    execute: Callable[[dict[str, Any]], dict[str, Any]]
