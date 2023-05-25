import functools
import requests
from flask import request

def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        session_token = request.headers.get('session-token')
        data = { 'sessionToken': session_token }
        response = requests.post('http://auth-app/session', json=data)
        
        if response.json().valid:
            return func(*args, **kwargs)
        else:
            return 'Unauthorized', 401

    return secure_function