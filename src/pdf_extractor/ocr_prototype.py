import re
from pdf2image import convert_from_path
import pytesseract

def extract_total_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        print(f"[DEBUG] Page {i+1} OCR Output:\n{text}\n")

        match = re.search(r"Total\s*:?\s*([\d.,]+)\s*(EUR|€)", text, re.IGNORECASE)
        if match:
            total_value = match.group(1)
            print(f"Total value found: {total_value} EUR")
            return total_value
    print("Total value not found.")
    return None

extract_total_from_pdf("docs/dummy_delivery.pdf")
