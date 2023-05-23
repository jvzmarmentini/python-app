from flask import Flask
from app.modules.students.student_controller import student_controller
from app.modules.subjects.subject_controller import subject_controller
from config import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@db/college'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(student_controller)
app.register_blueprint(subject_controller)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')