from flask import Blueprint, jsonify, request
from modules.students.student import Student
from modules.subjects.subject import Subject
from modules.common.login_required_decorator import login_required
from modules.subjects.subject_repository import SubjectRepository

subject_controller = Blueprint('subject_controller', __name__)
subject_repo = SubjectRepository()

@subject_controller.route('/students/<int:student_id>/subjects', methods=['GET'])
@login_required
def get_subjects(student_id):
    student = Student.query.get(student_id)
    subjects = student.subjects
    return jsonify([{'id': s.id, 'name': s.name} for s in subjects])

@subject_controller.route('/students/<int:student_id>/subjects', methods=['POST'])
@login_required
def create_subject():
    data = request.get_json()
    class_num = data.get('class_num')
    id = data.get('id')
    name = data.get('name')
    schedule = data.get('schedule')

    if not class_num or not id or not name or not schedule:
        return jsonify({'error': 'Missing data. Please provide Class number, Id, Name and Schedule.'}), 400

    subject = subject_repo.create_subject(class_num=class_num, id=id, name=name, schedule=schedule)

    return jsonify({'class_num': class_num, 'id': subject.id, 'name': subject.name, 'schedule': schedule}), 201

@subject_controller.route('/students/<int:student_id>/subjects/<int:id>', methods=['PUT'])
@login_required
def update_subject(student_id, id):
    data = request.get_json()
    name = data.get('name')
    schedule = data.get('schedule')

    if not name or not schedule:
        return jsonify({'error': 'Missing data. Please provide name and schedule.'}), 400

    subject = subject_repo.get_subject(id)

    if not subject:
        return jsonify({'error': 'Subject not found'}), 404

    subject_repo.update_subject(subject, name, schedule)

    return jsonify({'id': subject.id, 'name': subject.name, 'schedule': subject.schedule})

@subject_controller.route('/students/<int:student_id>/subjects/<int:id>', methods=['DELETE'])
@login_required
def delete_subject(student_id, id):
    subject = subject_repo.get_subject(id)

    if not subject:
        return jsonify({'error': 'Subject not found'}), 404

    subject_repo.delete_subject(subject)

    return jsonify({'message': 'Subject deleted'})
