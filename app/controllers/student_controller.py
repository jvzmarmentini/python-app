from flask import Blueprint, jsonify, request
from config import db
from models.student import Student

student_controller = Blueprint('student_controller', __name__)

@student_controller.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': s.id, 'name': s.name} for s in students])

@student_controller.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(name=data['name'])
    db.session.add(student)
    db.session.commit()
    return jsonify({'id': student.id, 'name': student.name})

@student_controller.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = Student.query.get(id)
    student.name = data['name']
    db.session.commit()
    return jsonify({'id': student.id, 'name': student.name})

@student_controller.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'})
