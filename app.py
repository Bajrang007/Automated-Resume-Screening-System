import streamlit as st
from PyPDF2 import PdfReader
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDFs
def extract_text_from_pdf(pdf_file):
    pdf = PdfReader(pdf_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text

# Function to rank resumes based on job description
def rank_resumes(job_desc, resume_texts):
    corpus = [job_desc] + resume_texts
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    return similarity_scores

# Streamlit UI
st.set_page_config(page_title="Automated Resume Screening", layout="wide")
st.title("📄 Automated Resume Screening System")

# Job Description Input
job_desc = st.text_area("Enter the job description", "")

# Resume Upload
st.subheader("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if st.button("Process Resumes") and job_desc and uploaded_files:
    resume_texts = []
    resume_names = []
    
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resume_texts.append(text)
        resume_names.append(file.name)
    
    # Ranking Resumes
    scores = rank_resumes(job_desc, resume_texts)
    ranked_resumes = sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True)
    
    # Displaying Results
    st.subheader("Ranking Resumes")
    st.table({"Resume": [r[0] for r in ranked_resumes], "Score": [round(r[1], 3) for r in ranked_resumes]})
