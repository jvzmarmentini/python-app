from modules.students.student_repository import StudentRepository
from config import db
from modules.enrollments.enrollment import Enrollment
from modules.subjects.subject_repository import SubjectRepository


class EnrollmentService:

    def __init__(self):
        self.subject_repository = SubjectRepository()
        self.student_repository = StudentRepository()

    def enroll_student_in_class(self, student_id, subject_num, class_num):
        subject = self.subject_repository.find_by_class_and_subject_nums(subject_num, class_num)
        student = self.student_repository.find_by_id(student_id)

        if subject is None:
            raise f'No subject with subject_num={subject_num} and class_num={class_num}'
        
        if student is None:
            raise f'No student with id={student_id}'

        
        enrollment = Enrollment(subject_id=subject.id, student_id=student_id)

        db.session.add(enrollment)
        db.session.commit()