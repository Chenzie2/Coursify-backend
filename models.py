from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import validates, relationship
from datetime import datetime
from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)

    #Relationships
    courses = db.relationship('Courses', back_populates='instructor')
    enrollments = db.relationship('Enrollment', back_populates='user')
    review = db.relationship('Review', back_populates='user')

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'gender': self.gender,
            'email': self.email,
            'role': self.role
        }



class Course(db.model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    level = db.Column(db.String(20), nullable=False)
    lesson_count = db.Column(db.Integer, nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationships
    instructor = db.relationship('User', back_populates='courses')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'duration': self.duration,
            'level': self.level,
            'lesson_count': self.lesson_count,
            'instructor_id': self.instructor_id
        }



class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=datetime)
    progress = db.Column(db.String, default=0.0)
    completion_date = db.Column(db.DateTime, nullable=True)
    review_score = db.Column(db.Integer, nullable=True)
    certificate_issued = db.Column(db.Boolean, default=False)

    # Relationships
    user = db.relationship('User', back_populates='enrollments')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'course_id': self.course_id,
            'enrollment_date': self.enrollment_date.isoformat(),
            'progress': self.progress,
            'completion_date': self.completion_date.isoformat() if self.completion_date else None,
            'review_score': self.review_score,
            'certificate_issued': self.certificate_issued
        }

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    # Relationships
    user = db.relationship('User', back_populates='reviews')
    course = db.relationship('Course', back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'course_id': self.course_id,
            'rating': self.rating,
            'comment': self.comment
        }
    





