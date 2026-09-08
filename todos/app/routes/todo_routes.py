from fastapi import APIRouter, HTTPException

from app.schemas.todos_schema import todosSchema
from app.handler.todo_handler import create_todo_handler

router=APIRouter()

@router.post("/todos")
def create_todo(todos : todosSchema):
    try:
        return create_todo_handler(todos)
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail = str(error)
        )