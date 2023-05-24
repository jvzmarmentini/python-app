from uuid import uuid4
from modules.auth.user import User
from modules.auth.user_repository import UserRepository

user_repo = UserRepository()
session_store_global = {}

class AuthService:

    def __init__(self):
        self.sessionStore = session_store_global

    def login(self, email, password):
        user = user_repo.get_user_by_email(email)
        print(user)

        if user and user.password == password:
            return self.create_token(user.id)

        return None

    def create_token(self, user_id):
        session_token = uuid4()
        self.sessionStore[user_id] = str(session_token)
        self.sessionStore[str(session_token)] = user_id
        return session_token
    
    def logout(self, session_token):
        self.sessionStore.pop(self.sessionStore[session_token])
        self.sessionStore.pop(session_token)
    
    def is_session_valid(self, session_token):
        return session_token in self.sessionStore