import streamlit as st
from langchain.prompts import PromptTemplate
import PyPDF2
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Load the API key from environment variables for security
#google_api_key = os.getenv("GOOGLE_API_KEY")
google_api_key = "AIzaSyB2d8VnVd4S4PR6J26OV7oWfzaALQQULMI" 
if google_api_key is None:
    st.error("Google API key not found. Please set it as an environment variable.")
else:
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)

def extract_text_from_pdf(uploaded_file):
    text = ""
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
    return text

info_prompt = PromptTemplate.from_template(
    "Evaluate the relevance of the following resume to this job description: {job_desc}. Resume text: {resume_text}"
)
chain = info_prompt | llm

st.title("Resume Relevance to Job Description")

uploaded_resumes = st.file_uploader("Choose resume files", accept_multiple_files=True, type=["pdf"])
job_description_text = st.text_area("Enter job description")

if st.button('Process'):
    if uploaded_resumes and job_description_text:
        relevance_scores = []
        for resume_file in uploaded_resumes:
            with st.spinner(f'Extracting text from {resume_file.name}...'):
                resume_text = extract_text_from_pdf(resume_file)
            if resume_text:
                with st.spinner(f'Analyzing relevance of {resume_file.name}...'):
                    result = chain.invoke({"job_desc": job_description_text, "resume_text": resume_text})
                    relevance_scores.append((resume_file.name, result.content))
            else:
                st.error(f"Failed to extract text from {resume_file.name}.")
        
        st.subheader("Relevance Scores:")
        for resume_name, score in relevance_scores:
            st.write(f"{resume_name}: {score}")
    else:
        st.error("Please upload resumes and provide a job description.")
