import sys
from flask import Blueprint, jsonify, request
from modules.common.login_required_decorator import login_required
from modules.enrollments.enrollment_service import EnrollmentService

enrollment_controller = Blueprint('enrollment_controller', __name__)
enrollment_service = EnrollmentService()

@enrollment_controller.route('/enrollments', methods=['POST'])
@login_required
def enroll_student_in_class():
    """
    Enroll a student in a class.
    ---
    tags:
      - Enrollments
    parameters:
      - name: subjectNum
        in: body
        description: Subject number
        required: true
        type: int
      - name: classNum
        in: body
        description: Class number
        required: true
        type: int
      - name: studentId
        in: body
        description: Student ID
        required: true
        type: int
      - name: auth
        in: header
        description: an authorization header
        required: true
        type: string
    responses:
      201:
        description: Student enrolled in class successfully.
      400:
        description: Missing data. Please provide subjectNum, classNum, studentId.
    """
    data = request.get_json()

    subject_num = data.get('subjectNum')
    class_num = data.get('classNum')
    student_id = data.get('studentId')

    if not subject_num or not class_num or not student_id:
        return jsonify({'error': 'Missing data. Please provide subjectNum, classNum, studentId.'}), 400

    enrollment_service.enroll_student_in_class(student_id, subject_num, class_num)

    return '', 201

@enrollment_controller.route('/enrollments', methods=['GET'])
@login_required
def list_enrollments():
    """
    List enrollments.
    ---
    tags:
      - Enrollments
    parameters:
      - name: studentId
        in: query
        description: Student ID
        required: false
        type: int
      - name: subjectNum
        in: query
        description: Subject number
        required: false
        type: int
      - name: classNum
        in: query
        description: Class number
        required: false
        type: int
      - name: auth
        in: header
        description: an authorization header
        required: true
        type: string
    responses:
      200:
        description: List of enrollments.
    """
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