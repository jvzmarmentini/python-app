from config import db
from modules.auth.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
