import requests
from flask import Blueprint, jsonify, request
from repositories.enrollment_service import EnrollmentService

enrollment_controller = Blueprint('enrollment_controller', __name__)
enrollment_service = EnrollmentService()

@enrollment_controller.route('/', methods=['POST'])
def enroll_student_in_class():
    data = request.get_json()
    
    student_id = data.get('studentId')
    subject_id = data.get('subjectId')
    
    if not student_id or not subject_id:
        return jsonify({'error': 'Missing data. Please provide subjectNum, classNum, studentId.'}), 400
    
    student_response = requests.get(f'localhost:81/{student_id}')
    if student_response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve student information.'}), 500
    
    print(f"{student_response.status_code=}")
    
    subject_response = requests.get(f'localhost:82/{subject_id}')
    if subject_response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve subject information.'}), 500

    print(f"{subject_response.status_code=}")

    # enrollment_service.enroll_student_in_class(student_id, subject_num, class_num)

    return '', 201

@enrollment_controller.route('/', methods=['GET'])
def list_enrollments():
    student_id = request.args.get('studentId', type=int)
    subject_num = request.args.get('subjectNum', type=int)
    class_num = request.args.get('classNum', type=int)

    enrollments = enrollment_service.list_enrollments()
    

    if student_id:
        enrollments = [x for x in enrollments if x.student_id == student_id]

    if subject_num:
        enrollments = [x for x in enrollments if x.subject_num == subject_num]

    if class_num:
        enrollments = [x for x in enrollments if x.class_num == class_num]

    enrollments = [{
        'student_id': x.student_id,
        'subject_num': x.subject_num,
        'class_num': x.class_num,
    } for x in enrollments]

    return jsonify({'result': enrollments }), 200