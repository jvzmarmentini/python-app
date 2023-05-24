from db.config import db
from models.student import Student

def populate_database():
    john = Student(id=1, name='John Doe', document=123456, address='123 Street')
    jane = Student(id=2, name='Jane Smith', document=789012, address='456 Avenue')
    mike = Student(id=3, name='Mike Johnson', document=345678, address='789 Road')

    db.session.add_all([john, jane, mike])

    db.session.commit()

if __name__ == '__main__':
    populate_database()