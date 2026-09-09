from app.repository.todo_repository import create_todo, get_todo, get_todos, delete_todo, delete_todos, update_todo, patch_todo
from app.exception.todo_exception import TodoNotFoundError

def create_todo_services(todo):
    if len(todo.title.strip())<3:
        raise ValueError("todo title must contain at least 3 character")

    todo_id= create_todo(
        todo.title,
        todo.description
    )

    return {
        "id":todo_id,
        "title" : todo.title,
        "description" : todo.description,
        "completed" : False
    }

def get_todo_services(todo_id):
    todo=get_todo(todo_id)

    if todo is None:
        raise TodoNotFoundError("Todo not found")

    return{
        "id" : todo["id"],
        "title" : todo["title"],
        "description" : todo["description"],
        "completed" : todo["completed"]
    }

def get_todos_services():
    todos=get_todos()

    if todos is None:
        raise TodoNotFoundError("Todo is empty")

    return todos

def delete_todos_services():
    row_count = delete_todos()

    if row_count==0:
        raise TodoNotFoundError("Todo is empty")

    return row_count

def delete_todo_serices(id:int):
    row_count = delete_todo(id)

    if row_count == 0:
        raise TodoNotFoundError("Todo nor found")

    return row_count

def update_todo_services(todo,todo_id,completed):
    if len(todo.title.strip())<3:
        raise ValueError("Todo title must be at least 3 character")

    todo = update_todo(todo_id, todo.title, todo.description, completed)

    if todo==0:
        raise TodoNotFoundError

    return {
        "message" : "Todo Update Successfully"
    }  

def patch_todo_services(todo_id,data):
    result=patch_todo(todo_id,data)

    if result==0:
        raise TodoNotFoundError

    return {"message":"Todo Update Successfully"}