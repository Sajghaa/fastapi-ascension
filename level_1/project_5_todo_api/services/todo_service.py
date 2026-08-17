import uuid
from typing import Dict, List
from schemas.todo import TodoCreate, TodoResponse
from exceptions import NotFoundError

class TodoService:
    def __init__(self):
        # In-memory "database" – dict of id -> dict
        self._todos: Dict[str, dict] = {}

    async def get_all(self) -> List[TodoResponse]:
        # Simulate async I/O (optional)
        return [TodoResponse(**todo) for todo in self._todos.values()]

    async def get_one(self, todo_id: uuid.UUID) -> TodoResponse:
        todo = self._todos.get(str(todo_id))
        if not todo:
            raise NotFoundError(f"Todo with id {todo_id} not found")
        return TodoResponse(**todo)

    async def create(self, todo_data: TodoCreate) -> TodoResponse:
        new_id = uuid.uuid4()
        todo_dict = todo_data.model_dump()  # Pydantic v2
        todo_dict["id"] = new_id
        self._todos[str(new_id)] = todo_dict
        return TodoResponse(**todo_dict)

    async def update(self, todo_id: uuid.UUID, todo_data: TodoCreate) -> TodoResponse:
        existing = await self.get_one(todo_id)  # reuse get_one to raise NotFound
        # Update fields
        updated_dict = todo_data.model_dump()
        updated_dict["id"] = todo_id
        self._todos[str(todo_id)] = updated_dict
        return TodoResponse(**updated_dict)

    async def delete(self, todo_id: uuid.UUID) -> None:
        if str(todo_id) not in self._todos:
            raise NotFoundError(f"Todo with id {todo_id} not found")
        del self._todos[str(todo_id)]