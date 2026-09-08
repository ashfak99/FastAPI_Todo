from app.services.todo_services import create_todo_services, get_todo_services

def create_todo_handler(todo):
    return create_todo_services(todo)


def get_todo_handler(todo_id):
    return get_todo_services(todo_id)