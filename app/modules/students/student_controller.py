from flask import Blueprint, jsonify, request
from config import db
from modules.students.student import Student
from modules.common.login_required_decorator import login_required

student_controller = Blueprint('student_controller', __name__)

@student_controller.route('/students', methods=['GET'])
@login_required
def get_students():
    name_query = request.args.get('name')

    if name_query:
        students = Student.query.filter(Student.name.ilike(f'%{name_query}%')).all()
    else:
        students = Student.query.all()
    
    return jsonify([{'id': s.id, 'name': s.name, 'document': s.document, 'address': s.address} for s in students])
  
@student_controller.route('/students/<int:id>', methods=['GET'])
@login_required
def get_student(id):
    if id:
        s = Student.query.get(id)
        if s:
            return jsonify({'id': s.id, 'name': s.name, 'document': s.document, 'address': s.address})

        return jsonify({'error': 'Student not found'}), 404

@student_controller.route('/students', methods=['POST'])
@login_required
def create_student():
    data = request.get_json()
    name = data.get('name')
    document = data.get('document')
    address = data.get('address')

    if not name or not document or not address:
        return jsonify({'error': 'Missing data. Please provide name, document and address.'}), 400

    student = Student(name=name, document=document, address=address)

    db.session.add(student)
    db.session.commit()

    return jsonify({'id': student.id, 'name': student.name}), 201

@student_controller.route('/students/<int:id>', methods=['PUT'])
@login_required
def update_student(id):
    data = request.get_json()
    name = data.get('name')
    document = data.get('document')
    address = data.get('address')

    if not name or not document or not address:
        return jsonify({'error': 'Missing data. Please provide name, document, and address.'}), 400

    student = Student.query.get(id)

    if not student:
        return jsonify({'error': 'Student not found'}), 404

    student.name = name
    student.document = document
    student.address = address

    db.session.commit()

    return jsonify({'id': student.id, 'name': student.name, 'document': student.document, 'address': student.address})

@student_controller.route('/students/<int:id>', methods=['DELETE'])
@login_required
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'})
