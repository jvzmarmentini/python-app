from config import db

class Subject(db.Model):
    class_num  = db.Column(db.Integer, primary_key=True) # different classes with same subject
    id         = db.Column(db.Integer, nullable=False)
    name       = db.Column(db.String(50), nullable=False)
    schedule   = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Subject(name='{self.name}')"
