from flask import Flask
from controllers.student_controller import student_controller
from controllers.health_controller import health_controller
from db.config import db, init_app
from db.populate import populate_database
from models.student import Student

app = Flask(__name__)

app.register_blueprint(student_controller)
app.register_blueprint(health_controller)

init_app(app)
with app.app_context():
    db.create_all()
    if Student.query.count() == 0 and not app.config['TESTING']: 
        populate_database()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)