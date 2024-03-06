import PyPDF2
from transformers import pipeline

import format_converter
import format_detector

qa_pipeline = pipeline('question-answering', model='bert-large-uncased-whole-word-masking-finetuned-squad')

path = input("Enter the path to the document: ")

if format_detector.format_detector(path)[:3] != 'PDF':
    format_converter.format_converter(path)
    with open('data.pdf', 'rb') as file:
        pdf_content = file.read()
        path = 'data.pdf'
else:
    with open(path, 'rb') as file:
        pdf_content = file.read()


def convert_pdf_to_text(pdf_content):
    pdf_text = ""
    with open(path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()
    return pdf_text


query = input("Enter your question: ")
result = qa_pipeline(question=query, context=convert_pdf_to_text(pdf_content))

print(result['answer'])
