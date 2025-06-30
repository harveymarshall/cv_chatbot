from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.llm_interface import answer_question
from pydantic import BaseModel
from typing import List

CV_JSON_PATH = './app/cv_data/cv.json'

app = FastAPI()

class Message(BaseModel):
    role: str  # 'user' or 'assistant'
    content: str

class ChatRequest(BaseModel):
    question: str
    history: List[Message] = []

@app.post("/ask")
def ask_question(req: ChatRequest):
    answer = answer_question(req.question, CV_JSON_PATH, [msg.dict() for msg in req.history])
    return {"answer": answer}

# Mount static files LAST so /ask and other API routes work
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
