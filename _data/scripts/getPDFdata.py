import PyPDF2

def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    page_obj = pdf_reader.getPage(0)
    text = page_obj.extractText()
    pdf_file_obj.close()
    return text

text = extract_text_from_pdf('path_to_your_pdf_file.pdf')

# Now you have the text of the PDF, you can use string operations or regular expressions to find the title and abstract
# This is a naive example, you might need to adjust it based on the actual structure of your PDFs
title_end = text.find('\n')
title = text[:title_end]

abstract_start = text.lower().find('abstract')
abstract_end = text.find('\n', abstract_start)
abstract = text[abstract_start:abstract_end]

print('Title:', title)
print('Abstract:', abstract)