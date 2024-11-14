from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user
import requests
import os

from app.utils.decorators import role_required
from app.forms.invite_form import InviteForm

um_bp = Blueprint('user-management', __name__)

@um_bp.route('/user-management')
@role_required('Admin')
def index():
    try:
        form = InviteForm()
        headers={
            "Authorization":f"Bearer {current_user.access_token}"
        }
        users_response=requests.get(f"{os.getenv("AUTH_URL")}/get-users",headers=headers)
        users = users_response.json() if users_response.status_code ==200 else []
        invitations_response = requests.get(f"{os.getenv("AUTH_URL")}/get-invitations",headers=headers)
        invitations = invitations_response.json() if invitations_response.status_code ==200 else []
        if form.validate_on_submit():
            email = form.email.data
            role = form.role.data
            print(email,flush=True)
    except Exception as e:
        print(f"Exception in User Management Index: {str(e)}")
    return render_template('user_management.html',users=users,invitations=invitations,form=form)

@um_bp.route('/user-management/send-invitation', methods=['POST'])
@role_required('Admin')
def send_invitation():
    try:
        form = InviteForm()
        email = form.email.data
        role = form.role.data
        headers={
            "Authorization":f"Bearer {current_user.access_token}"
        }
        response = requests.post(f"{os.getenv('AUTH_URL')}/invite",json={"email":email,"role":role},headers=headers)
        flash("Invite sent successful","success") if response.status_code == 200 else flash("Failed to send invitation","danger")
    except Exception as e:
        print(f"Exception in send invitation: {str(e)}",flush=True)
    return redirect(url_for('user-management.index'))
    
@um_bp.route('/user-management/revoke-invitation/<id>')
@role_required('Admin')
def revoke_invitation(id):
    try:
        headers={
            "Authorization":f"Bearer {current_user.access_token}"
        }
        requests.delete(f"{os.getenv('AUTH_URL')}/revoke/{id}",headers=headers)
    except Exception as e:
        print(f"Exception in revoke invitation: {str(e)}",flush=True)
    return redirect(url_for('user-management.index'))

@um_bp.route('/user-management/delete-user/<id>')
@role_required('Admin')
def delete_user(id):
    try:
        headers={
            "Authorization":f"Bearer {current_user.access_token}"
        }
        requests.delete(f"{os.getenv('AUTH_URL')}/delete-ser/{id}",headers=headers)
    except Exception as e:
        print(f"Exception in delete user: {str(e)}",flush=True)
    return redirect(url_for('user-management.index'))
    