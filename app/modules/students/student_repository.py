
from modules.students.student import Student


class StudentRepository:

    def find_by_id(self, id):
        return Student.query.get(id)