from db.config import db

class Subject(db.Model):
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_num  = db.Column(db.Integer, nullable=False)
    subject_num  = db.Column(db.Integer, nullable=False, unique=True)
    name       = db.Column(db.String(50), nullable=False)
    schedule   = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Subject(name='{self.name}')"
