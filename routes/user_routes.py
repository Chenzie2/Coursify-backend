from flask import Blueprint, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash

user_routes = Blueprint('user_routes', __name__)

# GET all users
@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# GET a single user by ID
@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

# PATCH update a user
@user_routes.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()

    # Only update fields if provided
    if 'first_name' in data:
        user.first_name = data['first_name']
    if 'last_name' in data:
        user.last_name = data['last_name']
    if 'age' in data:
        user.age = data['age']
    if 'gender' in data:
        user.gender = data['gender']
    if 'email' in data:
        user.email = data['email']
    if 'role' in data:
        user.role = data['role']
    if 'password' in data:
        user.password_hash = generate_password_hash(data['password'])  # Optional password update

    db.session.commit()
    return jsonify(user.to_dict()), 200

# Create a new user
@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(key in data for key in ('first_name', 'last_name', 'age', 'gender', 'email', 'role')):
        return jsonify({"error": "Missing required fields"}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 400
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        email=data['email'],
        gender=data['gender'],
        role=data['role'],
        password_hash=generate_password_hash(data.get('password', 'default_password'))
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


def register_user_routes(api):
    api.add_resource(get_users, '/users')
    api.add_resource(get_user, '/users/<int:user_id>')
    api.add_resource(update_user, '/users/<int:user_id>')
    api.add_resource(create_user, '/users')
    
