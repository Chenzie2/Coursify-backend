from flask import request, make_response
from flask_restful import Resource
from models import db, Course




# course resources

class Courses(Resource):
    def get(self):
        courses=Course.query.all()
        course_list=[course.to_dict() for course in courses]
        return make_response(course_list, 200)
    
    def post(self):
        try:
            data = request.get_json()
            
            title = data.get("title")
            description = data.get("description")
            duration = data.get("duration")
            level = data.get("level")
            lesson_count = data.get("lesson_count")
            instructor_id = data.get("instructor_id")

            course = Course(
                title=title,
                description=description,
                duration=duration,
                level=level,
                lesson_count=lesson_count,
                instructor_id=instructor_id
            )

            db.session.add(course)
            db.session.commit()

            response = {
                "status": "success",
                "code": 201,
                "message": "Course created successfully"
            }
            return make_response(response, 201)

        except Exception as e:
            response = {
                "status": "error",
                "code": 500,
                "message": "Something went wrong",
                "error": str(e)
            }
            return make_response(response, 500)
    


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


def register_course_routes(api):
    api.add_resource(Courses, "/courses")
    api.add_resource(CourseById, "/courses/<int:id>")
