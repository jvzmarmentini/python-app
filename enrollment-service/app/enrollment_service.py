import requests
from flask import jsonify
from app.repositories.enrollment_repository import EnrollmentRepository


class EnrollmentService:
    def enroll_student_in_class(self, student_id, subject_num, class_num):
        student_response = requests.get(f'http://student-app:80/{student_id}')
        if student_response.status_code != 200:
            return jsonify({'error': 'Failed to retrieve student information.'}), 500

        subject_response = requests.get(
            f'http://subject-app:80/{subject_num}&{class_num}')
        if subject_response.status_code != 200:
            return jsonify({'error': 'Failed to retrieve subject information.'}), 500

        enrollment = EnrollmentRepository.create_enrollment(
            subject_num=subject_num,
            class_num=class_num,
            student_id=student_id
        )

        return enrollment
