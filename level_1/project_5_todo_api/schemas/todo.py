from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: bool = False


class TodoResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    completed: bool

