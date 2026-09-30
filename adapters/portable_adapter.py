from core.agent import run_tool

class PortableAdapter:
    """Framework-independent adapter boundary for external runtimes."""
    def invoke(self, tool_name: str, inputs: dict) -> dict:
        return run_tool(tool_name, inputs)
