import pytest
import json
from flask import Flask
from unittest.mock import MagicMock, patch
from app.repositories.student_repository import StudentRepository
from app.controllers.student_controller import student_controller

def mock_login_required(func):
    def mock_secure_function(*args, **kwargs):
        return func(*args, **kwargs)
    return mock_secure_function

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(student_controller)
    return app

@pytest.fixture(autouse=True)
def mock_auth_decorator(monkeypatch):
    monkeypatch.setattr("app.login_required_decorator.login_required", mock_login_required)
    
def test_get_student(app):
    # Mocking the repository behavior
    with patch.object(StudentRepository, 'get_student') as mock_get_student:
        mock_get_student.return_value = MagicMock(id=1, name='John Doe', document=123456789, address='123 Main St')

        # Making the request to the endpoint
        response = app.test_client().get('/1')

        # Asserting the response status code and data
        assert response.status_code == 200
        assert response.json == {'id': 1, 'name': 'John Doe', 'document': 123456789, 'address': '123 Main St'}


# def test_get_student(client, student_repo):
#     # Create a test student
#     student = student_repo.create_student('John Doe', '12345', '123 Street')

#     response = client.get(f'/{student.id}')

#     # Assert the response
#     assert response.status_code == 200
#     assert response.json == {
#         'id': student.id,
#         'name': 'John Doe',
#         'document': '12345',
#         'address': '123 Street'
#     }

# def test_get_student_not_found(client):
#     response = client.get('/123')

#     # Assert the response
#     assert response.status_code == 404
#     assert response.json == {'error': 'Student not found'}

# Add more test functions for other routes and scenarios
