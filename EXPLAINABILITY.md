# Explainability

## Inputs and Data Sources
The agent accepts learner questions, source-code text, programming language identifiers, error messages, requested difficulty levels, and practice-topic descriptions through its tool contracts. Data sources are limited to the user-supplied inputs and deterministic rules implemented in the repository; no external database or hidden training dataset is consulted by these tools.

## Decision and Reasoning
The agent decides which structured operation to perform from the selected tool contract and then applies deterministic validation and analysis rules implemented in the corresponding tool. For static code analysis, findings are produced from explicit pattern checks and are labeled as static observations rather than claims about actual runtime behavior.

## Limits and Constraints
The agent cannot establish runtime-only behavior such as network failures, dependency compatibility, performance, or environment-specific compiler/interpreter behavior without an execution-capable integration. Its deterministic debugging rules cover only the patterns implemented in this repository, so absence of a finding does not prove that code is correct.

## Agent Purpose
The Programming Tutor Agent provides educational programming assistance through explanation, deterministic debugging guidance, and practice generation.

## Input Mechanisms
Inputs are dictionaries validated against explicit tool contracts. Required fields are rejected when missing, empty, or of the wrong type.

## Decision Mechanisms
Each tool has a narrow purpose and uses explicit validation followed by deterministic processing. The registry selects tools by kebab-case name and never uses a giant conditional dispatch block.

## Execution Limits
The repository performs static processing only. It does not execute arbitrary learner code, invoke shells, install packages, or access network services.

## Output Contract
Every tool returns a dictionary containing `ok`, `tool`, and either a structured `result` or structured `error` information. Tool results are designed to be serializable and portable.

## Complete Execution Lifecycle
An adapter receives an invocation, converts it to the framework-independent contract, validates the request through the registry, invokes the registered tool, and returns a structured result. Failures are caught at the registry boundary and returned without exposing internal tracebacks by default.

## Tool-by-tool Behavior
### Code Explanation
The explanation tool identifies basic structural elements such as imports, definitions, control-flow statements, and comments, then produces an educational explanation without claiming execution.

### Debugging
The debugging tool checks a small set of deterministic source patterns for likely syntax or logic mistakes. Findings include a pattern identifier, evidence, and a suggested direction for correction.

### Practice Generation
The practice tool creates a deterministic set of programming exercises from a topic, language, and difficulty. It does not claim that generated exercises came from an external curriculum.

## Tool Inputs
Each tool has a YAML contract and a Python implementation registered through the dynamic registry.

## Tool Validation
Input validation checks required keys and primitive types before execution. Invalid requests return structured errors rather than raising uncontrolled exceptions.

## Tool Failure Behavior
Unknown tools and invalid inputs are rejected safely. Internal implementation exceptions are converted into a structured failure result.

## Deterministic Rules
Tool behavior is deterministic for identical inputs and repository state. Debug findings are based on explicit pattern rules rather than an opaque model score.

## Formulas
No statistical or scientific formula is used by this implementation.

## Worked Examples
A learner can submit a Python function containing an unused variable or a suspicious equality/assignment pattern to the debugging tool and receive a static finding with evidence. A learner can also request beginner Python practice on loops and receive a fixed, reproducible exercise set.

## Explainability of Calculated Results
The tools do not calculate model probabilities or confidence scores. Where a rule triggers, the output identifies the exact rule and source evidence used for the finding.

## Provenance
Implementation provenance is the repository source itself. OpenGAP manifest semantics are based on the published OpenGAP v0.1.0 specification, while all domain behavior in this repository is original deterministic implementation code.
