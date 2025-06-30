from .services.pdf_to_text import extract_pdf_text
from .services.add_msg_to_history import add_msg_to_history
from .services.create_safe_cv import create_safe_cv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory


def answer_question(question: str, pdf_path: str, history: list) -> str:
    # Extract Text from PDF file
    cv_text = extract_pdf_text(pdf_path)
    # Escape curly braces in CV text to avoid prompt template KeyError
    safe_cv = create_safe_cv(cv_text)

    # Initialise the LLM model
    llm = ChatOpenAI(model="gpt-4o")
    memory = ConversationBufferMemory(return_messages=True)
    # Load history into memory
    add_msg_to_history(memory, history)

    system_msg = f"You're a helpful chatbot who answers questions about this CV (from PDF):\n{safe_cv}"
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        *[(msg["role"], msg["content"]) for msg in history],
        ("user", question)
    ])
    response = llm(prompt.format_prompt().to_messages())
    return response.content
