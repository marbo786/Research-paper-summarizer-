from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_file) -> str:
    """
    Extracts all text from a PDF file uploaded via Streamlit's file uploader.
    """
    reader = PdfReader(uploaded_file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
    return full_text
