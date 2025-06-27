import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_migrate import Migrate

# === App Setup ===
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-secret-key')

# === Initialize Extensions ===
from models import db, bcrypt
db.init_app(app)
bcrypt.init_app(app)

migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://127.0.0.1:5173"}})

# Register only working routes
from routes.auth_routes import Register, Login, Logout, Me
from routes.user_routes import register_user_routes
from routes.enrollment_routes import register_enrollment_routes
from routes.user_routes import register_user_routes


api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(Me, "/me")
register_course_routes(api)
register_enrollment_routes(api)
register_user_routes(api)

@app.route("/")
def home():
    return {"message": "API is running!"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
