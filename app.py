from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api, Resource

from models import db, User, Course, Enrollment, Review



# initialize app
app = Flask(__name__)
    
    # Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coursify.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)   

