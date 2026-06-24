"""Tiny quality gate summary helpers for the portfolio dashboard."""


def summarize_quality_gate(records: list[dict[str, str]]) -> dict[str, int]:
    """Summarize completed cases, generated patches, accepted cases, and PRs."""
    generated_outcome = "patch_generated_and_accepted_for_future_pr"

    return {
        "completed_cases": len(records),
        "generated_patches": sum(
            record.get("final_outcome") == generated_outcome
            for record in records
        ),
        "accepted_cases": sum(
            record.get("human_acceptability") == "acceptable"
            for record in records
        ),
        "real_prs_created": sum(bool(record.get("pr_url")) for record in records),
    }


if __name__ == "__main__":
    sample_records = [
        {
            "final_outcome": "patch_generated_and_accepted_for_future_pr",
            "human_acceptability": "acceptable",
            "pr_url": "",
        }
    ]
    print(summarize_quality_gate(sample_records))
