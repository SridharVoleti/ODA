from flask import Blueprint, render_template, redirect, url_for, flash,session,request
from flask_login import login_user, logout_user,current_user
import json
from datetime import datetime
import requests
import os

from app.models.user import User
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        try:
            response = requests.post(f"{os.getenv("AUTH_URL")}/login",json={"email":email,"password":password})
            if response.status_code==200:
                user = response.json().get("user")
                user["access_token"]=response.json().get("access_token")
                session['user']=user
                user = User(**user)
                login_user(user)
                return redirect(url_for('main.index'))
            else:
                flash(response.json().get("description"), 'danger')
        except Exception as e:
            flash("Something went wrong....Try again", 'danger')
            print(f"Login Exception: {str(e)}",flush=True)
    return render_template('login.html', form=form)

@auth_bp.route('/register/<token>', methods=['GET', 'POST'])
def register(token):
    try:
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))
        invitation_res = requests.get(f"{os.getenv("AUTH_URL")}/get-invite/{token}")
        if invitation_res.status_code !=200:
            flash("Invalid token", 'danger')
            return render_template('not_found.html')
        form = RegisterForm()
        invitation = invitation_res.json()
        if request.method == "GET" and invitation:
            for field_name, value in invitation.items():
                if hasattr(form, field_name):
                    field = getattr(form, field_name)
                    field.data = value
                    field.render_kw = {"readonly": True}
    except Exception as e:
        print(f"Register Exception: {str(e)}",flush=True)
    if form.validate_on_submit():
        try:
            current_datetime = datetime.now()
            user_data = {
                "firstname": form.firstname.data,
                "middlename": form.middlename.data,
                "lastname": form.lastname.data,
                "address": form.address.data,
                "phone": form.phone.data,
                "email": form.email.data,
                "password": form.password.data,
                "role": form.role.data,
                "CreatedAt":current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            } 
            response = requests.post(f"{os.getenv("AUTH_URL")}/register/{token}",json=user_data)
            if response.status_code == 200:
                flash(response.json().get('description'),"success")
                return redirect(url_for('auth.login'))
            else:
                flash(response.json().get('description'),"danger")
        except Exception as e:
            flash("Something went wrong.....Try Again")
            print(f"Signup Exception: {str(e)}",flush=True)
    return render_template('register.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
