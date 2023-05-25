from sqlalchemy import UniqueConstraint
from config import db

class Subject(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    class_num  = db.Column(db.Integer, nullable=False)
    subject_num  = db.Column(db.Integer, nullable=False)
    name       = db.Column(db.String(50), nullable=False)
    schedule   = db.Column(db.String(10), nullable=False)

    # __table_args__ = (UniqueConstraint('class_num', 'subject_num'))

    def __repr__(self):
        return f"Subject(name='{self.name}')"
