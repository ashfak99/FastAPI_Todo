from app.services.todo_services import create_todo_services, get_todo_services, get_todos_services, delete_todo_serices,delete_todos_services

def create_todo_handler(todo):
    return create_todo_services(todo)


def get_todo_handler(todo_id):
    return get_todo_services(todo_id)

def get_todos_handler():
    return get_todos_services()

def delete_todo_handler(todo_id):
    return delete_todo_serices(todo_id)

def delete_todos_handler():
    return delete_todos_services()