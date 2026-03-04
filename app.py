import streamlit as st
from core.orchestrator import run_agents
from core.report_generator import generate_report
from config.settings import GROQ_API_KEY, SERPER_API_KEY

st.set_page_config(page_title="AI SaaS Idea Validator")

st.title("AI SaaS Idea Validator")

missing_keys = []
if not GROQ_API_KEY:
    missing_keys.append("GROQ_API_KEY")
if not SERPER_API_KEY:
    missing_keys.append("SERPER_API_KEY")

if missing_keys:
    st.warning(
        "Missing API keys: " + ", ".join(missing_keys) +
        ". Add them to a `.env` file in the project root."
    )

idea = st.text_area("Enter your startup idea")

if st.button("Validate Idea"):
    with st.spinner("Running Multi-Agent Analysis..."):
        results = run_agents(idea)
        report = generate_report(results, idea)

    st.markdown(report)
