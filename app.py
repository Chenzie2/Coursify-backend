from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api





# initialize app
app = Flask(__name__)
    
    # Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coursify.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions

migrate = Migrate(app, db)
CORS(app)
db.init_app(app)
api=Api(app)


register_course_routes(api)



if __name__ == '__main__':
    app.run(debug=True)   

