import streamlit as st
from utils.parser import extract_text
from utils.similarity import get_similarity, get_missing_keywords
from utils.llm import get_ai_suggestions

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer + ATS Scorer")

st.write("Upload your resume and compare it with a job description using AI.")

pdf = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd = st.text_area("Paste Job Description")

if pdf and jd:
    resume_text = extract_text(pdf)

    score = get_similarity(resume_text, jd)
    st.subheader(f"✅ ATS Score: {score}%")

    missing = get_missing_keywords(resume_text, jd)
    st.subheader("❌ Missing Keywords")
    st.write(missing)

    if st.button("🤖 Analyze with AI"):
        with st.spinner("Analyzing..."):
            suggestions = get_ai_suggestions(resume_text, jd)

        st.subheader("💡 AI Suggestions")
        st.write(suggestions)
