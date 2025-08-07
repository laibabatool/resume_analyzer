# 📄 Resume Analyzer with Gemini Pro (LLM-Powered)

A powerful **Streamlit-based Resume Analyzer** that leverages **Google Gemini Pro (via LangChain)** to extract, summarize, and rank resume information. It supports both **single resume analysis** and **bulk resume-job fit evaluation**, making it a handy tool for recruiters, HR teams, and job portals.

---

## 🚀 Features

### 🔍 Single Resume Analysis
- Upload a PDF resume
- Extract:
  - Full Name
  - Experience (Role, Company, Duration)
  - Projects (Name + Tools/Tech used)
  - Contact Info (Email & Phone)
  - Education
- Ask **custom questions** about the resume

### 📊 Bulk Resume Comparison
- Upload multiple PDF resumes
- Provide a job description
- Get:
  - Relevance reasoning per resume
  - Ranked list from best to least matching candidate

---

## 📸 UI Preview

### 🧍 Single Resume Analysis

**Upload Interface:**

![Single Resume UI](UI%20images/Single%20resume%20UI.PNG)

---

### 🧑‍🤝‍🧑 Bulk Resume Comparison

**Upload Multiple Resumes + Job Description:**

![Bulk Resume UI](UI%20images/Bulk%20resume%20UI.PNG)

---

## 🎥 Demo Video

🎬 **Watch it in action**:

[![Watch the demo]](UI%20images/demo.mp4)

---

## 🧠 Tech Stack

| Tool/Library         | Purpose                                       |
|----------------------|-----------------------------------------------|
| Streamlit            | Frontend UI                                   |
| PyPDF2               | Resume text extraction from PDF               |
| LangChain            | Prompt engineering and chaining               |
| Gemini 1.5 Pro       | Large Language Model for text analysis        |
| pandas               | Managing ranked candidate data                |

---

## 📁 Project Structure

