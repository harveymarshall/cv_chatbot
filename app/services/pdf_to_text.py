import PyPDF2

def extract_pdf_text(pdf_path: str) -> str:
    """
    Extract all text from a PDF file and return as a single string.
    """
    text = []
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return '\n'.join(text)
