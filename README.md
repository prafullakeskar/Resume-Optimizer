# 🚀 AI Resume Optimizer (Python + Flask + NLP)

An **ATS-aware Resume Optimizer** that compares a resume against **any Job Description pasted from the web**, calculates a match score, identifies missing skills, and suggests optimized resume bullets.

---

## ✨ Features

- Upload resume (**PDF**)
- Paste **any Job Description** (copied from LinkedIn, company sites, etc.)
- ATS-style **match score** using NLP
- **Missing skill detection**
- AI‑ready **bullet point suggestions**
- Clean **Flask MVC architecture**
- Easily extensible to LLMs, Streamlit, or cloud deployment

---

## 🧠 Tech Stack

- **Python 3.11**
- **Flask** – web backend
- **spaCy** – NLP preprocessing
- **scikit-learn** – TF‑IDF & cosine similarity
- **pdfplumber** – resume PDF parsing

---

## 📁 Project Structure

```text
resume-optimizer/
│
├── app.py                  # Flask application entry point
├── parser.py               # Resume PDF parsing
├── nlp_utils.py            # NLP preprocessing utilities
├── scorer.py               # ATS scoring logic
├── optimizer.py            # Skill gap analysis & bullet suggestions
├── skills_db.py            # Skill taxonomy
│
├── templates/
│   └── index.html          # Frontend UI
│
├── uploads/                # Runtime uploads (git-ignored)
│
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

## 🖥️ How to Use

1. Upload your **resume PDF** from your computer
2. Paste the **Job Description** from the web
3. Click **Analyze Resume**
4. View:
   - ATS Match Score
   - Missing / weak skills
   - Suggested optimized bullets

---

## 📊 ATS Scoring Logic (Simplified)

- Text normalization (lemmatization + stopword removal)
- TF‑IDF vectorization
- Cosine similarity between resume and JD

This mimics **real ATS keyword matching behavior**.

---

## 💼 Why This Project Matters

This project demonstrates:
- Real-world **AI/NLP application**
- Clean backend architecture
- ATS awareness (highly relevant for recruiters)
- Practical problem solving
