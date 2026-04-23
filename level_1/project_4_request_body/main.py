from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model (schema)
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

# POST → receive data
@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created",
        "data": item
    }