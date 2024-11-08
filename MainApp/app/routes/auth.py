from flask import Blueprint, render_template, redirect, url_for, flash,session
from flask_login import login_user, logout_user
import json

from app.models.user import User
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm
from app.services.user_services import register_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            user = User.login(username,password)
            if user:
                session['user']=user.__dict__
                login_user(user)
                return redirect(url_for('main.index'))
            else:
                flash('Invalid credentials', 'danger')
        except Exception as e:
            flash(e, 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        role = form.role.data
        user = register_user(username, password, role)
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
