from flask import Blueprint, request, jsonify
from models.user import create_user, get_users, update_user, delete_user

user_routes = Blueprint('user_routes', __name__)

# Ruta para crear usuario
@user_routes.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    response = create_user(data['name'], data['email'], data['password'])
    return jsonify(response)

# Ruta para obtener todos los usuarios
@user_routes.route('/users', methods=['GET'])
def read():
    users = get_users()
    return jsonify(users)

# Ruta para actualizar usuario
@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    response = update_user(user_id, data['name'], data['email'], data['password'])
    return jsonify(response)

# Ruta para eliminar usuario
@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    response = delete_user(user_id)
    return jsonify(response)
