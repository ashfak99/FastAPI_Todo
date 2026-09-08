from app.repository.todo_repository import create_todo

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