from sqlalchemy import func

from app.db.config import db
from app.models.enrollment import Enrollment


class EnrollmentRepository:
    def get_enrollments():
        query = db.session.query(
            Enrollment.class_num,
            Enrollment.subject_num,
            func.array_agg(Enrollment.student_id).label('student_ids')
        ).group_by(
            Enrollment.class_num,
            Enrollment.subject_num
        ).all()

        return query

    def create_enrollment(subject_num, class_num, student_id):
        try:
            enrollment = Enrollment(subject_num=subject_num,
                                    class_num=class_num, student_id=student_id)

            db.session.add(enrollment)
            db.session.commit()

            return enrollment
        except:
            return None
