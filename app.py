import streamlit as st
from summarizer import extract_text, summarize_text

st.title("📄 GPT-Powered Document Summarizer")

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "txt", "docx"])
summary_type = st.selectbox("Choose summary type", ["short", "long", "bullet"])

if uploaded_file:
    raw_text = extract_text(uploaded_file)
    if raw_text:
        summary = summarize_text(raw_text, summary_type)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.error("Unable to extract text.")
