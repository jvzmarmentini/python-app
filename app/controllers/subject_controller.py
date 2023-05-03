from flask import Blueprint, jsonify, request
from config import db
from models.student import Student
from models.subject import Subject

subject_controller = Blueprint('subject_controller', __name__)

@subject_controller.route('/students/<int:student_id>/subjects', methods=['GET'])
def get_subjects(student_id):
    student = Student.query.get(student_id)
    subjects = student.subjects
    return jsonify([{'id': s.id, 'name': s.name} for s in subjects])

@subject_controller.route('/students/<int:student_id>/subjects', methods=['POST'])
def create_subject(student_id):
    data = request.get_json()
    subject = Subject(name=data['name'], student_id=student_id)
    db.session.add(subject)
    db.session.commit()
    return jsonify({'id': subject.id, 'name': subject.name})

@subject_controller.route('/students/<int:student_id>/subjects/<int:id>', methods=['PUT'])
def update_subject(student_id, id):
    data = request.get_json()
    subject = Subject.query.get(id)
    subject.name = data['name']
    db.session.commit()
    return jsonify({'id': subject.id, 'name': subject.name})

@subject_controller.route('/students/<int:student_id>/subjects/<int:id>', methods=['DELETE'])
def delete_subject(student_id, id):
    subject = Subject.query.get(id)
    db.session.delete(subject)
    db.session.commit()
    return jsonify({'message': 'Subject deleted'})
