from .services.load_cv_file import load_cv_file
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage

def answer_question(question: str, cv_path: str, history: list) -> str:
    cv = load_cv_file(cv_path)
    llm = ChatOpenAI(model="gpt-4o")
    memory = ConversationBufferMemory(return_messages=True)
    # Load history into memory
    for msg in history:
        if msg["role"] == "user":
            memory.chat_memory.add_message(HumanMessage(content=msg["content"]))
        else:
            memory.chat_memory.add_message(AIMessage(content=msg["content"]))
    # Escape curly braces in CV to avoid prompt template KeyError
    safe_cv = str(cv).replace("{", "{{").replace("}", "}}")
    system_msg = f"You're a helpful chatbot who answers questions about this CV:\n{safe_cv}"
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        *[(msg["role"], msg["content"]) for msg in history],
        ("user", question)
    ])
    response = llm(prompt.format_prompt().to_messages())
    return response.content
