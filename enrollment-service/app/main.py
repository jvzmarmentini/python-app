from flask import Flask
from controllers.enrollment_controller import enrollment_controller
from controllers.health_controller import health_controller
from db.config import db, init_app
# from db.populate import populate_database
# from models.enrollment import Enrollment

app = Flask(__name__)

app.register_blueprint(enrollment_controller)
app.register_blueprint(health_controller)

init_app(app)
with app.app_context():
    db.create_all()
    # if Enrollment.query.count() == 0: 
    #     populate_database()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)