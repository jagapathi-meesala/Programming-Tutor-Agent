# Programming Tutor Agent

A framework-independent OpenGAP agent focused on programming education. It provides deterministic static code explanation, a small set of static debugging checks, and deterministic practice generation.

## OpenGAP

The manifest targets OpenGAP/gitagent specification v0.1.0. The repository intentionally avoids runtime framework dependencies.

## Tools

- `explain-code`: structural source explanation.
- `debug-code`: deterministic static checks for selected Python patterns.
- `generate-practice`: deterministic exercises from topic/language/difficulty.

## Validation

Run `pytest -q` for repository tests and `python verification/readiness_audit.py` for structural checks. The OpenGAP CLI must be installed separately to run `opengap validate`; this environment did not have network access for installing or cloning it, so no OpenGAP CLI result is claimed here.

## Portability

`adapters/portable_adapter.py` is the framework-independent boundary. It can be wrapped by OpenAI, CrewAI, Claude Code, or Lyzr integrations without coupling the core implementation to those frameworks. Those external framework integrations are NOT claimed as tested by this repository.
