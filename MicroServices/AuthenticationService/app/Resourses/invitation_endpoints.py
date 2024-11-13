from flask import Blueprint,jsonify,request,abort,url_for
from flask_mail import Message
from flask_jwt_extended import decode_token
import uuid
import os

from app.Models.User import  User
from app.Models.Invitation import Invitation
from app import mail
from app import mongo
from app.utils.validate_token import verify_token
from app.utils.send_invitation import send_invitation_email

invitation_bp = Blueprint("Invitation",__name__)

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
        mongo.db.Invitations.insert_one(invitation)
        send_invitation_email(data.get('email'),invitation['_id'])
        return jsonify({"message":"Invitation sent successfully"}),200
    except Exception as e:
        print(f"Exception in invite endpoint: {str(e)}",flush=True)
        return jsonify({"message":str(e)}),400

@invitation_bp.route('/get-invitations')
def get_invitations():
    try:
        verify_token(required_roles=['Admin'])
        cursor = mongo.db.Invitations.find({})
        invitations = [doc for doc in cursor]
        return invitations
    except Exception as e:
        print(f"Exception in get_invites endpoint: {str(e)}",flush=True)
        return jsonify({"description":str(e)}),400

@invitation_bp.route('/get-invite/<string:id>')
def get_invitation_by_id(id):
    try:
        invitation = mongo.db.Invitations.find_one_or_404({"_id":id})
        return invitation
    except Exception as e:
        return jsonify({"description":str(e)}),400
    
@invitation_bp.route('/revoke/<string:id>',methods=['DELETE'])
def revoke(id):
    try:
        verify_token(required_roles=['Admin'])
        result = mongo.db.Invitations.delete_one({"_id": id})
        if result.deleted_count:
            return jsonify(description="Invitation revoked successfully."), 200
        else:
            abort(404, description="Invitation not found")
    except Exception as e:
        return jsonify(description=str(e)), 400