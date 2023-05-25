
import functools
from modules.auth.auth_service import AuthService
from flask import Blueprint, jsonify, request


auth_service = AuthService()

def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if auth_service.is_session_valid(request.headers.get('session-token')):
            return func(*args, **kwargs)
        else:
            return '', 401

    return secure_function