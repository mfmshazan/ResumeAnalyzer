import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT )", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role yor are targetting (optional)")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text=""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
            return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
             st.error("File does not have any content")
             st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback.
        Focus on the following aspects
        1. Content clarity and impact
        2. Skills presentations
        3. Experience descriptions
        4. Specific improvement for {job_role if job_role else 'general job applications'}

        Resume contentL
        {file_content}

        Please provide your analysis in a clear ,structured format with specific recommadtions"""

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                 {"role": "system", "content":"You are an expert resume reviwer with years of experience in HR and recruiment."},
                 {"role": "user", "content": prompt}
            ]          
             )     
        
    except:   