import pytest
from unittest.mock import patch
from flask import Flask
from app.controllers.student_controller import student_controller
from app.repositories.student_repository import StudentRepository
from app.models.student import Student

@pytest.fixture(scope='module')
def mocked_authenticate():
    with patch('app.login_required_decorator.authenticate') as mock:
        mock.return_value = True
        yield mock

@pytest.fixture(scope='module')
def app(mocked_authenticate):
    app = Flask(__name__)
    app.register_blueprint(student_controller)
    return app


def test_get_students(app):
    with app.test_request_context('/'):
        with patch.object(StudentRepository, 'get_students') as mock_get_students:
            fake_students = [
                Student.from_dict({
                    'id': 1,
                    'name': 'John Doe',
                    'document': 123456789,
                    'address': '123 Main St'
                }),
                Student.from_dict({
                    'id': 2,
                    'name':
                    'John Smith',
                    'document': 987654321,
                    'address': '456 Elm St'
                })
            ]
            mock_get_students.return_value = fake_students

            response = app.test_client().get('/')

            assert response.status_code == 200
            assert response.json == [fake_student.to_dict() for fake_student in fake_students]


def test_get_student(app):
    with app.test_request_context('/'):
        with patch.object(StudentRepository, 'get_student') as mock_get_students:
            fake_student = Student.from_dict({
                'id': 1,
                'name': 'John Doe',
                'document': 123456789,
                'address': '123 Main St'
            })

            mock_get_students.return_value = fake_student
            
            response = app.test_client().get('/1')

            assert response.status_code == 200
            assert response.json == fake_student.to_dict()


def test_get_non_existent_student(app):
    with app.test_request_context('/'):
        with patch.object(StudentRepository, 'get_student') as mock_get_students:
            mock_get_students.return_value = None
            
            response = app.test_client().get('/1')

            assert response.status_code == 404


def test_create_student(app):
    with app.test_request_context('/'):
        with patch.object(StudentRepository, 'create_student') as mock_create_student:
            with patch.object(StudentRepository, 'get_student_by_doc') as mock_get_student_by_doc:
                mock_create_student.side_effect = lambda name, document, address: Student(id=1, name=name, document=document, address=address)
                mock_get_student_by_doc.return_value = None

                student_to_create = {
                    'name': 'John Doe',
                    'document': 123456789,
                    'address': '123 Main St'
                }

                response = app.test_client().post('/', json=student_to_create)

                assert response.status_code == 201
                assert response.json == {
                    'id': 1,
                    'name': student_to_create.get('name')
                }


def test_create_invalid_student(app):
    with app.test_request_context('/'):
        with patch.object(StudentRepository, 'create_student') as mock_create_student:
            mock_create_student.side_effect = lambda name, document, address: Student(id=1, name=name, document=document, address=address)
            student_to_create = {
                'name': 'John Doe',
                'document': 123456789,
                # missing address
            }

            response = app.test_client().post('/', json=student_to_create)

            assert response.status_code == 400


def test_create_duplicated_student(app):
    with app.test_request_context('/'):
        with patch.object(StudentRepository, 'get_student_by_doc') as mock_get_student_by_doc:
            mock_get_student_by_doc.return_value = Student(id=1, name='John Doe', document=123456789, address='123 Main St')

            student_to_create = {
                'name': 'John Doe',
                'document': 123456789,
                'address': '123 Main St'
            }

            response = app.test_client().post('/', json=student_to_create)

            assert response.status_code == 400

def test_update_student(app):
    pass


def test_update_non_existent_student(app):
    pass


def test_delete_student(app):
    pass


def test_delete_non_existent_student(app):
    pass