from fastapi import FastAPI


app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id:int):
    return {"item_id": item_id}

@app.get("/search")
def search_item(q:str):
    return {"search":q}

@app.get("/users/{user_id}")
def get_user(user_id: int, active: bool = True):
    return {
        "user_id": user_id,
        "active": active
    }