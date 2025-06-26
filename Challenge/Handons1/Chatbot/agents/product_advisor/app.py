from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI()
DB_PATH = os.path.join(os.path.dirname(__file__), '../db/orders.db')

class Question(BaseModel):
    question: str

class Order(BaseModel):
    customer: str
    product: str
    quantity: int

class ProductFilter(BaseModel):
    keyword: str

@app.post('/ask')
def ask_product(q: Question):
    return {"answer": "Đây là agent tư vấn sản phẩm. Sẽ trả lời/tư vấn sản phẩm."}

@app.post('/order')
def create_order(order: Order):
    # Dummy: Lưu đơn vào DB (sẽ hoàn thiện sau)
    return {"status": "Đơn hàng đã được lưu (giả lập)."}

@app.post('/filter')
def filter_product(f: ProductFilter):
    # Dummy: Gọi tool filter sản phẩm (sẽ hoàn thiện sau)
    return {"products": ["Sản phẩm A", "Sản phẩm B"]} 