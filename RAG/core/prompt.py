from langchain_core.prompts import PromptTemplate

def load_prompt():
    template = """
    You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
    
    Question: {question} 
    Context: {context} 
    Answer:
    """
    return PromptTemplate(
        input_variables=["question", "context"],
        template=template.strip()
    )
