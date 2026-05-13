from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from database import engine

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

# Create table
Base.metadata.create_all(bind=engine)