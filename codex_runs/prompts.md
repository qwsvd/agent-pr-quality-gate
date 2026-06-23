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

TODO

### Patch File

TODO

### Prompt

TODO

### Purpose

Review the generated diff, identify risks, and decide whether the patch is acceptable for PR submission.
