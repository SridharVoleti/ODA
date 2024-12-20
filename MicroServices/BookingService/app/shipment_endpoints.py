import flask
from flask import request,jsonify,Blueprint,abort
from pymongo.errors import DuplicateKeyError
import os
import dotenv
import requests

dotenv.load_dotenv()

from .Models.shipment import ShipmentCreate, ShipmentBase
from app import mongo

shipment_bp = Blueprint('shipment', __name__)

def verify_token(required_roles=None):
    token = request.headers.get("Authorization","").replace("Bearer ","")
    if not token:
        abort(401,description="Missing Authorization Token")
    response = requests.post(os.getenv("AUTH_URL")+"/validate-token",json={"token":token})
    if response.status_code != 200:
        abort(401,description="Invalid Token")
    user = response.json().get("user")
    role = user.get("role")
    if required_roles and role not in required_roles:
        abort(403, description="Forbidden: Insufficient privileges")
    
    return {"user":user,"token":token}

@shipment_bp.route('/api/shipments', methods=["GET"])
def get_shipments():
    try:
        cursor = mongo.db.shipments.find()
        shipments = [ShipmentBase(**doc).to_json() for doc in cursor]
        return shipments,200
    except Exception as e:
        return jsonify(error=str(e)), 500

@shipment_bp.route('/api/shipments/<string:shipper_id>', methods=["GET"])
def get_shipments_by_shipper(shipper_id):
    try:
        verify_token(required_roles=['Shipper'])
        cursor = mongo.db.shipments.find({"shipper_id":shipper_id})
        shipments = [ShipmentBase(**doc).to_json() for doc in cursor]
        return shipments,200
    except Exception as e:
        return jsonify(error=str(e)), 500

@shipment_bp.route('/api/shipment', methods=["POST"])
def add_shipment():
    try:
        verify_token(required_roles=['Shipper'])
        raw_data = request.get_json()
        data = ShipmentCreate(**raw_data).to_bson()
        result = mongo.db.shipments.insert_one(data)
        if result.acknowledged:
            inserted_doc = mongo.db.shipments.find_one({"_id": result.inserted_id})
            return ShipmentBase(**inserted_doc).to_json(), 201
        else:
            return jsonify(description="Failed to insert shipment."), 400
    except DuplicateKeyError:
        return jsonify(description="Duplicate key error."), 400
    except Exception as e:
        return jsonify(description=str(e)), 500

@shipment_bp.route('/api/shipment/<string:id>',methods=["GET"])
def get_shipment(id):
    doc = mongo.db.shipments.find_one_or_404({"_id":id})
    return ShipmentBase(**doc).to_json()

@shipment_bp.route('/api/shipment/<string:id>', methods=["PUT"])
def update_shipment(id):
    try:
        verify_token(required_roles=['Shipper'])
        # Fetch the existing shipment document
        existing_shipment = mongo.db.shipments.find_one({"_id": id})
        if not existing_shipment:
            return jsonify(error="Shipment not found."), 404
        # Get the raw JSON payload
        raw_data = request.get_json()
        # Perform the update operation in MongoDB for the shipment document
        result = mongo.db.shipments.update_one({"_id": id}, {"$set": raw_data})

        # Check if the update was successful
        if result.acknowledged:
            updated_doc = mongo.db.shipments.find_one({"_id": id})
            return ShipmentBase(**updated_doc).to_json(), 200
        else:
            return jsonify(description="Failed to update shipment."), 400

    except Exception as e:
        return jsonify(error=str(e)), 500

@shipment_bp.route('/api/shipment/<string:id>', methods=["DELETE"])
def delete_shipment(id):
    try:
        verify_token(required_roles=['Shipper'])
        result = mongo.db.shipments.delete_one({"_id": id})
        if result.deleted_count:
            return jsonify(description="Shipment deleted successfully."), 200
        else:
            abort(404, description="Shipment not found")
    except Exception as e:
        return jsonify(description=str(e)), 400
