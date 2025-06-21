from flask import request, jsonify
from models import db, Enrollment, Course, User
from datetime import datetime

# POST / enrollments : Enroll a user in a course
def enroll_user():
    data = request.get_json()
    user_id = data.get('user_id')
    course_id = data.get('course_id')

    if not user_id or not course_id:
        return jsonify({"error": "User ID and Course ID are required"}), 400

    user = User.query.get(user_id)
    course = Course.query.get(course_id)

    if not user or not course:
        return jsonify({"error": "Invalid User ID or Course ID"}), 404

    existing_enrollment = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
    if existing_enrollment:
        return jsonify({"message": "User already enrolled in this course"}), 200

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

    return jsonify({"message": "User enrolled successfully", "enrollment": new_enrollment.to_dict()}), 201

