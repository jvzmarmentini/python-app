from db.config import db
from models.subject import Subject

class SubjectRepository:
    def get_subjects(self, name_query=None):
        if name_query:
            students = Subject.query.filter(Subject.name.ilike(f'%{name_query}%')).all()
        else:
            students = Subject.query.all()
        
        return students
    
    def get_subject(self, subject_id):
        return Subject.query.get(subject_id)

    def create_subject(self, class_num, subject_num, name, schedule):
        subject = Subject(class_num=class_num, subject_num=subject_num, name=name, schedule=schedule)
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
