import requests
from db.config import db
from flask import jsonify
from models.enrollment import Enrollment
from sqlalchemy import func


class EnrollmentService:
    def enroll_student_in_class(self, student_id, subject_num, class_num):
        student_response = requests.get(f'http://student-app:80/{student_id}')
        if student_response.status_code != 200:
            return jsonify({'error': 'Failed to retrieve student information.'}), 500
        
        subject_response = requests.get(f'http://subject-app:80/{subject_num}&{class_num}')
        if subject_response.status_code != 200:
            return jsonify({'error': 'Failed to retrieve subject information.'}), 500
    
        enrollment = Enrollment(subject_num=subject_num, class_num=class_num, student_id=student_id)

        db.session.add(enrollment)
        db.session.commit()

    def list_enrollments(self):
        return db.session.query(
                Enrollment.class_num,
                Enrollment.subject_num,
                func.array_agg(Enrollment.student_id).label('student_ids')
            ).group_by(
                Enrollment.class_num,
                Enrollment.subject_num
            ).all()
                
    