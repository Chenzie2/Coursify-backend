from app import app, db
from models import User, Course, Enrollment, Review
from datetime import datetime

with app.app_context():
    # Reset tables
    db.drop_all()
    db.create_all()

    # ---------- USERS ----------
    print("Creating users...")
    user1 = User(first_name='Edwin', last_name='Kipyego', age=30, gender='Male', email='edwin.kipyego@gmail.com', role='instructor')
    user1.set_password("Edwin123")

    user2 = User(first_name='Joy', last_name='Malinda', age=23, gender='Female', email='koki@gmail.com', role='student')
    user2.set_password("Joy123")

    user3 = User(first_name='Boniface', last_name='Muguro', age=55, gender='Male', email='boniface@gmail.com', role='student')
    user3.set_password("BonnieKim123")

    user4 = User(first_name='Celestine', last_name='Mecheo', age=26, gender='Female', email='celestine@gmail.com', role='instructor')
    user4.set_password("Celestine123")

    user5 = User(first_name='Aquila', last_name='Jedidia', age=28, gender='Male', email='aquila@gmail.com', role='instructor')
    user5.set_password("jedaqsaul123")

    user6 = User(first_name='Grace', last_name='Zawadi', age=22, gender='Female', email='gracezawadi@gmail.com', role='student')
    user6.set_password("gzawie123")

    users = [user1, user2, user3, user4, user5, user6]
    db.session.add_all(users)
    db.session.commit()
    print("Users created successfully.")

    # ---------- COURSES ----------
    print("Creating courses...")
    courses_data = [
        ('Python Programming', 'Learn Python from scratch.', 30, 'Beginner', 10, user1.id),
        ('Data Science with Python', 'Advanced data science concepts.', 45, 'Advanced', 15, user1.id),
        ('Web Development with Flask', 'Build web apps using Flask.', 40, 'Intermediate', 12, user4.id),
        ('Data Structures', 'Intro to data structures.', 35, 'Beginner', 10, user4.id),
        ('Machine Learning Basics', 'ML concepts explained.', 50, 'Intermediate', 14, user1.id),
        ('Deep Learning', 'Neural networks and deep learning.', 60, 'Advanced', 16, user1.id),
        ('Front-End Development', 'HTML, CSS, JS crash course.', 25, 'Beginner', 8, user4.id),
        ('React for Beginners', 'Intro to React and components.', 30, 'Beginner', 10, user4.id),
        ('APIs with Flask', 'REST API development.', 35, 'Intermediate', 11, user1.id),
        ('Database Design', 'SQL & NoSQL explained.', 30, 'Intermediate', 9, user4.id),
        ('DevOps Essentials', 'CI/CD, Docker, pipelines.', 40, 'Advanced', 12, user1.id),
        ('Cybersecurity Basics', 'Understanding digital security.', 30, 'Beginner', 7, user4.id),
    ]

    courses = [Course(title=title, description=desc, duration=dur, level=level, lesson_count=lessons, instructor_id=instructor)
               for (title, desc, dur, level, lessons, instructor) in courses_data]

    db.session.add_all(courses)
    db.session.commit()
    print("Courses created successfully.")

    # ---------- ENROLLMENTS ----------
    print("Creating enrollments...")
    enrollments = [
        Enrollment(user_id=user2.id, course_id=courses[0].id, progress=50, review_score=7, certificate_issued=True),
        Enrollment(user_id=user2.id, course_id=courses[2].id, progress=80, review_score=8, certificate_issued=True),
        Enrollment(user_id=user2.id, course_id=courses[6].id, progress=30, review_score=9, certificate_issued=False),

        Enrollment(user_id=user3.id, course_id=courses[1].id, progress=70, review_score=10, certificate_issued=True),
        Enrollment(user_id=user3.id, course_id=courses[3].id, progress=40, review_score=7, certificate_issued=False),

        Enrollment(user_id=user5.id, course_id=courses[4].id, progress=90, review_score=9, certificate_issued=True),
        Enrollment(user_id=user5.id, course_id=courses[6].id, progress=65, review_score=8, certificate_issued=True),

        Enrollment(user_id=user6.id, course_id=courses[5].id, progress=70, review_score=7, certificate_issued=True),
        Enrollment(user_id=user6.id, course_id=courses[7].id, progress=20, review_score=6, certificate_issued=False),
        Enrollment(user_id=user6.id, course_id=courses[8].id, progress=50, review_score=9, certificate_issued=True),

        Enrollment(user_id=user3.id, course_id=courses[10].id, progress=50, review_score=9, certificate_issued=True),
        Enrollment(user_id=user5.id, course_id=courses[11].id, progress=100, review_score=10, certificate_issued=True),
    ]
    db.session.add_all(enrollments)
    db.session.commit()
    print("Enrollments created successfully.")

    # ---------- REVIEWS ----------
    print("Creating reviews...")
    reviews = [
        Review(user_id=user2.id, course_id=courses[0].id, rating=4.5, comment='Really helpful.'),
        Review(user_id=user3.id, course_id=courses[1].id, rating=5.0, comment='Excellent content!'),
        Review(user_id=user2.id, course_id=courses[2].id, rating=4.0, comment='Well paced.'),
        Review(user_id=user3.id, course_id=courses[3].id, rating=4.2, comment='Good refresher.'),
        Review(user_id=user5.id, course_id=courses[4].id, rating=4.8, comment='ML was made easy!'),
        Review(user_id=user6.id, course_id=courses[5].id, rating=3.5, comment='Challenging but rewarding.'),
        Review(user_id=user5.id, course_id=courses[6].id, rating=4.0, comment='Frontend tools explained well.'),
        Review(user_id=user6.id, course_id=courses[7].id, rating=4.7, comment='React was fun!'),
        Review(user_id=user6.id, course_id=courses[8].id, rating=4.9, comment='Loved the API integration.'),
        Review(user_id=user3.id, course_id=courses[10].id, rating=4.4, comment='Very practical.'),
        Review(user_id=user5.id, course_id=courses[11].id, rating=5.0, comment='Important for everyone.'),
        Review(user_id=user4.id, course_id=courses[9].id, rating=4.1, comment='DB concepts well explained.')
    ]
    db.session.add_all(reviews)
    db.session.commit()
    print("Reviews created successfully.")

    print("Database seeded successfully.")
