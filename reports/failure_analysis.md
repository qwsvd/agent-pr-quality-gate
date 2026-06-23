# Failure Analysis

This report summarizes observed and expected failure modes when using AI coding agents for real GitHub Issue preflight review and patch preparation.

The current analysis is based on the first three documented cases in this project.

## 1. Case Coverage

| Case    | Issue Type                            | Patch Generated | Risk Level   | Current Outcome          |
| ------- | ------------------------------------- | --------------: | ------------ | ------------------------ |
| Case 01 | Documentation safety guide            |             Yes | Low          | Acceptable for future PR |
| Case 02 | Agent-readable setup documentation    |             Yes | Moderate-low | Acceptable for future PR |
| Case 03 | Agent-readable capabilities reference |             Yes | Moderate     | Acceptable for future PR |

## 2. Main Failure Modes

### 2.1 Scope Creep

AI coding agents may expand a small documentation Issue into a larger change than needed.

Observed risk:

* Case 01 could have become a long AI policy document.
* Case 02 could have generated both `llms.txt` and `llms-full.txt`.
* Case 03 could have modified existing docs or added too much tool detail.

Control method:

* Force the prompt to ask for the smallest safe change.
* Explicitly forbid source code, package, test, and unrelated documentation changes.
* Review the generated patch before any PR is created.

## 3. Documentation Accuracy Risk

Documentation-only Issues can still be technically risky.

Observed risk:

* Case 02 required accurate MCP client setup instructions.
* The MCP client entrypoint needed to point to the built `dist/index.js`.
* Case 03 required accurate coverage of all 20 tools.
* Tool names, arguments, output modes, and uncertainty notes could easily drift from the official tool reference.

Control method:

* Cross-check generated documentation against existing repository docs.
* Avoid restating volatile implementation details unless necessary.
* Reference authoritative existing docs such as README files, setup guides, and tool references.

## 4. Repository Contract Risk

AI coding agents may accidentally weaken repository-specific constraints.

Observed risk:

* Case 02 and Case 03 both needed to preserve the codebase-only contract.
* Generated wording could incorrectly imply runtime truth, test execution, telemetry inspection, debugger behavior, or production proof.

Control method:

* Add explicit prompt constraints about repository contracts.
* Use repeated diff review checks for forbidden implications.
* Preserve exact vocabulary when the repository defines specific confidence terms.

## 5. Private Information and Safety Risk

AI-generated documentation may accidentally mention or imply private implementation details.

Observed risk:

* Case 01 involved safe AI coding agent usage and private repository boundaries.
* The generated patch needed to avoid private SaaS code, private or production prompts, booking logic, payment logic, credentials, secrets, and real customer data.

Control method:

* Ask Codex to identify safety risks before patch generation.
* Use human review to check whether public and generic wording is preserved.
* Avoid adding examples that use real users, private systems, credentials, or business-sensitive logic.

## 6. Drift Risk

AI-generated documentation may duplicate existing documentation and become outdated later.

Observed risk:

* Case 02 added a compact `llms.txt` that references existing setup docs.
* Case 03 duplicated compact summaries for 20 tools, which may need updates when the official tool reference changes.

Control method:

* Keep generated documentation compact.
* Reference existing authoritative docs.
* Avoid exact tool counts or volatile implementation details unless required by the Issue.
* Record drift risk in the case notes and review reports.

## 7. Beginner Suitability Risk

Not all documentation Issues are equally beginner-friendly.

Observed pattern:

* Case 01 was beginner-friendly because it required a small safety subsection.
* Case 02 was more complex because it required synthesizing setup instructions from multiple files.
* Case 03 was significantly more complex because it required full tool coverage and chaining examples.

Control method:

* Classify Issues before generating patches.
* Start with small documentation-only changes.
* Avoid large capability references until the repository context is understood.
* Treat “documentation-only” as lower risk, not zero risk.

## 8. Current Lessons

The first three cases show that AI coding agents can produce useful open-source contribution drafts, but they require structured human review.

The most important quality gate checks are:

1. Is the Issue scope clear?
2. Is the patch the smallest safe change?
3. Does the patch modify only expected files?
4. Does it preserve repository-specific contracts?
5. Does it avoid private information?
6. Does it match existing documentation?
7. Does it avoid unsupported claims?
8. Does it include validation steps?
9. Is it acceptable for a future PR?

## 9. Current Conclusion

The main failure risk is not that Codex cannot generate text.

The main failure risk is that Codex may generate documentation that is too broad, slightly inaccurate, misaligned with repository constraints, or likely to drift from existing docs.

A useful AI Coding Agent quality gate should therefore combine:

1. Issue suitability analysis.
2. Prompt logging.
3. Patch generation.
4. Diff review.
5. Manual validation steps.
6. Human decision records.
7. Failure mode tracking.

No pull request has been created yet.
