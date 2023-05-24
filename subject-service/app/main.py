from flask import Flask
from controllers.subject_controller import subject_controller
from db.config import db, init_app
from db.populate import populate_database
from models.subject import Subject

app = Flask(__name__)

app.register_blueprint(subject_controller)

init_app(app)
with app.app_context():
    db.create_all()
    if Subject.query.count() == 0: 
        populate_database()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)