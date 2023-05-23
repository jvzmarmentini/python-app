from modules.subjects.subject import Subject
from config import db

class SubjectRepository:

    def find_by_subject_and_class_nums(subject_num, class_num):
        subject = Subject.query.filter(Subject.class_num == class_num, Subject.subject_num == subject_num).first()
        return subject