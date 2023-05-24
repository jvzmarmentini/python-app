from flask import Blueprint, jsonify, redirect, request, url_for
from modules.auth.user import User
from modules.auth.auth_service import AuthService
from config import db
from modules.common.login_required_decorator import login_required

user_controller = Blueprint('user_controller', __name__)
auth_service = AuthService()

@user_controller.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    ---
    tags:
      - User
    parameters:
      - name: email
        in: body
        description: User's email
        required: true
        type: string
      - name: password
        in: body
        description: User's password
        required: true
        type: string
      - name: name
        in: body
        description: User's name
        required: true
        type: string
    responses:
      201:
        description: User registered successfully.
      400:
        description: Email already taken.
    """    
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
    """
    Log in a user.
    ---
    tags:
      - User
    parameters:
      - name: email
        in: body
        description: User's email
        required: true
        type: string
      - name: password
        in: body
        description: User's password
        required: true
        type: string
    responses:
      201:
        description: User logged in successfully.
      401:
        description: Invalid email or password.
    """
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
    """
    Log out a user.
    ---
    tags:
      - User
    parameters:
      - name: auth
        in: header
        description: an authorization header
        required: true
        type: string
    responses:
      200:
        description: User logged out successfully.
      401:
        description: Unauthorized - session token required.
    """
    auth_service.logout(request.headers.get('session-token'))
