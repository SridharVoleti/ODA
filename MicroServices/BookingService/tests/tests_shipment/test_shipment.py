from app.Models.shipment import ShipmentCreate
from app import mongo

booking_data = {
  "_id":"BOOKING001",
  "container_details": {
    "_id": "CONTAINER20241009101727",
    "cargo_type": "Hazardous",
    "container_condition": "Damaged",
    "container_seal_number": "337",
    "container_size": "Virginia",
    "container_status": "1",
    "container_type": "40",
    "container_weight": 645,
    "date_of_manufacture": "2025-06-07T00:00:00Z",
    "iso_code": "33561",
    "last_date_inspection": "2025-08-07T00:00:00Z",
    "max_gross_weight": 409,
    "owner_or_operator_code": "93454-7604"
  },
  "shipment_details": {
    "_id": "SHIPMENT20241009101727",
    "bill_of_lading": "Negotiatable BL",
    "carting_point": "Enim ea voluptas consequatur expedita nihil ratione impedit inventore sunt.",
    "cbm": 255,
    "cha": "Global Trade Brokers Inc",
    "clearance_place": "Los Angeles International Airport",
    "co_loader": "Johnson LLC",
    "consignee": "245-696-1094",
    "consignee_address": "841 Dereck Parks",
    "container_stuffing": "El Salvador",
    "declared_value": 579,
    "delivery_date": "2024-06-24T00:00:00Z",
    "dimensions": "12.5*15*20",
    "file_reference_number": "FRN12345",
    "forwarder": "Eveniet error sapiente soluta ut corporis corrupti similique in.",
    "fpod": "Architecto distinctio magnam repellendus.",
    "gross_weight": 385,
    "insurance": True,
    "invoice_currency": "CAD",
    "invoice_currency_value": 418,
    "invoice_date": "2024-10-09T04:47:27Z",
    "invoice_number": "INV-011667-FMQ-7",
    "invoice_type": "Pro Forma",
    "item_description": "Deleniti hic id ut nemo dolorem eius eaque iure odit.",
    "job_date": "2024-10-09T04:47:27Z",
    "job_number": "JOB99243",
    "job_type": "Export",
    "nature_of_contract": "FOB",
    "nature_of_payment": "Letter of credit",
    "net_weight": 150,
    "number_of_packages": 533,
    "operation_handle_by": "JOHN SMITH",
    "package_type": "CRT",
    "plan_date": "2024-05-10T00:00:00Z",
    "pod": "Port of Rotterdam",
    "pol": "Port of Rotterdam",
    "por": "Port of Rotterdam",
    "remarks": "Numquam similique cumque officiis eius repellendus inventore et.",
    "sales_person_name": "Destin Haley",
    "sb_number": "SB18780775",
    "sb_number_date": "2024-10-09T04:47:27Z",
    "select_job": "JOB 7896",
    "sender_address": "589 Doyle Crescent",
    "sender_name": "Robert.Connelly75",
    "series": "Series B",
    "shipper_or_exporter": "SHIPPER A",
    "shipping_company": "GlobalShippingCo",
    "shipping_date": "2024-03-01T00:00:00Z",
    "shipping_line": "LINE B",
    "shipping_method": "Express",
    "special_instructions": "Impedit modi laborum quod aliquid nisi commodi perferendis recusandae.",
    "type_of_shipment": "LCL",
    "unit": "Suscipit aspernatur animi dolores quas quod.",
    "unit_type": "BOXES",
    "weight": 715
  }
}

def test_get_shipments_empty(client):
    """Test getting shipments when there are no shipments in the database."""
    response = client.get('/api/shipments')
    assert response.status_code == 200
    assert response.get_json() == []

def test_add_shipment(client):
    """Test adding a new shipment."""
    response = client.post('/api/shipment', json=booking_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data['_id'] == booking_data['_id']

def test_get_shipment(client):
    """Test retrieving a shipment by ID."""
    result = mongo.db.shipments.insert_one(ShipmentCreate(**booking_data).to_bson())
    booking_id = str(result.inserted_id)
    response = client.get(f'/api/shipment/{booking_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['_id'] == booking_id

def test_update_shipment(client):
    """Test updating an existing shipment."""
    result = mongo.db.shipments.insert_one(ShipmentCreate(**booking_data).to_bson())
    booking_id = str(result.inserted_id)
    updated_data = {
        "shipment_details":{
            "shipping_company": "Updated Shipping Co.",
            "sender_name": "Jane Doe",
        }
    }  
    response = client.put(f'/api/shipment/{booking_id}', json=updated_data)
    assert response.status_code == 201  
    # Fetch the updated shipment from the database to verify changes
    updated_shipment = mongo.db.shipments.find_one({"_id": booking_id})
    assert updated_shipment['shipping_details.shipping_company'] == "Updated Shipping Co."
    assert updated_shipment['shipping_details.sender_name'] == "Jane Doe"

def test_delete_shipment(client):
    """Test deleting a shipment by ID."""
    booking_data = {
        "_id":"BOOKING001",
        "container_details": {
            "_id": "CONTAINER20241009101727",
            "cargo_type": "Hazardous",
            "container_condition": "Damaged",
            "container_seal_number": "337",
            "container_size": "Virginia",
            "container_status": "1",
            "container_type": "40",
            "container_weight": 645,
            "date_of_manufacture": "2025-06-07T00:00:00Z",
            "iso_code": "33561",
            "last_date_inspection": "2025-08-07T00:00:00Z",
            "max_gross_weight": 409,
            "owner_or_operator_code": "93454-7604"
        },
        "shipment_details": {
            "_id": "SHIPMENT20241009101727",
            "bill_of_lading": "Negotiatable BL",
            "carting_point": "Enim ea voluptas consequatur expedita nihil ratione impedit inventore sunt.",
            "cbm": 255,
            "cha": "Global Trade Brokers Inc",
            "clearance_place": "Los Angeles International Airport",
            "co_loader": "Johnson LLC",
            "consignee": "245-696-1094",
            "consignee_address": "841 Dereck Parks",
            "container_stuffing": "El Salvador",
            "declared_value": 579,
            "delivery_date": "2024-06-24T00:00:00Z",
            "dimensions": "12.5*15*20",
            "file_reference_number": "FRN12345",
            "forwarder": "Eveniet error sapiente soluta ut corporis corrupti similique in.",
            "fpod": "Architecto distinctio magnam repellendus.",
            "gross_weight": 385,
            "insurance": True,
            "invoice_currency": "CAD",
            "invoice_currency_value": 418,
            "invoice_date": "2024-10-09T04:47:27Z",
            "invoice_number": "INV-011667-FMQ-7",
            "invoice_type": "Pro Forma",
            "item_description": "Deleniti hic id ut nemo dolorem eius eaque iure odit.",
            "job_date": "2024-10-09T04:47:27Z",
            "job_number": "JOB99243",
            "job_type": "Export",
            "nature_of_contract": "FOB",
            "nature_of_payment": "Letter of credit",
            "net_weight": 150,
            "number_of_packages": 533,
            "operation_handle_by": "JOHN SMITH",
            "package_type": "CRT",
            "plan_date": "2024-05-10T00:00:00Z",
            "pod": "Port of Rotterdam",
            "pol": "Port of Rotterdam",
            "por": "Port of Rotterdam",
            "remarks": "Numquam similique cumque officiis eius repellendus inventore et.",
            "sales_person_name": "Destin Haley",
            "sb_number": "SB18780775",
            "sb_number_date": "2024-10-09T04:47:27Z",
            "select_job": "JOB 7896",
            "sender_address": "589 Doyle Crescent",
            "sender_name": "Robert.Connelly75",
            "series": "Series B",
            "shipper_or_exporter": "SHIPPER A",
            "shipping_company": "GlobalShippingCo",
            "shipping_date": "2024-03-01T00:00:00Z",
            "shipping_line": "LINE B",
            "shipping_method": "Express",
            "special_instructions": "Impedit modi laborum quod aliquid nisi commodi perferendis recusandae.",
            "type_of_shipment": "LCL",
            "unit": "Suscipit aspernatur animi dolores quas quod.",
            "unit_type": "BOXES",
            "weight": 715
        }
    }

    result = mongo.db.shipments.insert_one(ShipmentCreate(**booking_data).to_bson())
    booking_id = str(result.inserted_id)
    response = client.delete(f'/api/shipment/{booking_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Shipment deleted successfully."
    # Ensure the shipment is actually deleted
    deleted_shipment = mongo.db.shipments.find_one({"_id": booking_id})
    assert deleted_shipment is None
