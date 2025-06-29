# Coursify Backend

This repository contains the backend API for **Coursify** - a learning platform that enables user registration as students/instructors, course management, and enrollment functionality.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#-features)
- [Technologies](#-technologies-used)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Endpoints](#-api-endpoints)
- [Database Models](#-database-models)
- [Authentication](#-authentication)
- [Error Handling](#-error-handling)
- [Deployment](#-deployment)
- [License](#-license)

---

## Introduction
Flask-based REST API backend for Coursify platform. Handles user authentication, course management, enrollment, and role-based access control.

---

## Features
- JWT-based user authentication
- Role-based access (Student/Instructor)
- Course creation/updating/deletion
- Student enrollment system
- User-specific course tracking
- Instructor/student course filtering

---

## Technologies Used
| Category       | Technologies                  |
|----------------|-------------------------------|
| Core           | Python 3.8+, Flask            |
| ORM            | SQLAlchemy                    |
| Database       | SQLite (Dev)                  |
| Authentication | Flask-JWT-Extended            |
| Migrations     | Flask-Migrate, Alembic        |
| Utilities      | Flask-CORS, python-dotenv     |

---

## Project Structure
```bash
coursify-backend/
├── app.py # Application entry point
├── models.py # Database models
├── seed.py # Sample data seeder
├── routes/ # API endpoints
│ ├── auth_routes.py # Authentication routes
│ ├── course_routes.py # Course operations
│ ├── enrollment_routes.py# Enrollment logic
│ └── user_routes.py # User management
├── migrations/ # Database migrations
├── instance/ # Database storage
│ └── project.db
├── .env.example # Environment template
└── requirements.txt # Dependencies
```


---

## Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/coursify-backend.git
cd coursify-backend
```

# Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
# Install dependencies
```bash
pip install -r requirements.txt
Environment Setup
bash
cp .env.example .env

Edit .env with your configuration:

env
FLASK_ENV=development
FLASK_APP=app.py
SECRET_KEY=your_secret_key_here
DATABASE_URI=sqlite:///instance/project.db
Running the Application
bash
```
# Initialize database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

# Seed sample data (optional)
```bash
python seed.py
```

# Start development server
```bash
flask run
Access API at: http://localhost:5000
```

# API Endpoints
 ## Authentication
 ```bash
Method	Endpoint	Description
POST	/register	User registration
POST	/login	User login
GET	/check_session	Session validation
```
 ## Courses
 ```bash
Method	Endpoint	Description
GET	/courses	List all courses
POST	/courses	Create new course (Instructor)
PUT	/courses/<id>	Update course (Instructor)
DELETE	/courses/<id>	Delete course (Instructor)
```
## User Management
```bash
Method	Endpoint	Description
GET	/users	List all users
GET	/my_enrollments	Get student's enrolled courses
GET	/my_created_courses	Get instructor's created courses
```
# Authentication
```bash
JWT token-based authentication

Include in headers: Authorization: Bearer <your_token>
```

Role-based permissions:

```bash
Students: Enroll in/view courses

Instructors: Create/manage courses
```
# Error Handling
Standardized JSON error responses:
```bash
json
{
  "error": "Resource not found",
  "message": "The requested instructor does not exist",
  "status": 404
}

```
Status codes:

```bash
400: Bad Request

401: Unauthorized

403: Forbidden

404: Not Found

500: Internal Server Error
```

# Deployment
Set production-ready database (PostgreSQL/MySQL)
Configure environment variables:
```bash
env
FLASK_ENV=production
SECRET_KEY=strong_production_secret
DATABASE_URI=postgresql://user:pass@localhost/dbname
```

# License
MIT License © 2025 - Coursify Team
