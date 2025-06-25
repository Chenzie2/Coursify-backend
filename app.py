
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from datetime import timedelta

from models import db
# Import your resources (adjust as needed for your project structure)
from routes.course_routes import Courses, CourseById
from routes.user_routes import Users, UserById
from routes.auth_routes import Register, Login


# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI", "sqlite:///coursify.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET", "super-secret")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)


# JWT error handling
@jwt.unauthorized_loader
def missing_token_callback(err):
    return {
        "message": "Authorization required",
        "success": False,
        "error": err
    }, 401


# Register API routes
api.add_resource(Courses, "/courses")
api.add_resource(CourseById, "/courses/<int:id>")
api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:id>")
api.add_resource(Register, "/signup")
api.add_resource(Login, "/login")

# Run app
if __name__ == "__main__":
    app.run(debug=True)

