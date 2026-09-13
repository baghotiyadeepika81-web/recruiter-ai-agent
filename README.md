# 🤖 Recruiter AI Agent

An AI-powered recruitment assistant that helps recruiters analyze candidate resumes and match them with job requirements.

## 📌 Project Overview

Recruiter AI Agent is designed to make the initial resume screening process faster and easier.

The system accepts a candidate's resume in PDF format and a Job Description. It extracts the resume text and uses an AI model to analyze how well the candidate matches the job requirements.

## 🚀 Features

- 📄 Upload candidate resumes in PDF format
- 📝 Extract text from resumes
- 💼 Enter job descriptions
- 🤖 AI-powered resume analysis
- 🎯 Resume-to-job matching
- 📊 Match score
- ✅ Matching skills identification
- ❌ Missing skills identification
- 💪 Candidate strengths
- 🎯 Recruiter recommendation

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Large Language Model (LLM)
- PyPDF
- python-dotenv

## 🔄 Workflow

Resume PDF
↓
Text Extraction
↓
Job Description
↓
AI Analysis
↓
Skill Matching
↓
Match Score & Recommendation

## 📂 Project Structure

```text
Recruiter-AI-Agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── prompts/
│   └── prompt.py
│
├── utils/
│   ├── embeddings.py
│   ├── llm.py
│   ├── pdf_loader.py
│   ├── retriever.py
│   └── txt_splitter.py
│
└── data/
    └── resumes/