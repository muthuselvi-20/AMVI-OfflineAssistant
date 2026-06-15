from pypdf import PdfReader

def pdf_reader(path):
    text = " "
    reader = PdfReader(path)
    for page_no in range(len(reader.pages)):
        page = reader.pages[page_no]
        text += page.extract_text()

    return text
