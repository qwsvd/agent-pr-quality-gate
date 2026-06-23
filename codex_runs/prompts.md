# Codex Prompts

This file records the prompts used for Codex during open-source issue analysis and patch generation.

## Prompt 01: Issue Understanding

### Target Repository

matilefaco/beauty-profile-ai-toolkit

### GitHub Issue

https://github.com/matilefaco/beauty-profile-ai-toolkit/issues/6

### Prompt

```text
You are helping me analyze a real GitHub Issue for an open-source contribution preflight review.

Target Issue:
https://github.com/matilefaco/beauty-profile-ai-toolkit/issues/6

Goal:
Do not make changes yet. First analyze whether this Issue is suitable for a beginner-friendly documentation contribution.

Tasks:
1. Explain the Issue in simple terms.
2. Identify what kind of documentation file should be added or modified.
3. Check whether this task requires code changes.
4. Identify possible risks.
5. Propose the smallest safe documentation change.
6. Give manual validation steps.
7. Do not create a pull request yet.

Output format:
- Issue summary
- Repository context
- Suggested file to add or modify
- Minimal change plan
- Risk analysis
- Validation steps
- Recommendation
```

### Purpose

Use Codex only for issue understanding and preflight analysis.

The goal of this prompt is to decide whether Issue #6 is suitable for a beginner-friendly documentation contribution before generating any patch or pull request.

## Prompt 02: Minimal Patch Generation

### Target Repository

matilefaco/beauty-profile-ai-toolkit

### GitHub Issue

https://github.com/matilefaco/beauty-profile-ai-toolkit/issues/6

### Prompt

```text
You are helping me generate a minimal documentation patch for a real open-source GitHub Issue.

Target Issue:
https://github.com/matilefaco/beauty-profile-ai-toolkit/issues/6

Target Repository:
matilefaco/beauty-profile-ai-toolkit

Known repository inspection:
The repository has a CONTRIBUTING.md file.
CONTRIBUTING.md already contains:
1. Safe contribution rules
2. Good first contributions
3. Prompt contribution guidelines
4. Development setup
5. Pull request checklist
6. License of contributions

Goal:
Generate the smallest safe documentation patch only.

Important constraints:
1. Do not modify source code.
2. Do not modify src/.
3. Do not modify prompts/.
4. Do not modify examples.
5. Do not modify package files.
6. Do not modify tests.
7. Do not create a pull request.
8. Do not apply changes automatically.
9. Only output a unified diff patch.
10. The patch should add a short subsection to CONTRIBUTING.md after the existing safe contribution rules and before Good first contributions.

Requested section title:
Using AI coding agents safely

The new section should cover:
1. Keep AI coding agents scoped to this public repository.
2. Do not share private Nera SaaS code, private prompts, booking logic, payment logic, credentials, secrets, or real customer data.
3. Review AI-generated changes before merging.
4. Prefer using agents for documentation, examples, tests, and prompt evaluation.
5. Keep examples fictional, minimal, and safe to publish.

Output format:
1. Brief patch summary
2. Unified diff patch only
3. Manual validation steps
4. Risk notes

Do not create a PR.
Do not apply changes.
```

### Purpose

Generate the smallest safe documentation patch for Issue #6 without applying changes, creating a pull request, or modifying code files.

## Prompt 03: Diff Review

### Target Repository

matilefaco/beauty-profile-ai-toolkit

### Patch File

```diff
diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
--- a/CONTRIBUTING.md
+++ b/CONTRIBUTING.md
@@ -14,6 +14,17 @@ Please do **not** contribute:
 
 All examples should be fictional, minimal, and safe to publish.
 
+## Using AI coding agents safely
+
+AI coding agents can be useful for this repository when they stay within the same safety boundaries as human contributors:
+
+- Keep agents scoped to this public repository.
+- Do not share private Nera SaaS code, private prompts, booking logic, payment logic, credentials, secrets, or real customer data with agents.
+- Review AI-generated changes before merging them.
+- Prefer using agents for documentation, examples, tests, and prompt evaluation.
+- Keep agent-generated examples fictional, minimal, and safe to publish.
+
 ## Good first contributions
 
 - Add fictional example profiles for additional beauty specialties.
```

### Prompt

```text
You are helping me review a generated documentation-only patch for a real open-source GitHub Issue.

Target Issue:
https://github.com/matilefaco/beauty-profile-ai-toolkit/issues/6

Target Repository:
matilefaco/beauty-profile-ai-toolkit

Patch:
The patch adds a short section to CONTRIBUTING.md titled "Using AI coding agents safely".

Review goals:
1. Check whether the patch matches Issue #6.
2. Check whether the patch changes only documentation.
3. Check whether the patch introduces private implementation details.
4. Check whether the patch duplicates existing CONTRIBUTING.md guidance too much.
5. Check whether the patch is small enough for a beginner-friendly contribution.
6. Check whether the wording is safe, public, and generic.
7. Decide whether this patch is acceptable for a future pull request.

Output format:
- Patch summary
- Scope check
- Safety check
- Duplication check
- Risk analysis
- Manual validation steps
- Final review decision

Do not apply changes.
Do not create a pull request.
```

### Purpose

Review the generated documentation diff before any pull request is created.

The goal is to confirm whether the patch is safe, minimal, documentation-only, aligned with Issue #6, and acceptable for a future open-source contribution.

## Prompt 04: Case 02 Issue Analysis

### Target Repository

Muggler2k/code-cartographer-mcp

### GitHub Issue

https://github.com/Muggler2k/code-cartographer-mcp/issues/70

### Prompt

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

### Purpose

Use Codex to analyze whether Issue #70 is suitable for a documentation-only or configuration-focused contribution before generating any patch.

The goal is to understand the repository setup requirements, identify the safest target file, and avoid source code changes.

## Prompt 05: Case 02 Diff Review

### Target Repository

Muggler2k/code-cartographer-mcp

### GitHub Issue

https://github.com/Muggler2k/code-cartographer-mcp/issues/70

### Patch File

patches/case_02.patch

### Prompt

```text
You are helping me review a generated documentation-only patch for a real open-source GitHub Issue.

Target Issue:
https://github.com/Muggler2k/code-cartographer-mcp/issues/70

Target Repository:
Muggler2k/code-cartographer-mcp

Patch:
The patch adds one new root-level file: `llms.txt`.

Patch content summary:
The new `llms.txt` contains compact agent setup instructions for Code Cartographer MCP. It includes:

1. Codebase-only contract
2. Preconditions
3. Install and build instructions
4. MCP client configuration
5. Target repository initialization
6. Init state verification
7. Output confidence vocabulary
8. References to existing docs

Important patch details:
1. It mentions `npm install`.
2. It mentions `npm run build`.
3. It says MCP clients should point to built `dist/index.js`.
4. It mentions `preview_scope`.
5. It mentions `init_codebase`.
6. It mentions `check_init_state`.
7. It preserves the codebase-only contract.
8. It preserves the confidence vocabulary: `confirmed`, `likely`, `candidate`, `unclear`, `unresolved`.
9. It avoids restating exact tool counts.
10. It does not modify source code, package files, tests, or existing docs.

Review goals:
1. Check whether the patch matches Issue #70.
2. Check whether adding root-level `llms.txt` is the smallest safe change.
3. Check whether the patch changes only documentation.
4. Check whether the patch preserves the codebase-only contract.
5. Check whether the MCP client setup instruction is accurate.
6. Check whether the confidence vocabulary is preserved exactly.
7. Check whether the patch creates drift risk against existing docs.
8. Decide whether this patch is acceptable for a future pull request.

Output format:
- Patch summary
- Scope check
- Accuracy check
- Codebase-only contract check
- Confidence vocabulary check
- Drift risk check
- Manual validation steps
- Final review decision

Do not apply changes.
Do not create a pull request.
```

### Purpose

Review the generated Case 02 documentation patch before any pull request is created.

The goal is to confirm whether the `llms.txt` patch is safe, minimal, documentation-only, accurate, and aligned with Issue #70.

## Prompt 06: Case 03 Issue Analysis

### Target Repository

Muggler2k/code-cartographer-mcp

### GitHub Issue

https://github.com/Muggler2k/code-cartographer-mcp/issues/71

### Prompt

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

### Purpose

Use Codex to analyze whether Issue #71 is suitable for a documentation-only or example-focused contribution before generating any patch.

The goal is to understand the scope, risks, required documentation target, and validation steps for an agent-readable capabilities reference.

## Prompt 07: Case 03 Patch Generation

### Target Repository

Muggler2k/code-cartographer-mcp

### GitHub Issue

https://github.com/Muggler2k/code-cartographer-mcp/issues/71

### Prompt

```text
You are helping me generate a minimal documentation-only patch for a real open-source GitHub Issue.

Target Issue:
https://github.com/Muggler2k/code-cartographer-mcp/issues/71

Target Repository:
Muggler2k/code-cartographer-mcp

Known repository context:
The repository already has:
1. README.md
2. docs/tools-reference.md
3. docs/mcp-client-config.md
4. docs/architecture.md

Issue goal:
Create an agent-readable capabilities reference that helps an LLM choose the right Code Cartographer MCP tool, pass correct arguments, prefer agent-friendly output modes, and chain tools correctly during a task.

Important repository contract:
The project is codebase-only.

Outputs are static inferences from checked-in files, not runtime truth.

Do not imply that the server runs the target app, executes tests, attaches a debugger, inspects telemetry, or proves production behavior.

Confidence terms must stay exactly:

`confirmed`, `likely`, `candidate`, `unclear`, `unresolved`

Goal:
Generate the smallest safe documentation-only patch.

Important constraints:
1. Do not modify source code.
2. Do not modify `src/`.
3. Do not modify package files.
4. Do not modify tests.
5. Do not modify existing docs unless absolutely necessary.
6. Do not create a pull request.
7. Do not apply changes automatically.
8. Only output a unified diff patch.
9. The patch should add one new documentation file: `docs/agent-capabilities.md`.
10. Keep the new document compact and agent-readable.
11. Ground the content in existing documentation.
12. Do not invent unsupported capabilities.
13. Avoid restating exact implementation details that could drift quickly.
14. Do not mention exact tool counts except where necessary to satisfy the issue.

The new `docs/agent-capabilities.md` should include:

1. A title: `# Agent capabilities reference`
2. A short codebase-only contract warning.
3. A compact `goal -> tool` table.
4. Coverage of all 20 tools.
5. For each tool, include:
   - purpose
   - when to use it
   - key required arguments
   - recommended output mode when used by agents
   - confidence or uncertainty note
6. At least 3 chaining recipes.
7. A note to prefer `llm_readable` or `dual` output for agent consumption.
8. References to:
   - `README.md`
   - `docs/tools-reference.md`
   - `docs/mcp-client-config.md`
   - `docs/architecture.md`

Suggested chaining recipes:
1. `preview_scope -> init_codebase -> check_init_state -> get_context_summary`
2. `get_context_summary -> find_callers -> find_path`
3. `review_preflight -> analyze_change_impact -> review_change`

Output format:
1. Brief patch summary
2. Unified diff patch only
3. Manual validation steps
4. Risk notes

Do not create a PR.
Do not apply changes.
```

### Purpose

Generate a minimal documentation-only patch for Case 03.

The goal is to add one agent-readable capabilities reference file without modifying source code, package files, tests, or existing documentation.

## Prompt 08: Case 03 Diff Review

### Target Repository

Muggler2k/code-cartographer-mcp

### GitHub Issue

https://github.com/Muggler2k/code-cartographer-mcp/issues/71

### Patch File

patches/case_03.patch

### Prompt

```text
You are helping me review a generated documentation-only patch for a real open-source GitHub Issue.

Target Issue:
https://github.com/Muggler2k/code-cartographer-mcp/issues/71

Target Repository:
Muggler2k/code-cartographer-mcp

Patch:
The patch adds one new documentation file:

`docs/agent-capabilities.md`

Patch content summary:
The new file is titled `Agent capabilities reference`.

It includes:

1. A codebase-only contract warning.
2. A note recommending `outputMode: "llm_readable"` or `outputMode: "dual"` for agent consumption.
3. The exact confidence vocabulary: `confirmed`, `likely`, `candidate`, `unclear`, `unresolved`.
4. A `Goal -> tool` table.
5. A tool reference table covering 20 tools.
6. Chaining recipes.
7. References to existing repository docs.

Tools covered in the patch:

1. `preview_scope`
2. `init_codebase`
3. `check_init_state`
4. `get_context_summary`
5. `analyze_reachability`
6. `analyze_change_impact`
7. `find_duplicate_behavior`
8. `classify_legacy_paths`
9. `get_ownership`
10. `review_preflight`
11. `review_change`
12. `investigate_failure`
13. `analyze_test_paths`
14. `detect_architecture_drift`
15. `find_callers`
16. `find_path`
17. `analyze_diff`
18. `map_call_stack`
19. `visualize_call_stack`
20. `visualize_architecture`

Chaining recipes included:

1. `preview_scope -> init_codebase -> check_init_state -> get_context_summary`
2. `get_context_summary -> find_callers -> find_path`
3. `review_preflight -> analyze_change_impact -> review_change`
4. `investigate_failure -> analyze_reachability -> analyze_test_paths`
5. `map_call_stack -> visualize_call_stack`

Review goals:
1. Check whether the patch matches Issue #71.
2. Check whether it covers all 20 tools.
3. Check whether the tool names match the existing `docs/tools-reference.md`.
4. Check whether the key required arguments are likely accurate.
5. Check whether the patch changes only documentation.
6. Check whether the patch preserves the codebase-only contract.
7. Check whether the confidence vocabulary is preserved exactly.
8. Check whether the chaining recipes are reasonable.
9. Check whether the patch creates documentation drift risk.
10. Decide whether this patch is acceptable for a future pull request.

Output format:
- Patch summary
- Scope check
- Tool coverage check
- Accuracy check
- Codebase-only contract check
- Confidence vocabulary check
- Chaining recipe check
- Drift risk check
- Manual validation steps
- Final review decision

Do not apply changes.
Do not create a pull request.
```

### Purpose

Review the generated Case 03 documentation patch before any pull request is created.

The goal is to confirm whether the patch is documentation-only, accurate, complete, grounded in the existing tool reference, and acceptable for future PR preparation.

