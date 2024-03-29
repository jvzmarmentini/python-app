from flask import Blueprint, jsonify, request
from repositories.subject_repository import SubjectRepository
from login_required_decorator import login_required

subject_controller = Blueprint('subject_controller', __name__)
subject_repo = SubjectRepository()

@subject_controller.route('/', methods=['GET'])
@login_required
def get_subjects():
    name_query = request.args.get('name')

    subjects = subject_repo.get_subjects(name_query)
    
    return jsonify([{'id': s.id, 'class_num': s.class_num, 'subject_num': s.subject_num, 'name': s.name, 'schedule': s.schedule} for s in subjects]), 200

@subject_controller.route('/<int:subject_num>&<int:class_num>', methods=['GET'])
@login_required
def get_subject(subject_num, class_num):
    if subject_num is None or class_num is None:
        return jsonify({'error': 'Invalid parameters. Please provide subject_num and class_num.'}), 400

    subject = subject_repo.get_subject_by_uniques(subject_num, class_num)

    if subject is None:
        return jsonify({'error': 'Subject not found.'}), 404

    return jsonify({'id': subject.id, 'class_num': subject.class_num, 'subject_num': subject.subject_num, 'name': subject.name, 'schedule': subject.schedule}), 200

@subject_controller.route('/', methods=['POST'])
@login_required
def create_subject():
    data = request.get_json()
    class_num = data.get('class_num')
    subject_num = data.get('subject_num')
    name = data.get('name')
    schedule = data.get('schedule')

    if not class_num or not subject_num or not name or not schedule:
        return jsonify({'error': 'Missing data. Please provide Class number, Id, Name and Schedule.'}), 400

    subject = subject_repo.create_subject(class_num=class_num, subject_num=subject_num, name=name, schedule=schedule)

    return jsonify({'class_num': class_num, 'subject_num': subject.subject_num, 'name': subject.name, 'schedule': schedule}), 201

@subject_controller.route('/<int:id>', methods=['PUT'])
@login_required
def update_subject(id):
    data = request.get_json()
    name = data.get('name')
    schedule = data.get('schedule')

    if not name or not schedule:
        return jsonify({'error': 'Missing data. Please provide name and schedule.'}), 400

    subject = subject_repo.get_subject(id)

    if not subject:
        return jsonify({'error': 'Subject not found'}), 404

    subject_repo.update_subject(subject, name, schedule)

    return jsonify({'id': subject.id, 'name': subject.name, 'schedule': subject.schedule}), 200

@subject_controller.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_subject(id):
    subject = subject_repo.get_subject(id)

    if not subject:
        return jsonify({'error': 'Subject not found'}), 404

    subject_repo.delete_subject(subject)

    return jsonify({'message': 'Subject deleted'}), 200
