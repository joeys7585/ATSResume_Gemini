# 📄 AI Resume Optimizer (Streamlit + Gemini 2.5 Flash)

An interactive, AI-powered resume optimizer that uses **Google Gemini 2.5 Flash** and **spaCy NLP** to:

✅ Enhance your resume  
✅ Rate it against a job description  
✅ Optimize it for ATS (Applicant Tracking Systems)

Built with **Streamlit**, **spaCy**, and **Gemini AI**, this tool helps job seekers tailor their resumes for better results.

---

## ✨ Features

- 🧠 **AI Resume Enhancement** (Gemini 2.5 Flash)
- 📊 **ATS Match Scoring** (spaCy keyword overlap)
- 🤖 **AI Feedback** on resume quality and relevance
- 🔍 **Keyword Optimization** Suggestions
- 🆚 **Visual Resume Diff** (see changes made by AI)
- 📄 Upload `.docx` resumes and `.txt` job descriptions

---

## 📦 Installation

### 1. Clone the repository
```
git clone https://github.com/yourusername/ai-resume-optimizer.git
cd ai-resume-optimizer
```

### 2. Install dependencies
```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Create a `.env` file

Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your-gemini-api-key-here
```

> 🔐 **Important:** Never commit your `.env` file to GitHub. Add it to `.gitignore`.

---

## ▶️ Running the App
```
streamlit run app.py
```

1. Upload your resume (`.docx`) and job description (`.txt`)
2. Choose an action:
   - Enhance Resume
   - Rate Resume
   - Optimize Resume
3. View:
   - Enhanced resume
   - ATS keyword match score
   - AI feedback
   - Keyword suggestions
   - Resume diff view

---

## 🧠 Technologies Used

| Tool                 | Purpose                           |
|----------------------|------------------------------------|
| [Streamlit](https://streamlit.io/) | Web UI |
| [spaCy](https://spacy.io/) | NLP for keyword extraction |
| [docx2txt](https://pypi.org/project/docx2txt/) | Resume parsing |
| [Google Generative AI](https://ai.google.dev/) | Gemini 2.5 Flash |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Load API key from `.env` |
| [difflib](https://docs.python.org/3/library/difflib.html) | Show resume changes |

---

## 📁 Project Structure
```
.
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── .env # Gemini API key (not committed)
├── README.md # Project documentation

```
---

## 🔒 Security

- ✅ API key is stored in a `.env` file (never hardcoded)
- ✅ `.env` should be added to `.gitignore`
- ❌ Never commit your API key to public repositories

---

## 📌 Roadmap / Future Features

- [ ] Export enhanced resume as `.docx`
- [ ] Support for `.pdf` resumes
- [ ] Downloadable feedback/report
- [ ] Deploy to Streamlit Cloud or Render

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

MIT License © 2025 [Your Name]

---

## 🙌 Acknowledgements

- Google Gemini AI
- Streamlit
- spaCy
- Python Community

---

## 🚀 Ready to Land Your Dream Job?

Start optimizing your resume today with the power of AI!  
**Run the app → Upload → Enhance → Apply!**
