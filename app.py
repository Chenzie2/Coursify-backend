from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Course, Enrollment, Review

def create_app():
    app = Flask(__name__)

    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coursify.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app)

    # Optionally register Blueprints here
    # from routes.auth_routes import auth_bp
    # app.register_blueprint(auth_bp)

    return app

# Optional: for development testing only
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
