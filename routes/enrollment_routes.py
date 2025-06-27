from flask_restful import Resource
from flask import request, make_response
from models import db, Enrollment, Course, User
from datetime import datetime


class EnrollUser(Resource):
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        course_id = data.get('course_id')

        if not user_id or not course_id:
            return make_response({"error": "User ID and Course ID are required"}, 400)

        user = User.query.get(user_id)
        course = Course.query.get(course_id)
        if not user or not course:
            return make_response({"error": "Invalid User ID or Course ID"}, 404)

        existing = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
        if existing:
            return make_response({"message": "User already enrolled in this course"}, 200)

        try:
            enrollment = Enrollment(
                user_id=user_id,
                course_id=course_id,
                progress="0.0",  # Keeping it string to match your model
                review_score=None,
                certificate_issued=False,
                enrollment_date=datetime.utcnow()
            )
            db.session.add(enrollment)
            db.session.commit()

            return make_response({
                "message": "User enrolled successfully",
                "enrollment": enrollment.to_dict()
            }, 201)

        except Exception as e:
            db.session.rollback()
            return make_response({"error": "Enrollment failed", "details": str(e)}, 500)


class UserEnrollments(Resource):
    def get(self, user_id):
        try:
            enrollments = Enrollment.query.filter_by(user_id=user_id).all()
            if not enrollments:
                return make_response({"message": "No enrollments found for this user"}, 404)

            return make_response({
                "enrollments": [e.to_dict() for e in enrollments]
            }, 200)
        except Exception as e:
            return make_response({"error": "Failed to fetch enrollments", "details": str(e)}, 500)


class UpdateEnrollment(Resource):
    def patch(self, enrollment_id):
        enrollment = Enrollment.query.get(enrollment_id)
        if not enrollment:
            return make_response({"error": "Enrollment not found"}, 404)

        data = request.get_json()
        try:
            for field in ["progress", "review_score", "certificate_issued"]:
                if field in data:
                    setattr(enrollment, field, data[field])

            db.session.commit()

            return make_response({
                "message": "Enrollment updated successfully",
                "enrollment": enrollment.to_dict()
            }, 200)

        except Exception as e:
            db.session.rollback()
            return make_response({"error": "Failed to update enrollment", "details": str(e)}, 500)


def register_enrollment_routes(api):
    api.add_resource(EnrollUser, '/enrollments')
    api.add_resource(UserEnrollments, '/enrollments/<int:user_id>')
    api.add_resource(UpdateEnrollment, '/enrollments/<int:enrollment_id>')
