#  Resume Analyzer

A powerful **Streamlit-based Resume Analyzer** that leverages **Google Gemini Pro (via LangChain)** to extract, summarize, and rank resume information. It supports both **single resume analysis** and **bulk resume-job fit evaluation**, making it a handy tool for recruiters, HR teams, and job portals.

---

##  Features

###  Single Resume Analysis
- Upload a PDF resume
- Extract:
  - Full Name
  - Experience (Role, Company, Duration)
  - Projects (Name + Tools/Tech used)
  - Contact Info (Email & Phone)
  - Education
- Ask **custom questions** about the resume

###  Bulk Resume Comparison
- Upload multiple PDF resumes
- Provide a job description
- Get:
  - Relevance reasoning per resume
  - Ranked list from best to least matching candidate

---

##  UI Preview

###  Single Resume Analysis

**Upload Interface:**

![Single Resume UI](UI%20images/Single%20resume%20UI.PNG)

---

###  Bulk Resume Comparison

**Upload Multiple Resumes + Job Description:**

![Bulk Resume UI](UI%20images/Bulk%20resume%20UI.PNG)

---

##  Demo Video

 **Watch it in action**:

[![Watch the demo]](UI%20images/demo.mp4)

---

##  Tech Stack

| Tool/Library         | Purpose                                       |
|----------------------|-----------------------------------------------|
| Streamlit            | Frontend UI                                   |
| PyPDF2               | Resume text extraction from PDF               |
| LangChain            | Prompt engineering and chaining               |
| Gemini 1.5 Pro       | Large Language Model for text analysis        |
| pandas               | Managing ranked candidate data                |

---

## 📁 Project Structure
```
resume-analyzer/
│
├── UI images/ 
│ ├── single resume UI.png
│ ├── bulk resume UI.png
│ └── demo-video.mp4
│
├── .streamlit/
│ └── secrets.toml # Store your API keys here
│
├── resume_analyzer.py # Main Streamlit app
├── requirements.txt 
└── README.md
```

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set API Keys
Create a `.streamlit/secrets.toml` file with your Google Gemini API key:
```toml
[api_keys]
GOOGLE_API_KEY = "your-google-api-key"
```

### 4. Run the App
```bash
streamlit run resume_analyzer.py
```

---

### Example Prompts for Queries
```
"What technologies has the candidate worked with?"

"Summarize the candidate's work experience."

"Which project relates to AI?"
```
---
Pull requests, ideas, and bug reports are welcome!  
If you find this useful, give it a ⭐️ and share your feedback!
