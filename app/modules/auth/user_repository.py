from config import db
from modules.auth.user import User

class UserRepository:
    def get_user_by_email(self, email):
        return User.query.filter(User.email == email).first()

    def create_user(self, email, password, name):
        user = User(email=email, password=password, name=name)
        db.session.add(user)
        db.session.commit()
        return user
