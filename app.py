import streamlit as st
from streamlit_option_menu import option_menu
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
    st.set_page_config(layout="wide")

    # Sidebar - Logo and File Upload
    with st.sidebar:
        st.image("C:/Users/HP/Desktop/ATSMaximizer/logo.jpg", use_column_width=True)
        uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    st.title("ATSMaximiser")

    # Main Menu - Home, Quick Scan, Detailed Analysis, ATS Optimization, Question Answering
    selected = option_menu(
        menu_title=None, 
        options=["Home", "Quick Scan", "Detailed Analysis", "ATS Optimization", "Question Answering"],
        icons=["house", "search", "list", "layers", "question-circle"],
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal"
    )

    # Initialize session state keys if they don't exist
    if 'response' not in st.session_state:
        st.session_state['ats_response'] = None
    if 'pdf_text' not in st.session_state:
        st.session_state['pdf_text'] = None
    
    api_key = load_api_key()
    if not api_key:
        return

    model = configure_model(api_key)
    
    if uploaded_file:
        pdf_text = read_pdf(uploaded_file)
        if not pdf_text:
            return
        st.session_state['pdf_text'] = pdf_text

    if selected == "Home":
        st.write("Welcome to ATSMaximiser! Upload your resume on the left and start analyzing.")
    
    if selected == "Quick Scan":
        st.write("Performing a Quick Scan of your resume...")
        if uploaded_file:
            if st.button("Quick Scan Now"):
                ats_response = analyze_resume(model, st.session_state['pdf_text'], "Quick Scan")
                if ats_response:
                    st.session_state['ats_response'] = ats_response
                    st.write(ats_response)

    if selected == "Detailed Analysis":
        st.write("Performing a Detailed Analysis of your resume...")
        if uploaded_file:
            if st.button("Detailed Analysis Now"):
                ats_response = analyze_resume(model, st.session_state['pdf_text'], "Detailed Analysis")
                if ats_response:
                    st.session_state['ats_response'] = ats_response
                    st.write(ats_response)

    if selected == "ATS Optimization":
        st.write("Optimizing your resume for ATS...")
        job_description = st.text_area("Paste the job description for ATS Optimization:")
        if uploaded_file and job_description:
            if st.button("Optimize Now"):
                ats_response = get_ats_optimization_response(model, st.session_state['pdf_text'], job_description)
                if ats_response:
                    st.session_state['ats_response'] = ats_response
                    st.write(ats_response)

    if selected == "Question Answering":
        st.write("Ask questions about your resume or analysis...")
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
