import pytest
from pytest_mock import module_mocker
from flask import Flask
from app.db.config import db
from app.controllers.student_controller import student_controller
from app.controllers.health_controller import health_controller
from app.models import Student

@pytest.fixture(scope='module')
def test_app():
    app = Flask(__name__)
    app.register_blueprint(student_controller)
    app.register_blueprint(health_controller)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    db.init_app(app)

    with app.app_context():
        db.create_all()

        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='module')
def mocked_db(test_app):

    with test_app.app_context():
        john = Student(name='John Doe', document=123456, address='123 Street')
        jane = Student(name='Jane Smith', document=789012, address='456 Avenue')
        mike = Student(name='Mike Johnson', document=345678, address='789 Road')
        db.session.add_all([john, jane, mike])
        db.session.commit()

    yield db  # Retorna o banco de dados para que os testes possam ser executados

    with test_app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='module')
def test_client(test_app, mocked_db):
    return test_app.test_client()


@pytest.fixture(scope='module')
def mocked_auth_service(module_mocker):
    module_mocker.patch('app.login_required_decorator.requests.post').return_value.json.return_value = {'valid': True}
    # module_mocker.patch.object('app.login_required_decorator','requests.post', {'valid': True})


def test_get_students(test_client, mocked_auth_service):
    response = test_client.get('/')
    assert response.status_code == 200

    data = response.get_json()
    print(data)
    # Verifica se retornou a quantidade correta de alunos
    assert len(data) == 3


def test_get_student(test_client, mocked_auth_service):
    response = test_client.get('/1')
    assert response.status_code == 200

    data = response.get_json()
    assert data['name'] == 'John Doe'


def test_create_student(test_client, mocked_auth_service):
    new_student = {
        'name': 'Alice Johnson',
        'document': 999999,
        'address': '789 Oak St'
    }

    response = test_client.post('/', json=new_student)
    assert response.status_code == 201

    data = response.get_json()
    assert data['name'] == 'Alice Johnson'
    assert 'id' in data


def test_update_student(test_client, mocked_auth_service):
    updated_student = {
        'name': 'John Doe',
        'document': 123456,
        'address': '321 Elm St'
    }

    response = test_client.put('/1', json=updated_student)
    assert response.status_code == 200

    data = response.get_json()
    assert data['address'] == '321 Elm St'


def test_delete_student(test_client, mocked_auth_service):
    response = test_client.delete('/2')
    assert response.status_code == 200

    data = response.get_json()
    assert data['message'] == 'Student deleted'


def test_health_student(test_client):
    response = test_client.get('/health')
    assert response.status_code == 200