from flask import request, make_response
from flask_restful import Resource
from models import Course, db


class Courses(Resource):
    def get(self):
        try:
            courses = Course.query.all()
            serialized = [course.to_dict() for course in courses]
            return make_response(serialized, 200)
        except Exception as e:
            print("ERROR in GET /courses:", str(e))
            # Fallback serializer (basic fields only)
            fallback = [
                {
                    "id": c.id,
                    "title": c.title,
                    "description": c.description,
                    "duration": c.duration,
                    "level": c.level,
                    "lesson_count": c.lesson_count,
                    "instructor_id": c.instructor_id
                } for c in Course.query.all()
            ]
            return make_response(fallback, 200)


    def post(self):
        data = request.get_json()
        required_fields = ["title", "description", "duration", "level", "lesson_count", "instructor_id"]
        if not all(field in data for field in required_fields):
            return make_response({"error": "Missing fields"}, 400)

        try:
            course = Course(**data)
            db.session.add(course)
            db.session.commit()
            return make_response({
                "status": "success",
                "message": "Course created successfully",
                "course": course.to_dict()
            }, 201)
        except Exception as e:
            db.session.rollback()
            print("ERROR in POST /courses:", str(e))
            return make_response({"error": str(e)}, 500)