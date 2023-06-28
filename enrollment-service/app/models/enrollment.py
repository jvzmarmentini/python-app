from app.db.config import db

class Enrollment(db.Model):
    subject_num = db.Column(db.Integer, nullable=False, primary_key=True)
    class_num = db.Column(db.Integer, nullable=False, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False, primary_key=True)

    def __repr__(self):
        return f"Enrollment(subject_num={self.subject_num}, class_num={self.class_num}, student_id={self.student_id})"
