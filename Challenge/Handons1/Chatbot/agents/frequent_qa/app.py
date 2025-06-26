from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post('/ask')
def ask_frequent_qa(q: Question):
    return {"answer": "Đây là agent Frequent QA. Chính sách bảo hành/đổi trả sẽ được trả lời ở đây."} 