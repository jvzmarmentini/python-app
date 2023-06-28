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
    with app.test_request_context('/1'):
        with patch.object(StudentRepository, 'get_student') as mock_get_students:
            fake_student = Student.from_dict({
                'id': 1,
                'name': 'John Doe',
                'document': 123456789,
                'address': '123 Main St'
            })

            mock_get_students.return_value = fake_student
            
            response = app.test_client().get(f'/1')
            print(f'response', response.json)

            assert response.status_code == 200
            assert response.json == fake_student.to_dict()


def test_get_non_existent_student(app):
    with app.test_request_context('/1'):
        with patch.object(StudentRepository, 'get_student') as mock_get_students:
            mock_get_students.return_value = None
            
            response = app.test_client().get(f'/1')
            print(f'response', response.json)

            assert response.status_code == 404
