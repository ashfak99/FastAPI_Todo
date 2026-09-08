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

def get_todo(id:int):
    connection = get_connection()

    cursor=connection.execute(
        """
            SELECT * FROM todos WHERE id =?
        """,(id,)
    )

    connection.commit()

    todo=cursor.fetchone()

    connection.close()
    return todo


def get_todos():
    connection=get_connection()

    cursor=connection.execute(
        """
            SELECT * FROM todos
        """
    )
    connection.commit()

    todos=cursor.fetchall()
    connection.close()
    return todos

