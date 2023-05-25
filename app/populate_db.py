from modules.enrollments.enrollment import Enrollment
from config import db
from modules.students.student import Student
from modules.subjects.subject import Subject
from modules.auth.user import User

def populate_database():
    # Admin user
    admin = User(id=1, email="admin@admin.com", name="admin", password="admin")

    # Create subjects
    math = Subject(id=1, name='Math', schedule='A', class_num=1, subject_num=1)
    science = Subject(id=2, name='Science', schedule='B', class_num=2, subject_num=2)
    history = Subject(id=3, name='History', schedule='C', class_num=3, subject_num=3)

    # Create students
    john = Student(id=1, name='John Doe', document=123456, address='123 Street')
    jane = Student(id=2, name='Jane Smith', document=789012, address='456 Avenue')
    mike = Student(id=3, name='Mike Johnson', document=345678, address='789 Road')

    john_in_math = Enrollment(student_id=1, subject_num=1, class_num=1)

    # Add subjects and students to the session
    db.session.add_all([math, science, history, john, jane, mike, john_in_math, admin])

    # Commit the session to persist the changes
    db.session.commit()

if __name__ == '__main__':
    populate_database()