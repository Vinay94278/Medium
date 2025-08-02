# RAG (Retrieval-Augmented Generation) App

A modular, scalable Streamlit application for document ingestion, chunking, embedding, and retrieval using state-of-the-art LLMs via ChatGroq. Designed for flexibility, robust error handling, and easy extension.

---

## 🚀 Features

- **PDF Upload & Ingestion:** Upload one or more PDFs (≤25MB each) for processing.
- **Document Chunking:** Splits documents into manageable chunks for efficient retrieval.
- **Embeddings & Vector Store:** Embeds chunks and stores them in a Chroma vector database.
- **Dynamic LLM Selection:** Choose from multiple free ChatGroq models, set temperature, and max tokens.
- **Rate Limit Awareness:** Displays model-specific rate limits (RPM, RPD, TPM, TPD).
- **Custom Exception Handling:** Robust, extensible error handling for files, database, and application logic.
- **Configurable & Maintainable:** Centralized constants, messages, and configuration.
- **User API Key Input:** Securely enter your own ChatGroq API key.

---

## 🗂️ Project Structure

```
RAG/
│
├── app.py                  # Main Streamlit app
├── config/                 # Configuration, constants, messages
│   ├── config.py
│   ├── constants.py
│   └── messages.py
│
├── core/                   # Core logic modules
│   ├── loader.py
│   ├── splitter.py
│   ├── embedder.py
│   ├── prompt.py
│   ├── llm.py
│   └── output_parser.py
│
├── exceptions/             # Custom exception classes
│   ├── __init__.py
│   ├── application_exception.py
│   ├── database_exception.py
│   └── file_exception.py
│
├── store/                  # Chroma vector store (auto-generated)
├── docs/                   # Documentation
│   └── README.md
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
```

---

## 🏁 Getting Started

### 1. **Clone the Repository**
```sh
git clone https://github.com/yourusername/rag-app.git
cd rag-app
```

### 2. **Install Dependencies**
```sh
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. **Run the App**
```sh
streamlit run app.py
```

---

## ⚙️ Configuration

- **API Key:** Enter your ChatGroq API key in the sidebar.
- **Model Selection:** Choose from available free ChatGroq models.
- **Temperature & Max Tokens:** Adjust generation parameters in the sidebar.

---

## 🧩 Core Modules

- **`core/loader.py`**  
  Loads and parses PDF files.
- **`core/splitter.py`**  
  Splits documents into chunks for embedding.
- **`core/embedder.py`**  
  Embeds chunks and stores them in Chroma.
- **`core/prompt.py`**  
  Loads and formats prompts for the LLM.
- **`core/llm.py`**  
  Initializes the ChatGroq LLM with user parameters.
- **`core/output_parser.py`**  
  Parses and formats LLM outputs.

---

## 🛡️ Exception Handling

- **`exceptions/application_exception.py`**  
  Base class for all custom exceptions.
- **`exceptions/database_exception.py`**  
  Handles database/vector store errors.
- **`exceptions/file_exception.py`**  
  Handles file loading and parsing errors.

All exceptions are caught and displayed as user-friendly messages in the UI.

---

## 📝 Customization

- **Add More Models:**  
  Update `config/constants.py` with new models and their rate limits.
- **Change Chunk Size:**  
  Adjust `CHUNK_SIZE` and `CHUNK_OVERLAP` in `constants.py`.
- **Extend Exception Handling:**  
  Add new exception classes in `exceptions/`.

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 🙋 FAQ

**Q:** Why do I get a "dimension mismatch" error?  
**A:** Delete the `store/` directory if you change embedding models.

**Q:** How do I add a new LLM?  
**A:** Add it to `config/constants.py` and update the sidebar logic in `app.py`.

---

## 📬 Contact

For questions or support, open an issue