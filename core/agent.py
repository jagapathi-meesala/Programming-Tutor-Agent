from core.registry import ToolRegistry
from core.tools import TOOLS


def build_registry() -> ToolRegistry:
    registry = ToolRegistry()
    for tool in TOOLS:
        registry.register(tool)
    return registry


def run_tool(name: str, data: dict) -> dict:
    return build_registry().execute(name, data)
