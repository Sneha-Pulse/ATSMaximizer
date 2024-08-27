import streamlit as st
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

@st.cache_data
def read_pdf(uploaded_file):
    try:
        pdf_reader = PdfReader(uploaded_file)
        pdf_text = ""
        for page in pdf_reader.pages: 
            pdf_text += page.extract_text()
        return pdf_text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

def load_api_key():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("API key not found. Please check your environment variables.")
        return None
    return api_key

def configure_model(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")

def analyze_resume(model, pdf_text, analysis_type):
    try:
        prompt = f"Analyze this resume for {analysis_type}:\n\n{pdf_text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return None

def get_ats_optimization_response(model, pdf_text, job_description):
    prompt = f"""
    You are ResumeChecker, an expert in ATS optimization. Analyze the following resume and provide optimization suggestions:
    
    1. Identify keywords from the job description that should be included in the resume.
    2. Suggest reformatting or restructuring to improve ATS readability.
    3. Recommend changes to improve keyword density without keyword stuffing.
    4. Provide 3-5 bullet points on how to tailor this resume for the specific job description.
    5. Give an ATS compatibility score out of 100 and explain how to improve it.
    
    Resume text: {pdf_text}
    Job description: {job_description}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating ATS optimization response: {e}")
        return None

def main():
    st.title("ResumeATS Pro")
    
    # Initialize session state keys if they don't exist
    if 'response' not in st.session_state:
        st.session_state['ats_response'] = None
    if 'pdf_text' not in st.session_state:
        st.session_state['pdf_text'] = None
    
    api_key = load_api_key()
    if not api_key:
        return

    model = configure_model(api_key)
    
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    if uploaded_file:
        pdf_text = read_pdf(uploaded_file)
        if not pdf_text:
            return
        st.session_state['pdf_text'] = pdf_text

    job_description = st.text_area("Paste the job description for ATS Optimization:")
    analysis_option = st.radio("Choose analysis type:", ["Quick Scan", "Detailed Analysis", "ATS Optimization"])
    
            
    if st.button("Analyze Resume"):
        if uploaded_file is not None:
            with st.spinner('Analyzing resume...'):
                if job_description and analysis_option == "ATS Optimization":
                    ats_response = get_ats_optimization_response(model, pdf_text, job_description)
                else:
                    ats_response = analyze_resume(model, pdf_text, analysis_option)
                if ats_response:
                    st.session_state['ats_response'] = ats_response
                    st.write(ats_response)
    
    user_question = st.text_input("Ask me anything about your resume or the analysis:")
    if user_question:
        chat_prompt = f"""
        Based on the resume and analysis above, answer the following question:
        {user_question}
        
        Resume text: {st.session_state['pdf_text']}
        Previous analysis: {st.session_state['ats_response']}
        """
        chat_response = analyze_resume(model, chat_prompt, "Custom Question")
        if chat_response:
            st.write(chat_response)

if __name__ == "__main__":
    main()
