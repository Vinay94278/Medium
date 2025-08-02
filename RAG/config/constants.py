MAX_FILE_SIZE_MB = 25
MAX_FILE_SIZE = MAX_FILE_SIZE_MB * 1024 * 1024

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

EMBED_MODEL = "sentence-transformers/all-mpnet-base-v2"
VECTOR_STORE_DIR = "store"
TEMP_PDF_PATH = "./temp.pdf"

RAG_DIR = "RAG"
APP_FILE = "app.py"
CONFIG_FILE = "config.py"
CONSTANTS_FILE = "constants.py"
MESSAGES_FILE = "messages.py"
REQUIREMENTS_FILE = "requirements.txt"

LOADER_FILE = "loader.py"
SPLITTER_FILE = "splitter.py"
EMBEDDER_FILE = "embedder.py"
PROMPT_FILE = "prompt.py"
LLM_FILE = "llm.py"
OUTPUT_PARSER_FILE = "output_parser.py"

EXCEPTIONS_DIR = "exceptions"
APPLICATION_EXCEPTION_FILE = "application_exception.py"
DATABASE_EXCEPTION_FILE = "database_exception.py"
FILE_EXCEPTION_FILE = "file_exception.py"

FREE_CHATGROQ_MODELS = {
    "llama3-70b": {
        "label": "Llama 3 70B",
        "model": "llama3-70b-8192",
        "rpm": 30,
        "rpd": 14400,
        "tpm": 6000,
        "tpd": 500000,
    },
    "deepseek-70b": {
        "label": "DeepSeek R1 Distill LLaMA 70B",
        "model": "deepseek-r1-distill-llama-70b",
        "rpm": 30,
        "rpd": 1000,
        "tpm": 6000,
        "tpd": 100000,
    },
    "moonshot-kimi-k2": {
        "label": "Kimi K2 Instruct",
        "model": "moonshotai/kimi-k2-instruct",
        "rpm": 60,
        "rpd": 1000,
        "tpm": 10000,
        "tpd": 300000,
    },
    "gemma2-9b": {
        "label": "Gemma 2 9B IT",
        "model": "gemma2-9b-it",
        "rpm": 30,
        "rpd": 14400,
        "tpm": 15000,
        "tpd": 500000,
    },
    "qwen3-32b": {
        "label": "Qwen 3 32B",
        "model": "qwen/qwen3-32b",
        "rpm": 60,
        "rpd": 1000,
        "tpm": 6000,
        "tpd": 500000,
    },
}
