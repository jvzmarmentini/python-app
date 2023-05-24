from flask import Blueprint, jsonify, request
from repositories.student_repository import StudentRepository

student_controller = Blueprint('student_controller', __name__)
student_repo = StudentRepository()

@student_controller.route('/', methods=['GET'])
def get_students():
    """
    Get a list of students.
    ---
    tags:
      - Students
    parameters:
      - name: name
        in: query
        description: Name query for filtering students
        required: false
        type: string
      - name: auth
        in: header
        description: an authorization header
        required: true
        type: string
    responses:
      200:
        description: List of students.
    """
    name_query = request.args.get('name')

    students = student_repo.get_students(name_query)
    student_data = [{'id': s.id, 'name': s.name, 'document': s.document, 'address': s.address} for s in students]
    
    return jsonify(student_data)

@student_controller.route('/<int:id>', methods=['GET'])
def get_student(id):
    """
    Get a student by ID.
    ---
    tags:
      - Students
    parameters:
      - name: id
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
        description: Student information.
      404:
        description: Student not found.
    """
    student = student_repo.get_student(id)

    if student:
        student_data = {'id': student.id, 'name': student.name, 'document': student.document, 'address': student.address}
        return jsonify(student_data), 200
    else:
        return jsonify({'error': 'Student not found'}), 404

@student_controller.route('/', methods=['POST'])
def create_student():
    """
    Create a new student.
    ---
    tags:
      - Students
    parameters:
      - name: name
        in: body
        description: Student name
        required: true
        type: string
      - name: document
        in: body
        description: Student document
        required: true
        type: string
      - name: address
        in: body
        description: Student address
        required: true
        type: string
      - name: auth
        in: header
        description: an authorization header
        required: true
        type: string
    responses:
      201:
        description: Student created successfully.
      400:
        description: Missing data. Please provide name, document, and address.
    """
    data = request.get_json()
    name = data.get('name')
    document = data.get('document')
    address = data.get('address')

    if not name or not document or not address:
        return jsonify({'error': 'Missing data. Please provide name, document, and address.'}), 400

    student = student_repo.create_student(name, document, address)

    return jsonify({'id': student.id, 'name': student.name}), 201

@student_controller.route('/<int:id>', methods=['PUT'])
def update_student(id):
    """
    Update a student.
    ---
    tags:
      - Students
    parameters:
      - name: id
        in: path
        description: Student ID
        required: true
        type: int
      - name: name
        in: body
        description: Student name
        required: true
        type: string
      - name: document
        in: body
        description: Student document
        required: true
        type: string
      - name: address
        in: body
        description: Student address
        required: true
        type: string
      - name: auth
        in: header
        description: an authorization header
        required: true
        type: string
    responses:
      200:
        description: Student updated successfully.
      400:
        description: Missing data. Please provide name, document, and address.
      404:
        description: Student not found.
    """
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

@student_controller.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    """
    Delete a student.
    ---
    tags:
      - Students
    parameters:
      - name: id
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
        description: Student deleted successfully.
    """
    student = student_repo.get_student(id)

    if student:
        student_repo.delete_student(student)
        return jsonify({'message': 'Student deleted'}), 200
    else:
        return jsonify({'error': 'Student not found'}), 404
