from flask import Blueprint, request, jsonify
from models import db, Enrollment

enrollment_bp = Blueprint('enrollments', __name__)

@enrollment_bp.route('/enrollments', methods=['GET'])
def get_enrollments():
    return jsonify([e.to_dict() for e in Enrollment.query.all()])

@enrollment_bp.route('/enrollments', methods=['POST'])
def create_enrollment():
    data = request.get_json()
    enrollment = Enrollment(
        user_id=data['user_id'],
        course_id=data['course_id']
    )
    db.session.add(enrollment)
    db.session.commit()
    return jsonify(enrollment.to_dict()), 201
