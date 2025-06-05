# 📄 GPT-Powered Document Summarizer Interface

This is a Python-based tool that reads documents (`.txt`, `.pdf`, `.docx`) and summarizes their content using GPT models from [Together.ai](https://together.ai/). It supports both CLI and simple Streamlit-based Web UI.

---

## 🚀 Features

- 📂 Supports `.txt`, `.pdf`, and `.docx` files
- 🧠 Summarizes content using **Meta Llama 3.3 70B Instruct Turbo** or **EXAONE models** via Together.ai API
- ✅ Choose summary format: short, bullet points, or long
- 🌐 Optional Streamlit web UI for easy interaction
- 🧩 Modular code using functions and templates

---

## 🛠 Requirements

- Python 3.8+
- Together.ai **Free API Key**
- Internet connection

---

## 📦 Installation

1. **Clone the repository**
```bash
https://github.com/Gauravv191/Document_Summarizer
cd document-summarizer

2. Create .env file and add your Together.ai API key
Create a file named .env in the project root:

TOGETHER_API_KEY=your_api_key_here

3. Install dependencies
pip install -r requirements.txt

4.  Web UI (Streamlit)
streamlit run app.py

📁 Sample Files
Sample .txt, .pdf, and .docx files are provided in the /samples directory for quick testing.

** 📂 Project Structure

document_summarizer/
├── app.py                  # Streamlit Web App
├── summarizer.py          # Summarization logic (API call + formatting)
├── sample_files/          # Example input files
├── requirements.txt       # Project dependencies
├── .env                   # API Key (excluded from GitHub)
└── README.md              # Project documentation
