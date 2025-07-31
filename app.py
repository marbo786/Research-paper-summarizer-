import streamlit as st
from pdfreader import extract_text_from_pdf
from chunker import chunk_text
from summarizer import summarize_text

st.title("📄 Research Paper Summarizer Framework")

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type=["pdf"])

if uploaded_file:
    raw_text = extract_text_from_pdf(uploaded_file)
    chunks = chunk_text(raw_text)

    st.subheader("🔍 Summary")
    full_summary = ""
    for chunk in chunks:
        try:
            summary = summarize_text(chunk)
            st.markdown(f"- {summary}")
            full_summary += summary + "\n"
        except Exception as e:
            st.error(f"❌ Error: {e}")

    st.download_button("📥 Download Full Summary", full_summary)
