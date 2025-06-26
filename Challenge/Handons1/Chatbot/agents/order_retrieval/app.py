from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

class OrderStatusRequest(BaseModel):
    order_code: str

@app.post('/ask')
def ask_order(q: Question):
    return {"answer": "Đây là agent đơn hàng. Sẽ trả lời về đơn hàng."}

@app.post('/order_status')
def order_status(req: OrderStatusRequest):
    # Dummy: Gọi tool tra cứu đơn hàng (sẽ hoàn thiện sau)
    return {"order_code": req.order_code, "status": "Đơn hàng đang được chuẩn bị."} 