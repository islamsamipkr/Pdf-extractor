
from pdfminer.high_level import extract_text,extract_pages

for page_layout in extract_pages("Islam, Sami.pdf"):
    for element in page_layout:
        print(element)