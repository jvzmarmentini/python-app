from app.db.config import db
from app.models.student import Student

class StudentRepository:
    def get_students(self, name_query=None):
        if name_query:
            students = Student.query.filter(Student.name.ilike(f'%{name_query}%')).all()
        else:
            students = Student.query.all()
        
        return students
        
    
    def get_student(self, id):
        return Student.query.get(id)

    def get_student_by_doc(self, document):
        return Student.query.filter_by(document=document).first() 

    def create_student(self, name, document, address):
        student = Student(name=name, document=document, address=address)

        db.session.add(student)
        db.session.commit()

        return student
    
    def update_student(self, student, name, document, address):
        student.name = name
        student.document = document
        student.address = address

        db.session.commit()

        return student
    
    def delete_student(self, student):
        db.session.delete(student)
        db.session.commit()