from fastapi import FastAPI
from database import SessionLocal
from models import Todo

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PostgreSQL connected"}

@app.post("/todos")
def create_todo(title: str):
    db = SessionLocal()

    new_todo = Todo(title=title)

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    db.close()

    return new_todo

@app.get("/todos")
def get_todos():
    db = SessionLocal()

    todos = db.query(Todo).all()

    db.close()

    return todos