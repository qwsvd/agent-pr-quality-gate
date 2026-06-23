import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Agent PR Quality Gate",
    layout="wide"
)

st.title("Agent PR Quality Gate")
st.write("AI Coding Agent PR Preflight Review and Failure Analysis")

data_path = Path("data/curated_issues.csv")

if data_path.exists():
    df = pd.read_csv(data_path)
    st.subheader("Curated GitHub Issues")
    st.dataframe(df)
else:
    st.warning("data/curated_issues.csv not found.")

results_path = Path("data/quality_gate_results.csv")

if results_path.exists():
    results_df = pd.read_csv(results_path)
    st.subheader("Quality Gate Results")
    st.dataframe(results_df)
else:
    st.warning("data/quality_gate_results.csv not found.")