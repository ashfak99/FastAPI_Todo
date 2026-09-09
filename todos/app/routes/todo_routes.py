from fastapi import APIRouter, HTTPException, status

from app.schemas.todos_schema import todosSchema, TodoPatchSchema, TodoPutSchema, TodoResponseSchema
from app.handler.todo_handler import create_todo_handler, get_todo_handler, get_todos_handler, delete_todo_handler, delete_todos_handler, update_todo_handler, patch_todo_handler
from app.exception.todo_exception import TodoNotFoundError

router=APIRouter()

@router.post("/todos",response_model=TodoResponseSchema,status_code=status.HTTP_201_CREATED)
def create_todo(todos : todosSchema):
    return create_todo_handler(todos)

@router.get("/todos/{todo_id}",response_model=TodoResponseSchema, status_code=status.HTTP_200_OK)
def get_todo(todo_id : int):
    return get_todo_handler(todo_id)

@router.get("/todos",response_model=list[TodoResponseSchema],status_code=status.HTTP_200_OK)
def get_todos():
    return get_todos_handler()

@router.delete("/todos", response_model=list[TodoResponseSchema], status_code=status.HTTP_204_NO_CONTENT)
def delete_todos():
    return delete_todos_handler()

@router.delete("/todos/{todo_id}", response_model=TodoResponseSchema, status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id:int):
    return delete_todo_handler(todo_id)

@router.put("/todos/{todo_id}", response_model=TodoResponseSchema, status_code=status.HTTP_200_OK)
def update_todo(todo:TodoPutSchema,todo_id:int):
    return update_todo_handler(todo,todo_id)

@router.patch("/todos/{todo_id}", response_model=TodoResponseSchema, status_code=status.HTTP_200_OK)
def patch_todo(todo_id:int,todo:TodoPatchSchema):
    data=todo.model_dump(exclude_unset=True)
    return patch_todo_handler(todo_id,data)