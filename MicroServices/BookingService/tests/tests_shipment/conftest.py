# tests/test_shipment.py

import pytest
from app import create_app, mongo
@pytest.fixture
def client():
    app = create_app('testing')
    
    with app.app_context():
        mongo.db.shipments.delete_many({})  # Clear test database
    
    client = app.test_client()
    
    yield client
