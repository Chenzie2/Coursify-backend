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

    def patch(self, id):
    course = Course.query.filter_by(id=id).first()
    if not course:
        return make_response({"error": "Course not found"}, 404)

    data = request.get_json()
    for field in ["title", "description", "duration", "level", "lesson_count", "instructor_id"]:
        if field in data:
            setattr(course, field, data[field])

    try:
        db.session.commit()
        return make_response({
            "message": "Course updated successfully",
            "course": course.to_dict()
        }, 200)
    except Exception as e:
        db.session.rollback()
        return make_response({"error": str(e)}, 500)

def delete(self, id):
    course = Course.query.filter_by(id=id).first()
    if not course:
        return make_response({"error": "Course not found"}, 404)

    try:
        db.session.delete(course)
        db.session.commit()
        return make_response({"message": "Course deleted successfully"}, 200)
    except Exception as e:
        db.session.rollback()
        return make_response({"error": str(e)}, 500)
