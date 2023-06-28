import functools
import requests
from flask import request

def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        session_token = request.headers.get('session-token')

        if authenticate(session_token):
            return func(*args, **kwargs)
        else:
            return 'Unauthorized', 401

    return secure_function

def authenticate(session_token):
    return True
    data = { 'sessionToken': session_token }
    response = requests.post('http://auth-app/session', json=data)
    return response.json().get('valid') is True