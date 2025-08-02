from langchain_groq import ChatGroq
from exceptions.application_exception import ApplicationException

def load_llm(api_key, model, temperature=0.7, max_tokens=4096):
    try:
        return ChatGroq(
            name="Q&A Chatbot",
            model=model,
            api_key=api_key,
            temperature=temperature,
            max_tokens=max_tokens
        )
    except Exception as e:
        raise ApplicationException(f"Error initializing LLM: {e}")