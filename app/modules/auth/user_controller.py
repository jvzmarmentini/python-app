from flask import Blueprint, jsonify, redirect, request, url_for
from modules.auth.user import User
from modules.auth.auth_service import AuthService
from config import db
from modules.common.login_required_decorator import login_required

user_controller = Blueprint('user_controller', __name__)
auth_service = AuthService()

@user_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if User.query.filter_by(email=email).first() is not None:
        return "Email already taken"

    user = User(email=email, password=password, name=name)

    db.session.add(user)
    db.session.commit()

    return '', 201

@user_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    session_token = auth_service.login(email, password)

    if session_token is None:
        return 'Invalid email or password.', 401
    
    return jsonify({ 'sessionToken': session_token }), 201

@user_controller.route('/logout')
@login_required
def logout():
    auth_service.logout(request.headers.get('session-token'))
