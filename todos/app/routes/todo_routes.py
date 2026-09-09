from fastapi import APIRouter, HTTPException

from app.schemas.todos_schema import todosSchema, TodoPatchSchema
from app.handler.todo_handler import create_todo_handler, get_todo_handler, get_todos_handler, delete_todo_handler, delete_todos_handler, update_todo_handler, patch_todo_handler
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

@router.get("/todos")
def get_todos():
    try :
        return get_todos_handler()
    except TodoNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

@router.delete("/todos")
def delete_todos():
    try :
        return delete_todos_handler()
    except TodoNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    try:
        return delete_todo_handler(todo_id)
    except TodoNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

@router.put("/todos/{todo_id}")
def update_todo(todo:todosSchema,todo_id:int,completed:bool):
    try:
        return update_todo_handler(todo,todo_id,completed)
    except TodoNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

@router.patch("/todos/{todo_id}")
def patch_todo(todo_id:int,todo:TodoPatchSchema):
    data=todo.model_dump(exclude_unset=True)
    try : 
        return patch_todo_handler(todo_id,data)
    except TodoNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )