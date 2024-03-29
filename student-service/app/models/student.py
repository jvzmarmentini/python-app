from app.db.config import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    document = db.Column(db.Integer, nullable=False, unique=True)
    address = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Student({self.id=}, {self.name=}, {self.document=}, {self.address=})"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'document': self.document,
            'address': self.address
        }
    
    def from_dict(data):
        student = Student()
        for field in data:
            if field in data:
                setattr(student, field, data[field])

        return student
