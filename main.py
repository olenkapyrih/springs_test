from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

import format_converter
import format_detector

path = input('Enter a path to the file: ')

if format_detector.format_detector(path)[:3] != 'PDF':
    format_converter.format_converter(path)
    loader = PyPDFLoader('data.pdf')
else:
    loader = PyPDFLoader(path)

document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=500,
    length_function=len,
    add_start_index=True
)

chunks = text_splitter.split_documents(document)
document = chunks[1]

print(document.page_content)
