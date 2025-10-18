# AI Resume Analyzer 🚀

An intelligent resume analysis tool powered by OpenAI's GPT-4 that provides professional, actionable feedback to help job seekers optimize their resumes and stand out in the competitive job market.

## 🎯 What This Project Does

The AI Resume Analyzer is a web-based application that acts as your personal career coach, providing expert-level resume feedback in seconds. Simply upload your resume, optionally specify your target job role, and receive comprehensive analysis with practical recommendations for improvement.

## 💡 How This Helps You

### For Job Seekers:
- **Save Time & Money**: Get instant professional feedback without waiting days or paying for expensive resume review services
- **Increase Interview Chances**: Optimize your resume for Applicant Tracking Systems (ATS) to ensure it gets seen by human recruiters
- **Role-Specific Guidance**: Receive tailored recommendations based on your target job role
- **Actionable Insights**: Get specific suggestions on how to improve, not just generic advice
- **Learn & Improve**: Understand what makes a strong resume through detailed analysis of your content

### Key Benefits:
✅ **Content Clarity Analysis** - Ensure your achievements and skills are communicated effectively  
✅ **Skills Presentation** - Optimize how you showcase your technical and soft skills  
✅ **Experience Descriptions** - Transform generic job duties into impactful accomplishments  
✅ **ATS Optimization** - Make sure your resume passes automated screening systems  
✅ **Quantifiable Achievements** - Learn how to add measurable results to strengthen your impact  
✅ **Action Verb Enhancement** - Replace weak verbs with powerful, industry-standard alternatives  

## 🛠️ Technology Stack

- **Python** - Core programming language
- **Streamlit** - Interactive web application framework
- **OpenAI GPT-4** - AI-powered resume analysis
- **PyPDF2** - PDF text extraction
- **python-dotenv** - Environment variable management

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

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

3. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. Run the application:
```bash
streamlit run main.py
```

5. Open your browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

## 📝 How to Use

1. **Upload Your Resume**: Click the file uploader and select your resume (PDF or TXT format)
2. **Specify Target Role** (Optional): Enter the job role you're targeting for more tailored feedback
3. **Click Analyze**: Hit the "Analyze Resume" button to generate your comprehensive report
4. **Review Feedback**: Read through the AI-generated analysis and recommendations
5. **Implement Changes**: Apply the suggested improvements to your resume

## 🎨 Features

- Support for multiple file formats (PDF and TXT)
- User-friendly interface with clean design
- Fast processing and instant results
- Detailed, structured feedback with clear sections
- Role-specific recommendations
- Expert-level analysis powered by advanced AI

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
