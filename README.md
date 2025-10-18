# AI Resume Analyzer 🚀

An intelligent resume analysis tool powered by multiple AI models (OpenAI GPT-4 & Google Gemini) that provides professional, actionable feedback to help job seekers optimize their resumes and stand out in the competitive job market.

## 🎯 What This Project Does

The AI Resume Analyzer is a web-based application that acts as your personal career coach, providing expert-level resume feedback in seconds. Simply upload your resume, choose your preferred AI model, optionally specify your target job role, and receive comprehensive analysis with practical recommendations for improvement. You can also ask follow-up questions to dive deeper into specific areas!

## 💡 How This Helps You

### For Job Seekers:
- **Save Time & Money**: Get instant professional feedback without waiting days or paying for expensive resume review services
- **Increase Interview Chances**: Optimize your resume for Applicant Tracking Systems (ATS) to ensure it gets seen by human recruiters
- **Role-Specific Guidance**: Receive tailored recommendations based on your target job role
- **Actionable Insights**: Get specific suggestions on how to improve, not just generic advice
- **Learn & Improve**: Understand what makes a strong resume through detailed analysis of your content
- **Interactive Q&A**: Ask follow-up questions about your resume to get clarification on any aspect

### Key Benefits:
✅ **Content Clarity Analysis** - Ensure your achievements and skills are communicated effectively  
✅ **Skills Presentation** - Optimize how you showcase your technical and soft skills  
✅ **Experience Descriptions** - Transform generic job duties into impactful accomplishments  
✅ **ATS Optimization** - Make sure your resume passes automated screening systems  
✅ **Quantifiable Achievements** - Learn how to add measurable results to strengthen your impact  
✅ **Action Verb Enhancement** - Replace weak verbs with powerful, industry-standard alternatives  
✅ **Multi-Model Support** - Choose between OpenAI GPT-4 or Google Gemini for analysis
✅ **Interactive Chat** - Ask unlimited follow-up questions about your resume

## 🛠️ Technology Stack

- **Python** - Core programming language
- **Streamlit** - Interactive web application framework
- **OpenAI GPT-4** - AI-powered resume analysis (Option 1)
- **Google Gemini** - AI-powered resume analysis (Option 2)
- **PyPDF2** - PDF text extraction
- **python-dotenv** - Environment variable management

## 🚀 Getting Started

### Prerequisites
- Python 3.12 or higher
- OpenAI API key (if using GPT-4) - Get one at [OpenAI Platform](https://platform.openai.com/)
- Google Gemini API key (if using Gemini) - Get one at [Google AI Studio](https://makersuite.google.com/app/apikey)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mfmshazan/ResumeAnalyzer.git
cd ResumeAnalyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
or if using `uv`:
```bash
uv sync
```

3. Create a `.env` file in the root directory and add your API key(s):
```
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```
*Note: You only need to add the API key for the model you plan to use*

4. Run the application:
```bash
streamlit run main.py
```
or if using `uv`:
```bash
uv run streamlit run main.py
```

5. Open your browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

## 📝 How to Use

1. **Select AI Model**: Choose between OpenAI GPT-4 or Google Gemini from the dropdown
2. **Upload Your Resume**: Click the file uploader and select your resume (PDF or TXT format)
3. **Specify Target Role** (Optional): Enter the job role you're targeting for more tailored feedback
4. **Click Analyze**: Hit the "Analyze Resume" button to generate your comprehensive report
5. **Review Feedback**: Read through the AI-generated analysis and recommendations
6. **Ask Follow-up Questions**: Use the chat interface to ask specific questions about your resume
7. **Implement Changes**: Apply the suggested improvements to your resume

## 🎨 Features

- **Multiple AI Models**: Choose between OpenAI GPT-4 or Google Gemini
- **Multi-Format Support**: Upload PDF or TXT files
- **Interactive Chat Interface**: Ask unlimited follow-up questions about your resume
- **Session Persistence**: Your resume content and chat history are maintained during the session
- **User-friendly Interface**: Clean, intuitive design powered by Streamlit
- **Fast Processing**: Instant results with streaming AI responses
- **Detailed Analysis**: Structured feedback with clear sections
- **Role-specific Recommendations**: Tailored advice based on your target job
- **Expert-level Insights**: Analysis powered by advanced AI models

## 💬 Example Follow-up Questions

After your initial analysis, you can ask questions like:
- "How can I make my skills section more impactful?"
- "What are the strongest parts of my resume?"
- "How can I better quantify my achievements in the marketing section?"
- "Is my resume optimized for ATS systems?"
- "What action verbs should I use instead of 'responsible for'?"
- "How can I tailor this resume for a senior developer position?"

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🌟 Support

If you find this project helpful, please consider giving it a star on GitHub!

## 📧 Contact

Created by [@mfmshazan](https://github.com/mfmshazan)

---

**Disclaimer**: This tool provides AI-generated suggestions and should be used as a guide. Always review and adapt the recommendations to your specific situation and ensure all information on your resume remains accurate and truthful.
