# 🧠 SimpleExplainer.AI

> An AI-powered code tutor that transforms complex source code into simple, plain-English explanations, analyzes algorithmic complexity, and generates interactive quizzes to strengthen programming concepts.

---

## 📸 Overview

SimpleExplainer.AI is an educational web application built with **Streamlit** and **Google Gemini 2.5 Flash**. It helps students and developers understand unfamiliar code by providing AI-generated explanations, complexity analysis, optimization suggestions, and interactive quizzes.

The application uses **chatbot.py** as the AI engine for code analysis and quiz generation.

---

## ✨ Features

- 📝 **Plain-English Code Explanation**
  - Converts complex code into easy-to-understand language.

- 🔍 **Line-by-Line Breakdown**
  - Explains each logical block of the code.

- ⏱️ **Time & Space Complexity Analysis**
  - Estimates Big-O Time and Space Complexity.

- 💡 **Optimization Suggestions**
  - Provides recommendations to improve code readability and efficiency.

- 🧠 **AI-Generated Interactive Quiz**
  - Automatically creates multiple-choice questions based on the uploaded code.

- 📊 **Modern Streamlit Dashboard**
  - Clean and responsive interface with tabs, metrics, progress indicators, and interactive components.

- ⚡ **Session State Management**
  - Preserves analysis results and quiz progress during the session.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12+ | Backend |
| Streamlit | Web Interface |
| Google Gemini 2.5 Flash | AI Code Analysis |
| Pydantic | Structured Data Validation |
| python-dotenv | Environment Variable Management |

---

## 📂 Project Structure

```text
SimpleExplainerAI/
│
├── app.py                 # Streamlit User Interface
├── chatbot.py             # AI Analysis & Quiz Generation
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/bhanusiingh/SimpleChatbot.git
cd SimpleChatbot
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

### 5. Run the Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Paste any code snippet into the editor.
2. Click **Analyze Code**.
3. The AI:
   - Detects the programming language.
   - Generates a plain-English explanation.
   - Estimates Time and Space Complexity.
   - Explains each logical block of the code.
   - Suggests possible improvements.
4. Switch to the **Quiz** tab to test your understanding with AI-generated multiple-choice questions.

---

## 🎯 Example Output

- ✅ Programming Language Detection
- ✅ Plain-English Summary
- ✅ Time & Space Complexity Analysis
- ✅ Line-by-Line Code Explanation
- ✅ Code Optimization Suggestions
- ✅ AI-Generated Quiz
- ✅ Quiz Score & Detailed Feedback

---

## 📦 Requirements

- Python 3.12 or later
- Streamlit
- Google Gemini API Key
- Internet Connection

---

## 🔮 Future Improvements

- 📁 Upload Source Code Files (.py, .cpp, .java, .js)
- 🌙 Dark Mode
- 📄 Export Analysis as PDF
- 📈 Complexity Visualization
- 💬 AI Chat for Follow-up Questions
- 🎙️ Voice-Based Code Explanation
- 🌍 Multi-Language Support
- 📊 Code Quality Scoring

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Bhanu Pratap Singh**

GitHub: https://github.com/bhanusiingh
