# Interview Summary

This file summarizes how to explain the project in interviews.

## 1. One Sentence Summary

This project is an AI coding agent PR preflight review and failure analysis system based on real GitHub Issues, Codex-generated patches, human review, diff risk analysis, and open-source contribution attempts.

## 2. Problem

AI coding agents can generate code and patches, but real open-source contribution requires more than code generation.

A patch must be understandable, minimal, testable, aligned with maintainer expectations, and safe to submit.

## 3. Project Approach

The project builds a small evidence-based workflow:

1. Collect real GitHub Issues
2. Classify issue difficulty and agent suitability
3. Use Codex to generate plans or patches
4. Review generated diffs manually
5. Check tests or manual validation steps
6. Attempt real GitHub PRs or Issue comments
7. Analyze why AI-generated outputs succeed or fail

## 4. My Role

My role in this project is not only to use Codex to generate code.

My role is to act as a human reviewer who checks whether AI-generated outputs are safe, minimal, verifiable, and suitable for real open-source collaboration.

## 5. Key Evidence

1. Curated GitHub Issue dataset
2. Deep case studies
3. Codex prompt and output records
4. Patch files
5. Quality gate evaluation report
6. Failure analysis report
7. Real PR or Issue interaction record

## 6. What This Project Demonstrates

This project demonstrates:

1. AI coding agent workflow understanding
2. GitHub open-source collaboration awareness
3. Diff risk analysis ability
4. Human-in-the-loop review ability
5. Failure analysis ability
6. Evidence-based project documentation ability

## 7. Interview Answer Draft

I built an AI coding agent PR preflight review and failure analysis project.

The core idea is that tools like Codex can generate code or patches, but real open-source contribution still requires human review, diff risk analysis, validation, maintainer context checking, and failure analysis.

In this project, I collected real GitHub Issues, used Codex to analyze issues and generate patches, manually reviewed the diff risk, recorded validation steps, and documented whether the result was suitable for a real PR or Issue comment.

The project is focused on making AI-generated code changes auditable, verifiable, and suitable for real engineering collaboration.

## 8. Limitations

TODO

## 9. Next Improvement

TODO
