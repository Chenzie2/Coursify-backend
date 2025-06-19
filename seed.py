from app import app, db
from models import User, Course, Enrollment, Review, db
from datetime import datetime


with app.app_context():

    # Clear existing data
    db.drop_all()
    db.create_all()
    
    # Create users
    print("Creating users...") 
    user1 = User(
        first_name='Edwin',
        last_name='Kipyego',
        age=30,
        gender='Male',
        email='edwin.kipyego@gmail.com',
        role='instructor'
    )
    user2 = User(
        first_name='Joy',
        last_name='Malinda',
        age=23,
        gender='Female',
        email='koki@gmail.com',
        role='student'
    )
    user3 = User(
        first_name='Boniface',
        last_name='Muguro',
        age=55,
        gender='Male',
        email='boniface@gmail.com',
        role='student'
    )
    user4 = User(
        first_name='Celestine',
        last_name='Mecheo',
        age= 26,    
        gender='Female',
        email='celestine@gmail.com',
        role='instructor'
    )

    users = [user1, user2, user3, user4]
    db.session.add_all(users)
    db.session.commit()
    print("User created successfully.")

    # Create courses
    print("Creating courses...")
    course1 = Course(
        title='Python Programming',
        description='Learn Python from scratch.',
        duration=30,
        level='Beginner',
        lesson_count=10,
        instructor_id=user1.id
    )
    course2 = Course(
        title='Data Science with Python',
        description='Advanced data science concepts using Python.',
        duration=45,
        level='Advanced',
        lesson_count=15,
        instructor_id=user3.id
    )
    course3 = Course(
        title='Web Development with Flask',
        description='Build web applications using Flask.',
        duration=40,
        level='Intermediate',
        lesson_count=12,
        instructor_id=user1.id
    )
    course4 = Course(
        title='Data Structures',
        description='Learn about data structures in Python.',
        duration=35,
        level='Beginner',
        lesson_count=10,
        instructor_id=user3.id
    )

    courses = [course1, course2, course3, course4]
    db.session.add_all(courses)
    db.session.commit()
    print("Courses created successfully.")

    # Create enrollments
    print("Creating enrollments...")
    enrollment1 = Enrollment(
        user_id=user2.id,
        course_id=course1.id,
        enrollment_date= datetime.utcnow(),
        progress=50,
        review_score=7.5,
        certificate_issued=True,
    )
    enrollment2 = Enrollment(
        user_id=user3.id,
        course_id=course2.id,
        enrollment_date=datetime.utcnow(),
        progress=80,
        review_score=9.0,
        certificate_issued=True,
    )
    enrollment3 = Enrollment(
        user_id=user2.id,
        course_id=course3.id,
        enrollment_date=datetime.utcnow(),
        progress=30,
        review_score=None,
        certificate_issued=False,
    )
    enrollment4 = Enrollment(
        user_id=user4.id,
        course_id=course4.id,
        enrollment_date=datetime.utcnow(),
        progress=20,
        review_score=None,
        certificate_issued=False,
    )
    enrollments = [enrollment1, enrollment2, enrollment3, enrollment4]
    db.session.add_all(enrollments)
    db.session.commit()
    print("Enrollments created successfully.")

    # Create reviews
    print("Creating reviews...")
    review1 = Review(
        user_id=user2.id,
        course_id=course1.id,
        rating=4.5,
        comment='Great course, learned a lot!'
    )
    review2 = Review(
        user_id=user3.id,
        course_id=course2.id,
        rating=5.0,
        comment='Excellent course, highly recommend!'
    )
    review3 = Review(
        user_id=user2.id,
        course_id=course3.id,
        rating=4.0,
        comment='Good course, but could use more examples.'
    )
    review4 = Review(
        user_id=user4.id,
        course_id=course4.id,
        rating=3.5,
        comment='Decent course, but not very in-depth.'
    )
    reviews = [review1, review2, review3, review4]
    db.session.add_all(reviews)
    db.session.commit()
    print("Reviews created successfully.")


if __name__ == '__main__':
    print("Database seeded successfully.")