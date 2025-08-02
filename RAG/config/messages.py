SUCCESS = {
    "UPLOAD_SUCCESS": "✅ File uploaded successfully.",
    "CHUNKS_GENERATED": "✅ {count} chunks generated.",
    "EMBEDDING_SUCCESS": "✅ Document embedded and indexed in vector store.",
    "READY_FOR_RETRIEVAL": "✅ Ingestion & indexing pipeline is ready for retrieval."
}

ERROR = {
    "FILE_TOO_LARGE": f"🚫 Only PDFs up to 25 MB allowed.",
    "NO_FILE": "🚫 No file uploaded. Please upload a PDF to begin.",
    "LOAD_ERROR": "🚫 Error loading PDF: {error}",
    "EMBEDDING_ERROR": "🚫 Error during embedding: {error}",
    "UNKNOWN": "🚫 An unknown error occurred: {error}",
    "GROQ_API_WARNING":"Please enter your Groq API Key to continue.",
    "HUGGINGFACE_API_WARNING":"Please enter your Hugging Face API Key to continue.",
    "HUGGINGFACE_API_ERROR": "🚫 Error with Hugging Face API: {error}",
}