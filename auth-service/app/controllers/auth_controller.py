from flask import Blueprint, jsonify, request
from services.auth_service import AuthService
from login_required_decorator import login_required
from repositories.auth_repository import AuthRepository

auth_controller = Blueprint('auth_controller', __name__)
auth_repo = AuthRepository()
auth_service = AuthService()

@auth_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if auth_repo.get_user_by_email(email) is not None:
        return "Email already taken"

    auth_repo.create_user(email=email, password=password, name=name)

    return 'Register success', 201

@auth_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    session_token = auth_service.login(email, password)

    if session_token is None:
        return 'Invalid email or password.', 401
    
    return jsonify({ 'sessionToken': session_token }), 200

@auth_controller.route('/logout', methods=['POST'])
@login_required
def logout():
    auth_service.logout(request.headers.get('session-token'))
    
    return 'Logout success', 200
