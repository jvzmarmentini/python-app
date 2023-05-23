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

@enrollment_controller.route('/enrollments', methods=['GET'])
def list_enrollments():
    student_id = request.args.get('studentId')
    subject_num = request.args.get('subjectNum')
    class_num = request.args.get('class_num')

    enrollments = enrollment_service.list_enrollments()
    
    if student_id:
        enrollments = [x for x in enrollments if x.student_id == student_id]

    if student_id:
        enrollments = [x for x in enrollments if x.subject_num == subject_num]

    if student_id:
        enrollments = [x for x in enrollments if x.class_num == class_num]

    enrollments = [{
        'id': ''
    }]

    return jsonify({'result': "aaaa" }), 201