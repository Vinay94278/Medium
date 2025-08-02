from langchain_community.document_loaders import PyPDFLoader
from exceptions.file_exception import FileException

def load_file(file):
    try:
        loader = PyPDFLoader(file)
        docs = loader.load()
        return docs
    except Exception as e:
        raise FileException(f"Error loading PDF: {e}")