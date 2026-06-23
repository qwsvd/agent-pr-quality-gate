# Case 02: Installation or Configuration Issue

## 1. Issue Link

https://github.com/Muggler2k/code-cartographer-mcp/issues/70

## 2. Repository

Muggler2k/code-cartographer-mcp

## 3. Issue Summary

This Issue asks for AI-friendly setup documentation for the repository.

The requested documentation appears to focus on making the repository easier for AI coding agents to understand, including setup information, repository structure, and possibly an agent-readable `llms.txt` or similar documentation file.

## 4. Why This Issue Was Selected

This Issue was selected because:

1. It is documentation-focused.
2. It is related to AI coding agent workflows.
3. It appears suitable for preflight review before making a real open-source contribution.
4. It can test whether Codex can understand repository setup needs without immediately changing code.
5. It matches the project goal: evaluating how AI coding agents handle real GitHub Issues before pull request submission.

## 5. Codex Prompt

The following prompt was sent to Codex:

```text
You are helping me analyze a real GitHub Issue for an open-source contribution preflight review.

Target Issue:
https://github.com/Muggler2k/code-cartographer-mcp/issues/70

Goal:
Do not make changes yet. First analyze whether this Issue is suitable for a beginner-friendly documentation or configuration contribution.

Tasks:
1. Explain the Issue in simple terms.
2. Identify what kind of documentation or configuration file should be added or modified.
3. Check whether this task requires source code changes.
4. Identify possible risks.
5. Propose the smallest safe documentation or configuration change.
6. Give manual validation steps.
7. Do not create a pull request yet.
8. Do not apply changes yet.

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

Codex analyzed Issue #70 as a documentation-focused task for making the repository easier for AI coding agents to set up and understand.

The Issue asks for an AI or agent-readable setup document, likely a root-level `llms.txt`.

In simple terms, the requested file should help an LLM agent understand how to:

1. Install the project.
2. Build the MCP server.
3. Configure an MCP client.
4. Initialize a target codebase.
5. Verify the initialization state.
6. Preserve the repository's codebase-only contract.

Codex identified the safest minimal change as adding only a compact root-level `llms.txt`.

Codex did not recommend modifying source code, package files, tests, or existing documentation in the first step.

## 7. Files Changed

No files were changed in this analysis step.

Suggested future target file:

`llms.txt`

Files that should not be changed for this Issue in the first safe attempt:

`src/`

`package.json`

`package-lock.json`

`tests/`

Existing documentation files, unless the maintainer later asks for a README link.

## 8. Diff Risk Analysis

The expected patch risk is moderate-low if it stays documentation-only.

Main risks:

1. Accuracy risk: the setup document must not incorrectly say that MCP clients should use `src/index.ts`; MCP clients should point to the built `dist/index.js`.
2. Contract risk: the document must preserve the codebase-only contract and avoid implying runtime truth.
3. Drift risk: existing docs may mention different tool counts, so the new document should avoid restating exact tool counts.
4. Scope risk: adding `llms-full.txt` would be too large for the first contribution.
5. Beginner risk: this is documentation-only, but it requires careful synthesis from multiple existing docs.

## 9. Validation Steps

Manual validation steps for a future patch:

1. Confirm only root-level `llms.txt` is added.
2. Cross-check every command against `README.md` and `docs/mcp-client-config.md`.
3. Confirm the MCP client config uses built `dist/index.js`.
4. Confirm the document includes the `init_codebase` and `check_init_state` flow.
5. Confirm it preserves the exact confidence vocabulary: `confirmed`, `likely`, `candidate`, `unclear`, `unresolved`.
6. Confirm wording says static and codebase-only results are not runtime truth.
7. Optional local check: run `npm install`, run `npm run build`, and verify that the documented path can be used in an MCP client config.

## 10. Human Review Decision

The Codex analysis is acceptable.

This Issue is suitable for a documentation-only contribution, but it is more complex than Case 01.

The safest next step is not to generate a large documentation package.

The safest next step is to generate one compact root-level `llms.txt` file that summarizes existing setup and initialization guidance for AI coding agents.

No pull request should be created yet.

## 11. Final Outcome

Issue understanding completed.

Codex recommended a minimal documentation-only contribution.

The proposed future patch target is:

`llms.txt`

No files were modified in this analysis step.

No patch was generated yet.

No pull request was created yet.

## 12. Failure or Learning Notes

Case 02 is more complex than Case 01 because it requires synthesizing multiple existing documentation files.

The main learning is that AI coding agents can identify a reasonable documentation target, but human review is needed to control scope, avoid inaccurate setup instructions, and preserve repository-specific contracts.

This case is useful for evaluating whether Codex can understand setup documentation, MCP client configuration, and repository-specific constraints before generating a patch.
