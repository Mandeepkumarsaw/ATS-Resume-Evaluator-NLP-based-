import streamlit as st
import PyPDF2
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- NLTK SETUP (FIXED) ----------
@st.cache_resource
def download_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab')

download_nltk()

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="ATS Resume Analyzer", page_icon="📄", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------- FUNCTIONS ----------
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def calculate_ats(resume, jd):
    vectorizer = CountVectorizer().fit_transform([resume, jd])
    vectors = vectorizer.toarray()
    score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    return round(score * 100, 2)

# ✅ FIXED TOKENIZER (Fallback added)
def safe_tokenize(text):
    try:
        return nltk.word_tokenize(text)
    except:
        return text.split()  # fallback

def keyword_analysis(resume, jd):
    resume_words = set(safe_tokenize(resume))
    jd_words = set(safe_tokenize(jd))
    return resume_words.intersection(jd_words), jd_words - resume_words

# ---------- UI ----------
st.title("📄 AI Resume Analyzer")
st.caption("Check your resume ATS score instantly")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📤 Upload Resume", type="pdf")

with col2:
    job_description = st.text_area("🧾 Paste Job Description")

if uploaded_file and job_description:

    with st.spinner("Analyzing Resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(job_description)

        score = calculate_ats(clean_resume, clean_jd)
        matched, missing = keyword_analysis(clean_resume, clean_jd)

    # ---------- SCORE ----------
    st.subheader("📊 ATS Score")
    st.progress(int(score))
    st.metric("Match Percentage", f"{score}%")

    if score > 75:
        st.success("Excellent Match 🚀")
    elif score > 50:
        st.warning("Good, but can improve ⚠️")
    else:
        st.error("Needs improvement ❌")

    # ---------- KEYWORDS ----------
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("✅ Matched Keywords")
        for word in list(matched)[:20]:
            st.success(word)

    with col4:
        st.subheader("❌ Missing Keywords")
        for word in list(missing)[:20]:
            st.error(word)