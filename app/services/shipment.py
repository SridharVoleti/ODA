import requests

def get_shipments():
    url = "http://127.0.0.1:5000/api/shipments"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
  
def create_shipment(shipment):
    url = "http://127.0.0.1:5000/api/shipment"
    print(shipment,flush=True)
    response = requests.post(url,json=shipment)
    if response.status_code == 201:
        return response.json()
    
def update_shipment(id,shipment):
    url = "http://127.0.0.1:5000/api/shipment/"+ id
    response = requests.put(url,json=shipment)
    if response.status_code == 201:
        return response.json()