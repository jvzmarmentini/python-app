from config import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subjects = db.relationship('Subject', backref='student', lazy=True)

    def __repr__(self):
        return f"Student(name='{self.name}')"
