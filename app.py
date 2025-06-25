from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api

# Initialize extensions
db = SQLAlchemy()


app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coursify.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions with app
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)
api = Api(app)


if __name__ == '__main__':
    app.run(debug=True)
