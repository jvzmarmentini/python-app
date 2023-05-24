from flask import Flask
from controllers.auth_controller import auth_controller
from db.config import db, init_app
from db.populate import populate_database
from models.user import User

app = Flask(__name__)

app.register_blueprint(auth_controller)

init_app(app)
with app.app_context():
    db.create_all()
    if User.query.count() == 0: 
        populate_database()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)