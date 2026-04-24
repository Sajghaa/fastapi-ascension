from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Fake database
todos = []

# Model
class Todo(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# HOME
@app.get("/")
def home():
    return {"message": "Todo API running"}

# GET all todos
@app.get("/todos")
def get_todos():
    return todos

# CREATE todo
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo added", "data": todo}

# GET one todo
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id < len(todos):
        return todos[todo_id]
    return {"error": "Todo not found"}

# UPDATE todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    if todo_id < len(todos):
        todos[todo_id] = updated_todo
        return {"message": "Updated", "data": updated_todo}
    return {"error": "Todo not found"}

# DELETE todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id < len(todos):
        deleted = todos.pop(todo_id)
        return {"message": "Deleted", "data": deleted}
    return {"error": "Todo not found"}