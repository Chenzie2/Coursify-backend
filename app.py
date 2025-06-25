from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api


# Import models and routes
from routes.course_routes import Courses, CourseById


app = Flask(__name__)
    
    # Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coursify.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)


# Initialize Flask-RESTful API
api = Api(app)


# Add course resources
api.add_resource(Courses, "/courses")
api.add_resource(CourseById, "/courses/<int:id>")

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
