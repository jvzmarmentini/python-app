from db.config import db
from models.subject import Subject

def populate_database():
    math = Subject(name='Math', schedule='A', class_num=1, subject_num=1)
    science = Subject(name='Science', schedule='B', class_num=2, subject_num=2)
    history = Subject(name='History', schedule='C', class_num=3, subject_num=3)

    db.session.add_all([math, science, history])

    db.session.commit()

if __name__ == '__main__':
    populate_database()