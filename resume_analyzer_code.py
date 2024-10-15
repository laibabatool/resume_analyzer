import streamlit as st
from langchain.prompts import PromptTemplate
import PyPDF2
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key = "AIzaSyB2d8VnVd4S4PR6J26OV7oWfzaALQQULMI")


def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = PyPDF2.PdfReader(uploaded_file)
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

#query = st.text_input('Enter your query:') # The specific information you want to extract

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

query_prompt = PromptTemplate.from_template("Extract specific information about {query} from the following text: {pdf_text}")
chain = info_prompt | llm
query_chain = query_prompt | llm

st.title("PDF Information Extraction")
uploaded_file = st.file_uploader("Choose a file")

if st.button('process'):
    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        result = chain.invoke({"pdf_text": pdf_text})
        st.write(result.content)

query = st.text_input('Enter your query:') # The specific information you want to extract
if st.button('Search'):
   if uploaded_file is not None:
      pdf_text = extract_text_from_pdf(uploaded_file)
      result = query_chain.invoke({"query":query,"pdf_text": pdf_text})
      st.write(result.content)
