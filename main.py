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
job_role = st.text_input("Enter the job role you are targetting (optional)")

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
        4. Tailored recommendations for improvement based on the target job role: {job_role if job_role else 'general job applications'}
        5. Suggestions for quantifiable achievements, stronger action verbs, and ATS (Applicant Tracking System) optimization

        Resume contentL
        {file_content}

        Please structure your analysis with clear sections and actionable recommendations for each area"""

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [
                 {"role": "system", "content":"You are an expert resume reviwer with years of experience in HR and recruiment."},
                 {"role": "user", "content": prompt}
            ],     
            temperature=0.7,
            max_tokens=1000     
            )
        
        st.markdown(response.choices[0].message.content)
        
    except Exception as e:
         st.error(f"An error occured: {str(e)}")   