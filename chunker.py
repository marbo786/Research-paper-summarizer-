import fitz  # PyMuPDF

def read_pdf(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        full_text = ""

        for page in doc:
            text = page.get_text("text")
            # Optional: strip whitespace and remove repeated line breaks
            cleaned = "\n".join([line.strip() for line in text.split("\n") if line.strip()])
            full_text += cleaned + "\n\n"

        doc.close()
        return full_text.strip()
    
    except Exception as e:
        return f"Error reading PDF: {e}"
