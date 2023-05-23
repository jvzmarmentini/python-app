from flask import Blueprint, jsonify, request
from modules.enrollments.enrollment_service import EnrollmentService
from config import db

enrollment_controller = Blueprint('enrollment_controller', __name__)
enrollment_service = EnrollmentService()

@enrollment_controller.route('/enrollments', methods=['POST'])
def enroll_student_in_class():
    data = request.get_json()

    subject_num = data.get('subjectNum')
    class_num = data.get('classNum')
    student_id = data.get('studentId')

    if not subject_num or not class_num or not student_id:
        return jsonify({'error': 'Missing data. Please provide subjectNum, classNum, studentId.'}), 400

    enrollment_service.enroll_student_in_class(student_id, subject_num, class_num)

    return '', 201