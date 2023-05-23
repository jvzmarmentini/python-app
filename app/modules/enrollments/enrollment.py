from config import db

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_num = db.Column(db.Integer, nullable=False)
    class_num = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Enrollment(subject_num='{self.subject_num}',class_num='{self.class_num}',student='{self.student_id}')"
