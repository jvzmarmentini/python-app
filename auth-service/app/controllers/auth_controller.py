from flask import Blueprint, jsonify, request
from app.services.auth_service import AuthService
from app.login_required_decorator import login_required
from app.repositories.auth_repository import AuthRepository

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

@auth_controller.route('/session', methods=['POST'])
def isSessionValid():
    data = request.get_json()
    session_token = data.get('sessionToken')
    valid = auth_service.is_session_valid(session_token)
    return jsonify({ 'valid': valid }), 200