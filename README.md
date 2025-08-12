# 📄 Automated Resume Screening System

An AI-powered web application built with **Streamlit** that automates the process of screening resumes by comparing them to a provided job description.  
The system uses **TF-IDF vectorization** and **cosine similarity** to rank resumes based on their textual relevance to the job description.

---

## 🚀 Live Demo
🔗 **[Click here to use the app](https://bajrang007-automated-resume-screening-system-app-dljkrq.streamlit.app/)**

---

## ✨ Features

- 📤 **Upload multiple resumes** (PDF format)
- 📝 **Enter any job description**
- ⚡ **Automatic text extraction** from PDF resumes
- 📊 **TF-IDF based similarity scoring**
- 🏆 **Ranks resumes from most relevant to least relevant**
- 🌐 **Deployed on Streamlit Cloud** — accessible anywhere

---

## 🛠️ Tech Stack

- **Python 3.x**
- [Streamlit](https://streamlit.io/) – Web app framework
- [PyPDF2](https://pypi.org/project/PyPDF2/) – PDF text extraction
- [NumPy](https://numpy.org/) – Numerical operations
- [scikit-learn](https://scikit-learn.org/) – Machine learning utilities (TF-IDF, cosine similarity)

---

## 📂 Project Structure

automated-resume-screening-system/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation


---

## ⚙️ How It Works

1. **Input Job Description**  
   The recruiter enters the job requirements in the text area.
   
2. **Upload Resumes**  
   Upload one or more PDF resumes.

3. **Processing**  
   - Text is extracted from each resume using `PyPDF2`.
   - TF-IDF vectorization converts text to numerical features.
   - Cosine similarity compares job description and resumes.

4. **Output**  
   - A ranked table showing resumes in order of relevance.
   - Similarity score for each resume (0 to 1).

---

## 💻 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Bajrang007/Automated-Resume-Screening-System.git
cd automated-resume-screening-system

