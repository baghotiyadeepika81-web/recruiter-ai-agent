import streamlit as st
from utils.pdf_loader import extract_text_from_pdf
from utils.llm import analyze_resume

st.set_page_config(
    page_title="Recruiter AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Recruiter AI Agent")

st.write(
    "An AI-powered recruitment assistant that analyzes "
    "candidate resumes and matches them with job requirements."
)

st.divider()

# -------------------------------
# Resume Upload
# -------------------------------

st.header("📄 Candidate Resume")

uploaded_file = st.file_uploader(
    "Upload candidate resume",
    type=["pdf"]
)

# -------------------------------
# Job Description
# -------------------------------

st.header("💼 Job Description")

job_description = st.text_area(
    "Paste the job description",
    height=250,
    placeholder="Paste the complete job description here..."
)

# -------------------------------
# Analysis
# -------------------------------

if uploaded_file:

    st.success(f"✅ Resume uploaded: {uploaded_file.name}")

    resume_text = extract_text_from_pdf(uploaded_file)

    with st.expander("📑 View Extracted Resume Text"):
        st.text(resume_text)

    if st.button("🔍 Analyze & Match Resume", type="primary"):

        if not job_description.strip():

            st.warning("⚠️ Please enter a job description.")

        else:

            with st.spinner("🤖 AI is analyzing the candidate..."):

                result = analyze_resume(
                    resume_text,
                    job_description
                )

            st.success("✅ Analysis Complete!")

            st.divider()

            st.header("🎯 Recruiter AI Analysis")

            st.markdown(result)

            st.divider()

            st.info(
                "💡 This AI-generated analysis is intended to "
                "assist recruiters in evaluating candidates."
            )