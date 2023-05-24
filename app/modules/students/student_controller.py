from flask import Blueprint, jsonify, request
from config import db
from modules.students.student import Student
from modules.common.login_required_decorator import login_required

student_controller = Blueprint('student_controller', __name__)

@student_controller.route('/students', methods=['GET'])
@login_required
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

    if name_query:
        students = Student.query.filter(Student.name.ilike(f'%{name_query}%')).all()
    else:
        students = Student.query.all()
    
    return jsonify([{'id': s.id, 'name': s.name, 'document': s.document, 'address': s.address} for s in students])
  
@student_controller.route('/students/<int:id>', methods=['GET'])
@login_required
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
    if id:
        s = Student.query.get(id)
        if s:
            return jsonify({'id': s.id, 'name': s.name, 'document': s.document, 'address': s.address})

        return jsonify({'error': 'Student not found'}), 404

@student_controller.route('/students', methods=['POST'])
@login_required
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
        return jsonify({'error': 'Missing data. Please provide name, document and address.'}), 400

    student = Student(name=name, document=document, address=address)

    db.session.add(student)
    db.session.commit()

    return jsonify({'id': student.id, 'name': student.name}), 201

@student_controller.route('/students/<int:id>', methods=['PUT'])
@login_required
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
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'})
