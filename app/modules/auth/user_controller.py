from flask import Blueprint, jsonify, request
from modules.auth.auth_service import AuthService
from config import db
from modules.common.login_required_decorator import login_required
from modules.auth.user_repository import UserRepository

user_controller = Blueprint('user_controller', __name__)
user_repo = UserRepository()
auth_service = AuthService()

@user_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if user_repo.get_user_by_email(email) is not None:
        return "Email already taken"

    user_repo.create_user(email=email, password=password, name=name)

    return 'Register success', 201

@user_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    session_token = auth_service.login(email, password)

    if session_token is None:
        return 'Invalid email or password.', 401
    
    return jsonify({ 'sessionToken': session_token }), 200

@user_controller.route('/logout', methods=['POST'])
@login_required
def logout():
    auth_service.logout(request.headers.get('session-token'))
    
    return 'Logout success', 200
