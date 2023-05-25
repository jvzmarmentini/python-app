from config import db
from modules.subjects.subject import Subject

class SubjectRepository:
    def get_subject(self, subject_id):
        return Subject.query.get(subject_id)

    def create_subject(self, class_num, id, name, schedule):
        subject = Subject(class_num=class_num, id=id, name=name, schedule=schedule)
        db.session.add(subject)
        db.session.commit()
        return subject

    def update_subject(self, subject, name, schedule):
        subject.name = name
        subject.schedule = schedule
        db.session.commit()

    def delete_subject(self, subject):
        db.session.delete(subject)
        db.session.commit()
