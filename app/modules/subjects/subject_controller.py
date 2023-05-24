from flask import Blueprint, jsonify, request
from config import db
from modules.students.student import Student
from modules.subjects.subject import Subject
from modules.common.login_required_decorator import login_required

subject_controller = Blueprint('subject_controller', __name__)

@subject_controller.route('/students/<int:student_id>/subjects', methods=['GET'])
@login_required
def get_subjects(student_id):
    """
    Get subjects for a student.
    ---
    tags:
      - Subjects
    parameters:
      - name: student_id
        in: path
        description: Student ID
        required: true
        type: int
      - name: auth
        in: header
        description: an authorization header
        required: true
        type: string
    responses:
      200:
        description: List of subjects for the student.
    """
    student = Student.query.get(student_id)
    subjects = student.subjects
    return jsonify([{'id': s.id, 'name': s.name} for s in subjects])

@subject_controller.route('/students/<int:student_id>/subjects', methods=['POST'])
@login_required
def create_subject():
    """
    Create a new subject.
    ---
    tags:
      - Subjects
    parameters:
      - name: student_id
        in: path
        description: Student ID
        required: true
        type: int
      - name: class_num
        in: body
        description: Class number
        required: true
        type: int
      - name: id
        in: body
        description: Subject ID
        required: true
        type: int
      - name: name
        in: body
        description: Subject name
        required: true
        type: string
      - name: schedule
        in: body
        description: Subject schedule
        required: true
        type: string
      - name: auth
        in: header
        description: an authorization header
        required: true
        type: string
    responses:
      201:
        description: Subject created successfully.
      400:
        description: Missing data. Please provide Class number, Id, Name, and Schedule.
    """
    data = request.get_json()
    class_num = data.get('class_num')
    id = data.get('id')
    name = data.get('name')
    schedule = data.get('schedule')

    if not class_num or not id or not name or not schedule:
        return jsonify({'error': 'Missing data. Please provide Class number, Id, Name and Schedule.'}), 400

    subject = Subject(class_num=class_num, id=id, name=name, schedule=schedule)

    db.session.add(subject)
    db.session.commit()

    return jsonify({'class_num': class_num, 'id': subject.id, 'name': subject.name, 'schedule': schedule}), 201

@subject_controller.route('/students/<int:student_id>/subjects/<int:id>', methods=['PUT'])
@login_required
def update_subject(student_id, id):
    """
    Update a subject.
    ---
    tags:
      - Subjects
    parameters:
      - name: student_id
        in: path
        description: Student ID
        required: true
        type: int
      - name: id
        in: path
        description: Subject ID
        required: true
        type: int
      - name: name
        in: body
        description: Subject name
        required: true
        type: string
      - name: schedule
        in: body
        description: Subject schedule
        required: true
        type: string
      - name: auth
        in: header
        description: an authorization header
        required: true
        type: string
    responses:
      200:
        description: Subject updated successfully.
      400:
        description: Missing data. Please provide name and schedule.
      404:
        description: Subject not found.
    """
    data = request.get_json()
    name = data.get('name')
    schedule = data.get('schedule')

    if not name or not schedule:
        return jsonify({'error': 'Missing data. Please provide name and schedule.'}), 400

    subject = Subject.query.get(id)

    if not subject:
        return jsonify({'error': 'Subject not found'}), 404

    subject.name = name
    subject.schedule = schedule

    db.session.commit()

    return jsonify({'id': subject.id, 'name': subject.name, 'schedule': subject.schedule})

@subject_controller.route('/students/<int:student_id>/subjects/<int:id>', methods=['DELETE'])
@login_required
def delete_subject(student_id, id):
    """
    Delete a subject.
    ---
    tags:
      - Subjects
    parameters:
      - name: student_id
        in: path
        description: Student ID
        required: true
        type: int
      - name: id
        in: path
        description: Subject ID
        required: true
        type: int
      - name: auth
        in: header
        description: an authorization header
        required: true
        type: string
    responses:
      200:
        description: Subject deleted successfully.
    """
    subject = Subject.query.get(id)
    db.session.delete(subject)
    db.session.commit()
    return jsonify({'message': 'Subject deleted'})
