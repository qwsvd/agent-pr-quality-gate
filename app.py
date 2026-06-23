import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
page_title="Agent PR Quality Gate",
layout="wide"
)

ROOT = Path(**file**).parent

DATA_DIR = ROOT / "data"
CASES_DIR = ROOT / "cases"
PATCHES_DIR = ROOT / "patches"
REPORTS_DIR = ROOT / "reports"
CODEX_DIR = ROOT / "codex_runs"

def load_csv(path: Path) -> pd.DataFrame:
if path.exists():
return pd.read_csv(path)
return pd.DataFrame()

def read_text(path: Path) -> str:
if path.exists():
return path.read_text(encoding="utf-8")
return "File not found."

st.title("Agent PR Quality Gate")
st.caption("AI Coding Agent PR Preflight Review and Failure Analysis")

st.markdown(
"""
This dashboard summarizes a small quality gate workflow for reviewing AI coding agent outputs before they are submitted to real open-source GitHub projects.

The project tracks real GitHub Issues, Codex prompts, generated patch drafts, diff review results, human decisions, and failure analysis.
"""
)

quality_results = load_csv(DATA_DIR / "quality_gate_results.csv")
curated_issues = load_csv(DATA_DIR / "curated_issues.csv")

completed_cases = 0
generated_patches = 0
accepted_cases = 0

if not quality_results.empty:
completed_cases = len(quality_results)
generated_patches = (quality_results["final_outcome"] == "patch_generated_and_accepted_for_future_pr").sum()
accepted_cases = (quality_results["human_acceptability"] == "acceptable").sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Completed Cases", completed_cases)
col2.metric("Generated Patches", generated_patches)
col3.metric("Accepted for Future PR", accepted_cases)
col4.metric("Real PRs Created", 0)

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(
[
"Quality Gate Results",
"Curated Issues",
"Case Studies",
"Patch Files",
"Reports",
]
)

with tab1:
st.subheader("Quality Gate Results")

```
if quality_results.empty:
    st.warning("data/quality_gate_results.csv not found or empty.")
else:
    st.dataframe(quality_results, use_container_width=True)

    st.markdown("### Result Summary")

    for _, row in quality_results.iterrows():
        st.markdown(
            f"""
```

**{row["case_id"]}**

* Repository: `{row["repo"]}`
* Issue: {row["issue_url"]}
* Patch submitted: `{row["patch_submitted"]}`
* Final outcome: `{row["final_outcome"]}`
* Human acceptability: `{row["human_acceptability"]}`
* Failure reason: `{row["failure_reason"]}`
  """
  )

with tab2:
st.subheader("Curated GitHub Issues")

```
if curated_issues.empty:
    st.warning("data/curated_issues.csv not found or empty.")
else:
    st.dataframe(curated_issues, use_container_width=True)
```

with tab3:
st.subheader("Case Studies")

```
case_files = {
    "Case 01: Documentation Safety Guide": CASES_DIR / "case_01_doc_fix.md",
    "Case 02: Agent-Readable Setup Documentation": CASES_DIR / "case_02_install_config.md",
    "Case 03: Agent-Readable Capabilities Reference": CASES_DIR / "case_03_example_fix.md",
    "Case 04: Bug Reproduction": CASES_DIR / "case_04_bug_repro.md",
    "Case 05: Agent Failure": CASES_DIR / "case_05_agent_failure.md",
}

selected_case = st.selectbox("Select a case file", list(case_files.keys()))
st.markdown(read_text(case_files[selected_case]))
```

with tab4:
st.subheader("Generated Patch Files")

```
patch_files = {
    "Case 01 Patch": PATCHES_DIR / "case_01.patch",
    "Case 02 Patch": PATCHES_DIR / "case_02.patch",
    "Case 03 Patch": PATCHES_DIR / "case_03.patch",
}

selected_patch = st.selectbox("Select a patch file", list(patch_files.keys()))
st.code(read_text(patch_files[selected_patch]), language="diff")
```

with tab5:
st.subheader("Project Reports")

```
report_files = {
    "Failure Analysis": REPORTS_DIR / "failure_analysis.md",
    "Evaluation Report": REPORTS_DIR / "evaluation_report.md",
    "Interview Summary": REPORTS_DIR / "interview_summary.md",
    "Contribution Log": REPORTS_DIR / "contribution_log.md",
    "Codex Prompts": CODEX_DIR / "prompts.md",
    "Codex Results": CODEX_DIR / "results.md",
}

selected_report = st.selectbox("Select a report", list(report_files.keys()))
st.markdown(read_text(report_files[selected_report]))
```

st.divider()

st.markdown(
"""

### Current Status

The first project version includes three completed case studies, three generated patch files, Codex prompt logs, Codex result logs, a failure analysis report, an evaluation report, and an interview summary.

No pull request has been created yet.
"""
)

