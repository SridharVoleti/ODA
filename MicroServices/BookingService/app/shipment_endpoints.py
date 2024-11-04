import flask
from flask import request,jsonify,Blueprint
from .Models.shipment import ShipmentCreate,ShipmentUpdate, ShipmentUpdateDetails,ContainerUpdateDetails, ShipmentBase
from app import mongo
from pymongo.errors import DuplicateKeyError

shipment_bp = Blueprint('shipment', __name__)
@shipment_bp.route('/api/shipments', methods=["GET"])
def get_shipments():
    try:
        cursor = mongo.db.shipments.find()
        shipments = [ShipmentBase(**doc).to_json() for doc in cursor]
        if len(shipments) > 0:
            return shipments,200
        return jsonify(error="No records found"),404
    except Exception as e:
        return jsonify(error=str(e)), 500

@shipment_bp.route('/api/shipments/<string:shipper_id>', methods=["GET"])
def get_shipments_by_shipper(shipper_id):
    try:
        cursor = mongo.db.shipments.find({"shipper_id":shipper_id})
        shipments = [ShipmentBase(**doc).to_json() for doc in cursor]
        if len(shipments) > 0:
            return shipments,200
        return jsonify(error="No records found"),404
    except Exception as e:
        return jsonify(error=str(e)), 500


@shipment_bp.route('/api/shipment', methods=["POST"])
def add_shipment():
    try:
        raw_data = request.get_json()
        data = ShipmentCreate(**raw_data).to_bson()
        result = mongo.db.shipments.insert_one(data)
        if result.acknowledged:
            inserted_doc = mongo.db.shipments.find_one({"_id": result.inserted_id})
            return ShipmentBase(**inserted_doc).to_json(), 201
        else:
            return jsonify(error="Failed to insert shipment."), 400
    except DuplicateKeyError:
        return jsonify(error="Duplicate key error."), 400
    except Exception as e:
        return jsonify(error=str(e)), 500

@shipment_bp.route('/api/shipment/<string:id>',methods=["GET"])
def get_shipment(id):
    doc = mongo.db.shipments.find_one_or_404({"_id":id})
    return ShipmentBase(**doc).to_json()

@shipment_bp.route('/api/shipment/<string:id>',methods=["PUT"])
@shipment_bp.route('/api/shipment/<string:id>', methods=["PUT"])
def update_shipment(id):
    try:
        # Fetch the existing shipment document
        existing_shipment = mongo.db.shipments.find_one({"_id": id})
        if not existing_shipment:
            return jsonify(error="Shipment not found."), 404

        # Get the raw JSON payload
        raw_data = request.get_json()

        # Extract shipment and container details from the raw payload
        shipment_data = raw_data.get("shipment_details", {})
        container_data = raw_data.get("container_details", {})

        # Initialize an update dictionary
        update_data = {}

        # Merge existing shipment details with incoming data for shipment
        if shipment_data:
            existing_details = existing_shipment.get("shipment_details", {})
            # Use the existing details and update with any new data
            updated_shipment_details = {**existing_details, **shipment_data}
            update_data['shipment_details'] = updated_shipment_details

        # Merge existing container details with incoming data for container
        if container_data:
            existing_container_details = existing_shipment.get("container_details", {})
            # Use the existing container details and update with any new data
            updated_container_details = {**existing_container_details, **container_data}
            update_data['container_details'] = updated_container_details

        # Check if there is any valid data to update
        if not update_data:
            return jsonify(error="No valid fields to update."), 400

        # Perform the update operation in MongoDB for the shipment document
        result = mongo.db.shipments.update_one({"_id": id}, {"$set": update_data})

        # Check if the update was successful
        if result.acknowledged:
            updated_doc = mongo.db.shipments.find_one({"_id": id})
            return ShipmentBase(**updated_doc).to_json(), 200
        else:
            return jsonify(error="Failed to update shipment."), 400

    except Exception as e:
        return jsonify(error=str(e)), 500

@shipment_bp.route('/api/shipment/<string:id>', methods=["DELETE"])
def delete_shipment(id):
    result = mongo.db.shipments.delete_one({"_id": id})
    if result.deleted_count:
        return jsonify(message="Shipment deleted successfully."), 200
    else:
        flask.abort(404, "Shipment not found")
