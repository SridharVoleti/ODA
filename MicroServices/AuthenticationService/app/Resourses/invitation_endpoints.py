from flask import Blueprint,jsonify,request,abort,url_for
from flask_mail import Message
from flask_jwt_extended import decode_token
import uuid
import os

from app.Models.User import  User
from app.Models.Invitation import Invitation
from app import mail
from app import mongo

invitation_bp = Blueprint("Invitation",__name__)

def verify_token():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if not token:
        abort(401, description="Missing token")
    
    decoded_token = decode_token(token)
    user = decoded_token['sub']
    if user['role'] != "Admin":
        abort(401,description="You do not have required privilages to access")
    return user

def send_invitation_email(email, token):
    try :
        invite_link = f"localhost:5000/register/{token}"
        message = Message("You're Invited to Join", recipients=[email])
        message.body = f"Click the link to create your account: {invite_link}"
        mail.send(message)  # Send the email with Flask-Mail
    except Exception as e:
        print(f"Error sending invitation email: {e}")

@invitation_bp.route('/invite',methods=['POST'])
def invite():
    try:
        verify_token()
        data = request.get_json()
        invite = mongo.db.Invitations.find_one({"email":data.get('email')})
        if invite:
            return jsonify({"message":"User already invited"}),400
        response = mongo.db.Users.find_one({"email":data.get('email')})
        if response:
            return jsonify({"message":"User already exists"}),400
        invitation = Invitation(**data).to_bson()
        invitation['_id']=str(uuid.uuid4())
        print(invitation,flush=True)
        mongo.db.Invitations.insert_one(invitation)
        send_invitation_email(data.get('email'),invitation['_id'])
        return jsonify({"message":"Invitation sent successfully"}),200
    except Exception as e:
        return jsonify({"message":str(e)}),400

@invitation_bp.route('/get-invite/<string:id>')
def get_invitation_by_id(id):
    try:
        invitation = mongo.db.Invitations.find_one_or_404({"_id":id})
        return invitation
    except Exception as e:
        return jsonify({"message":str(e)}),400