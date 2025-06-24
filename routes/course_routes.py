from flask import request, make_response
from flask_restful import Resource
from models import Course, db

class CourseById(Resource):
    def get(self, id):
    course = Course.query.filter_by(id=id).first()
    if course:
        return make_response(course.to_dict(), 200)
    else:
        return make_response({
            "code": 404, 
            "message": "Course not found",
            "status":"unsuccessful"
        }, 404)

    