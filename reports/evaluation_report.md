# Evaluation Report

This report evaluates the first three AI coding agent preflight cases in this project.

The goal is to assess whether Codex-generated outputs are safe, scoped, reviewable, and acceptable for future open-source contribution preparation.

No pull request has been created yet.

## 1. Evaluation Scope

This report currently covers three cases:

| Case    | Repository                           | Issue Type                            | Patch File              | Status                             |
| ------- | ------------------------------------ | ------------------------------------- | ----------------------- | ---------------------------------- |
| Case 01 | matilefaco/beauty-profile-ai-toolkit | AI coding agent safety documentation  | `patches/case_01.patch` | Accepted for future PR preparation |
| Case 02 | Muggler2k/code-cartographer-mcp      | Agent-readable setup documentation    | `patches/case_02.patch` | Accepted for future PR preparation |
| Case 03 | Muggler2k/code-cartographer-mcp      | Agent-readable capabilities reference | `patches/case_03.patch` | Accepted for future PR preparation |

## 2. Evaluation Criteria

Each case was evaluated using the following quality gate criteria:

1. Issue clarity
2. Repository context understanding
3. Patch scope control
4. Documentation accuracy
5. Safety and privacy risk
6. Repository-specific contract preservation
7. Diff review result
8. Manual validation readiness
9. PR readiness

## 3. Case 01 Evaluation

### 3.1 Summary

Case 01 focused on a documentation issue about safe use of AI coding agents.

Codex recommended adding a short subsection to `CONTRIBUTING.md` titled `Using AI coding agents safely`.

### 3.2 Strengths

1. The Issue was clear and beginner-friendly.
2. The patch was small.
3. The patch changed only documentation.
4. The wording stayed public and generic.
5. The patch avoided source code, package files, tests, and examples.
6. The diff review found no blocking issues.

### 3.3 Main Risk

The main risk was safety wording.

The patch needed to avoid mentioning private SaaS implementation details, real customer data, credentials, private or production prompts, booking logic, and payment logic.

### 3.4 Evaluation Result

Case 01 is acceptable for future PR preparation.

Risk level: Low.

## 4. Case 02 Evaluation

### 4.1 Summary

Case 02 focused on adding an agent-readable setup file, likely `llms.txt`, for Code Cartographer MCP.

Codex generated a root-level `llms.txt` patch.

### 4.2 Strengths

1. The patch added only one file.
2. The patch was documentation-only.
3. It included `npm install`.
4. It included `npm run build`.
5. It correctly stated that MCP clients should point to the built `dist/index.js`.
6. It mentioned `preview_scope`, `init_codebase`, and `check_init_state`.
7. It preserved the codebase-only contract.
8. It preserved the confidence vocabulary.

### 4.3 Main Risk

The main risk was setup accuracy.

An incorrect MCP entrypoint or wrong initialization flow could mislead future agents or users.

### 4.4 Evaluation Result

Case 02 is acceptable for future PR preparation.

Risk level: Moderate-low.

## 5. Case 03 Evaluation

### 5.1 Summary

Case 03 focused on adding an agent-readable capabilities reference for Code Cartographer MCP.

Codex generated a `docs/agent-capabilities.md` patch.

### 5.2 Strengths

1. The patch added only one documentation file.
2. It included a `goal -> tool` table.
3. It covered 20 tools.
4. It included chaining recipes.
5. It preserved the codebase-only contract.
6. It preserved the exact confidence vocabulary.
7. It recommended `llm_readable` or `dual` output for agent consumption.

### 5.3 Main Risk

The main risk was documentation drift.

Because the patch summarizes all documented tools, it may become outdated if `docs/tools-reference.md` changes.

Another risk is tool accuracy. A wrong argument, output mode, or tool purpose could mislead an AI agent.

### 5.4 Evaluation Result

Case 03 is acceptable for future PR preparation.

Risk level: Moderate.

## 6. Cross-Case Comparison

| Criterion                   | Case 01 | Case 02     | Case 03                      |
| --------------------------- | ------- | ----------- | ---------------------------- |
| Issue clarity               | High    | Medium-high | Medium                       |
| Beginner suitability        | High    | Medium      | Medium-low                   |
| Patch size                  | Small   | Small       | Medium                       |
| Source code risk            | Low     | Low         | Low                          |
| Documentation accuracy risk | Low     | Medium      | Medium-high                  |
| Drift risk                  | Low     | Medium      | Medium-high                  |
| Safety risk                 | Medium  | Low         | Low                          |
| PR readiness                | Good    | Good        | Good with careful validation |

## 7. Key Findings

### 7.1 Documentation-only does not mean risk-free

All three cases were documentation-focused, but Case 02 and Case 03 still required technical accuracy.

Documentation can fail when it gives wrong setup commands, wrong tool names, wrong arguments, or misleading capability claims.

### 7.2 Small patches are safer

The safest patches were the ones that changed only one file and avoided unrelated edits.

This supports the quality gate rule:

Keep the first contribution as small as possible.

### 7.3 Repository-specific contracts matter

Case 02 and Case 03 required preserving the codebase-only contract.

This means the generated documentation must not imply runtime execution, test execution, debugger behavior, telemetry inspection, or production proof.

### 7.4 Codex output needs human review

Codex produced useful outputs, but human review was still required to check:

1. Scope
2. Accuracy
3. Safety
4. Drift risk
5. File targets
6. Validation steps
7. PR readiness

## 8. Current Quality Gate Checklist

Before any AI-generated patch is submitted as a PR, it should pass this checklist:

1. The Issue is real and still open.
2. The Issue scope is clear.
3. The patch changes the smallest reasonable set of files.
4. The patch does not touch source code unless required.
5. The patch does not touch package files unless required.
6. The patch does not touch tests unless required.
7. The patch is grounded in existing repository docs.
8. The patch avoids private data and unsupported claims.
9. The patch preserves repository-specific contracts.
10. The patch includes manual validation steps.
11. The patch has been reviewed before PR creation.
12. The final human decision is recorded.

## 9. Current Conclusion

The first three cases show that Codex can generate useful documentation-only contribution drafts for real GitHub Issues.

However, Codex should not be treated as an automatic PR creator.

The better workflow is:

1. Select a suitable Issue.
2. Ask Codex for issue analysis.
3. Ask Codex for a minimal patch.
4. Review the diff.
5. Record risks and validation steps.
6. Make a human decision.
7. Only then consider a PR or Issue comment.

At this stage, all three generated patches are acceptable for future PR preparation, but no PR has been created yet.

