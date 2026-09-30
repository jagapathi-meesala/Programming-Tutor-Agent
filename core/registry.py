from contracts.tool_contract import ToolContract

class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolContract] = {}

    def register(self, contract: ToolContract) -> None:
        if contract.name in self._tools:
            raise ValueError(f"tool already registered: {contract.name}")
        self._tools[contract.name] = contract

    def discover(self) -> list[str]:
        return sorted(self._tools)

    def execute(self, name: str, data: dict) -> dict:
        contract = self._tools.get(name)
        if contract is None:
            return {"ok": False, "tool": name, "error": {"code": "UNKNOWN_TOOL", "message": "tool is not registered"}}
        try:
            result = contract.execute(data)
            return {"ok": True, "tool": name, "result": result}
        except (ValueError, TypeError) as exc:
            return {"ok": False, "tool": name, "error": {"code": "INVALID_INPUT", "message": str(exc)}}
        except Exception:
            return {"ok": False, "tool": name, "error": {"code": "TOOL_FAILURE", "message": "tool execution failed"}}
