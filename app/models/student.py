from config import db

class Student(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(50), nullable=False)
    document   = db.Column(db.Integer, nullable=False, unique=True)
    address    = db.Column(db.String(50), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=True)

    def __repr__(self):
        return f"Student(name='{self.name}')"
