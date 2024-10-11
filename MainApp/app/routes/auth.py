from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm
from app.services.user_services import create_user
from werkzeug.security import check_password_hash
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.find_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username,flush=True)
        role = form.role.data
        user = create_user(username, password, role)
        if user:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('User already exists', 'danger')
    return render_template('register.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
