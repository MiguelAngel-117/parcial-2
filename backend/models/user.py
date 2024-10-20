import pymysql
from db import connect_db  # Importar la función de conexión desde db.py

# Crear un nuevo usuario
def create_user(name, email, password):
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, password))
        connection.commit()
        return {"message": "Usuario creado con éxito"}
    except pymysql.MySQLError as e:
        return {"error": str(e)}
    finally:
        connection.close()

# Obtener todos los usuarios
def get_users():
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
        return users
    finally:
        connection.close()

# Actualizar usuario
def update_user(user_id, name, email, password):
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s"
            cursor.execute(sql, (name, email, password, user_id))
        connection.commit()
        return {"message": "Usuario actualizado con éxito"}
    finally:
        connection.close()

# Eliminar usuario
def delete_user(user_id):
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        connection.commit()
        return {"message": "Usuario eliminado con éxito"}
    finally:
        connection.close()
