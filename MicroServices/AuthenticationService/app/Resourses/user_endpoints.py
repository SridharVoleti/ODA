from flask import Blueprint,jsonify,request,abort
from flask_jwt_extended import create_access_token,decode_token
from passlib.hash import pbkdf2_sha256

from app.Models.User import  User
from app import mongo

user_bp = Blueprint("User",__name__)

@user_bp.route('/register',methods=['POST'])
def register():
    try:
        data = request.get_json()
        data["password"] = pbkdf2_sha256.hash(data["password"])
        user = User(**data).to_bson()
        user['_id']="user001"
        response = mongo.db.Users.insert_one(user)
        if response.acknowledged:
            return jsonify(status="success",message="User registration  successful"),200
        else:
            abort(404,message="Failed to register user")
    except Exception as e:
        return jsonify({"error":str(e)}),400

@user_bp.route('/login',methods=['POST'])
def login():
    try:
        user = request.get_json()
        response = mongo.db.Users.find_one_or_404({"username":user["username"]})
        if response and pbkdf2_sha256.verify(user["password"],response["password"]):
            response.pop('password',None)
            access_token = create_access_token(identity=response)
            return jsonify(access_token=access_token,user=response),200
        else:
            abort(401,message="Invalid Credentials")
    except Exception as e:
        return jsonify({"error":str(e)}),400

@user_bp.route('/get-user/<string:id>')
def get_user_by_id(id):
    try:
        response = mongo.db.Users.find_one_or_404({"_id":id})
        if response:
            response.pop('password',None)
            return response
    except Exception as e:
        return jsonify({"error":str(e)}),400
    
@user_bp.route('/validate-token',methods=['POST'])
def validate_token():
    try:
        token = request.json.get('token')
        decoded_token = decode_token(token)
        return jsonify({"valid":True,"user":decoded_token['sub']}),200
    except Exception as e:
        return jsonify({"valid":False,"error":str(e)}),401