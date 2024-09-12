import pytest
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
        'container_type' : "20",
        'container_size' :"10*12*40",
        'container_weight': 70,
        'max_gross_weight' : 50,
        'owner_or_operator_code' : "Rachana2000",
        'container_status' : "Empty",
        'iso_code' : "7896",
        'container_condtition' : "Clean",
        'date_of_manufacture' : "2024-08-20",
        'last_date_inspection' : "2025-07-30",
        'cargo_type' : "General",
        'container_seal_number':"Seal123"
     }