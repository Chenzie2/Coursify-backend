from flask import Flask, make_response, request
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
db.init_app(app)
api=Api(app)



# course resources

class Courses(Resource):
    def get(self):
        courses=Course.query.all()
        course_list=[course.to_dict() for course in courses]
        return make_response(course_list, 200)
    


class CourseById(Resource):
    def get(self, id):
        course=Course.query.filter_by(id=id).first()


        if course:
            return make_response(course.to_dict(), 200)
        else:
            return make_response({
                "code": 404, 
                "message": "Course not found",
                "status":"unsuccessful"
            }, 404)
        

api.add_resource(Courses, "/courses")
api.add_resource(CourseById, "/courses/<int:id>")



if __name__ == '__main__':
    app.run(debug=True)   

