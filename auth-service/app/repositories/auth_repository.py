from db.config import db
from models.user import User

class AuthRepository:
    def get_user_by_email(self, email):
        return User.query.filter(User.email == email).first()

    def create_user(self, email, password, name):
        user = User(email=email, password=password, name=name)
        db.session.add(user)
        db.session.commit()
        return user
