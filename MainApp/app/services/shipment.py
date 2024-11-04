import requests
import os
def get_shipments():
    url = os.getenv("BOOKING_SERVICE_URL")+"/shipments"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

def get_shipper_shipments(shipper_id):
    url = os.getenv("BOOKING_SERVICE_URL")+"/shipments/"+shipper_id
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    
def create_shipment(shipment):
    url = os.getenv("BOOKING_SERVICE_URL")+"/shipment"
    response = requests.post(url,json=shipment)
    if response.status_code == 201:
        return response.json()
    
def update_shipment(id,shipment):
    url = os.getenv("BOOKING_SERVICE_URL")+"/shipment/"+ id
    response = requests.put(url,json=shipment)
    if response.status_code == 201:
        return response.json()