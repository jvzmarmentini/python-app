from flask import Blueprint, redirect, request, url_for
from flask_login import login_user, logout_user
from modules.auth.user import User

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate the username and password
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            # Login the user
            login_user(user)
            print("success")
            return redirect('/students')

        return 'Invalid username or password.'
    return 'welcome to login'

@user_controller.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
