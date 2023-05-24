from flask import Flask
from modules.students.student_controller import student_controller
from modules.subjects.subject_controller import subject_controller
from modules.enrollments.enrollment_controller import enrollment_controller
from modules.auth.user_controller import user_controller
from modules.common.health_check import health_controller
from config import db, init_app
from populate_db import populate_database
from modules.students.student import Student

app = Flask(__name__)
app.register_blueprint(student_controller)
app.register_blueprint(subject_controller)
app.register_blueprint(enrollment_controller)
app.register_blueprint(user_controller)
app.register_blueprint(health_controller)

init_app(app)
with app.app_context():
    db.create_all()
    if Student.query.count() == 0: 
        populate_database()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)