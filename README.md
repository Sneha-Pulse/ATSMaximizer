# ATS Maximizer


**ATSMaximiser** is a Streamlit-based web application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). The tool analyzes resumes, identifies ATS-related issues, and provides actionable recommendations to improve your chances of getting shortlisted for your dream job.

## Features

1. **PDF Resume Upload**: 
   - Upload your resume in PDF format for analysis.
   - The app uses `PyPDF2` to extract and process the text content.

2. **Quick Scan**:
   - Perform a brief analysis of your resume to identify key issues and strengths.
   - Get quick feedback on potential improvements.

3. **Detailed Analysis**:
   - Dive deeper into your resume's structure, keywords, and content alignment with ATS requirements.
   - Detailed recommendations are provided to enhance your resume's effectiveness.

4. **ATS Optimization**:
   - Analyze your resume against a specific job description.
   - Suggestions include keyword optimizations, restructuring, and ATS compatibility scoring.

5. **Question Answering**:
   - Ask specific questions about your resume or the analysis.
   - Get tailored advice and guidance based on your resume content and optimization suggestions.

6. **Generative AI-Powered Analysis**:
   - The app integrates with Google's Generative AI (`gemini-1.5-flash`) to provide intelligent, context-aware insights and recommendations.

7. **User-Friendly Interface**:
   - Clean and intuitive interface with horizontal navigation for easy access to different functionalities.
   - Sidebar for uploading resumes and additional information.

## Key Technologies Used

- **[Streamlit](https://streamlit.io/)**: For building the web application and providing an interactive user interface.
- **[PyPDF2](https://pypi.org/project/PyPDF2/)**: To extract text from uploaded PDF resumes.
- **[Google Generative AI](https://ai.google/)**: For AI-powered resume analysis and suggestions.
- **[dotenv](https://pypi.org/project/python-dotenv/)**: To manage sensitive information like the Google API key.
- **[Pillow (PIL)](https://pypi.org/project/Pillow/)**: For handling image files like the logo used in the sidebar.

## How It Works

### 1. Resume Upload
Users upload their resumes in PDF format through the sidebar. The application reads and extracts the text content using `PyPDF2`.

### 2. Google Generative AI Configuration
The app uses the `dotenv` library to load the Google API key from an `.env` file. The API key is used to configure the Generative AI model.

### 3. Resume Analysis Options
Users can choose from several analysis types through the horizontal navigation menu:
- **Quick Scan**: Provides a high-level overview of the resume's quality.
- **Detailed Analysis**: Gives an in-depth review of content, structure, and ATS alignment.
- **ATS Optimization**: Compares the resume against a provided job description and gives actionable recommendations.
- **Question Answering**: Allows users to ask specific questions about their resume or previous analyses.

### 4. Analysis Output
The app generates analysis results using AI models and displays them in an easy-to-read format. Users receive suggestions for improvement, ATS compatibility scores, and tailored keyword recommendations.

## Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ATSMaximiser.git
   cd ATSMaximiser
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

4. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```

5. Access the app in your browser at `http://localhost:8501`.

## File Structure

```
ATSMaximiser/
├── main.py                   # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env                      # Environment file for sensitive keys (not included in repo)
├── logo.jpg                  # Logo displayed in the sidebar
└── README.md                 # Project documentation
```

## Screenshots

![image](https://github.com/user-attachments/assets/beae719a-9608-47ca-8bf1-0e294694a834)
*Description: The ATS Optimization page allows users to analyze their resume against a specific job description.*

## Future Improvements

- Integration with multiple AI models for comparative analysis.
- Support for additional file formats (e.g., Word documents).
- Enhanced visualization for ATS scoring and recommendations.
- User account management to save and track analyses over time.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your suggestions and improvements.
