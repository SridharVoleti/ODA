from flask import Blueprint,jsonify,request,abort
from flask_jwt_extended import create_access_token,decode_token
from passlib.hash import pbkdf2_sha256
import uuid

from app.Models.User import  User
from app import mongo
from app.utils.validate_token import verify_token

user_bp = Blueprint("User",__name__)

@user_bp.route('/get-users')
def get_users():
    try:
        user = verify_token(required_roles=["Admin"])
        print(user.get('user'),flush=True)
        cursor = mongo.db.Users.find({})
        users = [doc for doc in cursor]
        return users,200
    except Exception as e:
        print(f"Exception in get users endpoint: {str(e)}",flush=True)
        return jsonify({"description":str(e)}),401

@user_bp.route('/register/<token>',methods=['POST'])
def register(token):
    try:
        data = request.get_json()
        data["password"] = pbkdf2_sha256.hash(data["password"])
        invite = mongo.db.Invitations.find_one({"_id":token})
        print(invite,flush=True)
        if not invite or invite["is_used"]:
            abort(400,description="You are not allowed to register...Contact Admin")
        user = User(**data).to_bson()
        user['_id']=str(uuid.uuid4())
        response = mongo.db.Users.insert_one(user)
        if response.acknowledged:
            mongo.db.Invitations.update_one({"_id":token},{"$set":{"is_used":True}})
            return jsonify(status="success",description="User registration  successful"),200
        else:
            abort(404,description="Failed to register user")
    except Exception as e:
        print(f"Exception in register endpoint: {str(e)}")
        return jsonify({"description":str(e)}),400

@user_bp.route('/login',methods=['POST'])
def login():
    try:
        user = request.get_json()
        response = mongo.db.Users.find_one_or_404({"email":user["email"]})
        if response and pbkdf2_sha256.verify(user["password"],response["password"]):
            response.pop('password',None)
            access_token = create_access_token(identity=response)
            return jsonify(access_token=access_token,user=response),200
        else:
            abort(401,description="Invalid Credentials")
    except Exception as e:
        print(f"Exception in Login endpoint: {str(e)}")
        return jsonify({"description":str(e)}),400
    
@user_bp.route('/validate-token',methods=['POST'])
def validate_token():
    try:
        token = request.json.get('token')
        decoded_token = decode_token(token)
        return jsonify({"valid":True,"user":decoded_token['sub']}),200
    except Exception as e:
        return jsonify({"valid":False,"error":str(e)}),401
    
@user_bp.route('/delete-user/<string:id>',methods=['DELETE'])
def delete_user(id):
    try:
        verify_token(required_roles=['Admin'])
        result = mongo.db.Users.delete_one({"_id": id})
        if result.deleted_count:
            return jsonify(description="User deleted successfully."), 200
        else:
            abort(404, description="User not found")
    except Exception as e:
        return jsonify(description=str(e)), 400