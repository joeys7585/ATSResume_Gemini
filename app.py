import streamlit as st
import spacy
import docx2txt
import google.generativeai as genai
import difflib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

# === INIT ===
genai.configure(api_key=GEMINI_API_KEY)
nlp = spacy.load("en_core_web_sm")

# === UTILS ===

def extract_keywords(text: str):
    doc = nlp(text)
    return set(token.text.lower() for token in doc if token.pos_ in ['NOUN', 'PROPN'])

def extract_resume_text(uploaded_file):
    return docx2txt.process(uploaded_file)

def extract_jd_text(uploaded_file):
    return uploaded_file.read().decode("utf-8")

def call_gemini(prompt: str) -> str:
    model = genai.GenerativeModel(model_name=MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text.strip()

def show_diff(original: str, enhanced: str):
    diff = difflib.unified_diff(
        original.splitlines(),
        enhanced.splitlines(),
        fromfile='Original Resume',
        tofile='Enhanced Resume',
        lineterm=''
    )
    return "\n".join(diff)

def gemini_rate_resume(resume_text: str, jd_text: str) -> str:
    prompt = f"""
You are an expert recruiter and resume reviewer.

Here is a resume:
{resume_text}

Here is the job description:
{jd_text}

Please do the following:
1. Rate how well the resume matches the job description (score out of 100).
2. Highlight strengths and weaknesses.
3. Suggest specific improvements to make it more ATS-friendly and impactful.
4. Return the result in a clear, readable format.
"""
    return call_gemini(prompt)

def ats_score(resume_text: str, jd_text: str):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)
    matched = resume_keywords & jd_keywords
    missing = jd_keywords - resume_keywords
    score = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0
    return score, matched, missing

# === STREAMLIT UI ===

st.set_page_config(page_title="AI Resume Optimizer", layout="wide")
st.title("📄 AI Resume Optimizer (Gemini + ATS)")

with st.sidebar:
    st.header("Upload Files")
    resume_file = st.file_uploader("Upload Resume (.docx)", type=["docx"])
    jd_file = st.file_uploader("Upload Job Description (.txt)", type=["txt"])
    action = st.radio("Select Action", ["Enhance Resume", "Rate Resume", "Optimize Resume"])
    run = st.button("🚀 Run")

if run and resume_file and jd_file:
    resume_text = extract_resume_text(resume_file)
    jd_text = extract_jd_text(jd_file)

    if action == "Enhance Resume":
        st.subheader("📊 ATS Score (Before Enhancement)")
        score_before, matched_before, missing_before = ats_score(resume_text, jd_text)
        st.write(f"**Score:** {score_before:.2f}%")
        st.write(f"✅ Matched Keywords: {matched_before}")
        st.write(f"❌ Missing Keywords: {missing_before}")

        # Enhance with Gemini
        with st.spinner("Enhancing resume with Gemini..."):
            prompt = f"""
You are a professional resume writer.

Here is a resume:
{resume_text}

Here is a job description:
{jd_text}

Please rewrite the resume to:
- Improve the summary section
- Add missing relevant keywords from the job description
- Rewrite experience bullet points to be more impactful
- Keep formatting simple and ATS-friendly

Return the enhanced resume in plain text format.
            """
            enhanced_resume = call_gemini(prompt)

        st.subheader("✅ Enhanced Resume")
        st.text_area("Enhanced Resume", enhanced_resume, height=400)

        st.subheader("🆚 Differences")
        diff = show_diff(resume_text, enhanced_resume)
        st.code(diff, language="diff")

        st.subheader("📊 ATS Score (After Enhancement)")
        score_after, matched_after, missing_after = ats_score(enhanced_resume, jd_text)
        st.write(f"**Score:** {score_after:.2f}%")
        st.write(f"✅ Matched Keywords: {matched_after}")
        st.write(f"❌ Missing Keywords: {missing_after}")

        st.subheader("🤖 Gemini Feedback")
        feedback = gemini_rate_resume(enhanced_resume, jd_text)
        st.markdown(feedback)

    elif action == "Rate Resume":
        st.subheader("📊 ATS Match Score")
        score, matched, missing = ats_score(resume_text, jd_text)
        st.write(f"**Score:** {score:.2f}%")
        st.write(f"✅ Matched Keywords: {matched}")
        st.write(f"❌ Missing Keywords: {missing}")

        st.subheader("🤖 Gemini AI Feedback")
        feedback = gemini_rate_resume(resume_text, jd_text)
        st.markdown(feedback)

    elif action == "Optimize Resume":
        st.subheader("🧠 Keyword Optimization")
        resume_keywords = extract_keywords(resume_text)
        jd_keywords = extract_keywords(jd_text)
        missing_keywords = jd_keywords - resume_keywords

        st.write(f"✅ Resume Keywords: {resume_keywords}")
        st.write(f"📋 JD Keywords: {jd_keywords}")
        st.write(f"❌ Missing Keywords: {missing_keywords}")

        if missing_keywords:
            st.info("Add these keywords to your resume's Skills or Experience sections for better ATS compliance.")
        else:
            st.success("Your resume already contains all major keywords from the job description!")
else:
    st.info("👈 Upload your resume and job description to begin.")
