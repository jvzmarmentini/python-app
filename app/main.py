from flask import Flask, redirect
from flasgger import Swagger
from modules.students.student_controller import student_controller
from modules.subjects.subject_controller import subject_controller
from modules.enrollments.enrollment_controller import enrollment_controller
from modules.auth.user_controller import user_controller
from modules.common.health_check import health_controller
from config import db, init_app
from populate_db import populate_database
from modules.students.student import Student

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'REST Classroom API',
    'uiversion': 3,
    'version': 1.0,
    'specs_route': '/',
    'default_endpoint': '/',
    'description': 'A Flask REST API for Software Engineering II Class',
    'tos': ''
}

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['swagger_ui_bundle_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js'
swagger_config['swagger_ui_standalone_preset_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js'
swagger_config['jquery_js'] = '//unpkg.com/jquery@2.2.4/dist/jquery.min.js'
swagger_config['swagger_ui_css'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui.css'

swagger = Swagger(app,swagger_config)
app.register_blueprint(student_controller)
app.register_blueprint(subject_controller)
app.register_blueprint(enrollment_controller)
app.register_blueprint(user_controller)
app.register_blueprint(health_controller)

@app.route('/')
def swagger_ui():
    return #redirect('/apidocs/')

init_app(app)
with app.app_context():
    db.create_all()
    if Student.query.count() == 0: 
        populate_database()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)