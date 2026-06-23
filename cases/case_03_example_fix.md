# Case 03: Example Code Fix

## 1. Issue Link

https://github.com/Muggler2k/code-cartographer-mcp/issues/71

## 2. Repository

Muggler2k/code-cartographer-mcp

## 3. Issue Summary

This Issue asks for AI-friendly demo or capability documentation for the repository.

The requested documentation appears to focus on helping AI coding agents understand what Code Cartographer MCP can do, how its tools can be used, and how an agent should reason about tool outputs.

## 4. Why This Issue Was Selected

This Issue was selected because:

1. It is related to AI coding agent workflows.
2. It focuses on documentation rather than source code changes.
3. It is useful for testing whether Codex can understand a repository's capabilities.
4. It may require summarizing existing tool behavior without inventing unsupported claims.
5. It can be used to evaluate whether AI-generated documentation stays accurate, scoped, and grounded in existing repository docs.

## 5. Codex Prompt

The following prompt was sent to Codex:

```text
You are helping me analyze a real GitHub Issue for an open-source contribution preflight review.

Target Issue:
https://github.com/Muggler2k/code-cartographer-mcp/issues/71

Target Repository:
Muggler2k/code-cartographer-mcp

Goal:
Do not make changes yet. First analyze whether this Issue is suitable for a beginner-friendly documentation or example contribution.

Tasks:
1. Explain the Issue in simple terms.
2. Identify what kind of documentation, demo, example, or agent-readable file should be added or modified.
3. Check whether this task requires source code changes.
4. Identify possible risks.
5. Propose the smallest safe documentation or example change.
6. Give manual validation steps.
7. Do not create a pull request yet.
8. Do not apply changes yet.

Important constraints:
1. Do not modify source code.
2. Do not modify package files.
3. Do not modify tests.
4. Do not invent unsupported capabilities.
5. Ground the recommendation in existing repository docs.
6. Preserve the repository's codebase-only contract if relevant.

Output format:
- Issue summary
- Repository context
- Suggested file to add or modify
- Minimal change plan
- Risk analysis
- Validation steps
- Recommendation
```

## 6. Codex Output Summary

Codex analyzed Issue #71 as an agent-readable capabilities documentation task.

The Issue asks for a compact guide that helps an LLM agent understand:

1. Which Code Cartographer MCP tool to use for a given goal.
2. What arguments each tool needs.
3. When to prefer `llm_readable` or `dual` output.
4. How to chain tools during a task.
5. How to preserve the repository's codebase-only contract.

Codex identified that the existing repository docs already contain the source material:

1. `README.md`
2. `docs/tools-reference.md`
3. `docs/mcp-client-config.md`
4. `docs/architecture.md`

Codex suggested the safest documentation target as:

`docs/agent-capabilities.md`

This file would summarize tool capabilities in an agent-readable shape without changing source code.

## 7. Files Changed

No files were changed in this analysis step.

Suggested future target file:

`docs/agent-capabilities.md`

Files that should not be changed for this Issue in the first safe attempt:

`src/`

`package.json`

`package-lock.json`

`tests/`

Existing implementation files.

## 8. Diff Risk Analysis

The expected patch risk is moderate.

Main risks:

1. Accuracy risk: the future document must cover all 20 tools without omitting or misrepresenting any tool.
2. Argument risk: tool inputs and outputs must match `docs/tools-reference.md`.
3. Contract risk: wording must not imply runtime proof, dynamic tracing, debugger behavior, telemetry inspection, or test execution.
4. Drift risk: duplicating tool details creates another place that may become outdated when tools change.
5. Scope risk: acceptance criteria require all 20 tools plus at least 3 chaining recipes, so the patch may become larger than a beginner-friendly documentation fix.
6. Unsupported-claim risk: the document must not invent capabilities that are not already documented.

## 9. Validation Steps

Manual validation steps for a future patch:

1. Confirm only one documentation file is added or changed.
2. Cross-check the new file against `docs/tools-reference.md`.
3. Confirm all 20 tools are covered.
4. Confirm a `goal -> tool` table exists.
5. Confirm at least 3 chaining recipes exist.
6. Confirm `llm_readable` or `dual` output is mentioned for agent consumption.
7. Confirm the confidence vocabulary remains exactly: `confirmed`, `likely`, `candidate`, `unclear`, `unresolved`.
8. Search for forbidden implication words such as `proves runtime`, `executes tests`, `runs the app`, `debugger`, or `telemetry`, unless used to explicitly deny those capabilities.
9. Confirm the document preserves the codebase-only contract.

## 10. Human Review Decision

The Codex analysis, patch generation, and diff review are acceptable.

Case 03 is suitable for a documentation-only contribution, but it is more complex than Case 01 and Case 02 because it requires summarizing all documented tools.

The generated patch is acceptable because:

1. It adds only one documentation file: `docs/agent-capabilities.md`.
2. It does not modify source code.
3. It does not modify `src/`.
4. It does not modify package files.
5. It does not modify tests.
6. It does not modify existing documentation files.
7. It includes a `goal -> tool` table.
8. It covers all 20 tools.
9. It includes multiple chaining recipes.
10. It preserves the repository's codebase-only contract.
11. It keeps the confidence vocabulary exactly as: `confirmed`, `likely`, `candidate`, `unclear`, `unresolved`.

The patch is acceptable for future pull request preparation.

No pull request should be created until the case file, prompt log, result log, and patch file are all complete.

## 11. Final Outcome

Issue understanding completed.

A documentation-only patch was generated and saved as:

`patches/case_03.patch`

The patch targets the documentation directory of the target repository and adds a new file:

`docs/agent-capabilities.md`

The proposed file gives an agent-readable capabilities reference for Code Cartographer MCP.

It includes:

1. A codebase-only contract warning.
2. Output mode guidance for AI agents.
3. The exact confidence vocabulary.
4. A `goal -> tool` table.
5. A compact tool reference table covering 20 tools.
6. Chaining recipes.
7. References to existing documentation.

The patch passed Codex diff review.

No source code, package files, tests, or existing documentation files were modified.

No pull request was created yet.

## 12. Failure or Learning Notes

Case 03 shows that a documentation-only Issue can still be complex.

The main risk is not source code failure, but documentation drift and inaccurate tool summarization.

The most important learning from this case is that AI coding agents can generate useful agent-readable documentation, but human review is needed to check:

1. Whether every tool is covered.
2. Whether tool names match the official tool reference.
3. Whether required arguments are accurate.
4. Whether output modes are described correctly.
5. Whether chaining recipes are reasonable.
6. Whether the generated document preserves the codebase-only contract.
7. Whether confidence vocabulary is copied exactly.
8. Whether the patch stays compact enough for a safe open-source contribution.

This case is useful because it tests Codex on a real agent-capability documentation task with higher scope and higher drift risk than a simple README edit.

