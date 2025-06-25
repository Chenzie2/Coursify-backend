from flask_restful import Resource
from flask import request, jsonify
from models import db, Enrollment, Course, User
from datetime import datetime

class EnrollUser(Resource):
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        course_id = data.get('course_id')

        if not user_id or not course_id:
            return {"error": "User ID and Course ID are required"}, 400

        user = User.query.get(user_id)
        course = Course.query.get(course_id)

        if not user or not course:
            return {"error": "Invalid User ID or Course ID"}, 404

        existing_enrollment = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
        if existing_enrollment:
            return {"message": "User already enrolled in this course"}, 200

        new_enrollment = Enrollment(
            user_id=user_id,
            course_id=course_id,
            progress=0,
            review_score=None,
            certificate_issued=False,
            enrollment_date=datetime.utcnow()
        )

        db.session.add(new_enrollment)
        db.session.commit()

        return {
            "message": "User enrolled successfully",
            "enrollment": new_enrollment.to_dict()
        }, 201

class UserEnrollments(Resource):
    def get(self, user_id):
        enrollments = Enrollment.query.filter_by(user_id=user_id).all()
        if not enrollments:
            return {"message": "No enrollments found for this user"}, 404

        return {
            "enrollments": [e.to_dict() for e in enrollments]
        }, 200

class UpdateEnrollment(Resource):
    def patch(self, enrollment_id):
        data = request.get_json()
        enrollment = Enrollment.query.get(enrollment_id)
        if not enrollment:
            return {"error": "Enrollment not found"}, 404

        progress = data.get('progress')
        review_score = data.get('review_score')
        certificate_issued = data.get('certificate_issued')

        if progress is not None:
            enrollment.progress = progress
        if review_score is not None:
            enrollment.review_score = review_score
        if certificate_issued is not None:
            enrollment.certificate_issued = certificate_issued

        db.session.commit()

        return {
            "message": "Enrollment updated successfully",
            "enrollment": enrollment.to_dict()
        }, 200




def register_enrollment_routes(api):
    api.add_resource(EnrollUser, '/enrollments')  
    api.add_resource(UserEnrollments, '/enrollments/<int:user_id>')  
    api.add_resource(UpdateEnrollment, '/enrollments/<int:enrollment_id>')  