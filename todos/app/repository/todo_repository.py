from app.core.database import get_connection

def create_todo(title : str, description : str):
    connection = get_connection()

    cursor = connection.execute(
        """
            INSERT INTO todos (title,description) VALUES (?,?)
        """,(title,description)
    )

    connection.commit()
    todo_id = cursor.lastrowid

    connection.close()

    return todo_id

