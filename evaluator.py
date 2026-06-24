"""Evaluation helpers for quality gate case records."""


def evaluate_case(case_record: dict[str, str]) -> str:
    """Return a concise quality gate decision for one case record."""
    acceptability = case_record.get("human_acceptability", "").lower()
    failure_reason = case_record.get("failure_reason", "").lower()

    if acceptability == "acceptable" and failure_reason in {"", "none_blocking"}:
        return "ready_for_future_pr_review"
    if acceptability == "acceptable":
        return "acceptable_with_known_risk"
    return "needs_more_review"


if __name__ == "__main__":
    sample = {
        "human_acceptability": "acceptable",
        "failure_reason": "none_blocking",
    }
    print(evaluate_case(sample))
