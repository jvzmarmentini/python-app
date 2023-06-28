import pytest
from unittest.mock import patch
from flask import Flask
from app.controllers.student_controller import student_controller
from app.repositories.student_repository import StudentRepository


@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    app.register_blueprint(student_controller)
    return app


@pytest.fixture(scope='module')
def mocked_auth_service(module_mocker):
    module_mocker.patch(
        'app.login_required_decorator.requests.post').return_value.json.return_value = {'valid': True}


def test_get_students(app, mocked_auth_service):
    with app.test_request_context('/'):
        with patch.object(StudentRepository, 'get_students') as mock_get_students:
            mock_get_students.return_value = [
                {'id': 1, 'name': 'John Doe',
                 'document': 123456789, 'address': '123 Main St'},
                {'id': 2, 'name': 'John Smith',
                 'document': 987654321, 'address': '456 Elm St'}
            ]

            response = app.test_client().get('/')

            assert response.status_code == 200
            assert response.json == [
                {'id': 1, 'name': 'John Doe',
                 'document': 123456789, 'address': '123 Main St'},
                {'id': 2, 'name': 'John Smith',
                 'document': 987654321, 'address': '456 Elm St'}
            ]
