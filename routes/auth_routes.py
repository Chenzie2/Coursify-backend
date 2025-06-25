
import os
import re
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from flask_restful import Resource, Api
from sqlalchemy_serializer import SerializerMixin

# === App Setup ===
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-secret-key')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app)
api = Api(app)
jwt = JWTManager(app)

# === Models ===
class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Department(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    students = db.relationship("Student", backref="department", lazy=True)

class Student(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    enrollments = db.relationship("Enrollment", backref="student", lazy=True)

class Course(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    enrollments = db.relationship("Enrollment", backref="course", lazy=True)

class Enrollment(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    note = db.Column(db.String(255))

# === Resources ===
class Register(Resource):
    def post(self):
        data = request.get_json()
        if not data.get("username") or not data.get("email") or not data.get("password"):
            return {"error": "Missing required fields"}, 400

        if not re.match(r"[^@]+@[^@]+\.[^@]+", data["email"]):
            return {"error": "Invalid email format"}, 400

        if User.query.filter((User.email == data['email']) | (User.username == data['username'])).first():
            return {"error": "User already exists"}, 400

        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered successfully"}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            token = create_access_token(identity={
                "id": user.id,
                "username": user.username,
                "is_admin": user.is_admin
            })
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
        return user.to_dict(), 200

class DepartmentList(Resource):
    def get(self):
        departments = Department.query.all()
        return [d.to_dict() for d in departments], 200

class StudentList(Resource):
    @jwt_required()
    def get(self):
        students = Student.query.all()
        return [s.to_dict() for s in students], 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        if not data.get("name") or not data.get("email") or not data.get("department_id"):
            return {"error": "Missing fields"}, 400

        if not Department.query.get(data["department_id"]):
            return {"error": "Department not found"}, 404

        student = Student(name=data["name"], email=data["email"], department_id=data["department_id"])
        db.session.add(student)
        db.session.commit()
        return student.to_dict(), 201

class CourseList(Resource):
    def get(self):
        courses = Course.query.all()
        return [c.to_dict() for c in courses], 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        if not data.get("title") or not data.get("description"):
            return {"error": "Missing fields"}, 400

        course = Course(title=data["title"], description=data["description"])
        db.session.add(course)
        db.session.commit()
        return course.to_dict(), 201

class EnrollmentList(Resource):
    @jwt_required()
    def get(self):
        enrollments = Enrollment.query.all()
        return [e.to_dict() for e in enrollments], 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        if not data.get("student_id") or not data.get("course_id"):
            return {"error": "Missing fields"}, 400

        if not Student.query.get(data["student_id"]) or not Course.query.get(data["course_id"]):
            return {"error": "Student or Course not found"}, 404

        enrollment = Enrollment(
            student_id=data["student_id"],
            course_id=data["course_id"],
            note=data.get("note", "")
        )
        db.session.add(enrollment)
        db.session.commit()
        return enrollment.to_dict(), 201

class MyCourses(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        student = Student.query.filter_by(email=identity["username"]).first()
        if not student:
            return {"error": "Student not found"}, 404
        return [e.course.to_dict() for e in student.enrollments], 200

# === Register Resources ===
api.add_resource(Register, "/register")
print("✅ Register route loaded")

api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(Me, "/me")
api.add_resource(DepartmentList, "/departments")
api.add_resource(StudentList, "/students")
api.add_resource(CourseList, "/courses")
api.add_resource(EnrollmentList, "/enrollments")
api.add_resource(MyCourses, "/my-courses")

# === Main Run ===
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

