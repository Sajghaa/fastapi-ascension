from fastapi import HTTPException, status

class NotFoundError(Exception):
    def __init__(self, detail: str = "Resource not found"):
        self.detail = detail

class DuplicateError(Exception):
    def __init__(self, detail: str = "Resource already exists"):
        self.detail = detail