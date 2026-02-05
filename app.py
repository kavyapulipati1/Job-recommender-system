import streamlit as st
import pandas as pd
import pdfplumber

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load job dataset
jobs = pd.read_csv("data/jobs.csv")

st.title("💼 Job Recommendation System (PDF Resume Upload)")
st.write("Upload your resume PDF and get the best matching job roles!")

# Upload Resume PDF
uploaded_file = st.file_uploader("📌 Upload Resume (PDF only)", type=["pdf"])


# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


if uploaded_file is not None:

    # Extract resume text
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Resume Extracted Text Preview")
    st.text(resume_text[:500])

    if st.button("Recommend Jobs"):

        # Combine resume + job descriptions
        documents = [resume_text] + jobs["JobDescription"].tolist()

        # TF-IDF Vectorization
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Cosine Similarity
        similarity_scores = cosine_similarity(
            tfidf_matrix[0:1], tfidf_matrix[1:]
        ).flatten()

        # Add similarity scores
        jobs["Score"] = similarity_scores

        # Sort recommendations
        recommendations = jobs.sort_values(by="Score", ascending=False)

        st.success("✅ Top Job Recommendations:")
        st.dataframe(recommendations[["JobTitle", "Score"]])

else:
    st.info("Please upload a PDF resume to continue.")
