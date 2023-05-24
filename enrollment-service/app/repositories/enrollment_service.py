from db.config import db
from models.enrollment import Enrollment


class EnrollmentService:
    def enroll_student_in_class(self, student_id, subject_num, class_num):
        subject = self.subject_repository.find_by_subject_and_class_nums(subject_num, class_num)
        student = self.student_repository.find_by_id(student_id)

        if subject is None:
            raise Exception(f'No subject with subject_num={subject_num} and class_num={class_num}')
        
        if student is None:
            raise Exception(f'No student with id={student_id}')

        enrollment = Enrollment(subject_num=subject_num, class_num=class_num, student_id=student_id)

        db.session.add(enrollment)
        db.session.commit()

    def list_enrollments(self):
        return Enrollment.query.all()