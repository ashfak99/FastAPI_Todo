from fastapi import APIRouter, HTTPException

from app.schemas.todos_schema import todosSchema
from app.handler.todo_handler import create_todo_handler, get_todo_handler
from app.exception.todo_exception import TodoNotFoundError

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

@router.get("/todos/{todo_id}")
def get_todo(todo_id : int):
    try:
        return get_todo_handler(todo_id)
    except TodoNotFoundError as error:
        raise HTTPException(
            status_code= 404,
            detail = str(error)
        )