import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

# Initialize session state for chat history and resume content
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'resume_content' not in st.session_state:
    st.session_state.resume_content = None
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False
if 'job_role' not in st.session_state:
    st.session_state.job_role = ""

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# AI Model Selection
ai_model = st.selectbox(
    "Select AI Model",
    ["OpenAI GPT-4", "Google Gemini"],
    help="Choose which AI model to use for analysis and questions"
)

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are targeting (optional)", value=st.session_state.job_role)

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

def get_ai_response(prompt, model_choice, system_message="You are an expert resume reviewer with years of experience in HR and recruitment."):
    """Get response from selected AI model"""
    try:
        if model_choice == "OpenAI GPT-4":
            if not OPENAI_API_KEY:
                return "Error: OpenAI API key not found. Please add it to your .env file."
            
            client = OpenAI(api_key=OPENAI_API_KEY)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content
        
        elif model_choice == "Google Gemini":
            if not GEMINI_API_KEY:
                return "Error: Gemini API key not found. Please add it to your .env file."
            
            genai.configure(api_key=GEMINI_API_KEY)
            # Use the stable Gemini 2.5 Flash model
            model = genai.GenerativeModel('models/gemini-2.5-flash')
            full_prompt = f"{system_message}\n\n{prompt}"
            response = model.generate_content(full_prompt)
            return response.text
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main Analysis Section
if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content")
            st.stop()

        # Store resume content and job role in session state
        st.session_state.resume_content = file_content
        st.session_state.job_role = job_role
        st.session_state.analysis_done = True
        st.session_state.chat_history = []  # Reset chat history on new analysis

        prompt = f"""Please analyze this resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentations
        3. Experience descriptions
        4. Tailored recommendations for improvement based on the target job role: {job_role if job_role else 'general job applications'}
        5. Suggestions for quantifiable achievements, stronger action verbs, and ATS (Applicant Tracking System) optimization

        Resume content:
        {file_content}

        Please structure your analysis with clear sections and actionable recommendations for each area."""

        with st.spinner(f"Analyzing your resume with {ai_model}..."):
            analysis = get_ai_response(prompt, ai_model)
        
        st.markdown("### 📊 Resume Analysis")
        st.markdown(analysis)
        
        # Add to chat history
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": analysis
        })
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Chat Interface for Follow-up Questions
if st.session_state.analysis_done and st.session_state.resume_content:
    st.markdown("---")
    st.markdown("### 💬 Ask Follow-up Questions")
    st.markdown("Have more questions about your resume? Ask away!")
    
    # Display chat history (excluding the initial analysis)
    for i, message in enumerate(st.session_state.chat_history[1:], 1):
        if message["role"] == "user":
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**AI:** {message['content']}")
    
    # Chat input
    user_question = st.text_input(
        "Your question:",
        key="user_question",
        placeholder="e.g., How can I make my skills section more impactful?"
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        ask_button = st.button("Ask")
    with col2:
        clear_chat = st.button("Clear Chat History")
    
    if clear_chat:
        st.session_state.chat_history = st.session_state.chat_history[:1]  # Keep only initial analysis
        st.rerun()
    
    if ask_button and user_question:
        # Create context-aware prompt
        context_prompt = f"""Based on this resume:
        
{st.session_state.resume_content}

Target job role: {st.session_state.job_role if st.session_state.job_role else 'general applications'}

User's question: {user_question}

Please provide a helpful, specific answer based on the resume content."""

        with st.spinner(f"Getting answer from {ai_model}..."):
            answer = get_ai_response(context_prompt, ai_model)
        
        # Add to chat history
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_question
        })
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer
        })
        
        st.rerun()
   