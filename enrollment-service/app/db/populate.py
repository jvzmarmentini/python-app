from db.config import db
from models.enrollment import Enrollment

def populate_database():
    john_in_math = Enrollment(student_id=1, subject_num=1, class_num=1)

    db.session.add_all([john_in_math])

    db.session.commit()

if __name__ == '__main__':
    populate_database()