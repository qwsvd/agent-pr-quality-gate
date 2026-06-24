"""Minimal diff inspection helpers for generated patch drafts."""


def analyze_diff(diff_text: str) -> dict[str, int]:
    """Count changed files, added lines, and removed lines in a unified diff."""
    files_changed = 0
    additions = 0
    deletions = 0

    for line in diff_text.splitlines():
        if line.startswith("diff --git "):
            files_changed += 1
        elif line.startswith("+") and not line.startswith("+++"):
            additions += 1
        elif line.startswith("-") and not line.startswith("---"):
            deletions += 1

    return {
        "files_changed": files_changed,
        "additions": additions,
        "deletions": deletions,
    }


if __name__ == "__main__":
    sample_diff = """diff --git a/README.md b/README.md
+Added setup note
-Old setup note
"""
    print(analyze_diff(sample_diff))
