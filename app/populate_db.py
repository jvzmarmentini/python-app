from config import db
from modules.students.student import Student
from modules.subjects.subject import Subject

def populate_database():
    # Create subjects
    math = Subject(name='Math', schedule='A', class_num=1, subject_num=1)
    science = Subject(name='Science', schedule='B', class_num=2, subject_num=2)
    history = Subject(name='History', schedule='C', class_num=3, subject_num=3)

    # Create students
    john = Student(name='John Doe', document=123456, address='123 Street')
    jane = Student(name='Jane Smith', document=789012, address='456 Avenue')
    mike = Student(name='Mike Johnson', document=345678, address='789 Road')

    # Add subjects and students to the session
    db.session.add_all([math, science, history, john, jane, mike])

    # Commit the session to persist the changes
    db.session.commit()

if __name__ == '__main__':
    populate_database()