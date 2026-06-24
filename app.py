from pathlib import Path
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Agent PR Quality Gate", layout="wide")

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
CASES_DIR = ROOT / "cases"
PATCHES_DIR = ROOT / "patches"
REPORTS_DIR = ROOT / "reports"
CODEX_DIR = ROOT / "codex_runs"


def load_csv(path: Path) -> pd.DataFrame:
    """Read a CSV file, returning an empty dataframe when it is unavailable."""
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()


def read_text(path: Path) -> str:
    """Read a UTF-8 text file for display in the dashboard."""
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "File not found."


def count_real_prs(results: pd.DataFrame) -> int:
    """Count rows with a recorded pull request URL."""
    if "pr_url" not in results.columns:
        return 0

    pr_urls = results["pr_url"].fillna("").astype(str).str.strip()
    return int((pr_urls != "").sum())


st.title("Agent PR Quality Gate")
st.caption("AI Coding Agent PR Preflight Review and Failure Analysis")

st.write(
    "This dashboard summarizes a quality gate workflow for reviewing AI coding "
    "agent outputs before they are submitted to real open-source GitHub projects."
)

st.write(
    "The project tracks real GitHub Issues, Codex prompts, generated patch drafts, "
    "diff review results, human decisions, and failure analysis."
)

quality_results = load_csv(DATA_DIR / "quality_gate_results.csv")
curated_issues = load_csv(DATA_DIR / "curated_issues.csv")

completed_cases = 0
generated_patches = 0
accepted_cases = 0

if not quality_results.empty:
    completed_cases = len(quality_results)

if "final_outcome" in quality_results.columns:
    generated_patches = int(
        (
            quality_results["final_outcome"]
            == "patch_generated_and_accepted_for_future_pr"
        ).sum()
    )

if "human_acceptability" in quality_results.columns:
    accepted_cases = int(
        (quality_results["human_acceptability"] == "acceptable").sum()
    )

col1, col2, col3, col4 = st.columns(4)

col1.metric("Completed Cases", completed_cases)
col2.metric("Generated Patches", generated_patches)
col3.metric("Accepted for Future PR", accepted_cases)
col4.metric("Real PRs Created", count_real_prs(quality_results))

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

    if quality_results.empty:
        st.warning("data/quality_gate_results.csv not found or empty.")
    else:
        st.dataframe(quality_results, use_container_width=True)

        st.subheader("Result Summary")

        for _, row in quality_results.iterrows():
            st.markdown(f"Case: {row.get('case_id', '')}")
            st.write(f"Repository: {row.get('repo', '')}")
            st.write(f"Issue: {row.get('issue_url', '')}")
            st.write(f"Patch submitted: {row.get('patch_submitted', '')}")
            st.write(f"Final outcome: {row.get('final_outcome', '')}")
            st.write(f"Human acceptability: {row.get('human_acceptability', '')}")
            st.write(f"Failure reason: {row.get('failure_reason', '')}")
            st.divider()

with tab2:
    st.subheader("Curated GitHub Issues")

    if curated_issues.empty:
        st.warning("data/curated_issues.csv not found or empty.")
    else:
        st.dataframe(curated_issues, use_container_width=True)

with tab3:
    st.subheader("Case Studies")

    case_files = {
        "Case 01: Documentation Safety Guide": CASES_DIR / "case_01_doc_fix.md",
        "Case 02: Agent-Readable Setup Documentation": CASES_DIR
        / "case_02_install_config.md",
        "Case 03: Agent-Readable Capabilities Reference": CASES_DIR
        / "case_03_example_fix.md",
        "Case 04: Bug Reproduction": CASES_DIR / "case_04_bug_repro.md",
        "Case 05: Agent Failure": CASES_DIR / "case_05_agent_failure.md",
    }

    selected_case = st.selectbox("Select a case file", list(case_files.keys()))
    st.markdown(read_text(case_files[selected_case]))

with tab4:
    st.subheader("Generated Patch Files")

    patch_files = {
        "Case 01 Patch": PATCHES_DIR / "case_01.patch",
        "Case 02 Patch": PATCHES_DIR / "case_02.patch",
        "Case 03 Patch": PATCHES_DIR / "case_03.patch",
    }

    selected_patch = st.selectbox("Select a patch file", list(patch_files.keys()))
    st.code(read_text(patch_files[selected_patch]), language="diff")

with tab5:
    st.subheader("Project Reports")

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

st.divider()

st.subheader("Current Status")
st.write(
    "The current version is a preflight review and evidence-recording workflow. "
    "It includes three completed case studies, three generated patch files, Codex "
    "prompt logs, Codex result logs, a failure analysis report, an evaluation "
    "report, and an interview summary."
)
st.write("No real pull request has been created yet.")
