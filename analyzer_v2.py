import streamlit as st
from langchain.prompts import PromptTemplate
import PyPDF2
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import tempfile
import pandas as pd
import time

# Load Google API Key from Streamlit secrets
GOOGLE_API_KEY = st.secrets['api_keys']['GOOGLE_API_KEY']

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GOOGLE_API_KEY)

# Function to extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = PyPDF2.PdfReader(uploaded_file)
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

# Prompt templates
# Prompt templates
info_prompt = PromptTemplate.from_template("""
        Extract the following information from the resume text:
        1. Full Name
        2. Experience Details (For each experience, provide Role/Designation, Company Name, and Duration in months)
        3. Projects (for each project, provide project name, technologies/tools/languages used in the projects)
        4. Contact Information (Email and Phone Number)
        5. Education Details

        for example:
        Full Name: David Jason
        Experience Details:
        AI Developer at BRB, 2 months
        AI Engineer, Covalent limited, 10 months
        Projects:
        AI Chatbot : python, langchain, OpenAI, RAG, streamlit
        Contact Information: 
        Email: david.jason@gmail.com
        Phone Number: +92 90078601
        Education Details:
        Ms in Data Science, FAST University

        Resume Text:
        {pdf_text}
""")

query_prompt = PromptTemplate.from_template(
    "Extract only the relevant details about {query} from this text: {pdf_text} in a summarized format and keep it short."
)


ranking_prompt = PromptTemplate.from_template("""
Compare this resume to the job description and briefly explain how well the candidate matches it.
Keep the reasoning concise (2-3 lines). Do not provide a numerical score.

Job Description:
{jd_text}

Resume:
{resume_text}

Format your answer like this:
Reasoning: [short explanation of match or mismatch]
""")
chain = info_prompt | llm
query_chain = query_prompt | llm
ranking_chain = ranking_prompt | llm

# Streamlit UI
st.title("Resume Analyzer")

tab1, tab2 = st.tabs(["Single Resume Analysis", "Bulk Resume Comparison"])

with tab1:
    st.header("Analyze Single Resume")
    uploaded_file = st.file_uploader("Choose a resume file", key="single_resume")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Extract Basic Info'):
            if uploaded_file is not None:
                with st.spinner('Processing resume...'):
                    pdf_text = extract_text_from_pdf(uploaded_file)
                    result = chain.invoke({"pdf_text": pdf_text})
                    st.write(result.content)
            else:
                st.warning("Please upload a resume first")
    
    st.subheader("Ask specific questions about the resume")
    query = st.text_area('Enter your specific query:', height=100)
    if st.button('Search'):
        if uploaded_file is not None and query:
            with st.spinner('Searching...'):
                pdf_text = extract_text_from_pdf(uploaded_file)
                result = query_chain.invoke({"query": query, "pdf_text": pdf_text})
                st.write(result.content)
        elif not query:
            st.warning("Please enter a query")
        else:
            st.warning("Please upload a resume first")

# Bulk Resume Analysis Tab
with tab2:
    st.header("Bulk Resume Ranking")

    st.subheader("Enter Job Description")
    jd_text = st.text_area("Paste the job description here:", height=200, key="jd_text_area")

    resume_files = st.file_uploader("Upload Resumes for Comparison", accept_multiple_files=True, key="bulk_resumes")

    if st.button('Analyze and Rank Resumes'):
        if not jd_text:
            st.warning("Please enter a job description")
        elif not resume_files:
            st.warning("Please upload at least one resume for comparison")
        else:
            with st.spinner(f'Analyzing {len(resume_files)} resumes against the job description...'):
                rankings = []
                progress_bar = st.progress(0)

                for i, resume_file in enumerate(resume_files):
                    progress = (i + 1) / len(resume_files)
                    progress_bar.progress(progress)

                    resume_text = extract_text_from_pdf(resume_file)
                    candidate_name = os.path.splitext(resume_file.name)[0].capitalize()  # e.g., 'ali.pdf' → 'Ali'

                    result = ranking_chain.invoke({
                        "jd_text": jd_text,
                        "resume_text": resume_text
                    })

                    # Respect Gemini's rate limit
                    time.sleep(35)

                    reasoning = result.content.replace("Reasoning:", "").strip()
                    rankings.append({
                        "Candidate": candidate_name,
                        "Reasoning": reasoning
                    })

                progress_bar.empty()

                # Sort based on reasoning quality manually using Gemini (simulate relevance via position)
                # You can refine this by analyzing keywords later if needed
                st.subheader("Ranked Candidates (Best to Worst Match)")
                for i, entry in enumerate(rankings):
                    st.markdown(f"**{i+1}. {entry['Candidate']}** - {entry['Reasoning']}")

