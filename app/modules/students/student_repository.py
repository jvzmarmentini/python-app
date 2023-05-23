
from modules.students.student import Student


class StudentRepository:

    def find_by_id(id):
        return Student.query.get(id)