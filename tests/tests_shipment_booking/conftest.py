import pytest
from flask import Flask, request
from app import app as create_app

# Fixture to create the Flask app instance
@pytest.fixture
def app():
    app = create_app
    app.config['WTF_CSRF_ENABLED'] = False # Disabled CSRF
    return app

# Fixture to provide the test client from Flask for making requests
@pytest.fixture
def client(app):
    return app.test_client()

# Fixture to establish the application context, allowing access to global objects like current_app
@pytest.fixture
def app_context(app):
    with app.app_context():
        yield app  # The app context is available during the test

# Fixture to establish a request context, making request-specific variables (like request) available
@pytest.fixture
def request_context(app, client):
    with app.test_request_context():
        yield  # The request context is available during the test

@pytest.fixture
def form_data():
    return {
        "shipment_id": "AB123456",
        "shipping_company": "GlobalShippingCo",
        "sender_name": "John Doe",
        "sender_address": "123 Elm Street, Apt 4B, Springfield",
        "consignee": "Jane Doe",
        "consignee_address": "456 Oak Avenue, Suite 300, Shelbyville",
        "package_type": "BOX",
        "weight": 200,
        "dimensions": "12.5*15*20",
        "shipping_date": "2024-08-20",
        "delivery_date": "2025-08-23",
        "shipping_method": "Standard",
        "insurance": True,
        "declared_value": 1234,
        "special_instructions": "Handle with care. Fragile items.",
        "bill_of_lading": "Master BL",
        "carting_point": "Warehouse 12, Industrial Zone",
        "cbm": 28,
        "cha": "ABC Customs Services Ltd",
        "clearance_place": "Port of New York",
        "co_loader": "FastLogisticsCo",
        "container_stuffing": "Stuffing completed on site",
        "file_reference_number": "FRN12345",
        "forwarder": "XYZ Forwarders Ltd",
        "fpod": "Singapore Port",
        "gross_weight": 345,
        "invoice_currency": "USD",
        "invoice_currency_value": 344,
        "invoice_date": "2024-08-20",
        "invoice_number": "INV-240823-CLI-1",
        "invoice_type": "Commercial",
        "item_description": "Electronics - Computers and Accessories",
        "job_date": "2024-08-13",
        "job_number": "JOB78901",
        "job_type": "Import",
        "nature_of_contract": "CIF",
        "nature_of_payment": "Advance Payment",
        "net_weight": 322,
        "number_of_packages": 12,
        "operation_handle_by": "TEAM A",
        "plan_date": "2024-08-13",
        "pod": "Port of Singapore",
        "pol": "Port of Singapore",
        "por": "Port of Singapore",
        "remarks": "Urgent shipment, expedite process.",
        "sales_person_name": "Alice Johnson",
        "sb_number": "SB1234",
        "sb_number_date": "2024-08-20",
        "select_job": "JOB 12345",
        "series": "Series A",
        "shipper_or_exporter": "EXPORTER A",
        "shipping_line": "LINE A",
        "type_of_shipment": "FCL",
        "unit": "Kilograms",
        "unit_type": "STANDARD"
    }
