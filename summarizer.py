import fitz  # PyMuPDF
import docx
import requests
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access the variable
api_key = os.getenv("TOGETHER_API_KEY")

def extract_text(file):
    if file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join([page.get_text() for page in doc])
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""

def summarize_text(text, summary_type="bullet points"):
    prompt = f"Summarize the following text in {summary_type} format:\n\n{text[:3000]}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/Meta-Llama-3-70B-Instruct-Turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 400
    }

    response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=data)
    result = response.json()
    return result.get("choices", [{}])[0].get("message", {}).get("content", "No summary generated.")
