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

    user2 = User(first_name='Celestine', last_name='Mecheo', age=26, gender='Female', email='celestine@gmail.com', role='instructor')
    user2.set_password("Celestine123")

    user3 = User(first_name='Aquila', last_name='Jedidia', age=28, gender='Male', email='aquila@gmail.com', role='instructor')
    user3.set_password("jedaqsaul123")

    user4 = User(first_name='Naomi', last_name='Achieng', age=31, gender='Female', email='naomi.achieng@gmail.com', role='instructor')
    user4.set_password("naomi20")

    user5 = User(first_name='James', last_name='Ochieng', age=35, gender='Male', email='jamesochieng@gmail.com', role='instructor')
    user5.set_password("jimmyoch123")

    user6 = User(first_name='Joy', last_name='Malinda', age=23, gender='Female', email='koki@gmail.com', role='student')
    user6.set_password("Joy123")

    user7 = User(first_name='Boniface', last_name='Muguro', age=27, gender='Male', email='boniface@gmail.com', role='student')
    user7.set_password("BonnieKim123")

    user8 = User(first_name='Grace', last_name='Zawadi', age=22, gender='Female', email='gracezawadi@gmail.com', role='student')
    user8.set_password("gzawie123")

    user9 = User(first_name='Daniel', last_name='Odhiambo', age=29, gender='Male', email='dan.odhiambo@gmail.com', role='student')
    user9.set_password("dan123")

    user10 = User(first_name='Lucy', last_name='Wambui', age=24, gender='Female', email='lucywambui@gmail.com', role='student')
    user10.set_password("lucypass")

    user11 = User(first_name='Kevin', last_name='Wanyonyi', age=34, gender='Male', email='kevinw@gmail.com', role='student')
    user11.set_password("kevinpass")

    user12 = User(first_name='Brenda', last_name='Atieno', age=25, gender='Female', email='brendaatieno@gmail.com', role='student')
    user12.set_password("brenda24")

    user13 = User(first_name='Brian', last_name='Kimani', age=19, gender='Male', email='briankimani@gmail.com', role='student')
    user13.set_password("brian123")

    user14 = User(first_name='Faith', last_name='Mwende', age=21, gender='Female', email='faithmwende@gmail.com', role='student')
    user14.set_password("faithpass")

    user15 = User(first_name='Leon', last_name='Mburu', age=26, gender='Male', email='leonmburu@gmail.com', role='student')
    user15.set_password("leonpass")

    users = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10,
             user11, user12, user13, user14, user15]
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
        Enrollment(user_id=user6.id, course_id=1, progress=50, review_score=7, certificate_issued=True),
        Enrollment(user_id=user6.id, course_id=3, progress=80, review_score=8, certificate_issued=True),
        Enrollment(user_id=user7.id, course_id=2, progress=60, review_score=9, certificate_issued=True),
        Enrollment(user_id=user8.id, course_id=6, progress=70, review_score=7, certificate_issued=True),
        Enrollment(user_id=user8.id, course_id=8, progress=20, review_score=6, certificate_issued=False),
        Enrollment(user_id=user9.id, course_id=4, progress=75, review_score=9, certificate_issued=True),
        Enrollment(user_id=user10.id, course_id=5, progress=90, review_score=8, certificate_issued=True),
        Enrollment(user_id=user11.id, course_id=7, progress=65, review_score=9, certificate_issued=True),
        Enrollment(user_id=user12.id, course_id=1, progress=55, review_score=7, certificate_issued=True),
        Enrollment(user_id=user13.id, course_id=3, progress=45, review_score=7, certificate_issued=False),
        Enrollment(user_id=user14.id, course_id=2, progress=80, review_score=9, certificate_issued=True),
        Enrollment(user_id=user15.id, course_id=4, progress=50, review_score=6, certificate_issued=False),
        Enrollment(user_id=user10.id, course_id=9, progress=60, review_score=8, certificate_issued=True),
        Enrollment(user_id=user9.id, course_id=10, progress=40, review_score=7, certificate_issued=False),
        Enrollment(user_id=user7.id, course_id=12, progress=85, review_score=9, certificate_issued=True),
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
