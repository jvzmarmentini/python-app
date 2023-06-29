import pytest
from unittest.mock import patch
from app.models.user import User
from app.repositories.auth_repository import AuthRepository
from app.services.auth_service import AuthService


def test_login_with_valid_credentials():
    
    with patch.object(AuthRepository, "get_user_by_email") as mock_get_user_by_email:
        email = "test@example.com"
        password = "password123"
        user_id = 1
        session_token = "session_token"
        
        mock_get_user_by_email.return_value = User(id=user_id, email=email, password=password)

        auth_service = AuthService()

        auth_service.create_token = lambda _: session_token

        result = auth_service.login(email, password)

        assert result == session_token


def test_login_with_invalid_credentials():
    with patch.object(AuthRepository, "get_user_by_email") as mock_get_user_by_email:
        email = "test@example.com"
        password = "password123"
        
        mock_get_user_by_email.return_value = None

        auth_service = AuthService()

        result = auth_service.login(email, password)

        assert result == None


def test_logout():
    session_token = "session_token"
    user_id = 1

    auth_service = AuthService()
    auth_service.sessionStore[user_id] = session_token
    auth_service.sessionStore[session_token] = user_id

    auth_service.logout(session_token)

    assert user_id not in auth_service.sessionStore
    assert session_token not in auth_service.sessionStore

def test_is_session_valid_with_valid_session_token():
    session_token = "session_token"

    auth_service = AuthService()
    auth_service.sessionStore[session_token] = 1

    result = auth_service.is_session_valid(session_token)

    assert result is True