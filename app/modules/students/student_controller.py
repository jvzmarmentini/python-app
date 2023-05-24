from flask import Blueprint, jsonify, request
from modules.students.student_repository import StudentRepository
from modules.common.login_required_decorator import login_required

student_controller = Blueprint('student_controller', __name__)
student_repo = StudentRepository()

@student_controller.route('/students', methods=['GET'])
@login_required
def get_students():
    name_query = request.args.get('name')

    students = student_repo.get_students(name_query)
    student_data = [{'id': s.id, 'name': s.name, 'document': s.document, 'address': s.address} for s in students]
    
    return jsonify(student_data)

@student_controller.route('/students/<int:id>', methods=['GET'])
@login_required
def get_student(id):
    student = student_repo.get_student(id)

    if student:
        student_data = {'id': student.id, 'name': student.name, 'document': student.document, 'address': student.address}
        return jsonify(student_data), 200
    else:
        return jsonify({'error': 'Student not found'}), 404

@student_controller.route('/students', methods=['POST'])
@login_required
def create_student():
    data = request.get_json()
    name = data.get('name')
    document = data.get('document')
    address = data.get('address')

    if not name or not document or not address:
        return jsonify({'error': 'Missing data. Please provide name, document, and address.'}), 400

    student = student_repo.create_student(name, document, address)

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

    student = student_repo.get_student(id)

    if not student:
        return jsonify({'error': 'Student not found'}), 404

    student = student_repo.update_student(student, name, document, address)

    return jsonify({'id': student.id, 'name': student.name, 'document': student.document, 'address': student.address}), 200

@student_controller.route('/students/<int:id>', methods=['DELETE'])
@login_required
def delete_student(id):
    student = student_repo.get_student(id)

    if student:
        student_repo.delete_student(student)
        return jsonify({'message': 'Student deleted'}), 200
    else:
        return jsonify({'error': 'Student not found'}), 404
