from config import db

class Enrollment(db.Model):   
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def __repr__(self):
        return f"Enrollment(subject='{self.subject_id}',student='{self.student_id}')"
