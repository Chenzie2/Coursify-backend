from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from app import db
from models import User

auth_bp = Blueprint('auth_bp', __name__)


blacklist = set()

# Register route
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if user exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'User already exists'}), 400

    hashed_password = generate_password_hash(data['password'])

    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        gender=data['gender'],
        email=data['email'],
        role=data['role'],
        password_hash=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


# Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({'error': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200


# Logout route (JWT blacklist)
@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti'] 
    blacklist.add(jti)
    return jsonify({'message': 'Successfully logged out'}), 200


# Example protected route
@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user.to_dict()), 200
