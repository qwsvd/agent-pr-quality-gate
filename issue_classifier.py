"""Small helper for classifying curated GitHub Issues by contribution type."""


def classify_issue(issue_title: str, issue_type: str = "") -> str:
    """Return a simple issue category for dashboard and review notes."""
    text = f"{issue_title} {issue_type}".lower()

    if "doc" in text or "readme" in text or "llms" in text:
        return "documentation"
    if "bug" in text or "fix" in text or "error" in text:
        return "bugfix"
    if "test" in text:
        return "test"
    return "unknown"


if __name__ == "__main__":
    sample = "Docs AI-friendly Setup agent-readable llms.txt"
    print(f"{sample}: {classify_issue(sample)}")
