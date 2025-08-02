from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from exceptions.database_exception import DatabaseException
from config.constants import VECTOR_STORE_DIR

def embed_and_index(chunks, model_name):
    """Generate embeddings and create a vectorstore."""
    try:
        emb = HuggingFaceEmbeddings(model_name=model_name)
        return Chroma.from_documents(chunks, embedding=emb, persist_directory=VECTOR_STORE_DIR)
    except Exception as e:
        raise DatabaseException(f"Error during embedding: {e}")