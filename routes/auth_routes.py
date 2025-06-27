from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)

from models import db, User


class Register(Resource):
    def post(self):
        data = request.get_json()
        required_fields = ["first_name", "last_name", "email", "password", "age", "gender", "role"]
        if not all(field in data for field in required_fields):
            return {"error": "Missing required fields"}, 400

        if User.query.filter_by(email=data["email"]).first():
            return {"error": "User with this email already exists"}, 400

        user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            age=data["age"],
            gender=data["gender"],
            role=data["role"]
        )
        user.set_password(data["password"])
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered successfully"}, 201


class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data.get("email") or not data.get("password"):
            return {"error": "Missing email or password"}, 400

        user = User.query.filter_by(email=data["email"]).first()
        if user and user.check_password(data["password"]):
            token = create_access_token(identity={"id": user.id, "email": user.email, "role": user.role})
            return {"token": token, "user": user.to_dict()}, 200
        return {"error": "Invalid credentials"}, 401


class Logout(Resource):
    @jwt_required()
    def post(self):
        return {"message": "Logout handled on client side."}, 200


class Me(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        user = User.query.get(identity["id"])
        if not user:
            return {"error": "User not found"}, 404
        return user.to_dict(), 200
