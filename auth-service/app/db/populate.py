from db.config import db
from models.user import User

def populate_database():

    admin = User(id=1, email="admin@admin.com", name="admin", password="admin")
    db.session.add_all([admin])
    db.session.commit()

if __name__ == '__main__':
    populate_database()