from flask import Flask
from flask_cors import CORS
from routes.user_routes import user_routes  # Importar el blueprint de las rutas de usuario
from db import connect_db  # Importar la función de conexión a la base de datos desde db.py

app = Flask(__name__)
CORS(app)

# Registrar el blueprint para las rutas de usuario
app.register_blueprint(user_routes)

# Ruta de prueba para verificar que la conexión a la base de datos funciona
@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            result = cursor.fetchone()
        return {"message": f"Conectado a la base de datos: {result['DATABASE()']}"}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True)
