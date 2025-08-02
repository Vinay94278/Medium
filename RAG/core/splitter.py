from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(docs, chunk_size, overlap):
    """Split docs into manageable chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=overlap
    )
    return splitter.split_documents(docs)
