from flask import Blueprint, jsonify, request
from repositories.enrollment_service import EnrollmentService

enrollment_controller = Blueprint('enrollment_controller', __name__)
enrollment_service = EnrollmentService()

@enrollment_controller.route('/', methods=['POST'])
def enroll_student_in_class():
    data = request.get_json()
    
    student_id = data.get('studentId')
    subject_num = data.get('subjectNum')
    class_num = data.get('classNum')
    
    if not student_id or not subject_num or not class_num:
        return jsonify({'error': 'Missing data. Please provide subjectNum, classNum, studentId.'}), 400
    
    enrollment_service.enroll_student_in_class(student_id, subject_num, class_num)

    return 'Enroll success', 201

@enrollment_controller.route('/', methods=['GET'])
def list_enrollments():
    enrollments = enrollment_service.list_enrollments()

    enrollment_data = [{'class_num': e.class_num, 'subject_num': e.subject_num, "student_ids": e.student_ids} for e in enrollments]
    
    return jsonify(enrollment_data), 200