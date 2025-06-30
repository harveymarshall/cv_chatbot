from docx import Document
from fpdf import FPDF
import os

def docx_to_pdf(docx_path: str, pdf_path: str) -> None:
    """
    Convert a .docx file to a simple PDF using fpdf.
    This is a basic implementation and may not preserve all formatting.
    """
    doc = Document(docx_path)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            pdf.multi_cell(0, 10, text)
    pdf.output(pdf_path)

# Example usage:
# docx_to_pdf("/path/to/input.docx", "/path/to/output.pdf")
