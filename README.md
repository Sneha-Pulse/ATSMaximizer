# ATS Maximizer Project:

ATSMaximiser
ATSMaximiser is a Streamlit-based web application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). The tool analyzes resumes, identifies ATS-related issues, and provides actionable recommendations to improve your chances of getting shortlisted for your dream job.

Features
PDF Resume Upload:

Upload your resume in PDF format for analysis.
The app uses PyPDF2 to extract and process the text content.
Quick Scan:

Perform a brief analysis of your resume to identify key issues and strengths.
Get quick feedback on potential improvements.
Detailed Analysis:

Dive deeper into your resume's structure, keywords, and content alignment with ATS requirements.
Detailed recommendations are provided to enhance your resume's effectiveness.
ATS Optimization:

Analyze your resume against a specific job description.
Suggestions include keyword optimizations, restructuring, and ATS compatibility scoring.
Question Answering:

Ask specific questions about your resume or the analysis.
Get tailored advice and guidance based on your resume content and optimization suggestions.
Generative AI-Powered Analysis:

The app integrates with Google's Generative AI (gemini-1.5-flash) to provide intelligent, context-aware insights and recommendations.
User-Friendly Interface:

Clean and intuitive interface with horizontal navigation for easy access to different functionalities.
Sidebar for uploading resumes and additional information.
Key Technologies Used
Streamlit: For building the web application and providing an interactive user interface.
PyPDF2: To extract text from uploaded PDF resumes.
Google Generative AI: For AI-powered resume analysis and suggestions.
dotenv: To manage sensitive information like the Google API key.
Pillow (PIL): For handling image files like the logo used in the sidebar.
How It Works
1. Resume Upload
Users upload their resumes in PDF format through the sidebar. The application reads and extracts the text content using PyPDF2.

2. Google Generative AI Configuration
The app uses the dotenv library to load the Google API key from an .env file. The API key is used to configure the Generative AI model.

3. Resume Analysis Options
Users can choose from several analysis types through the horizontal navigation menu:

Quick Scan: Provides a high-level overview of the resume's quality.
Detailed Analysis: Gives an in-depth review of content, structure, and ATS alignment.
ATS Optimization: Compares the resume against a provided job description and gives actionable recommendations.
Question Answering: Allows users to ask specific questions about their resume or previous analyses.
4. Analysis Output
The app generates analysis results using AI models and displays them in an easy-to-read format. Users receive suggestions for improvement, ATS compatibility scores, and tailored keyword recommendations.

Installation and Setup
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/ATSMaximiser.git
cd ATSMaximiser
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the root directory and add your Google API key:

makefile
Copy code
GOOGLE_API_KEY=your_google_api_key
Run the Streamlit application:

bash
Copy code
streamlit run main.py
Access the app in your browser at http://localhost:8501.

File Structure
bash
Copy code
ATSMaximiser/
├── main.py                   # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env                      # Environment file for sensitive keys (not included in repo)
├── logo.jpg                  # Logo displayed in the sidebar
└── README.md                 # Project documentation
Screenshots

Description: The homepage provides an overview of ATSMaximiser and its features.


Description: The ATS Optimization page allows users to analyze their resume against a specific job description.

Future Improvements
Integration with multiple AI models for comparative analysis.
Support for additional file formats (e.g., Word documents).
Enhanced visualization for ATS scoring and recommendations.
User account management to save and track analyses over time.
Contributing
Contributions are welcome! Please open an issue or submit a pull request with your suggestions and improvements.

License
This project is licensed under the MIT License.
