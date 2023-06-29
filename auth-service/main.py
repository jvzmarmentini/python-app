from flask import Flask
from app.controllers.auth_controller import auth_controller
from app.controllers.health_controller import health_controller
from app.db.config import db, init_app
from app.db.populate import populate_database
from app.models.user import User

app = Flask(__name__)

app.register_blueprint(auth_controller)
app.register_blueprint(health_controller)

init_app(app)
with app.app_context():
    db.create_all()
#    if User.query.count() == 0: 
#        populate_database()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)