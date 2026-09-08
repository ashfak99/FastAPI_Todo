from app.repository.todo_repository import create_todo, get_todo, get_todos
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