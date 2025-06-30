from langchain.schema import HumanMessage, AIMessage


def add_msg_to_history(memory, history: list):
    for msg in history:
        if msg["role"] == "user":
            memory.chat_memory.add_message(HumanMessage(content=msg["content"]))
        else:
            memory.chat_memory.add_message(AIMessage(content=msg["content"]))
