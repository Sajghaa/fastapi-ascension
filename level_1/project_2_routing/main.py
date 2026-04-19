from fastapi import FastAPI

app = FastAPI()

# GET → retrieve data
@app.get("/items")
def get_items():
    return {"message": "Getting all items"}

# POST → create data
@app.post("/items")
def create_item():
    return {"message": "Item created"}

# PUT → update data
@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {"message": f"Item {item_id} updated"}

# DELETE → remove data
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}