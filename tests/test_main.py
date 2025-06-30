from fastapi.testclient import TestClient
from app.main import app

def test_ask_question():
    client = TestClient(app)
    response = client.post("/ask", json={"question": "What is your name?"})
    assert response.status_code == 200
    assert "answer" in response.json()
