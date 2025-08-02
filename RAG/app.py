import streamlit as st
from config import *
from config.constants import *
from config.messages import SUCCESS, ERROR
from core.loader import load_file
from core.splitter import split_documents
from core.embedder import embed_and_index
from core.prompt import load_prompt
from core.llm import load_llm
from core.outputParser import load_parser
from exceptions.file_exception import FileException

st.set_page_config(page_title="RAG Document Ingestion", layout="wide")
st.title("📚 RAG Application")

# --- Sidebar Configuration ---
with st.sidebar:
    st.sidebar.title("⚙️ Configuration")

    api_key = st.text_input("Enter your Groq API Key", type="password")

    uploaded_files = st.file_uploader(
        "Upload PDF (≤25 MB)", type="pdf", accept_multiple_files=True
    )

    # Advanced options collapsible
    with st.expander("Advanced Options"):
        model_options = {v["label"]: v["model"] for v in FREE_CHATGROQ_MODELS.values()}
        selected_label = st.selectbox("Select ChatGroq Model", list(model_options.keys()))
        selected_model = model_options[selected_label]
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
        max_tokens = st.number_input("Max Tokens", min_value=256, max_value=4096, value=4096, step=64)

    # Info button at the end
    if st.button("ℹ️ Info"):
        st.info(
            f"**Application Flow:**\n"
            f"1. Upload PDFs (≤25MB each)\n"
            f"2. Documents are chunked and embedded\n"
            f"3. Chunks are indexed for retrieval\n"
            f"4. Ask questions and get answers from your documents\n\n"
            f"**Current Stats:**\n"
            f"- Total Docs: {st.session_state.get('total_docs', 0)}\n"
            f"- Total Chunks: {st.session_state.get('total_chunks', 0)}\n\n"
   
            f"**Understanding Rate Limits**\n"
            f"Rate limits are measured in:\n"
            f"1. RPM: Requests per minute\n"
            f"2. RPD: Requests per day\n"
            f"3. TPM: Tokens per minute\n"
            f"4. TPD: Tokens per day\n"
            f"5. ASH: Audio seconds per hour\n"
            f"6. ASD: Audio seconds per day\n"
        )

if not api_key:
    st.sidebar.warning(ERROR["GROQ_API_WARNING"])
    st.stop()

if not uploaded_files:
    st.sidebar.info(ERROR["NO_FILE"])
    st.stop()

documents = []
for uploaded_file in uploaded_files:
    if uploaded_file.size > MAX_FILE_SIZE:
        st.sidebar.error(ERROR["FILE_TOO_LARGE"])
        st.stop()
    try:
        with open(TEMP_PDF_PATH, "wb") as file:
            file.write(uploaded_file.getvalue())
        docs = load_file(TEMP_PDF_PATH)
        documents.extend(docs)
    except FileException as fe:
        st.sidebar.error(str(fe))
        st.stop()
    except Exception as e:
        st.sidebar.error(ERROR["UNKNOWN"].format(error=str(e)))
        st.stop()

# Chunking with progress
with st.spinner("Splitting documents into chunks..."):
    chunks = split_documents(documents, CHUNK_SIZE, CHUNK_OVERLAP)
st.success(SUCCESS["CHUNKS_GENERATED"].format(count=len(chunks)))

# Save stats in session for sidebar info
st.session_state['total_docs'] = len(documents)
st.session_state['total_chunks'] = len(chunks)

# Embedding with progress
if "vectorstore" not in st.session_state:
    with st.spinner("Embedding and indexing chunks..."):
        st.session_state.vectorstore = embed_and_index(chunks, EMBED_MODEL)
    st.success(SUCCESS["EMBEDDING_SUCCESS"])

retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 5})
st.success(SUCCESS["READY_FOR_RETRIEVAL"])

def load_context(user_input):
    list_context = retriever.invoke(user_input)
    return "\n".join([context.page_content for context in list_context])

prompt = load_prompt()
try:
    llm = load_llm(api_key, selected_model, temperature, max_tokens)
except Exception as e:
    st.sidebar.error(str(e))
    st.stop()
parser = load_parser()
rag = prompt | llm | parser

user_input = st.text_input("Your question:")
if user_input:
    context = load_context(user_input)
    try:
        response = rag.invoke({'question': user_input, 'context': context})
        st.write(response)
    except Exception as e:
        st.error(ERROR["UNKNOWN"].format(error=str(e)))