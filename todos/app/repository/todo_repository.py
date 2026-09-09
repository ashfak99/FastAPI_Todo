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

def delete_todos():
    connection = get_connection()

    cursor = connection.execute(
        """
        DELETE FROM todos
        """
    )
    connection.commit()
    result = cursor.rowcount
    connection.close()
    return result


def delete_todo(id:int):
    connection = get_connection()

    cursor=connection.execute(
        """
            DELETE FROM todos WHERE id=?
        """,(id,)
    )

    connection.commit()
    result = cursor.rowcount
    connection.close()
    return result

def update_todo(todo_id : int , title : str , description : str , completed : bool):
    connection = get_connection()

    cursor=connection.execute(
        """
        UPDATE todos SET title=?, description = ?, completed=? WHERE id=?
        """,(title,description,completed,todo_id)
    )

    connection.commit()

    connection.close()
    return cursor.rowcount

def patch_todo(todo_id, data):
    fields=[]
    values=[]

    for key,value in data.items():
        fields.append(f"{key}=?")
        values.append(value)

    values.append(todo_id)

    connection = get_connection()
    cursor=connection.execute(f"UPDATE todos SET {','.join(fields)} WHERE id=?",values)

    connection.commit()
    connection.close()
    return cursor.rowcount