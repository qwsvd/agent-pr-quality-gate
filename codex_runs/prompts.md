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

TODO

### GitHub Issue

TODO

### Prompt

TODO

### Purpose

Generate the smallest safe patch without unrelated refactoring or unnecessary dependencies.

## Prompt 03: Diff Review

### Target Repository

TODO

### Patch File

TODO

### Prompt

TODO

### Purpose

Review the generated diff, identify risks, and decide whether the patch is acceptable for PR submission.
